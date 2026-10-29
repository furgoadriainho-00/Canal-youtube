"""Control de calidad automático (sección 8 de CLAUDE.md). Lo que no se puede medir se revisa a ojo
con el mosaico de fotogramas que genera.

Uso: python -m motor.control <carpeta_video>
Sale con código 1 si falla algo.
"""
import csv
import difflib
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml
from PIL import Image

from .graficos import RAIZ


def _probe(f):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "stream=codec_name,width,height,r_frame_rate:format=duration", "-of", "json", str(f)],
                       capture_output=True, text=True, check=True)
    return json.loads(r.stdout)


def _lufs(f):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(f), "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True)
    resumen = r.stderr[r.stderr.rindex("Summary:"):]
    i = float(re.search(r"I:\s+(-?[\d.]+) LUFS", resumen).group(1))
    pico = float(re.search(r"Peak:\s+(-?[\d.]+) dBFS", resumen).group(1))
    return i, pico


def _transcribir(f):
    from faster_whisper import WhisperModel
    m = WhisperModel("small", device="cpu", compute_type="int8")
    segs, _ = m.transcribe(str(f), language="en")
    return " ".join(s.text for s in segs)


def _norm(t):
    t = t.lower().replace("-", " ")
    return re.findall(r"[a-z]+|\d+", t)


def mosaico(video, destino, n=12, ancho=480):
    dur = float(_probe(video)["format"]["duration"])
    cuadros = []
    for k in range(n):
        t = dur * (k + 0.5) / n
        p = destino.with_name(f"_f{k}.png")
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", f"{t:.2f}", "-i", str(video), "-frames:v", "1",
                        "-vf", f"scale={ancho}:-1", str(p)], check=True)
        cuadros.append(Image.open(p))
        p.unlink()
    w, h = cuadros[0].size
    cols = 4 if w > h else 6
    filas = (n + cols - 1) // cols
    m = Image.new("RGB", (w * cols, h * filas))
    for k, c in enumerate(cuadros):
        m.paste(c, ((k % cols) * w, (k // cols) * h))
    m.save(destino)
    return destino


def controlar(carpeta: Path):
    g = yaml.safe_load((carpeta / "guion.yaml").read_text())
    short = g.get("formato") == "short"
    final = carpeta / "final.mp4"
    res = []

    def ok(nombre, cond, detalle=""):
        res.append((cond, nombre, detalle))

    info = _probe(final)
    v = next(s for s in info["streams"] if s["codec_name"] == "h264")
    a = next((s for s in info["streams"] if s["codec_name"] == "aac"), None)
    dur = float(info["format"]["duration"])
    W, H = (1080, 1920) if short else (1920, 1080)
    ok("Resolución", (v["width"], v["height"]) == (W, H), f'{v["width"]}×{v["height"]}')
    ok("30 fps, H.264 + AAC", v["r_frame_rate"] == "30/1" and a is not None, v["r_frame_rate"])
    ok("Duración", (30 <= dur <= 60) if short else (8 * 60 <= dur <= 12 * 60), f"{dur:.1f} s")
    i, pico = _lufs(final)
    ok("Volumen ≈ −14 LUFS", abs(i + 14) <= 1.0, f"{i:.1f} LUFS")
    ok("Sin picos (true peak ≤ −1 dBFS)", pico <= -1.0, f"{pico:.1f} dBFS")

    palabras = sum(len(s["t"].split()) for s in g["segmentos"])
    ok("Longitud del guion", (80 <= palabras <= 150) if short else (1300 <= palabras <= 1800), f"{palabras} palabras")
    primera = g["segmentos"][0]["t"].lower()
    ok("Gancho sin saludo", not re.match(r"(hi|hello|hey|welcome)\b", primera), primera[:50])

    tiempos = json.loads((carpeta / "audio" / "tiempos.json").read_text())
    from .video import golpes
    hueco = max(t["dur"] / (golpes(t["dur"]) + 1) for t in tiempos)
    ok("Cambio visual cada 2–4 s", hueco <= 4.2, f"hueco máximo {hueco:.1f} s")

    for f in ("fuentes.md", "licencias.md", "metadatos.json"):
        ok(f"Existe {f}", (carpeta / f).exists())
    m = json.loads((carpeta / "metadatos.json").read_text())
    ok("Título < 60 caracteres", len(m["titulo"]) < 60, str(len(m["titulo"])))
    ok("Etiqueta de IA decidida", isinstance(m.get("etiqueta_ia"), bool))
    if not short:
        ok("3 miniaturas", len(list((carpeta / "miniaturas").glob("*.jpg"))) == 3)

    # cifras del guion presentes en fuentes.md
    fuentes = (carpeta / "fuentes.md").read_text()
    if "../" in fuentes:  # los Shorts remiten a las fuentes del largo
        for ref in re.findall(r"`(\.\./[^`]+)`", fuentes):
            fuentes += (carpeta / ref).read_text() if (carpeta / ref).exists() else ""
    numeros = set()
    for s in g["segmentos"]:
        for k in ("valor",):
            if isinstance(s["v"].get(k), (int, float)):
                numeros.add(s["v"][k])
    fuentes_num = fuentes.replace(".", "").replace(",", ".")
    faltan = [n for n in sorted(numeros) if not re.search(rf"(?<![\d.]){re.escape(str(n).rstrip('0').rstrip('.') if isinstance(n, float) else str(n))}(?![\d])", fuentes_num)]
    ok("Cifras en pantalla documentadas en fuentes.md", not faltan, str(faltan))

    # variedad frente a los 3 últimos publicados
    pub = carpeta.parent.parent / "publicados.csv"
    filas = [f for f in csv.DictReader(pub.open())] if pub.exists() else []
    previos = [f for f in filas if f["carpeta"] != carpeta.name][-3:]
    if len(previos) == 3:
        ok("Estructura no repite 3 seguidas", not all(f["estructura"] == g.get("estructura") for f in previos))
        ok("Miniatura base no repite 3 seguidas", not all(f["miniatura_base"] == m.get("miniatura_base") for f in previos))
        ok("Frase de inicio no repite 3 seguidas",
           not all(f["frase_inicio"] == " ".join(g["segmentos"][0]["t"].split()[:5]) for f in previos))

    # la voz dice lo que pone el guion
    oido = _norm(_transcribir(final))
    escrito = _norm(" ".join(s["t"] for s in g["segmentos"]))
    sim = difflib.SequenceMatcher(None, escrito, oido).ratio()
    ok("Voz = guion (transcripción Whisper)", sim >= 0.85, f"similitud {sim:.2f}")

    mos = mosaico(final, carpeta / "visuales" / "mosaico_qc.png")
    print(f"\nControl de calidad · {carpeta.name}")
    for cond, nombre, det in res:
        print(f"  {'✓' if cond else '✗'} {nombre}" + (f"  ({det})" if det else ""))
    print(f"  · Revisión visual: {mos}")
    fallos = [r for r in res if not r[0]]
    (carpeta / "control.json").write_text(json.dumps(
        {"ok": not fallos, "resultados": [{"ok": c, "prueba": n, "detalle": d} for c, n, d in res]}, indent=1,
        ensure_ascii=False))
    return not fallos


if __name__ == "__main__":
    sys.exit(0 if controlar(Path(sys.argv[1]).resolve()) else 1)
