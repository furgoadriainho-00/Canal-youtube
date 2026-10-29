"""Identidad del canal: logo (800×800), banner (2560×1440) y marca de agua (150×150).

Uso: python -m motor.marca <carpeta_canal> "<Nombre del canal>" "<lema>"
"""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter

from .graficos import COLORES as C, fondo, icono, texto, encajar, pegar, halo, caja_redondeada
from .casa import vista_casa


def logo(tam=800):
    img = Image.new("RGBA", (tam, tam), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.ellipse((0, 0, tam - 1, tam - 1), fill=C["fondo"] + (255,))
    d.ellipse((tam * 0.04, tam * 0.04, tam * 0.96, tam * 0.96), outline=C["calor"] + (255,), width=int(tam * 0.035))
    pegar(img, halo(int(tam * 0.9), C["frio"]), tam / 2, tam * 0.52, alfa=0.6)
    casa = icono("home", int(tam * 0.62), C["texto"])
    pegar(img, casa, tam / 2, tam * 0.47)
    # barras dentro de la casa: «by the numbers»
    base = tam * 0.66
    for k, (alto, col) in enumerate([(0.10, C["frio"]), (0.16, C["frio"]), (0.23, C["calor"])]):
        x = tam * (0.39 + k * 0.085)
        d.rounded_rectangle((x, base - tam * alto, x + tam * 0.06, base), radius=int(tam * 0.012), fill=col + (255,))
    return img


def banner(nombre, lema):
    W, H = 2560, 1440
    img = fondo(W, H).crop((0, 0, W, H))
    # zona segura (visible en todos los dispositivos): 1546×423 centrada
    sx, sy, sw, sh = (W - 1546) / 2, (H - 423) / 2, 1546, 423
    vista_casa(img, (sx - 40, sy - 20, 560, sh + 40), "todos", 6.0, 6.0, 0.55)
    xt = sx + 560
    t1 = encajar(texto(nombre.upper(), 108, C["texto"]), int(sw - 600))
    pegar(img, t1, xt + (sw - 560) / 2, sy + sh * 0.36)
    t2 = encajar(texto(lema, 46, C["calor"], "Inter", "Bold"), int(sw - 600))
    pegar(img, t2, xt + (sw - 560) / 2, sy + sh * 0.66)
    t3 = texto("New videos every week", 34, C["suave"], "Inter", "SemiBold")
    pegar(img, t3, xt + (sw - 560) / 2, sy + sh * 0.86)
    return img.convert("RGB")


def generar(carpeta: Path, nombre: str, lema: str):
    out = carpeta / "marca"
    out.mkdir(exist_ok=True)
    lg = logo()
    lg.save(out / "logo_800.png")
    lg.resize((150, 150), Image.LANCZOS).save(out / "marca_de_agua_150.png")
    banner(nombre, lema).save(out / "banner_2560x1440.jpg", quality=92)
    for f in sorted(out.iterdir()):
        print("✓", f)


if __name__ == "__main__":
    generar(Path(sys.argv[1]).resolve(), sys.argv[2], sys.argv[3])
