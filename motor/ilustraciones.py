"""Ilustraciones animadas hechas por código: aparatos con su propio movimiento, la casa en corte,
monedas, contador de luz y partículas. Todo es dibujo propio (sin recursos de terceros salvo los iconos).
"""
import math
from functools import lru_cache

from PIL import Image, ImageDraw, ImageFilter

from .graficos import COLORES as C, icono, texto, pegar, halo, caja_redondeada, ease_out, ease_back, prog

ORO = (255, 196, 40)


def _rnd(i, k=0):
    """Pseudoaleatorio estable (mismo valor en cada fotograma)."""
    x = math.sin(i * 127.1 + k * 311.7) * 43758.5453
    return x - math.floor(x)


# ---------- partículas ----------

def _capa(w, h):
    return Image.new("RGBA", (int(w), int(h)), (0, 0, 0, 0))


def nieve(lienzo, cx, cy, r, t, n=18, color=(200, 235, 255)):
    capa = _capa(2 * r, 2 * r)
    d = ImageDraw.Draw(capa)
    for i in range(n):
        vel = 0.25 + 0.35 * _rnd(i, 1)
        fase = (t * vel + _rnd(i, 2)) % 1
        x = r + (2 * _rnd(i, 3) - 1) * r * 0.9 + math.sin(t * 2 + i) * r * 0.06
        y = fase * 2 * r
        s = 3 + 5 * _rnd(i, 4)
        a = int(255 * math.sin(math.pi * fase))
        d.ellipse((x - s, y - s, x + s, y + s), fill=color + (a,))
    pegar(lienzo, capa, cx, cy)


def burbujas(lienzo, cx, cy, r, t, n=14, color=(150, 220, 255)):
    capa = _capa(2 * r, 2 * r)
    d = ImageDraw.Draw(capa)
    for i in range(n):
        vel = 0.3 + 0.4 * _rnd(i, 1)
        fase = (t * vel + _rnd(i, 2)) % 1
        x = r + (2 * _rnd(i, 3) - 1) * r * 0.6 + math.sin(t * 3 + i * 2) * 8
        y = (1 - fase) * 2 * r
        s = 4 + 9 * _rnd(i, 4) * (0.5 + fase)
        a = int(230 * math.sin(math.pi * fase))
        d.ellipse((x - s, y - s, x + s, y + s), outline=color + (a,), width=3)
    pegar(lienzo, capa, cx, cy)


def calor(lienzo, cx, cy, r, t, n=4, color=C["calor"]):
    """Ondas de calor que suben."""
    capa = _capa(2 * r, 2 * r)
    d = ImageDraw.Draw(capa)
    for i in range(n):
        x0 = r + (i - (n - 1) / 2) * r * 0.32
        fase = (t * 0.6 + i * 0.25) % 1
        pts = []
        for k in range(24):
            y = 2 * r * (1 - k / 23)
            x = x0 + math.sin(k * 0.6 - t * 6 + i) * r * 0.06
            pts.append((x, y - fase * r * 0.3))
        a = int(200 * math.sin(math.pi * fase) + 40)
        d.line(pts, fill=color + (a,), width=6, joint="curve")
    pegar(lienzo, capa.filter(ImageFilter.GaussianBlur(1.5)), cx, cy)


def vapor(lienzo, cx, cy, r, t, n=6):
    capa = _capa(2 * r, 2 * r)
    d = ImageDraw.Draw(capa)
    for i in range(n):
        fase = (t * 0.35 + _rnd(i, 1)) % 1
        x = r + (2 * _rnd(i, 2) - 1) * r * 0.5 + math.sin(t * 2 + i) * r * 0.15 * fase
        y = (1 - fase) * 2 * r
        s = r * (0.12 + 0.25 * fase)
        a = int(110 * math.sin(math.pi * fase))
        d.ellipse((x - s, y - s, x + s, y + s), fill=(235, 240, 250, a))
    pegar(lienzo, capa.filter(ImageFilter.GaussianBlur(r * 0.08)), cx, cy)


