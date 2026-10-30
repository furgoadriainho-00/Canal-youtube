"""Genera la biblioteca de clips 3D (uno por aparato) en recursos/clips3d/<aparato>.mp4.

Uso: python -m motor3d.biblioteca [aparato ...]      (sin argumentos: todos los que falten)
Cada clip: 90 fotogramas (3 s a 30 fps), 1280×720, Cycles CPU. Unos 12 min por clip en 4 núcleos.
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BLENDER = Path("/home/user/herramientas/blender/blender")
SALIDA = RAIZ / "recursos" / "clips3d"
APARATOS = ["nevera", "lavadora", "secadora", "lavavajillas", "termo", "aire", "calefaccion", "tv", "microondas",
            "cocina", "deshumidificador", "congelador", "ventiladores", "luz", "medidor"]
FOTOGRAMAS = 90


def clip(aparato):
    destino = SALIDA / f"{aparato}.mp4"
    if destino.exists():
        return destino
    tmp = Path(tempfile.mkdtemp(prefix=f"clip_{aparato}_"))
    r = subprocess.run([str(BLENDER), "-b", "--python", str(RAIZ / "motor3d" / "estudio.py"), "--", aparato, str(tmp),
                        "--fotogramas", str(FOTOGRAMAS)], capture_output=True, text=True)
    pngs = sorted(tmp.glob("f_*.png"))
    if len(pngs) != FOTOGRAMAS:
        print(r.stdout[-2000:], r.stderr[-2000:])
        raise RuntimeError(f"{aparato}: {len(pngs)} fotogramas")
    SALIDA.mkdir(parents=True, exist_ok=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", "30", "-i", str(tmp / "f_%04d.png"),
                    "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", str(destino)], check=True)
    shutil.rmtree(tmp)
    return destino


if __name__ == "__main__":
    for a in sys.argv[1:] or APARATOS:
        print("·", a, flush=True)
        print("✓", clip(a), flush=True)
    print("FIN", flush=True)
