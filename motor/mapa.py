"""Mapa de EE. UU. dibujado desde recursos/mapa/estados.json (límites del Censo, us-atlas, proyección Albers)."""
from functools import lru_cache
import json

from PIL import Image, ImageDraw

from .graficos import RAIZ, COLORES as C

ANCHO, ALTO = 975, 610
SS = 2  # sobremuestreo para que los bordes salgan suaves


@lru_cache(maxsize=1)
def _estados():
    return json.loads((RAIZ / "recursos" / "mapa" / "estados.json").read_text())


def _dibujar(d, polys, k, relleno, borde):
    for p in polys:
        puntos = [(x * k, y * k) for x, y in p]
        d.polygon(puntos, fill=relleno)
        d.line(puntos + puntos[:1], fill=borde, width=2 * SS)


@lru_cache(maxsize=4)
def base(w, h):
    img = Image.new("RGBA", (w * SS, h * SS), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    for polys in _estados().values():
        _dibujar(d, polys, w * SS / ANCHO, C["panel"] + (255,), C["fondo"] + (255,))
    return img.resize((w, h), Image.LANCZOS)


@lru_cache(maxsize=32)
def estado(nombre, w, h, color):
    img = Image.new("RGBA", (w * SS, h * SS), (0, 0, 0, 0))
    _dibujar(ImageDraw.Draw(img), _estados()[nombre], w * SS / ANCHO, color + (255,), C["texto"] + (255,))
    return img.resize((w, h), Image.LANCZOS)