def gotas(lienzo, cx, cy, r, t, n=8, color=(110, 200, 255)):
    capa = _capa(2 * r, 2 * r)
    d = ImageDraw.Draw(capa)
    for i in range(n):
        fase = (t * (0.7 + 0.3 * _rnd(i, 1)) + _rnd(i, 2)) % 1
        x = r + (2 * _rnd(i, 3) - 1) * r * 0.5
        y = fase ** 1.6 * 2 * r
        s = 5 + 4 * _rnd(i, 4)
        a = int(255 * (1 - fase))
        d.polygon([(x, y - 2.2 * s), (x - s, y), (x + s, y)], fill=color + (a,))
        d.ellipse((x - s, y - s, x + s, y + s), fill=color + (a,))
    pegar(lienzo, capa, cx, cy)


def rayos(lienzo, cx, cy, r, t, color=(255, 230, 120)):
    capa = _capa(2 * r, 2 * r)
    d = ImageDraw.Draw(capa)
    pulso = 0.5 + 0.5 * math.sin(t * 5)
    for k in range(12):
        ang = k * math.pi / 6 + t * 0.4
        r0, r1 = r * 0.45, r * (0.75 + 0.15 * pulso)
        d.line([(r + math.cos(ang) * r0, r + math.sin(ang) * r0), (r + math.cos(ang) * r1, r + math.sin(ang) * r1)],
               fill=color + (int(120 + 120 * pulso),), width=6)
    pegar(lienzo, capa, cx, cy)


def chispas(lienzo, cx, cy, r, t, n=10, color=(120, 255, 200)):
    capa = _capa(2 * r, 2 * r)
    d = ImageDraw.Draw(capa)
    for i in range(n):
        fase = (t * 1.2 + _rnd(i, 1)) % 1
        ang = _rnd(i, 2) * 2 * math.pi
        dist = r * (0.3 + 0.6 * fase)
        x, y = r + math.cos(ang) * dist, r + math.sin(ang) * dist
        s = 6 * (1 - fase) + 2
        a = int(255 * (1 - fase))
        d.line([(x - s, y), (x + s, y)], fill=color + (a,), width=3)
        d.line([(x, y - s), (x, y + s)], fill=color + (a,), width=3)
    pegar(lienzo, capa, cx, cy)


def olas(lienzo, cx, cy, ancho, t, color=(80, 190, 255)):
    capa = _capa(ancho, 60)
    d = ImageDraw.Draw(capa)
    for fila in range(3):
        pts = [(x, 30 + fila * 12 + math.sin(x * 0.04 - t * 3 + fila) * 6) for x in range(0, int(ancho), 6)]
        d.line(pts, fill=color + (200 - fila * 50,), width=4)
    pegar(lienzo, capa, cx, cy)


def monedas_subiendo(lienzo, cx, cy, r, t, ritmo=1.0, n=8):
    """Monedas que salen del aparato y suben: el dinero que se va."""
    capa = _capa(2 * r, 2 * r)
    d = ImageDraw.Draw(capa)
    f = ImageDraw.ImageDraw.font if False else None
    for i in range(n):
        fase = (t * 0.45 * ritmo + i / n) % 1
        x = r + (2 * _rnd(i, 1) - 1) * r * 0.55 + math.sin(t * 2 + i) * 10
        y = (1 - fase) * 2 * r
        s = 16 + 6 * _rnd(i, 2)
        a = int(255 * math.sin(math.pi * fase))
        ancho = s * abs(math.cos(t * 4 + i))  # moneda girando
        d.ellipse((x - ancho - 2, y - s, x + ancho + 2, y + s), fill=ORO + (a,), outline=(200, 140, 0, a), width=3)
    pegar(lienzo, capa, cx, cy)


# ---------- aparatos animados ----------

EFECTOS = {
    "ac_unit": "nieve", "mode_fan": "girar", "heat": "calor", "local_fire_department": "calor", "mode_heat": "calor",
    "water_heater": "burbujas", "shower": "gotas", "water_drop": "gotas", "dishwasher": "burbujas",
    "local_laundry_service": "temblar", "laundry": "temblar_calor", "kitchen": "escarcha", "microwave": "pulso",
    "skillet": "vapor", "oven": "calor", "tv": "parpadeo", "lightbulb": "rayos", "humidity_high": "gotas",
    "pool": "olas", "ev_station": "chispas", "hot_tub": "vapor", "payments": "monedas", "savings": "monedas",
    "electric_meter": "chispas", "heat_pump": "girar_lento", "thermostat": "pulso", "bolt": "chispas",
    "power_settings_new": "pulso", "outlet": "chispas", "trending_up": "pulso", "emoji_events": "rayos",
}


