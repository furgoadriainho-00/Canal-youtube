"""Casa en corte dibujada por código. La cámara viaja a la habitación del aparato del que se habla,
el aparato cobra vida y la electricidad corre por los cables desde el contador.
"""
import math
from functools import lru_cache

from PIL import Image, ImageDraw, ImageFilter

from .graficos import COLORES as C, icono, texto, pegar, prog, ease_in_out, ease_out
from .ilustraciones import aparato, monedas_subiendo

CW, CH = 2400, 1600  # tamaño del dibujo de la casa
SUELO = 1250

PARED = (34, 58, 92)
PARED2 = (40, 66, 104)
SOTANO = (30, 48, 76)
LINEA = (70, 100, 140)
TEJADO = (60, 40, 50)
TIERRA = (40, 32, 30)

# aparato -> (icono, x, y, tamaño)
APARATOS = {
    "nevera": ("kitchen", 600, 1150, 150),
    "cocina": ("skillet", 780, 1170, 110),
    "microondas": ("microwave", 930, 1010, 100),
    "lavavajillas": ("dishwasher", 1060, 1170, 110),
    "tv": ("tv", 1500, 1110, 150),
    "luz": ("lightbulb", 1350, 900, 90),
    "ventiladores": ("mode_fan", 1720, 900, 110),
    "termostato": ("thermostat", 1230, 1060, 70),
    "aire": ("ac_unit", 700, 560, 130),
    "calefaccion": ("heat", 1000, 760, 120),
    "ducha": ("shower", 1500, 620, 120),
    "lavadora": ("local_laundry_service", 640, 1460, 130),
    "secadora": ("laundry", 820, 1460, 130),
    "termo": ("water_heater", 1040, 1440, 150),
    "deshumidificador": ("humidity_high", 1380, 1470, 110),
    "congelador": ("ac_unit", 1580, 1470, 110),
    "bomba_calor": ("heat_pump", 1770, 1450, 120),
    "nevera2": ("kitchen", 230, 1160, 140),
    "coche": ("ev_station", 410, 1160, 130),
    "piscina": ("pool", 2130, 1205, 110),
    "jacuzzi": ("hot_tub", 2130, 1020, 110),
    "medidor": ("electric_meter", 1945, 1030, 80),
}
MEDIDOR = (1945, 1030)


@lru_cache(maxsize=1)
def dibujo_casa():
    img = Image.new("RGBA", (CW, CH), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # tierra y suelo
    d.rectangle((0, SUELO, CW, CH), fill=TIERRA + (255,))
    d.rectangle((0, SUELO - 6, CW, SUELO + 6), fill=(70, 110, 70, 255))
    # sótano
    d.rectangle((500, SUELO, 1900, 1555), fill=SOTANO + (255,), outline=LINEA + (255,), width=8)
    d.line([(1200, SUELO), (1200, 1555)], fill=LINEA + (255,), width=6)
    # cuerpo de la casa
    d.rectangle((500, 450, 1900, SUELO), fill=PARED + (255,), outline=LINEA + (255,), width=8)
    d.rectangle((1150, 850, 1900, SUELO), fill=PARED2 + (255,))
    d.rectangle((500, 450, 1200, 850), fill=PARED2 + (255,))
    d.line([(500, 850), (1900, 850)], fill=LINEA + (255,), width=10)
    d.line([(1150, 850), (1150, SUELO)], fill=LINEA + (255,), width=6)
    d.line([(1200, 450), (1200, 850)], fill=LINEA + (255,), width=6)
    # tejado y chimenea
    d.rectangle((1550, 170, 1640, 330), fill=(90, 60, 60, 255))
    d.polygon([(420, 460), (1200, 120), (1980, 460)], fill=TEJADO + (255,))
    d.line([(420, 460), (1200, 120), (1980, 460)], fill=(110, 80, 90, 255), width=10)
    # ventanas con luz cálida
    for (x, y) in [(560, 600), (1300, 520), (1700, 520), (1600, 920)]:
        d.rounded_rectangle((x, y, x + 120, y + 110), radius=10, fill=(255, 210, 120, 255), outline=LINEA + (255,), width=6)
        d.line([(x + 60, y), (x + 60, y + 110)], fill=LINEA + (255,), width=5)
    # muebles mínimos: encimera, sofá, cama, bañera
    d.rectangle((520, 1205, 1140, 1225), fill=(90, 120, 160, 255))
    d.rounded_rectangle((1600, 1170, 1860, 1240), radius=20, fill=(120, 80, 110, 255))
    d.rounded_rectangle((760, 760, 1120, 830), radius=16, fill=(90, 110, 150, 255))
    d.rounded_rectangle((1600, 740, 1860, 830), radius=30, fill=(200, 215, 230, 255))
    # garaje
    d.rectangle((110, 900, 500, SUELO), fill=(30, 50, 80, 255), outline=LINEA + (255,), width=8)
    d.polygon([(90, 910), (300, 800), (510, 910)], fill=TEJADO + (255,))
    # jardín: piscina
    d.rectangle((1990, SUELO - 4, 2280, SUELO + 70), fill=(40, 140, 210, 255))
    # contador en la fachada
    d.rounded_rectangle((1905, 975, 1985, 1085), radius=10, fill=(200, 210, 220, 255))
    # cableado tenue
    for nombre, (_, x, y, _) in APARATOS.items():
        for a, b in _ruta(x, y):
            d.line([a, b], fill=(255, 255, 255, 22), width=4)
    # todos los aparatos en reposo
    for nombre, (ic, x, y, tam) in APARATOS.items():
        ico = icono(ic, tam, (170, 190, 215))
        img.alpha_composite(ico, (int(x - ico.width / 2), int(y - ico.height / 2)))
    return img


@lru_cache(maxsize=16)
def _mascara(w, h, r):
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h - 1), radius=r, fill=255)
    return m


