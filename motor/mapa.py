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


ABREV = {"AL": "Alabama", "AR": "Arkansas", "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware",
         "IA": "Iowa", "ID": "Idaho", "IN": "Indiana", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana", "MA": "Massachusetts",
         "MD": "Maryland", "ME": "Maine", "MI": "Michigan", "MO": "Missouri", "MS": "Mississippi", "MT": "Montana",
         "NC": "North Carolina", "ND": "North Dakota", "NE": "Nebraska", "NH": "New Hampshire", "NJ": "New Jersey",
         "NM": "New Mexico", "NV": "Nevada", "NY": "New York", "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon",
         "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota", "TN": "Tennessee",
         "TX": "Texas", "UT": "Utah", "VA": "Virginia", "VT": "Vermont", "WI": "Wisconsin", "WV": "West Virginia", "WY": "Wyoming"}


# Regiones del Censo (las de RECS)
REGIONES = {
    "Northeast": ["CT", "ME", "MA", "NH", "RI", "VT", "NJ", "NY", "PA"],
    "Midwest": ["IL", "IN", "IA", "KS", "MI", "MN", "MO", "NE", "ND", "OH", "SD", "WI"],
    "South": ["DE", "District of Columbia", "FL", "GA", "MD", "NC", "SC", "VA", "WV", "AL", "KY", "MS", "TN",
              "AR", "LA", "OK", "TX"],
    "West": ["AZ", "CO", "ID", "MT", "NV", "NM", "UT", "WY", "Alaska", "CA", "Hawaii", "OR", "WA"],
}


@lru_cache(maxsize=128)
def estado(nombre, w, h, color):
    img = Image.new("RGBA", (w * SS, h * SS), (0, 0, 0, 0))
    _dibujar(ImageDraw.Draw(img), _estados()[ABREV.get(nombre, nombre)], w * SS / ANCHO, color + (255,), C["texto"] + (255,))
    return img.resize((w, h), Image.LANCZOS)