@lru_cache(maxsize=256)
def _icono_rotado(nombre, tam, color, angulo_q):
    return icono(nombre, tam, color).rotate(angulo_q, resample=Image.BICUBIC, expand=False)


def aparato(lienzo, nombre, cx, cy, tam, t, color=C["texto"], resplandor=None, entrada=1.0):
    """Dibuja un icono con su movimiento propio (gira, tiembla, suelta nieve, burbujas, vapor…)."""
    if entrada <= 0.01:
        return
    ef = EFECTOS.get(nombre, "flotar")
    r = int(tam * 0.9)
    if resplandor:
        pulso = 0.85 + 0.15 * math.sin(t * 4)
        pegar(lienzo, halo(int(tam * 2.1), resplandor), cx, cy, alfa=entrada * pulso, escala=entrada)
    # efectos de detrás
    if ef == "calor" or ef == "temblar_calor":
        calor(lienzo, cx, cy - tam * 0.75, int(tam * 0.55), t)
    if ef == "vapor":
        vapor(lienzo, cx, cy - tam * 0.8, int(tam * 0.6), t)
    dx = dy = 0.0
    ang = 0
    if ef in ("temblar", "temblar_calor"):
        dx = math.sin(t * 38) * tam * 0.025
        dy = math.cos(t * 31) * tam * 0.015
    elif ef == "escarcha":
        dx = math.sin(t * 60) * tam * 0.006
    elif ef == "flotar" or ef == "monedas":
        dy = math.sin(t * 2.2) * tam * 0.04
    if ef == "girar":
        ang = int((-t * 360) % 360 // 6 * 6)
    elif ef == "girar_lento" or ef == "nieve":
        ang = int((-t * 40) % 360 // 3 * 3)
    escala = entrada
    if ef == "pulso":
        escala *= 1 + 0.05 * math.sin(t * 6)
    sprite = _icono_rotado(nombre, tam, color, ang) if ang else icono(nombre, tam, color)
    if ef == "parpadeo":
        pegar(lienzo, halo(int(tam * 1.6), (120, 160, 255) if int(t * 3) % 2 else (255, 140, 200)), cx, cy - tam * 0.05,
              alfa=0.6 * entrada)
    pegar(lienzo, sprite, cx + dx, cy + dy, escala=max(0.01, escala))
    # efectos de delante
    if ef == "nieve":
        nieve(lienzo, cx, cy + tam * 0.3, r, t)
    elif ef == "burbujas":
        burbujas(lienzo, cx, cy - tam * 0.2, int(tam * 0.7), t)
    elif ef == "gotas":
        gotas(lienzo, cx, cy + tam * 0.85, int(tam * 0.5), t)
    elif ef == "escarcha":
        nieve(lienzo, cx, cy, int(tam * 0.75), t * 0.4, n=8, color=(220, 245, 255))
    elif ef == "rayos":
        rayos(lienzo, cx, cy - tam * 0.1, int(tam * 0.95), t)
    elif ef == "chispas":
        chispas(lienzo, cx, cy, r, t)
    elif ef == "olas":
        olas(lienzo, cx, cy + tam * 0.55, int(tam * 1.4), t)
    elif ef == "monedas":
        monedas_subiendo(lienzo, cx, cy - tam * 0.6, int(tam * 0.6), t, n=5)


# ---------- dinero ----------

@lru_cache(maxsize=8)
def _moneda(tam):
    img = _capa(tam, int(tam * 0.42) + 6)
    d = ImageDraw.Draw(img)
    d.ellipse((0, 6, tam - 1, int(tam * 0.42) + 5), fill=(200, 140, 0, 255))
    d.ellipse((0, 0, tam - 1, int(tam * 0.42) - 1), fill=ORO + (255,), outline=(230, 160, 0, 255), width=3)
    return img


def pila_monedas(lienzo, cx, base_y, valor, t, u=1.0, ini=0.1, por_moneda=25, max_monedas=22, columnas=1):
    """Monedas que caen y se apilan; la altura sale del valor en dólares."""
    n = max(1, min(max_monedas * columnas, round(valor / por_moneda)))
    tam = int(110 * u)
    paso = int(tam * 0.18)
    caidas = n
    dur_total = 1.2
    for k in range(caidas):
        col = k % columnas
        fila = k // columnas
        t_k = ini + dur_total * k / max(1, caidas)
        p = prog(t, t_k, 0.35)
        if p <= 0:
            break
        y_final = base_y - fila * paso
        y = y_final - (1 - ease_out(p)) * 500 * u
        x = cx + (col - (columnas - 1) / 2) * tam * 1.15 + (_rnd(k, 7) - 0.5) * 6
        pegar(lienzo, _moneda(tam), x, y, alfa=min(1, p * 3))


def billete_volando(lienzo, cx, cy, t, u=1.0, n=6):
    for i in range(n):
        fase = (t * 0.5 + i / n) % 1
        x = cx + (2 * _rnd(i, 1) - 1) * 300 * u + math.sin(t * 2 + i) * 30 * u
        y = cy + (fase - 0.5) * 500 * u
        b = caja_redondeada(int(90 * u), int(44 * u), int(6 * u), (60, 170, 90, int(220 * math.sin(math.pi * fase))))
        pegar(lienzo, b.rotate(math.sin(t * 3 + i) * 25, expand=True), x, y)


# ---------- contador de luz ----------

def contador(lienzo, cx, cy, radio, t, valor, u=1.0, ini=0.0, etiqueta="kWh"):
    capa = _capa(2 * radio + 20, 2 * radio + 20)
    d = ImageDraw.Draw(capa)
    c = radio + 10
    d.ellipse((c - radio, c - radio, c + radio, c + radio), fill=(225, 230, 238, 255), outline=(90, 110, 140, 255), width=int(10 * u))
    d.ellipse((c - radio * 0.88, c - radio * 0.88, c + radio * 0.88, c + radio * 0.88), fill=(245, 247, 250, 255))
    for k in range(40):
        ang = math.pi * 0.75 + k / 39 * math.pi * 1.5
        r0 = radio * (0.72 if k % 5 == 0 else 0.78)
        d.line([(c + math.cos(ang) * r0, c + math.sin(ang) * r0),
                (c + math.cos(ang) * radio * 0.84, c + math.sin(ang) * radio * 0.84)], fill=(40, 55, 80, 255),
               width=int(4 * u) if k % 5 == 0 else int(2 * u))
    # aguja que da vueltas cada vez más rápido
    p = prog(t, ini, 2.0)
    ang = math.pi * 0.75 + (ease_out(p) * 6 + 0.3 * math.sin(t * 9) * p) * math.pi * 1.5
    d.line([(c, c), (c + math.cos(ang) * radio * 0.7, c + math.sin(ang) * radio * 0.7)], fill=C["calor"] + (255,), width=int(10 * u))
    d.ellipse((c - 18 * u, c - 18 * u, c + 18 * u, c + 18 * u), fill=(40, 55, 80, 255))
    pegar(lienzo, capa, cx, cy)
    v = valor * ease_out(prog(t, ini, 2.0))
    num = texto(f"{v:,.0f}", int(radio * 0.28), (15, 27, 45), "Inter", "Bold")
    pegar(lienzo, caja_redondeada(int(radio * 1.0), int(radio * 0.32), int(10 * u), (15, 27, 45, 255)), cx, cy + radio * 0.45)
    pegar(lienzo, texto(f"{v:,.0f}", int(radio * 0.24), C["ahorro"], "Inter", "Bold"), cx, cy + radio * 0.45)
    pegar(lienzo, texto(etiqueta, int(radio * 0.13), (60, 80, 110), "Inter", "Bold"), cx, cy - radio * 0.35)
    chispas(lienzo, cx, cy, int(radio * 1.15), t, n=8)


# ---------- partículas de fondo ----------

def particulas_fondo(lienzo, W, H, tg, n=34):
    d = ImageDraw.Draw(lienzo)
    for i in range(n):
        vel = 0.01 + 0.02 * _rnd(i, 1)
        fase = (tg * vel + _rnd(i, 2)) % 1
        x = _rnd(i, 3) * W + math.sin(tg * 0.5 + i) * 30
        y = (1 - fase) * (H + 40) - 20
        s = 1.5 + 3 * _rnd(i, 4)
        brillo = 0.35 + 0.35 * math.sin(tg * 2 + i)
        base = C["frio"] if i % 3 else C["calor"]
        col = tuple(int(c * brillo * 0.6 + 18) for c in base)
        d.ellipse((x - s, y - s, x + s, y + s), fill=col)