@lru_cache(maxsize=16)
def _marco(w, h, r):
    img = Image.new("RGBA", (w + 16, h + 16), (0, 0, 0, 0))
    ImageDraw.Draw(img).rounded_rectangle((0, 0, w + 15, h + 15), radius=r, fill=(70, 100, 140, 255))
    return img


def _ruta(x, y):
    """Cable del contador al aparato: horizontal por dentro del muro y luego vertical."""
    mx, my = MEDIDOR
    yc = my if abs(y - my) < 120 else (y - 90 if y < my else y - 80)
    return [((mx, my), (mx - 40, my)), ((mx - 40, my), (mx - 40, yc)), ((mx - 40, yc), (x, yc)), ((x, yc), (x, y - 60))]


def _puntos_ruta(x, y, t, paso=70):
    segs = _ruta(x, y)
    largo = sum(math.dist(a, b) for a, b in segs)
    off = (t * 260) % paso
    pts = []
    s = off
    while s < largo:
        acc = 0
        for a, b in segs:
            l = math.dist(a, b)
            if acc + l >= s:
                k = (s - acc) / l if l else 0
                pts.append((a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k))
                break
            acc += l
        s += paso
    return pts


def _todos(lienzo, x0, y0, w, h, l, tp, esc, t, dur):
    """Plano general: la electricidad llega a cada aparato y se van encendiendo uno a uno."""
    nombres = [n for n in APARATOS if n != "medidor"]
    capa = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    dc = ImageDraw.Draw(capa)
    reparto = max(0.08, (dur * 0.7) / len(nombres))
    for k, n in enumerate(nombres):
        ic, ax, ay, tam = APARATOS[n]
        if t < 0.2 + k * reparto:
            continue
        for (X, Y) in _puntos_ruta(ax, ay, t, paso=110):
            sx, sy = (X - l) * esc, (Y - tp) * esc
            dc.ellipse((sx - 4, sy - 4, sx + 4, sy + 4), fill=(255, 230, 90, 170))
    lienzo.alpha_composite(capa, (x0, y0))
    for k, n in enumerate(nombres):
        ic, ax, ay, tam = APARATOS[n]
        ent = ease_out(prog(t, 0.2 + k * reparto, 0.3))
        if ent > 0:
            sx, sy = x0 + (ax - l) * esc, y0 + (ay - tp) * esc
            aparato(lienzo, ic, sx, sy, int(tam * esc), t, C["texto"], resplandor=C["calor"], entrada=ent)


def vista_casa(lienzo, caja, foco, t, dur, u=1.0, coste=None, zoom_final=2.3, color=None):
    """Dibuja la casa dentro de `caja` con la cámara viajando del plano general al aparato `foco`."""
    x0, y0, w, h = [int(v) for v in caja]
    casa = dibujo_casa()
    todos = foco == "todos"
    if todos:
        foco = None
    ic, ax, ay, tam = APARATOS[foco] if foco else (None, CW / 2, CH / 2, 0)
    p = ease_in_out(prog(t, 0.0, 1.1)) if foco else 0
    zoom = 1 + (zoom_final - 1) * p + 0.04 * (t / max(dur, 1))
    # ventana de cámara en coordenadas de la casa (mantiene la proporción de la caja)
    vw = CW / zoom
    vh = vw * h / w
    if vh > CH / zoom * 1.0 and not foco:
        vh = CH
        vw = vh * w / h
    cxc = CW / 2 + (ax - CW / 2) * p
    cyc = CH / 2 + (ay - CH / 2) * p
    l = min(max(-vw * 0.1, cxc - vw / 2), CW - vw * 0.9)
    tp = min(max(-vh * 0.1, cyc - vh / 2), CH - vh * 0.9)
    vista = casa.crop((int(l), int(tp), int(l + vw), int(tp + vh))).resize((w, h), Image.BILINEAR)
    esc = w / vw
    panel = Image.new("RGBA", (w, h), (16, 30, 52, 255))
    panel.alpha_composite(vista)
    pegar(lienzo, _marco(w, h, int(36 * u)), x0 + w / 2, y0 + h / 2)
    lienzo.paste(panel, (x0, y0), _mascara(w, h, int(30 * u)))
    a_pant = lambda X, Y: (x0 + (X - l) * esc, y0 + (Y - tp) * esc)
    if todos:
        _todos(lienzo, x0, y0, w, h, l, tp, esc, t, dur)
    if not foco:
        return
    # electricidad corriendo por el cable
    capa = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    dc = ImageDraw.Draw(capa)
    for (X, Y) in _puntos_ruta(ax, ay, t):
        sx, sy = (X - l) * esc, (Y - tp) * esc
        r = 7 * esc ** 0.5
        dc.ellipse((sx - r, sy - r, sx + r, sy + r), fill=(255, 230, 90, 230))
    lienzo.alpha_composite(capa.filter(ImageFilter.GaussianBlur(1)), (x0, y0))
    # el aparato cobra vida
    sx, sy = a_pant(ax, ay)
    col = color or (C["calor"] if (coste or 0) >= 150 else C["frio"])
    aparato(lienzo, ic, sx, sy, int(tam * esc * 1.05), t, C["texto"], resplandor=col, entrada=max(0.3, ease_out(prog(t, 0.5, 0.5))))
    if coste:
        monedas_subiendo(lienzo, sx, sy - tam * esc * 0.9, int(tam * esc * 0.9), t, ritmo=0.6 + coste / 250, n=6)
