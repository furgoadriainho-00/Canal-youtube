"""Miniaturas 1280×720 a partir de la sección `miniaturas:` del guion.yaml.

Uso: python -m motor.miniaturas <carpeta_video>
Tipos: icono_grande (icono + cifra + texto), versus (dos iconos con cifras), ranking (podio de barras).
Máximo 4 palabras de texto por miniatura (sin contar cifras).
"""
import sys
from pathlib import Path

import yaml
from PIL import Image, ImageDraw, ImageFilter

from .graficos import COLORES as C, fondo, icono, texto, encajar, pegar, halo, caja_redondeada

W, H = 1280, 720


def _base():
    img = fondo(W, H).crop((60, 40, 60 + W, 40 + H))
    # viñeta para dar contraste
    v = Image.new("L", (W, H), 0)
    ImageDraw.Draw(v).ellipse((-W * 0.2, -H * 0.3, W * 1.2, H * 1.3), fill=255)
    v = v.filter(ImageFilter.GaussianBlur(120))
    negro = Image.new("RGBA", (W, H), (5, 10, 20, 255))
    return Image.composite(img, negro, v).convert("RGBA")


def _color(n):
    return C.get(n, C["calor"])


def icono_grande(m):
    img = _base()
    col = _color(m.get("color", "calor"))
    pegar(img, halo(720, col), 330, 380)
    pegar(img, icono(m["icono"], 400, C["texto"]), 330, 380)
    cifra = encajar(texto(m["cifra"], 210, col, borde=0), 640)
    pegar(img, cifra, 900, 300)
    for i, l in enumerate(m["texto"]):
        s = encajar(texto(l.upper(), 92, C["texto"]), 620)
        pegar(img, s, 900, 470 + i * 105)
    return img


def versus(m):
    img = _base()
    (ia, va, ca), (ib, vb, cb) = m["a"], m["b"]
    for cx, ic, v, c, esc in [(300, ia, va, _color(ca), 0.75), (900, ib, vb, _color(cb), 1.15)]:
        pegar(img, halo(int(560 * esc), c), cx, 300)
        pegar(img, icono(ic, int(300 * esc), C["texto"]), cx, 300)
        pegar(img, encajar(texto(v, int(130 * esc), c), 520), cx, 560)
    pegar(img, texto("vs", 110, C["texto"]), 610, 330)
    if m.get("texto"):
        banda = caja_redondeada(W - 120, 110, 24, (245, 247, 250, 245))
        pegar(img, banda, W / 2, 75)
        pegar(img, encajar(texto(m["texto"].upper(), 76, (15, 27, 45)), W - 180), W / 2, 75)
    return img


def ranking(m):
    img = _base()
    items = m["items"]  # [[icono, valor_texto, valor_num]]
    vmax = max(i[2] for i in items)
    for k, (ic, vt, vn) in enumerate(items):
        y = 210 + k * 170
        col = C["calor"] if k == 0 else C["frio"]
        pegar(img, texto(f"#{k + 1}", 90, col), 110, y)
        pegar(img, icono(ic, 120, C["texto"]), 270, y)
        largo = int(560 * vn / vmax)
        pegar(img, caja_redondeada(largo, 80, 40, col + (255,)), 360, y, ancla="l")
        pegar(img, texto(vt, 80, C["texto"]), 380 + largo, y, ancla="l")
    pegar(img, encajar(texto(m["texto"].upper(), 84, C["texto"], borde=0), W - 120), W / 2, 75)
    return img


TIPOS = {"icono_grande": icono_grande, "versus": versus, "ranking": ranking}


def generar(carpeta: Path):
    g = yaml.safe_load((carpeta / "guion.yaml").read_text())
    out = carpeta / "miniaturas"
    out.mkdir(exist_ok=True)
    rutas = []
    for i, m in enumerate(g.get("miniaturas", []), 1):
        palabras = sum(len(t.split()) for t in (m["texto"] if isinstance(m.get("texto"), list) else [m.get("texto", "")]))
        assert palabras <= 4, f"miniatura {i}: {palabras} palabras (máximo 4)"
        img = TIPOS[m["tipo"]](m).convert("RGB")
        p = out / f"miniatura_{chr(64 + i)}.jpg"
        img.save(p, quality=92)
        rutas.append(p)
        print("✓", p)
    return rutas


if __name__ == "__main__":
    generar(Path(sys.argv[1]).resolve())
