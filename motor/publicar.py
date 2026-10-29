"""Deja un vídeo listo para subir a mano: salida/<fecha>/<carpeta>/ con vídeo, miniaturas, subtítulos y subir.txt.

Uso: python -m motor.publicar <carpeta_video> <fecha_publicacion AAAA-MM-DD>
Lee metadatos.json, añade los capítulos (a partir de `capitulo:` en guion.yaml y audio/tiempos.json)
y registra el vídeo en publicados.csv del canal.
"""
import csv
import json
import shutil
import sys
from pathlib import Path

import yaml

from .graficos import RAIZ


def _mmss(x):
    m, s = divmod(int(x), 60)
    return f"{m}:{s:02d}"


def capitulos(g, tiempos):
    caps = [(tiempos[i]["ini"], s["capitulo"]) for i, s in enumerate(g["segmentos"]) if s.get("capitulo")]
    if caps and caps[0][0] > 0:
        caps.insert(0, (0, "Intro"))
    return [f"{_mmss(t)} {c}" for t, c in caps]


def preparar(carpeta: Path, fecha: str):
    g = yaml.safe_load((carpeta / "guion.yaml").read_text())
    m = json.loads((carpeta / "metadatos.json").read_text())
    tiempos = json.loads((carpeta / "audio" / "tiempos.json").read_text())
    final = carpeta / "final.mp4"
    assert final.exists(), "falta final.mp4"
    assert len(m["titulo"]) < 60, f"título de {len(m['titulo'])} caracteres"

    desc = m["descripcion"].rstrip()
    if g.get("formato") != "short":
        caps = capitulos(g, tiempos)
        if caps:
            desc += "\n\nChapters:\n" + "\n".join(caps)
            m["capitulos"] = caps
    if m.get("afiliados"):
        desc += "\n\n" + "\n".join(m["afiliados"]) + "\n\nAs an Amazon Associate I earn from qualifying purchases."
    if m.get("fuentes_publicas"):
        desc += "\n\nSources:\n" + "\n".join(m["fuentes_publicas"])
    m["descripcion_final"] = desc
    (carpeta / "metadatos.json").write_text(json.dumps(m, indent=2, ensure_ascii=False))

    destino = RAIZ / "salida" / fecha / carpeta.name
    destino.mkdir(parents=True, exist_ok=True)
    shutil.copy2(final, destino / "video.mp4")
    for f in (carpeta / "miniaturas").glob("*.jpg") if (carpeta / "miniaturas").exists() else []:
        shutil.copy2(f, destino / f.name)
    if (carpeta / "subtitulos.srt").exists():
        shutil.copy2(carpeta / "subtitulos.srt", destino / "subtitulos_en.srt")

    pasos = [
        f"TÍTULO:\n{m['titulo']}",
        f"DESCRIPCIÓN:\n{desc}",
        f"ETIQUETAS:\n{', '.join(m['etiquetas'])}",
        "AJUSTES EN YOUTUBE STUDIO:",
        f"- Idioma del vídeo: {m.get('idioma', 'English')} · Subtítulos: sube subtitulos_en.srt (Inglés)" if (destino / "subtitulos_en.srt").exists() else f"- Idioma del vídeo: {m.get('idioma', 'English')}",
        f"- Lista de reproducción: {m['lista']}",
        "- Contenido para niños: NO",
        f"- Contenido alterado o sintético: {'SÍ' if m['etiqueta_ia'] else 'NO'} ({m.get('motivo_ia', '')})",
        "- Miniatura: miniatura_A.jpg (si tu cuenta tiene «Probar y comparar», sube también B y C)" if (destino / "miniatura_A.jpg").exists() else "- Short: sin miniatura personalizada",
    ]
    if m.get("video_relacionado"):
        pasos.append(f"- Vídeo relacionado (Shorts): enlázalo a «{m['video_relacionado']}»")
    if m.get("hora"):
        pasos.append(f"- Programar para: {fecha} {m['hora']}")
    (destino / "subir.txt").write_text("\n\n".join(pasos) + "\n")

    pub = carpeta.parent.parent / "publicados.csv"
    filas = list(csv.reader(pub.open())) if pub.exists() else []
    if not any(len(f) > 2 and f[2] == carpeta.name for f in filas):
        primera = g["segmentos"][0]["t"]
        with pub.open("a", newline="") as f:
            csv.writer(f).writerow([fecha, g.get("formato", "largo"), carpeta.name, m["titulo"], g.get("estructura", ""),
                                    m.get("miniatura_base", ""), " ".join(primera.split()[:5]), "si" if m["etiqueta_ia"] else "no", ""])
    print(f"✓ {destino}")
    return destino


if __name__ == "__main__":
    preparar(Path(sys.argv[1]).resolve(), sys.argv[2])
