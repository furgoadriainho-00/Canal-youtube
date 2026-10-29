"""Piezas gráficas: fuentes, iconos, sprites de texto, curvas de animación y pegado con alfa."""
from functools import lru_cache
from pathlib import Path
import math
import re

from PIL import Image, ImageDraw, ImageFont, ImageFilter

RAIZ = Path(__file__).resolve().parent.parent
FUENTES = RAIZ / "recursos" / "fuentes"
ICONOS = RAIZ / "recursos" / "iconos"

COLORES = {
    "fondo": (15, 27, 45),
    "fondo2": (24, 44, 72),
    "calor": (255, 122, 26),
    "frio": (46, 196, 241),
    "texto": (245, 247, 250),
    "suave": (150, 168, 190),
    "ahorro": (61, 220, 132),
    "panel": (30, 50, 80),
    "rojo": (235, 64, 52),
}


# ---------- fuentes ----------

@lru_cache(maxsize=None)
def fuente(familia: str, tam: int, peso: str = "Bold") -> ImageFont.FreeTypeFont:
    f = ImageFont.truetype(str(FUENTES / f"{familia}.ttf"), tam, layout_engine=ImageFont.Layout.RAQM)
    f.set_variation_by_name(peso)
    return f


@lru_cache(maxsize=None)
def _fuente_iconos(tam: int) -> ImageFont.FreeTypeFont:
    f = ImageFont.truetype(str(ICONOS / "MaterialSymbolsRounded.ttf"), tam)
    f.set_variation_by_axes([1, 0, 48, 500])  # relleno, grado, tamaño óptico, peso
    return f


@lru_cache(maxsize=1)
def _codigos() -> dict:
    return dict(l.split() for l in (ICONOS / "MaterialSymbolsRounded.codepoints").read_text().splitlines() if l.strip())


@lru_cache(maxsize=512)
def icono(nombre: str, tam: int, color: tuple) -> Image.Image:
    ch = chr(int(_codigos()[nombre], 16))
    f = _fuente_iconos(tam)
    l, t, r, b = f.getbbox(ch)
    img = Image.new("RGBA", (r - l + 4, b - t + 4), (0, 0, 0, 0))
    ImageDraw.Draw(img).text((2 - l, 2 - t), ch, font=f, fill=color)
    return img


# ---------- texto ----------

@lru_cache(maxsize=2048)
def texto(cadena: str, tam: int, color: tuple, familia: str = "Montserrat", peso: str = "ExtraBold",
          borde: int = 0) -> Image.Image:
    f = fuente(familia, tam, peso)
    l, t, r, b = f.getbbox(cadena, stroke_width=borde)
    asc, desc = f.getmetrics()
    img = Image.new("RGBA", (max(1, r - l + 4), asc + desc + 2 * borde + 4), (0, 0, 0, 0))
    ImageDraw.Draw(img).text((2 - l, 2 + borde), cadena, font=f, fill=color,
                             stroke_width=borde, stroke_fill=(0, 0, 0) if borde else None)
    return img


@lru_cache(maxsize=1024)
def linea_rica(linea: str, tam: int, base=COLORES["texto"], acento=COLORES["calor"]) -> Image.Image:
    """Una línea donde lo que va entre *asteriscos* sale en color de acento."""
    trozos = [t for t in re.split(r"(\*[^*]+\*)", linea) if t]
    sprites = [texto(t.strip("*"), tam, acento if t.startswith("*") else base) for t in trozos]
    ancho = sum(s.width for s in sprites)
    alto = max(s.height for s in sprites)
    img = Image.new("RGBA", (ancho, alto), (0, 0, 0, 0))
    x = 0
    for s in sprites:
        img.alpha_composite(s, (x, 0))
        x += s.width
    return img


def encajar(sprite: Image.Image, ancho_max: int) -> Image.Image:
    if sprite.width <= ancho_max:
        return sprite
    k = ancho_max / sprite.width
    return sprite.resize((ancho_max, max(1, int(sprite.height * k))), Image.LANCZOS)


# ---------- animación ----------

def prog(t: float, ini: float, dur: float) -> float:
    if dur <= 0:
        return 1.0 if t >= ini else 0.0
    return min(1.0, max(0.0, (t - ini) / dur))


