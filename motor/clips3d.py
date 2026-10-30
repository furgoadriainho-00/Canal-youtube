"""Clips 3D de la biblioteca (recursos/clips3d/<aparato>.mp4) dentro de un panel redondeado.

Los clips duran 3 s; si la frase es más larga se reproducen más despacio y en ida y vuelta,
para que nunca haya un salto.
"""
import subprocess
from functools import lru_cache
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

from .graficos import RAIZ, pegar, prog, ease_out
from .ilustraciones import monedas_subiendo

CLIPS = RAIZ / "recursos" / "clips3d"


def existe(nombre):
    return bool(nombre) and (CLIPS / f"{nombre}.mp4").exists()


@lru_cache(maxsize=3)
def _fotogramas(nombre, w, h):
    """Decodifica el clip ya recortado y escalado al tamaño del panel."""
    cmd = ["ffmpeg", "-loglevel", "error", "-i", str(CLIPS / f"{nombre}.mp4"), "-vf",
           f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    datos = subprocess.run(cmd, capture_output=True, check=True).stdout
    return np.frombuffer(datos, np.uint8).reshape(-1, h, w, 3)


@lru_cache(maxsize=8)
def _mascara(w, h, r):
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h - 1), radius=r, fill=255)
    return m


@lru_cache(maxsize=8)
def _marco(w, h, r, color):
    img = Image.new("RGBA", (w + 16, h + 16), (0, 0, 0, 0))
    ImageDraw.Draw(img).rounded_rectangle((0, 0, w + 15, h + 15), radius=r, fill=color + (255,))
    return img


def panel_clip(lienzo, caja, nombre, t, dur, u=1.0, coste=None, color=(70, 100, 140)):
    x0, y0, w, h = [int(v) for v in caja]
    fr = _fotogramas(nombre, w, h)
    n = len(fr)
    vel = max(0.55, min(1.0, n / 30 / max(dur, 0.1)))  # más lento si la frase es larga
    k = int(t * 30 * vel) % (2 * n - 2)
    idx = k if k < n else 2 * n - 2 - k                  # ida y vuelta
    img = Image.fromarray(fr[idx])
    pe = ease_out(prog(t, 0, 0.35))
    pegar(lienzo, _marco(w, h, int(36 * u), color), x0 + w / 2, y0 + h / 2, alfa=pe)
    m = _mascara(w, h, int(30 * u))
    if pe < 0.99:
        m = m.point(lambda v: int(v * pe))
    lienzo.paste(img, (x0, y0), m)
    if coste:
        monedas_subiendo(lienzo, x0 + w * 0.5, y0 + h * 0.3, int(min(w, h) * 0.35), t, ritmo=0.6 + coste / 250, n=6)
