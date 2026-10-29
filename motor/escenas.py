"""Tipos de escena. Cada función dibuja un fotograma: (lienzo, caja, spec, t, dur, u).

caja = (x0, y0, ancho, alto) zona donde va el contenido; u = escala (1 en 1920×1080).
Los elementos entran escalonados para que haya movimiento continuo, y las escenas largas
añaden un segundo tiempo a mitad para que la imagen cambie cada 2–4 s.
"""
from PIL import Image, ImageDraw

from .graficos import (COLORES, icono, texto, linea_rica, encajar, prog, ease_out, ease_back,
                       pegar, caja_redondeada, halo, fmt_num)

C = COLORES


def _color(nombre):
    return C.get(nombre or "calor", C["calor"])


def _fuente_pie(lienzo, caja, u, t, cadena):
    x0, y0, w, h = caja
    s = encajar(texto("Source: " + cadena, int(30 * u), C["suave"], "Inter", "Medium"), int(w * 0.9))
    pegar(lienzo, s, x0 + w / 2, y0 + h - 50 * u, alfa=prog(t, 0.5, 0.4))


def _icono_animado(lienzo, nombre, tam, color, cx, cy, t, ini=0.0, halo_col=None):
    p = ease_back(prog(t, ini, 0.45))
    if halo_col:
        pegar(lienzo, halo(int(tam * 1.9), halo_col), cx, cy, alfa=prog(t, ini, 0.5), escala=max(0.01, p))
    flot = 6 * (t * 0.7 % 2 - 1) ** 2  # ligero balanceo
    pegar(lienzo, icono(nombre, tam, color), cx, cy - flot, escala=max(0.01, p))


def numero(lienzo, caja, s, t, dur, u):
    x0, y0, w, h = caja
    col = _color(s.get("color"))
    vertical = w < h * 1.2
    v = s["valor"]
    dec = s.get("decimales", 0)
    contar = isinstance(v, (int, float)) and not any(ch.isdigit() for ch in s.get("prefijo", ""))
    valor = v * ease_out(prog(t, 0.15, 0.9)) if contar else v
    cad = f'{s.get("prefijo", "")}{fmt_num(valor, dec) if isinstance(valor, (int, float)) else valor}{s.get("sufijo", "")}'
    num = encajar(texto(cad, int(200 * u), col), int(w * (0.86 if vertical else 0.55)))
    lab = encajar(texto(s.get("etiqueta", ""), int(52 * u), C["texto"], "Inter", "SemiBold"), int(w * 0.85))
    if vertical:
        cx_i, cy_i = x0 + w / 2, y0 + h * 0.28
        cx_n, cy_n = x0 + w / 2, y0 + h * 0.6
        cy_l = cy_n + num.height / 2 + 50 * u
        cx_l = cx_n
    else:
        cx_i, cy_i = x0 + w * 0.25, y0 + h * 0.5
        cx_n, cy_n = x0 + w * 0.62, y0 + h * 0.46
        cx_l, cy_l = cx_n, cy_n + num.height / 2 + 55 * u
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
        _icono_animado(lienzo, s["icono"], int(150 * u), C["frio"], x0 + w / 2, y0 + h * 0.24, t, 0.0, C["frio"])
    _lineas(lienzo, s["lineas"], x0 + w / 2, cy, u, t, 0.1, 110, int(w * 0.88))


def titulo(lienzo, caja, s, t, dur, u):
    x0, y0, w, h = caja
    _lineas(lienzo, s["lineas"], x0 + w / 2, y0 + h * 0.3, u, t, 0.0, 120, int(w * 0.9))
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


def puesto(lienzo, caja, s, t, dur, u, maximo=505):
    x0, y0, w, h = caja
    vertical = w < h * 1.2
    n, coste = s["n"], s["coste"]
    col = C["calor"] if n <= 3 else C["frio"]
    # placa del puesto
    pb = ease_back(prog(t, 0.0, 0.4))
    placa = texto(f"#{n}", int(170 * u), col)
    cx_p, cy_p = (x0 + w * 0.17, y0 + h * 0.42) if not vertical else (x0 + w * 0.22, y0 + h * 0.18)
    pegar(lienzo, halo(int(380 * u), col), cx_p, cy_p, alfa=prog(t, 0, 0.4))
    pegar(lienzo, placa, cx_p, cy_p, escala=max(0.01, pb))
    # icono y nombre
    cx_i, cy_i = (x0 + w * 0.42, y0 + h * 0.42) if not vertical else (x0 + w * 0.7, y0 + h * 0.18)
    _icono_animado(lienzo, s["icono"], int(210 * u), C["texto"], cx_i, cy_i, t, 0.15)
    nombre = encajar(texto(s["nombre"], int(76 * u), C["texto"]), int(w * (0.42 if not vertical else 0.9)))
    pc = ease_out(prog(t, 0.35, 1.0))
    cad = f"${fmt_num(coste * pc)}"
    precio = texto(cad, int(150 * u), col)
    sub = texto("per year", int(44 * u), C["suave"], "Inter", "SemiBold")
    if not vertical:
        xr = x0 + w * 0.56
        pegar(lienzo, nombre, xr, y0 + h * 0.3, alfa=prog(t, 0.25, 0.3), ancla="l")
        pegar(lienzo, precio, xr, y0 + h * 0.46, alfa=prog(t, 0.35, 0.3), ancla="l")
        pegar(lienzo, sub, xr + precio.width + 20 * u, y0 + h * 0.49, alfa=prog(t, 0.6, 0.3), ancla="l")
    else:
        pegar(lienzo, nombre, x0 + w / 2, y0 + h * 0.38, alfa=prog(t, 0.25, 0.3))
        pegar(lienzo, precio, x0 + w / 2, y0 + h * 0.52, alfa=prog(t, 0.35, 0.3))
        pegar(lienzo, sub, x0 + w / 2, y0 + h * 0.62, alfa=prog(t, 0.6, 0.3))
    # segundo tiempo: barra frente al nº 1
    ini_b = min(1.6, dur * 0.45)
    pbar = ease_out(prog(t, ini_b, 0.8))
    if pbar > 0:
        bx0, bw = x0 + w * 0.12, w * 0.76
        by = y0 + h * (0.74 if not vertical else 0.78)
        pegar(lienzo, caja_redondeada(int(bw), int(26 * u), int(13 * u), (255, 255, 255, 30)), bx0, by, alfa=pbar, ancla="l")
        largo = max(6, int(bw * coste / maximo * pbar))
        pegar(lienzo, caja_redondeada(largo, int(26 * u), int(13 * u), col + (255,)), bx0, by, ancla="l")
        ref = texto(f"#1 = ${maximo}/yr", int(34 * u), C["suave"], "Inter", "SemiBold")
        pegar(lienzo, ref, bx0 + bw - ref.width, by + 45 * u, alfa=pbar, ancla="l")
        mes = texto(f"≈ ${fmt_num(coste / 12, 1 if coste < 120 else 0)}/month", int(40 * u), C["texto"], "Inter", "Bold")
        pegar(lienzo, mes, bx0, by + 50 * u, alfa=pbar, ancla="l")


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