def ease_out(p: float) -> float:
    return 1 - (1 - p) ** 3


def ease_back(p: float) -> float:
    c1, c3 = 1.70158, 2.70158
    return 1 + c3 * (p - 1) ** 3 + c1 * (p - 1) ** 2 if p > 0 else 0.0


def ease_in_out(p: float) -> float:
    return 4 * p ** 3 if p < 0.5 else 1 - (-2 * p + 2) ** 3 / 2


# ---------- composición ----------

def pegar(lienzo: Image.Image, sprite: Image.Image, cx: float, cy: float, alfa: float = 1.0,
          escala: float = 1.0, ancla: str = "c"):
    """Pega un sprite RGBA centrado (o anclado a la izquierda con ancla='l') con alfa y escala."""
    if alfa <= 0.01 or escala <= 0.01:
        return
    s = sprite
    if abs(escala - 1) > 0.01:
        s = s.resize((max(1, int(s.width * escala)), max(1, int(s.height * escala))), Image.BILINEAR)
    if alfa < 0.99:
        s = s.copy()
        s.putalpha(s.getchannel("A").point(lambda v: int(v * alfa)))
    x = int(cx - s.width / 2) if ancla == "c" else int(cx)
    y = int(cy - s.height / 2)
    lienzo.alpha_composite(s, (x, y)) if x >= 0 and y >= 0 and x + s.width <= lienzo.width and y + s.height <= lienzo.height \
        else lienzo.paste(s, (x, y), s)


def caja_redondeada(ancho: int, alto: int, radio: int, color: tuple) -> Image.Image:
    img = Image.new("RGBA", (max(1, ancho), max(1, alto)), (0, 0, 0, 0))
    ImageDraw.Draw(img).rounded_rectangle((0, 0, ancho - 1, alto - 1), radius=min(radio, alto // 2, ancho // 2), fill=color)
    return img


@lru_cache(maxsize=64)
def halo(tam: int, color: tuple) -> Image.Image:
    """Resplandor circular suave detrás de iconos."""
    img = Image.new("RGBA", (tam, tam), (0, 0, 0, 0))
    ImageDraw.Draw(img).ellipse((tam * 0.2, tam * 0.2, tam * 0.8, tam * 0.8), fill=color + (110,))
    return img.filter(ImageFilter.GaussianBlur(tam * 0.12))


def fondo(ancho: int, alto: int) -> Image.Image:
    """Fondo más grande que el cuadro, con degradado y manchas suaves, para desplazarlo despacio."""
    W, H = int(ancho * 1.25), int(alto * 1.25)
    img = Image.new("RGB", (W, H), COLORES["fondo"])
    d = ImageDraw.Draw(img)
    for i in range(H):
        k = i / H
        c = tuple(int(COLORES["fondo"][j] * (1 - k * 0.35) + COLORES["fondo2"][j] * k * 0.35) for j in range(3))
        d.line([(0, i), (W, i)], fill=c)
    capa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    dc = ImageDraw.Draw(capa)
    for (fx, fy, fr, col, a) in [(0.15, 0.2, 0.35, COLORES["frio"], 26), (0.85, 0.8, 0.4, COLORES["calor"], 20),
                                 (0.7, 0.15, 0.25, COLORES["frio"], 14)]:
        r = fr * W
        dc.ellipse((fx * W - r, fy * H - r, fx * W + r, fy * H + r), fill=col + (a,))
    capa = capa.filter(ImageFilter.GaussianBlur(W * 0.08))
    img = Image.alpha_composite(img.convert("RGBA"), capa)
    # rejilla técnica muy tenue
    rejilla = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(rejilla)
    paso = int(alto / 12)
    for x in range(0, W, paso):
        d.line([(x, 0), (x, H)], fill=(255, 255, 255, 7))
    for y in range(0, H, paso):
        d.line([(0, y), (W, y)], fill=(255, 255, 255, 7))
    return Image.alpha_composite(img, rejilla)


def fmt_num(v: float, decimales: int = 0) -> str:
    return f"{v:,.{decimales}f}"
