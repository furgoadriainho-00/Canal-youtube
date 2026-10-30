"""Tipos de escena. Cada función dibuja un fotograma: (lienzo, caja, spec, t, dur, u).

caja = (x0, y0, ancho, alto) zona donde va el contenido; u = escala (1 en 1920×1080).
Los elementos entran escalonados para que haya movimiento continuo, y las escenas largas
añaden un segundo tiempo a mitad para que la imagen cambie cada 2–4 s.
"""
from PIL import Image, ImageDraw

import math
import re

from .graficos import (COLORES, icono, texto, linea_rica, encajar, prog, ease_out, ease_back,
                       pegar, caja_redondeada, halo, fmt_num)
from .ilustraciones import aparato, pila_monedas, contador
from .casa import vista_casa
from . import clips3d

C = COLORES


def _color(nombre):
    return C.get(nombre or "calor", C["calor"])


def _fuente_pie(lienzo, caja, u, t, cadena):
    x0, y0, w, h = caja
    s = encajar(texto("Source: " + cadena, int(30 * u), C["suave"], "Inter", "Medium"), int(w * 0.9))
    pegar(lienzo, s, x0 + w / 2, y0 + h - 50 * u, alfa=prog(t, 0.5, 0.4))


def _icono_animado(lienzo, nombre, tam, color, cx, cy, t, ini=0.0, halo_col=None):
    """Icono que entra con rebote y luego hace su propio movimiento (gira, suelta vapor, gotea…)."""
    p = ease_back(prog(t, ini, 0.45))
    aparato(lienzo, nombre, cx, cy, tam, t, color, resplandor=halo_col, entrada=max(0.0, p))


def _anillo(lienzo, cx, cy, radio, pct, color, u, grosor=26):
    capa = Image.new("RGBA", (int(2 * radio + 2 * grosor), int(2 * radio + 2 * grosor)), (0, 0, 0, 0))
    d = ImageDraw.Draw(capa)
    caja = (grosor, grosor, grosor + 2 * radio, grosor + 2 * radio)
    d.arc(caja, 0, 360, fill=(255, 255, 255, 35), width=int(grosor * u))
    if pct > 0.002:
        d.arc(caja, -90, -90 + 360 * min(1, pct), fill=color + (255,), width=int(grosor * u))
    pegar(lienzo, capa, cx, cy)


def _palabras(linea):
    """'Hola *mundo azul*' -> [('Hola', False), ('mundo', True), ('azul', True)]"""
    out = []
    for trozo in re.split(r"(\*[^*]+\*)", linea):
        acento = trozo.startswith("*")
        out += [(w, acento) for w in trozo.strip("*").split()]
    return out


def _lineas_cineticas(lienzo, lineas, cx, cy, u, t, dur, tam, ancho_max, ini=0.05):
    """Texto que aparece palabra a palabra con rebote; las palabras de acento laten."""
    filas = []
    for l in lineas:
        ps = [(texto(w, int(tam * u), C["calor"] if a else C["texto"]), a) for w, a in _palabras(l)]
        esp = int(tam * u * 0.28)
        ancho = sum(sp.width for sp, _ in ps) + esp * (len(ps) - 1)
        filas.append((ps, ancho, esp))
    k = min(1.0, ancho_max / max(1, max(a for _, a, _ in filas)))
    alto_fila = int(tam * u * 1.25 * k)
    n = sum(len(ps) for ps, _, _ in filas)
    paso = min(0.22, max(0.08, dur * 0.5 / max(1, n)))
    y = cy - alto_fila * (len(filas) - 1) / 2
    i = 0
    for ps, ancho, esp in filas:
        x = cx - ancho * k / 2
        for sp, acento in ps:
            p = ease_back(prog(t, ini + i * paso, 0.35))
            if p > 0:
                lat = 1 + (0.05 * math.sin((t - ini - i * paso) * 5) if acento and p >= 1 else 0)
                pegar(lienzo, sp, x + sp.width * k / 2, y + (1 - min(1, p)) * 35 * u,
                      alfa=min(1, p * 2), escala=max(0.01, k * (0.6 + 0.4 * p) * lat))
            x += (sp.width + esp) * k
            i += 1
        y += alto_fila


