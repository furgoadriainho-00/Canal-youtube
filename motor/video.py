"""Convierte la carpeta de un vídeo (con guion.yaml) en final.mp4.

Uso:
    python -m motor.video <carpeta_video> [--prueba N] [--sin-cache]

Pasos: voz por frase (Kokoro) → tiempos → música generada → escenas renderizadas en paralelo
→ mezcla y normalización a −14 LUFS → final.mp4 + subtitulos.srt.
--prueba N renderiza solo las N primeras frases (para revisar rápido).
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
import soundfile as sf
import yaml
from PIL import Image

from .graficos import RAIZ, COLORES, fondo, texto, encajar, pegar, prog, ease_out, ease_in_out, caja_redondeada
from .escenas import ESCENAS, escalera

FPS = 30
SR_VOZ = 24000
MODELOS = RAIZ / "modelos"


def formato(g):
    if g.get("formato") == "short":
        return 1080, 1920, 0.9
    return 1920, 1080, 1.0


def caja_contenido(g, W, H):
    if g.get("formato") == "short":
        return (0, int(H * 0.1), W, int(H * 0.56))
    return (0, 0, W - 110, H)  # deja sitio a la escalera de puestos


# ---------- voz ----------

def _recortar_silencio(x, umbral=0.012, margen=0.03):
    idx = np.where(np.abs(x) > umbral)[0]
    if len(idx) == 0:
        return x
    m = int(margen * SR_VOZ)
    return x[max(0, idx[0] - m): idx[-1] + m]


def generar_voz(carpeta: Path, g, sin_cache=False):
    from kokoro_onnx import Kokoro
    audio = carpeta / "audio"
    audio.mkdir(exist_ok=True)
    voz = g.get("voz", {})
    nombre, vel = voz.get("nombre", "am_michael"), voz.get("velocidad", 1.05)
    pausa_base = 0.12 if g.get("formato") == "short" else 0.3
    k = None
    trozos, tiempos, t = [], [], 0.0
    for i, s in enumerate(g["segmentos"]):
        clave = hashlib.sha1(f'{nombre}|{vel}|{s["t"]}'.encode()).hexdigest()[:12]
        f = audio / f"seg{i:03d}_{clave}.wav"
        if f.exists() and not sin_cache:
            x, _ = sf.read(f, dtype="float32")
        else:
            if k is None:
                k = Kokoro(str(MODELOS / "kokoro-v1.0.onnx"), str(MODELOS / "voices-v1.0.bin"))
            x, sr = k.create(s["t"], voice=nombre, speed=vel, lang="en-us")
            assert sr == SR_VOZ
            x = _recortar_silencio(x.astype("float32"))
            for viejo in audio.glob(f"seg{i:03d}_*.wav"):
                viejo.unlink()
            sf.write(f, x, SR_VOZ)
        pausa = pausa_base + float(s.get("pausa", 0))
        x = np.concatenate([x, np.zeros(int(pausa * SR_VOZ), dtype="float32")])
        trozos.append(x)
        dur = len(x) / SR_VOZ
        tiempos.append({"ini": t, "dur": dur, "voz": (len(x) - int(pausa * SR_VOZ)) / SR_VOZ})
        t += dur
    sf.write(audio / "voz.wav", np.concatenate(trozos), SR_VOZ)
    (audio / "tiempos.json").write_text(json.dumps(tiempos, indent=1))
    return tiempos


# ---------- música (generada por código: original, sin derechos de terceros) ----------

def generar_musica(destino: Path, dur: float, sr=44100, semilla=1):
    rng = np.random.default_rng(semilla)
    progresion = [[48, 55, 64, 71], [45, 52, 60, 67], [41, 48, 57, 64], [43, 50, 59, 62]]  # Cmaj7 Am7 Fmaj7 G
    largo_acorde = 4.0
    n = int(dur * sr) + sr
    out = np.zeros(n)
    hz = lambda m: 440 * 2 ** ((m - 69) / 12)
    for k in range(int(dur / largo_acorde) + 2):
        notas = progresion[k % 4]
        s0 = int(k * largo_acorde * sr)
        if s0 >= n:
            break
        s1 = min(n, s0 + int((largo_acorde + 1.5) * sr))
        tt = np.arange(s1 - s0) / sr
        env = np.minimum(1, tt / 1.5) * np.where(tt < largo_acorde, 1, np.exp(-(tt - largo_acorde) * 2.5))
        for m in notas:
            f = hz(m)
            out[s0:s1] += env * (np.sin(2 * np.pi * f * tt) + 0.25 * np.sin(2 * np.pi * 2.003 * f * tt)) * 0.12
        # arpegio suave en corcheas
        for j in range(8):
            a0 = s0 + int(j * 0.5 * sr)
            if a0 >= n:
                break
            nota = notas[[0, 2, 1, 3, 2, 1, 3, 2][j]] + 12
            a1 = min(n, a0 + int(1.2 * sr))
            ta = np.arange(a1 - a0) / sr
            vel = 0.05 + 0.02 * rng.random()
            out[a0:a1] += vel * np.exp(-ta * 4) * np.sin(2 * np.pi * hz(nota) * ta)
    # bajo
    for k in range(int(dur / largo_acorde) + 2):
        s0 = int(k * largo_acorde * sr)
        if s0 >= n:
            break
        s1 = min(n, s0 + int(largo_acorde * sr))
        tt = np.arange(s1 - s0) / sr
        out[s0:s1] += 0.10 * np.sin(2 * np.pi * hz(progresion[k % 4][0] - 12) * tt) * np.minimum(1, tt * 4)
    # filtro paso bajo de un polo para suavizar
    from scipy.signal import lfilter
    a = 0.15
    y = lfilter([a], [1, -(1 - a)], out)
    y = y[: int(dur * sr)]
    fade = int(2 * sr)
    y[:fade] *= np.linspace(0, 1, fade)
    y[-fade:] *= np.linspace(1, 0, fade)
    y /= max(1e-6, np.abs(y).max()) / 0.5
    sf.write(destino, np.stack([y, y], axis=1).astype("float32"), sr)


# ---------- render ----------

def golpes(dur):
    """Golpes de cámara dentro de una frase para que la imagen cambie como mucho cada ~3 s."""
    return 0 if dur <= 4.2 else int(dur / 3.2)


def _version_motor():
    return hashlib.sha1(b"".join(p.read_bytes() for p in sorted(Path(__file__).parent.glob("*.py")))).hexdigest()[:8]


_BG = {}


def _fondo(W, H):
    if (W, H) not in _BG:
        _BG[(W, H)] = fondo(W, H)
    return _BG[(W, H)]


def _cuadro(g, i, t, tiempos, extra):
    """Dibuja el fotograma del segmento i en el instante local t."""
    W, H, u = formato(g)
    seg = g["segmentos"][i]
    dur = tiempos[i]["dur"]
    tg = tiempos[i]["ini"] + t
    bg = _fondo(W, H)
    # fondo que deriva despacio
    dx = (bg.width - W) / 2 * (1 + 0.8 * np.sin(tg * 0.05))
    dy = (bg.height - H) / 2 * (1 + 0.8 * np.cos(tg * 0.04))
    lienzo = bg.crop((int(dx), int(dy), int(dx) + W, int(dy) + H)).copy()
    caja = caja_contenido(g, W, H)
    ESCENAS[seg["v"]["tipo"]](lienzo, caja, seg["v"], t, dur, u)
    # cámara: zoom lento + golpe de zoom a mitad en frases largas (segundo tiempo visual)
    z = 1 + 0.025 * (t / max(dur, 0.1))
    for k in range(1, golpes(dur) + 1):
        z += 0.045 * ease_in_out(prog(t, k * dur / (golpes(dur) + 1), 0.5))
    if z > 1.001:
        cw, ch = W / z, H / z
        cx, cy = W / 2, (caja[1] + caja[3] / 2)
        x0 = min(max(0, cx - cw / 2), W - cw)
        y0 = min(max(0, cy - ch / 2), H - ch)
        lienzo = lienzo.resize((W, H), Image.BILINEAR, box=(x0, y0, x0 + cw, y0 + ch))
    if g.get("formato") != "short":
        if g.get("estructura") == "lista" and extra.get("puesto"):
            escalera(lienzo, W, H, extra["puesto"], u, alfa=1.0)
        total = tiempos[-1]["ini"] + tiempos[-1]["dur"]
        largo = int(W * min(1, tg / total))
        if largo > 2:
            pegar(lienzo, caja_redondeada(largo, 6, 3, COLORES["calor"] + (210,)), 0, H - 3, ancla="l")
    else:
        _subtitulo(lienzo, W, H, tg, extra.get("palabras", []))
    return lienzo.convert("RGB")


def _subtitulo(lienzo, W, H, tg, palabras):
    """Subtítulos grandes por grupos de hasta 3 palabras, con la palabra que suena en naranja."""
    if not palabras:
        return
    grupos, actual = [], []
    for p in palabras:
        actual.append(p)
        if len(actual) == 3 or p["w"].rstrip().endswith((".", ",", "?", "!", ":")):
            grupos.append(actual)
            actual = []
    if actual:
        grupos.append(actual)
    for gr in grupos:
        if gr[0]["ini"] - 0.05 <= tg < gr[-1]["fin"] + 0.15:
            trozos = []
            sonando = [p for p in gr if p["ini"] <= tg]
            actual = sonando[-1] if sonando else None
            for p in gr:
                activa = p is actual
                trozos.append(texto(p["w"].strip().upper(), 96, COLORES["calor"] if activa else COLORES["texto"],
                                    borde=6))
            ancho = sum(s.width for s in trozos) + 24 * (len(trozos) - 1)
            k = min(1, W * 0.9 / ancho)
            x = W / 2 - ancho * k / 2
            pe = ease_out(prog(tg, gr[0]["ini"] - 0.05, 0.12))
            for s in trozos:
                pegar(lienzo, s, x + s.width * k / 2, H * 0.74, escala=k * (0.85 + 0.15 * pe))
                x += (s.width + 24) * k
            return


def _render_segmento(args):
    carpeta, g, i, tiempos, extra, salida = args
    W, H, _ = formato(g)
    t0 = tiempos[i]["ini"]
    f_ini = round(t0 * FPS)
    f_fin = round((t0 + tiempos[i]["dur"]) * FPS)
    n = f_fin - f_ini
    previo = None
    if i > 0:
        previo = _cuadro(g, i - 1, tiempos[i - 1]["dur"] - 1 / FPS, tiempos, extra.get("prev", {}))
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
           "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
           "-r", str(FPS), str(salida)]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for f in range(n):
        t = (f_ini + f) / FPS - t0
        img = _cuadro(g, i, t, tiempos, extra)
        if previo is not None and f < 5:
            img = Image.blend(previo, img, (f + 1) / 6)
        proc.stdin.write(img.tobytes())
    proc.stdin.close()
    if proc.wait() != 0:
        raise RuntimeError(f"ffmpeg falló en el segmento {i}")
    return i


def _ffmpeg(*args):
    subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", *args], check=True)


def _normalizar(entrada, salida, objetivo, tp=-1.5, lineal=True, previo=""):
    """loudnorm en dos pasadas. En la mezcla final va en modo dinámico: el lineal se queda corto
    cuando el límite de picos no deja subir la ganancia."""
    previo = previo + "," if previo else ""
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(entrada), "-af",
                        f"{previo}loudnorm=I={objetivo}:TP={tp}:LRA=11:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True)
    m = json.loads(r.stderr[r.stderr.rindex("{"):])
    _ffmpeg("-i", str(entrada), "-af",
            f"{previo}loudnorm=I={objetivo}:TP={tp}:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
            f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:"
            f"linear={'true' if lineal else 'false'}",
            "-ar", "48000", str(salida))


def _palabras(carpeta: Path):
    """Marcas de tiempo por palabra con faster-whisper (para los subtítulos de los Shorts)."""
    from faster_whisper import WhisperModel
    m = WhisperModel("small", device="cpu", compute_type="int8")
    segs, _ = m.transcribe(str(carpeta / "audio" / "voz.wav"), word_timestamps=True, language="en")
    out = [{"w": w.word, "ini": w.start, "fin": w.end} for s in segs for w in s.words]
    (carpeta / "audio" / "palabras.json").write_text(json.dumps(out, indent=0))
    return out


def _srt(carpeta, g, tiempos, palabras=None):
    def ts(x):
        h, r = divmod(x, 3600)
        m, s = divmod(r, 60)
        return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int((s % 1) * 1000):03d}"
    lineas = []
    for i, (s, tt) in enumerate(zip(g["segmentos"], tiempos)):
        lineas += [str(i + 1), f'{ts(tt["ini"])} --> {ts(tt["ini"] + tt["voz"])}', s["t"], ""]
    (carpeta / "subtitulos.srt").write_text("\n".join(lineas))


def mezclar(carpeta: Path, total: float, mudo: Path, final: Path):
    print("· audio: música, mezcla y −14 LUFS…", flush=True)
    a = carpeta / "audio"
    generar_musica(a / "musica.wav", total)
    # compresor suave: la voz sintética tiene picos altos y sin él no se llega a −14 LUFS sin pasar de −1,5 dBTP
    _normalizar(a / "voz.wav", a / "voz_norm.wav", -16,
                previo="acompressor=threshold=-24dB:ratio=3:attack=5:release=120:makeup=4")
    _normalizar(a / "musica.wav", a / "musica_norm.wav", -34)  # ≈18 dB por debajo de la voz
    _ffmpeg("-i", str(a / "voz_norm.wav"), "-i", str(a / "musica_norm.wav"), "-filter_complex",
            "[0][1]amix=inputs=2:duration=first:normalize=0", "-ar", "48000", str(a / "mezcla.wav"))
    _normalizar(a / "mezcla.wav", a / "mezcla_norm.wav", -14, lineal=False)
    _ffmpeg("-i", str(mudo), "-i", str(a / "mezcla_norm.wav"), "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
            "-shortest", "-movflags", "+faststart", str(final))


def producir(carpeta: Path, prueba: int = 0, sin_cache=False):
    g = yaml.safe_load((carpeta / "guion.yaml").read_text())
    if prueba:
        g["segmentos"] = g["segmentos"][:prueba]
    print(f"· voz ({len(g['segmentos'])} frases)…", flush=True)
    tiempos = generar_voz(carpeta, g, sin_cache)
    total = tiempos[-1]["ini"] + tiempos[-1]["dur"]
    print(f"  duración {total / 60:.1f} min", flush=True)
    palabras = _palabras(carpeta) if g.get("formato") == "short" else []

    vis = carpeta / "visuales" / "segmentos"
    vis.mkdir(parents=True, exist_ok=True)
    trabajos, puesto, prev = [], None, {}
    for i, s in enumerate(g["segmentos"]):
        if s["v"]["tipo"] == "puesto":
            puesto = s["v"]["n"]
        extra = {"puesto": puesto, "palabras": palabras, "prev": prev}
        clave = hashlib.sha1(json.dumps([{k: v for k, v in s.items() if k != "capitulo"}, tiempos[i], puesto, g.get("formato"),
                                         [p for p in palabras if tiempos[i]["ini"] - 1 <= p["ini"] <= tiempos[i]["ini"] + tiempos[i]["dur"] + 1],
                                         round(total, 2), _version_motor()], sort_keys=True).encode()).hexdigest()[:12]
        salida = vis / f"s{i:03d}_{clave}.mp4"
        if not salida.exists() or sin_cache:
            for viejo in vis.glob(f"s{i:03d}_*.mp4"):
                viejo.unlink()
            trabajos.append((carpeta, g, i, tiempos, extra, salida))
        prev = {"puesto": puesto, "palabras": palabras}
    print(f"· render de {len(trabajos)} segmentos en {os.cpu_count()} núcleos…", flush=True)
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as ex:
        for k, i in enumerate(ex.map(_render_segmento, trabajos), 1):
            if k % 10 == 0 or k == len(trabajos):
                print(f"  {k}/{len(trabajos)}", flush=True)
    lista = carpeta / "visuales" / "lista.txt"
    lista.write_text("".join(f"file '{p.resolve()}'\n" for p in sorted(vis.glob("s*.mp4"))
                             if int(p.name[1:4]) < len(g["segmentos"])))
    mudo = carpeta / "visuales" / "mudo.mp4"
    _ffmpeg("-f", "concat", "-safe", "0", "-i", str(lista), "-c", "copy", str(mudo))

    final = carpeta / ("prueba.mp4" if prueba else "final.mp4")
    mezclar(carpeta, total, mudo, final)
    _srt(carpeta, g, tiempos)
    print(f"✓ {final}", flush=True)
    return final


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("carpeta")
    ap.add_argument("--prueba", type=int, default=0)
    ap.add_argument("--sin-cache", action="store_true")
    ap.add_argument("--solo-audio", action="store_true", help="rehace solo la mezcla sobre visuales/mudo.mp4")
    a = ap.parse_args()
    c = Path(a.carpeta).resolve()
    if a.solo_audio:
        t = json.loads((c / "audio" / "tiempos.json").read_text())
        mezclar(c, t[-1]["ini"] + t[-1]["dur"], c / "visuales" / "mudo.mp4", c / "final.mp4")
    else:
        producir(c, a.prueba, a.sin_cache)