def numero(lienzo, caja, s, t, dur, u):
    x0, y0, w, h = caja
    col = _color(s.get("color"))
    vertical = w < h * 1.2
    v = s["valor"]
    dec = s.get("decimales", 0)
    pre, suf = s.get("prefijo", ""), s.get("sufijo", "")
    contar = isinstance(v, (int, float)) and not any(ch.isdigit() for ch in pre)
    pc = ease_out(prog(t, 0.15, 0.9))
    valor = v * pc if contar else v
    cad = f'{pre}{fmt_num(valor, dec) if isinstance(valor, (int, float)) else valor}{suf}'
    num = encajar(texto(cad, int(200 * u), col), int(w * (0.86 if vertical else 0.55)))
    lab = encajar(texto(s.get("etiqueta", ""), int(52 * u), C["texto"], "Inter", "SemiBold"), int(w * 0.85))
    dinero = pre.endswith("$") and isinstance(v, (int, float)) and v >= 4
    pct = suf.strip() == "%" and isinstance(v, (int, float)) and 0 < v <= 100 and not pre
    if vertical:
        cx_i, cy_i = x0 + w / 2, y0 + h * 0.28
        cx_n, cy_n = x0 + w / 2, y0 + h * 0.62
        cx_l, cy_l = cx_n, cy_n + num.height / 2 + 50 * u
    else:
        cx_i, cy_i = x0 + w * 0.24, y0 + h * 0.5
        cx_n, cy_n = x0 + w * 0.62, y0 + h * 0.46
        cx_l, cy_l = cx_n, cy_n + num.height / 2 + 55 * u
    if s.get("clip") and clips3d.existe(s["clip"]) and not vertical:
        clips3d.panel_clip(lienzo, (x0 + 50 * u, y0 + 110 * u, w * 0.5, h - 220 * u), s["clip"], t, dur, u,
                           coste=v if dinero else None, color=col)
        cx_n, cx_l = x0 + w * 0.77, x0 + w * 0.77
        num = encajar(num, int(w * 0.42))
    elif dinero:
        por = 2.5 if "/mo" in suf else 25
        cols = 1 if v / por <= 22 else (2 if v / por <= 44 else 4)
        if vertical:
            pila_monedas(lienzo, x0 + w * 0.78, y0 + h * 0.42, v, t, u * 0.8, 0.2, por, 22, cols)
            _icono_animado(lienzo, s["icono"], int(200 * u), C["texto"], x0 + w * 0.3, cy_i, t, 0.0, col)
        else:
            n_mon = max(1, min(22 * cols, round(v / por)))
            base = y0 + h * 0.78
            alto_pila = (n_mon // cols) * int(110 * u * 0.18)
            cy_ic = max(y0 + h * 0.2, base - alto_pila - 150 * u)
            _icono_animado(lienzo, s["icono"], int(170 * u), C["texto"], cx_i, cy_ic, t, 0.0, col)
            pila_monedas(lienzo, cx_i, base, v, t, u, 0.25, por, 22, cols)
    elif pct:
        _anillo(lienzo, cx_i, cy_i, int(190 * u), v / 100 * pc, col, u)
        _icono_animado(lienzo, s["icono"], int(190 * u), C["texto"], cx_i, cy_i, t, 0.0, None)
    else:
        _icono_animado(lienzo, s["icono"], int(230 * u), C["texto"], cx_i, cy_i, t, 0.0, col)
    pn = ease_out(prog(t, 0.1, 0.5))
    pegar(lienzo, num, cx_n + (1 - pn) * 60 * u, cy_n, alfa=pn)
    pegar(lienzo, lab, cx_l, cy_l, alfa=prog(t, 0.45, 0.4))
    if s.get("fuente"):
        _fuente_pie(lienzo, caja, u, t, s["fuente"])


def _lineas(lienzo, lineas, cx, cy, u, t, ini, tam, ancho_max):
    sprites = [encajar(linea_rica(l, int(tam * u)), ancho_max) for l in lineas]
    alto = sum(s.height for s in sprites) + 20 * u * (len(sprites) - 1)
    y = cy - alto / 2
    for i, s in enumerate(sprites):
        p = ease_back(prog(t, ini + i * 0.18, 0.45))
        pegar(lienzo, s, cx, y + s.height / 2 + (1 - p) * 40 * u, alfa=min(1, p * 1.5), escala=0.9 + 0.1 * p)
        y += s.height + 20 * u
    return alto


def texto_escena(lienzo, caja, s, t, dur, u):
    x0, y0, w, h = caja
    cy = y0 + h * (0.55 if s.get("icono") else 0.5)
    if s.get("icono"):
        _icono_animado(lienzo, s["icono"], int(190 * u), C["frio"], x0 + w / 2, y0 + h * 0.26, t, 0.0, C["frio"])
    _lineas_cineticas(lienzo, s["lineas"], x0 + w / 2, cy + 20 * u, u, t, dur, 110, int(w * 0.88), 0.15)


def titulo(lienzo, caja, s, t, dur, u):
    x0, y0, w, h = caja
    _lineas_cineticas(lienzo, s["lineas"], x0 + w / 2, y0 + h * 0.3, u, t, min(dur, 2.0), 120, int(w * 0.9))
    iconos = s.get("iconos", [])
    por_fila = 6 if w > h else 4
    filas = (len(iconos) + por_fila - 1) // por_fila
    tam = int(110 * u)
    paso_x = min(w * 0.85 / por_fila, tam * 1.9)
    reparto = max(0.12, min(0.3, (dur - 1.0) / max(1, len(iconos))))
    for i, n in enumerate(iconos):
        fila, col = divmod(i, por_fila)
        cx = x0 + w / 2 + (col - (por_fila - 1) / 2) * paso_x
        cy = y0 + h * 0.62 + fila * tam * 1.6 - (filas - 1) * tam * 0.8
        color = C["calor"] if i >= len(iconos) - 3 else C["texto"]
        _icono_animado(lienzo, n, tam, color, cx, cy, t, 0.4 + i * reparto)


def fuente_escena(lienzo, caja, s, t, dur, u):
    x0, y0, w, h = caja
    pw, ph = int(min(w * 0.82, 1250 * u)), int(380 * u)
    p = ease_out(prog(t, 0.0, 0.5))
    cx, cy = x0 + w / 2, y0 + h / 2 + (1 - p) * 80 * u
    pegar(lienzo, caja_redondeada(pw, ph, int(30 * u), (245, 247, 250, 240)), cx, cy, alfa=p)
    oscuro = (15, 27, 45)
    pegar(lienzo, icono("description", int(120 * u), C["calor"]), cx - pw / 2 + 110 * u, cy - 40 * u, alfa=p)
    xt = cx - pw / 2 + 210 * u
    ancho_txt = int(pw - 250 * u)
    tit = encajar(texto(s["titulo"], int(58 * u), oscuro), ancho_txt)
    det = encajar(texto(s.get("detalle", ""), int(40 * u), (60, 80, 110), "Inter", "SemiBold"), ancho_txt)
    nota = encajar(texto(s.get("nota", ""), int(34 * u), (110, 125, 145), "Inter", "Medium"), ancho_txt)
    pegar(lienzo, tit, xt, cy - 85 * u, alfa=prog(t, 0.25, 0.3), ancla="l")
    pegar(lienzo, det, xt, cy - 5 * u, alfa=prog(t, 0.4, 0.3), ancla="l")
    pegar(lienzo, nota, xt, cy + 70 * u, alfa=prog(t, 0.6, 0.3), ancla="l")
    # sello «verified data» en el segundo tiempo
    ps = ease_back(prog(t, min(1.4, dur * 0.5), 0.4))
    sello = texto("OFFICIAL DATA", int(34 * u), C["ahorro"], "Inter", "Bold")
    pegar(lienzo, sello, cx + pw / 2 - sello.width / 2 - 40 * u, cy - ph / 2 - 30 * u, escala=max(0.01, ps), alfa=min(1, ps))


def formula(lienzo, caja, s, t, dur, u):
    x0, y0, w, h = caja
    partes = s["partes"]
    rev = s.get("revelar", len(partes))
    vertical = w < h * 1.2
    sprites = []
    for i, ptxt in enumerate(partes):
        op = ptxt in ("×", "=", "≈", "+", "÷")
        col = C["suave"] if op else (C["calor"] if i == len(partes) - 1 else (C["frio"] if i < rev else C["texto"]))
        sprites.append(texto(ptxt, int((90 if op else 70) * u), col))
    if vertical:
        alto = sum(s_.height for s_ in sprites) + 10 * u * len(sprites)
        y = y0 + h / 2 - alto / 2
        for i, sp in enumerate(sprites):
            sp = encajar(sp, int(w * 0.9))
            visible = i < rev
            p = ease_back(prog(t, i * 0.2, 0.4)) if visible else 1
            pegar(lienzo, sp, x0 + w / 2, y + sp.height / 2, alfa=1.0 if visible and p > 0 else 0.22,
                  escala=max(0.01, p) if visible else 1)
            y += sp.height + 10 * u
        return
    ancho = sum(sp.width for sp in sprites) + 40 * u * (len(sprites) - 1)
    k = min(1.0, w * 0.92 / ancho)
    x = x0 + w / 2 - ancho * k / 2
    for i, sp in enumerate(sprites):
        visible = i < rev
        p = ease_back(prog(t, i * 0.22, 0.4)) if visible else 1
        pegar(lienzo, sp, x + sp.width * k / 2, y0 + h / 2, alfa=1.0 if visible and p > 0 else 0.22,
              escala=max(0.01, p * k) if visible else k)
        x += (sp.width + 40 * u) * k
    # subrayado del resultado en el segundo tiempo
    if rev >= len(partes) - 1:
        pl = ease_out(prog(t, 0.2 * len(partes) + 0.3, 0.5))
        sp = sprites[-1]
        xr = x - (sp.width + 40 * u) * k + sp.width * k / 2
        largo = int(sp.width * k * pl)
        if largo > 2:
            pegar(lienzo, caja_redondeada(largo, int(10 * u), int(5 * u), C["calor"] + (255,)), xr, y0 + h / 2 + 70 * u)


def comparar(lienzo, caja, s, t, dur, u):
    x0, y0, w, h = caja
    a, b = s["a"], s["b"]
    vals = [v for v in (a[1], b[1]) if isinstance(v, (int, float))]
    vmax = max(vals) if vals else 1
    dec = s.get("decimales", 0)
    alto_max = h * 0.42
    base_y = y0 + h * 0.78
    ancho_barra = int(min(w * 0.18, 260 * u))
    if s.get("etiqueta"):
        pegar(lienzo, encajar(texto(s["etiqueta"], int(44 * u), C["suave"], "Inter", "SemiBold"), int(w * 0.8)),
              x0 + w / 2, y0 + h * 0.08, alfa=prog(t, 0, 0.3))
    for j, (item, cx) in enumerate([(a, x0 + w * 0.3), (b, x0 + w * 0.7)]):
        nombre, v, ic = item
        ini = 0.1 + j * 0.45
        col = C["frio"] if j == 0 else C["calor"]
        p = ease_out(prog(t, ini, 0.8))
        if isinstance(v, (int, float)):
            hb = max(4, int(alto_max * (v / vmax) * p))
            pegar(lienzo, caja_redondeada(ancho_barra, hb, int(16 * u), col + (255,)), cx, base_y - hb / 2)
            cad = f'{s.get("prefijo", "")}{fmt_num(v * p, dec)}{s.get("sufijo", "")}'
            vtxt = encajar(texto(cad, int(66 * u), C["texto"]), int(w * 0.42))
            pegar(lienzo, vtxt, cx, base_y - hb - 55 * u, alfa=prog(t, ini, 0.3))
            top = base_y - hb - 100 * u
        else:
            hb = int(alto_max * 0.6)
            pq = ease_back(prog(t, ini, 0.5))
            pegar(lienzo, caja_redondeada(ancho_barra, hb, int(16 * u), col + (70,)), cx, base_y - hb / 2, alfa=prog(t, ini, 0.3))
            pegar(lienzo, texto("?", int(150 * u), C["texto"]), cx, base_y - hb / 2, escala=max(0.01, pq))
            top = base_y - hb - 40 * u
        _icono_animado(lienzo, ic, int(110 * u), col, cx, min(top - 60 * u, y0 + h * 0.3), t, ini)
        nom = encajar(texto(nombre, int(46 * u), C["texto"], "Inter", "Bold"), int(w * 0.4))
        pegar(lienzo, nom, cx, base_y + 50 * u, alfa=prog(t, ini, 0.3))
    if s.get("fuente"):
        _fuente_pie(lienzo, caja, u, t, s["fuente"])


def barras(lienzo, caja, s, t, dur, u):
    x0, y0, w, h = caja
    items = s["items"]
    vmax = s.get("max") or max(i[1] for i in items)
    n = len(items)
    alto_fila = min(150 * u, h * 0.75 / n)
    y_ini = y0 + h * 0.5 - alto_fila * n / 2 + alto_fila / 2 + (20 * u if s.get("etiqueta") else 0)
    vertical = w < h * 1.2
    x_ic = x0 + w * (0.08 if not vertical else 0.09)
    x_lab = x_ic + 70 * u
    ancho_lab = w * (0.27 if not vertical else 0.36)
    x_bar = x_lab + ancho_lab + 20 * u
    largo_max = x0 + w * 0.92 - x_bar - 200 * u
    if s.get("etiqueta"):
        pegar(lienzo, encajar(texto(s["etiqueta"], int(44 * u), C["suave"], "Inter", "SemiBold"), int(w * 0.8)),
              x0 + w / 2, y_ini - alto_fila * 0.9, alfa=prog(t, 0, 0.3))
    reparto = min(0.35, max(0.12, (dur * 0.5) / n))
    for i, (nombre, v, ic) in enumerate(items):
        cy = y_ini + i * alto_fila
        ini = 0.1 + i * reparto
        p = ease_out(prog(t, ini, 0.7))
        col = C["calor"] if i == 0 else C["frio"]
        tam_ic = int(min(70 * u, alto_fila * 0.55))
        pegar(lienzo, icono(ic, tam_ic, col), x_ic, cy, alfa=prog(t, ini, 0.25))
        lab = encajar(texto(nombre, int(min(44 * u, alto_fila * 0.36)), C["texto"], "Inter", "SemiBold"), int(ancho_lab))
        pegar(lienzo, lab, x_lab, cy, alfa=prog(t, ini, 0.25), ancla="l")
        largo = max(4, int(largo_max * v / vmax * p))
        hb = int(alto_fila * 0.5)
        pegar(lienzo, caja_redondeada(largo, hb, hb // 2, col + (255,)), x_bar, cy, ancla="l")
        cad = f'{s.get("prefijo", "")}{fmt_num(v * p)}{s.get("sufijo", "")}'
        pegar(lienzo, texto(cad, int(min(48 * u, alto_fila * 0.4)), C["texto"]), x_bar + largo + 20 * u, cy,
              alfa=prog(t, ini + 0.2, 0.3), ancla="l")
    if s.get("nota"):
        pegar(lienzo, encajar(texto(s["nota"], int(30 * u), C["suave"], "Inter", "Medium"), int(w * 0.9)),
              x0 + w / 2, y0 + h - 50 * u, alfa=prog(t, 0.8, 0.4))


def iconos(lienzo, caja, s, t, dur, u):
    x0, y0, w, h = caja
    nombres = s["iconos"]
    etiquetas = s.get("etiquetas", [""] * len(nombres))
    n = len(nombres)
    vertical = w < h * 1.2
    tam = int((190 if n <= 3 else 150) * u * (0.85 if vertical and n > 3 else 1))
    paso = min(w * 0.88 / n, tam * 2.2)
    reparto = max(0.25, min(0.9, (dur * 0.6) / n))
    for i, (nom, et) in enumerate(zip(nombres, etiquetas)):
        cx = x0 + w / 2 + (i - (n - 1) / 2) * paso
        cy = y0 + h * 0.45
        ini = 0.05 + i * reparto
        col = C["calor"] if i == n - 1 and n > 1 else C["frio"]
        _icono_animado(lienzo, nom, tam, C["texto"] if nom.startswith("arrow") else col, cx, cy, t, ini,
                       None if nom.startswith("arrow") else col)
        if et:
            lab = encajar(texto(et, int(44 * u), C["texto"], "Inter", "Bold"), int(paso * 0.95))
            pegar(lienzo, lab, cx, cy + tam * 0.85, alfa=prog(t, ini + 0.15, 0.3))
        if s.get("tachar") == i:
            pt = prog(t, ini + 0.5, 0.3)
            if pt > 0:
                capa = Image.new("RGBA", lienzo.size, (0, 0, 0, 0))
                d = ImageDraw.Draw(capa)
                r = tam * 0.6
                d.line([(cx - r, cy - r), (cx - r + 2 * r * pt, cy - r + 2 * r * pt)], fill=C["rojo"] + (255,), width=int(16 * u))
                lienzo.alpha_composite(capa)


FOCO_POR_ICONO = {
    "local_laundry_service": "lavadora", "microwave": "microondas", "dishwasher": "lavavajillas",
    "mode_fan": "ventiladores", "skillet": "cocina", "tv": "tv", "lightbulb": "luz", "laundry": "secadora",
    "humidity_high": "deshumidificador", "water_heater": "termo", "heat": "calefaccion", "ac_unit": "aire",
    "pool": "piscina", "ev_station": "coche", "hot_tub": "jacuzzi", "shower": "ducha", "thermostat": "termostato",
}


def puesto(lienzo, caja, s, t, dur, u, maximo=505):
    """Puesto del ranking: la casa con la cámara en el aparato + puesto, nombre y coste contando."""
    x0, y0, w, h = caja
    vertical = w < h * 1.2
    n, coste = s["n"], s["coste"]
    col = C["calor"] if n <= 3 else C["frio"]
    foco = s.get("foco") or FOCO_POR_ICONO.get(s["icono"])
    if vertical:
        cc = (x0 + 40 * u, y0, w - 80 * u, h * 0.56)
        xr, ancho_r = x0 + w / 2, w * 0.9
        ys = [h * 0.64, h * 0.73, h * 0.85, h * 0.95]
    else:
        cc = (x0 + 50 * u, y0 + 110 * u, w * 0.56, h - 220 * u)
        xr, ancho_r = x0 + w * 0.8, w * 0.36
        ys = [h * 0.22, h * 0.36, h * 0.53, h * 0.66]
    pe = ease_out(prog(t, 0, 0.4))
    clip = "nevera" if foco == "nevera2" else foco
    if clips3d.existe(clip):  # el aparato en 3D si está en la biblioteca; si no, la casa
        clips3d.panel_clip(lienzo, cc, clip, t, dur, u, coste=coste, color=col)
    else:
        vista_casa(lienzo, cc, foco, t, dur, u, coste=coste, color=col)
    # columna derecha
    placa = texto(f"#{n}", int(150 * u), col)
    pegar(lienzo, halo(int(320 * u), col), xr, y0 + ys[0], alfa=pe)
    pegar(lienzo, placa, xr, y0 + ys[0], escala=max(0.01, ease_back(prog(t, 0.0, 0.4))))
    nombre = encajar(texto(s["nombre"], int(70 * u), C["texto"]), int(ancho_r))
    pegar(lienzo, nombre, xr + (1 - ease_out(prog(t, 0.2, 0.4))) * 80 * u, y0 + ys[1], alfa=prog(t, 0.2, 0.3))
    pc = ease_out(prog(t, 0.5, 1.2))
    precio = encajar(texto(f"${fmt_num(coste * pc)}", int(150 * u), col), int(ancho_r))
    pegar(lienzo, precio, xr, y0 + ys[2], alfa=prog(t, 0.45, 0.3), escala=1 + 0.06 * math.sin(math.pi * prog(t, 1.6, 0.4)))
    # segundo tiempo: al mes y comparación con el nº 1
    ini_b = min(1.8, dur * 0.45)
    pbar = ease_out(prog(t, ini_b, 0.8))
    if pbar > 0:
        mes = texto(f"per year · ≈ ${fmt_num(coste / 12, 1 if coste < 120 else 0)}/month", int(42 * u), C["texto"], "Inter", "Bold")
        pegar(lienzo, mes, xr, y0 + ys[3], alfa=pbar)
        bw = ancho_r
        by = y0 + ys[3] + 70 * u
        pegar(lienzo, caja_redondeada(int(bw), int(22 * u), int(11 * u), (255, 255, 255, 30)), xr - bw / 2, by, alfa=pbar, ancla="l")
        largo = max(6, int(bw * coste / maximo * pbar))
        pegar(lienzo, caja_redondeada(largo, int(22 * u), int(11 * u), col + (255,)), xr - bw / 2, by, ancla="l")
        ref = texto(f"vs #1: ${maximo}", int(30 * u), C["suave"], "Inter", "SemiBold")
        pegar(lienzo, ref, xr + bw / 2 - ref.width, by + 36 * u, alfa=pbar, ancla="l")


def casa_escena(lienzo, caja, s, t, dur, u):
    """La casa en corte: plano general («todos») o la cámara en un aparato, con texto opcional al lado."""
    x0, y0, w, h = caja
    vertical = w < h * 1.2
    lineas = s.get("lineas")
    foco = s.get("foco")
    if lineas and not vertical:
        vista_casa(lienzo, (x0 + 50 * u, y0 + 90 * u, w * 0.58, h - 180 * u), foco, t, dur, u, coste=s.get("coste"))
        _lineas_cineticas(lienzo, lineas, x0 + w * 0.81, y0 + h / 2, u, t, dur, 96, int(w * 0.36), 0.4)
    elif lineas:
        vista_casa(lienzo, (x0 + 40 * u, y0, w - 80 * u, h * 0.62), foco, t, dur, u, coste=s.get("coste"))
        _lineas_cineticas(lienzo, lineas, x0 + w / 2, y0 + h * 0.82, u, t, dur, 84, int(w * 0.9), 0.4)
    else:
        mw = w * (0.9 if vertical else 0.74)
        mh = h * (0.8 if vertical else 0.86)
        vista_casa(lienzo, (x0 + (w - mw) / 2, y0 + (h - mh) / 2, mw, mh), foco, t, dur, u, coste=s.get("coste"))


def contador_escena(lienzo, caja, s, t, dur, u):
    """Contador de la luz con la aguja girando y los kWh subiendo."""
    x0, y0, w, h = caja
    vertical = w < h * 1.2
    r = int((260 if vertical else 300) * u)
    if vertical:
        contador(lienzo, x0 + w / 2, y0 + h * 0.35, r, t, s["valor"], u, 0.1, s.get("unidad", "kWh"))
        cx, cy = x0 + w / 2, y0 + h * 0.78
    else:
        contador(lienzo, x0 + w * 0.3, y0 + h / 2, r, t, s["valor"], u, 0.1, s.get("unidad", "kWh"))
        cx, cy = x0 + w * 0.7, y0 + h / 2
    _lineas_cineticas(lienzo, s.get("lineas", []), cx, cy, u, t, dur, 90, int(w * (0.9 if vertical else 0.42)), 0.5)


ESCENAS = {
    "numero": numero,
    "texto": texto_escena,
    "titulo": titulo,
    "fuente": fuente_escena,
    "formula": formula,
    "comparar": comparar,
    "barras": barras,
    "iconos": iconos,
    "puesto": puesto,
    "casa": casa_escena,
    "contador": contador_escena,
}


def escalera(lienzo, ancho, alto, n_actual, u, alfa=1.0, total=15):
    """Columna de puestos a la derecha (formato largo, vídeos tipo lista) que marca dónde vamos."""
    x = ancho - 60 * u
    paso = alto * 0.7 / total
    y0 = alto * 0.15
    for i, n in enumerate(range(total, 0, -1)):
        y = y0 + i * paso
        if n == n_actual:
            col = C["calor"]
            pegar(lienzo, texto(f"{n}", int(30 * u), col, "Inter", "Bold"), x, y, alfa=alfa)
        else:
            hecho = n > n_actual if n_actual else False
            r = int(7 * u)
            punto = caja_redondeada(2 * r, 2 * r, r, (C["frio"] if hecho else (255, 255, 255)) + (200 if hecho else 60,))
            pegar(lienzo, punto, x, y, alfa=alfa)
