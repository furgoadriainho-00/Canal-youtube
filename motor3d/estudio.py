"""Plató 3D del canal en Blender: un aparato en un estudio con los colores de la marca y una cámara
que se mueve despacio a su alrededor. Se ejecuta DENTRO de Blender:

    blender -b --python motor3d/estudio.py -- <aparato> <salida_dir> [--fotogramas N] [--fijo F]

Los aparatos salen de modelos CC0 de Poly Haven (recursos/3d/) o se modelan aquí por código.
"""
import math
import sys
from pathlib import Path

import bpy
from mathutils import Vector

RAIZ = Path(__file__).resolve().parent.parent
R3D = RAIZ / "recursos" / "3d"

NAVY = (0.012, 0.03, 0.07, 1)
NARANJA = (1.0, 0.33, 0.05, 1)
AZUL = (0.08, 0.55, 0.85, 1)


# ---------- materiales ----------

def mat(nombre, color, rugosidad=0.4, metal=0.0, emision=None, fuerza=0.0, transmision=0.0):
    m = bpy.data.materials.get(nombre)
    if m:
        return m
    m = bpy.data.materials.new(nombre)
    m.use_nodes = True
    p = m.node_tree.nodes["Principled BSDF"]
    p.inputs["Base Color"].default_value = color
    p.inputs["Roughness"].default_value = rugosidad
    p.inputs["Metallic"].default_value = metal
    if transmision:
        p.inputs["Transmission Weight"].default_value = transmision
    if emision:
        p.inputs["Emission Color"].default_value = emision
        p.inputs["Emission Strength"].default_value = fuerza
    return m


def M():
    return {
        "esmalte": mat("esmalte", (0.85, 0.87, 0.9, 1), 0.25),
        "inox": mat("inox", (0.72, 0.74, 0.77, 1), 0.28, 0.9),
        "negro": mat("negro", (0.02, 0.02, 0.025, 1), 0.35),
        "cristal": mat("cristal", (0.6, 0.75, 0.85, 1), 0.05, 0, transmision=0.9),
        "pantalla": mat("pantalla", (0, 0, 0, 1), 0.2, 0, emision=(0.2, 0.8, 1.0, 1), fuerza=4),
        "led_naranja": mat("led_naranja", (0, 0, 0, 1), 0.3, 0, emision=NARANJA, fuerza=6),
        "cobre": mat("cobre", (0.85, 0.45, 0.25, 1), 0.3, 1.0),
        "gris": mat("gris", (0.35, 0.37, 0.4, 1), 0.5),
        "blanco_mate": mat("blanco_mate", (0.9, 0.9, 0.9, 1), 0.7),
    }


# ---------- piezas ----------

def caja(nombre, tam, pos, material, bisel=0.02):
    bpy.ops.mesh.primitive_cube_add(size=1, location=pos)
    o = bpy.context.object
    o.name = nombre
    o.scale = tam
    bpy.ops.object.transform_apply(scale=True)
    if bisel:
        b = o.modifiers.new("bisel", "BEVEL")
        b.width = bisel
        b.segments = 4
    o.data.materials.append(material)
    bpy.ops.object.shade_smooth()
    return o


def cilindro(nombre, r, h, pos, material, rot=(0, 0, 0), vertices=48, bisel=0.01):
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=h, location=pos, rotation=rot, vertices=vertices)
    o = bpy.context.object
    o.name = nombre
    if bisel:
        b = o.modifiers.new("bisel", "BEVEL")
        b.width = bisel
        b.segments = 3
    o.data.materials.append(material)
    bpy.ops.object.shade_smooth()
    return o


def toro(nombre, r1, r2, pos, material, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_torus_add(major_radius=r1, minor_radius=r2, location=pos, rotation=rot)
    o = bpy.context.object
    o.name = nombre
    o.data.materials.append(material)
    bpy.ops.object.shade_smooth()
    return o


def agrupar(nombre, objs):
    raiz = bpy.data.objects.new(nombre, None)
    bpy.context.collection.objects.link(raiz)
    for o in objs:
        o.parent = raiz
    return raiz


# ---------- aparatos modelados por código (frente hacia -Y) ----------

def nevera(m):
    p = [caja("cuerpo", (0.8, 0.7, 1.8), (0, 0, 0.9), m["inox"]),
         caja("puerta_alta", (0.8, 0.04, 1.15), (0, -0.37, 1.22), m["inox"], 0.015),
         caja("puerta_baja", (0.8, 0.04, 0.6), (0, -0.37, 0.32), m["inox"], 0.015),
         caja("asa1", (0.03, 0.05, 0.6), (0.33, -0.42, 1.2), m["negro"], 0.01),
         caja("asa2", (0.03, 0.05, 0.3), (0.33, -0.42, 0.45), m["negro"], 0.01),
         caja("panel", (0.18, 0.01, 0.1), (-0.2, -0.395, 1.55), m["pantalla"], 0.005)]
    return agrupar("nevera", p)


def congelador(m):
    p = [caja("cuerpo", (1.1, 0.7, 0.85), (0, 0, 0.425), m["esmalte"]),
         caja("tapa", (1.12, 0.72, 0.06), (0, 0, 0.88), m["esmalte"], 0.02),
         caja("asa", (0.3, 0.05, 0.03), (0, -0.38, 0.84), m["gris"], 0.01),
         caja("led", (0.06, 0.01, 0.03), (0.4, -0.355, 0.75), m["pantalla"], 0.003)]
    return agrupar("congelador", p)


def lavadora(m, secadora=False):
    p = [caja("cuerpo", (0.6, 0.6, 0.85), (0, 0, 0.425), m["esmalte"]),
         caja("panel", (0.6, 0.02, 0.12), (0, -0.305, 0.77), m["blanco_mate"], 0.01),
         cilindro("mando", 0.04, 0.03, (0.18, -0.32, 0.77), m["inox"], rot=(math.pi / 2, 0, 0)),
         caja("display", (0.14, 0.01, 0.05), (-0.1, -0.318, 0.77), m["pantalla"], 0.004),
         toro("aro", 0.2, 0.035, (0, -0.31, 0.38), m["inox"], rot=(math.pi / 2, 0, 0)),
         cilindro("ojo", 0.19, 0.02, (0, -0.31, 0.38), m["cristal"] if not secadora else m["negro"], rot=(math.pi / 2, 0, 0))]
    return agrupar("secadora" if secadora else "lavadora", p)


def lavavajillas(m):
    p = [caja("cuerpo", (0.6, 0.6, 0.85), (0, 0, 0.425), m["inox"]),
         caja("puerta", (0.6, 0.03, 0.72), (0, -0.31, 0.38), m["inox"], 0.01),
         caja("asa", (0.4, 0.04, 0.03), (0, -0.345, 0.7), m["negro"], 0.01),
         caja("panel", (0.6, 0.02, 0.1), (0, -0.3, 0.8), m["negro"], 0.01),
         caja("display", (0.1, 0.01, 0.04), (0.15, -0.312, 0.8), m["pantalla"], 0.004)]
    return agrupar("lavavajillas", p)


def termo(m):
    p = [cilindro("cuerpo", 0.3, 1.4, (0, 0, 0.75), m["esmalte"], bisel=0.04),
         cilindro("tapa", 0.31, 0.06, (0, 0, 1.47), m["gris"]),
         cilindro("base", 0.31, 0.06, (0, 0, 0.05), m["gris"]),
         cilindro("tubo_frio", 0.025, 0.5, (-0.12, 0, 1.7), m["cobre"]),
         cilindro("tubo_caliente", 0.025, 0.5, (0.12, 0, 1.7), m["cobre"]),
         caja("etiqueta", (0.2, 0.01, 0.25), (0, -0.298, 0.9), m["led_naranja"], 0.005)]
    return agrupar("termo", p)


def deshumidificador(m):
    p = [caja("cuerpo", (0.38, 0.28, 0.62), (0, 0, 0.33), m["esmalte"], 0.05),
         caja("rejilla", (0.3, 0.01, 0.2), (0, -0.142, 0.48), m["gris"], 0.01),
         caja("deposito", (0.34, 0.01, 0.22), (0, -0.142, 0.17), m["cristal"], 0.01),
         caja("display", (0.12, 0.01, 0.04), (0, -0.142, 0.6), m["pantalla"], 0.004)]
    return agrupar("deshumidificador", p)


def contador(m):
    p = [caja("caja", (0.32, 0.18, 0.45), (0, 0, 1.2), m["gris"], 0.03),
         cilindro("visor", 0.12, 0.05, (0, -0.1, 1.25), m["cristal"], rot=(math.pi / 2, 0, 0)),
         caja("digitos", (0.16, 0.01, 0.05), (0, -0.13, 1.25), m["pantalla"], 0.004),
         cilindro("tubo", 0.03, 1.0, (0, 0, 0.5), m["gris"])]
    return agrupar("contador", p)


def tv(m):
    pantalla = mat("tv_pantalla", (0, 0, 0, 1), 0.15, emision=(1, 1, 1, 1), fuerza=1.3)
    img = RAIZ / "canales/how-your-home-works/marca/banner_2560x1440.jpg"
    if img.exists():  # la tele enseña la imagen del propio canal
        nt = pantalla.node_tree
        tex = nt.nodes.new("ShaderNodeTexImage")
        tex.image = bpy.data.images.load(str(img))
        nt.links.new(tex.outputs["Color"], nt.nodes["Principled BSDF"].inputs["Emission Color"])
    p = [caja("marco", (1.25, 0.05, 0.74), (0, 0, 0.95), m["negro"], 0.01),
         caja("pantalla", (1.2, 0.01, 0.69), (0, -0.027, 0.95), pantalla, 0.002),
         caja("pie", (0.35, 0.22, 0.02), (0, 0.02, 0.51), m["negro"], 0.005),
         caja("cuello", (0.06, 0.04, 0.08), (0, 0.02, 0.56), m["negro"], 0.005),
         caja("mueble", (1.6, 0.42, 0.5), (0, 0.05, 0.25), mat("madera", (0.35, 0.22, 0.13, 1), 0.5), 0.02)]
    return agrupar("tv", p)


def split(m):
    p = [caja("cuerpo", (0.95, 0.24, 0.3), (0, 0, 1.6), m["esmalte"], 0.06),
         caja("rejilla", (0.85, 0.02, 0.05), (0, -0.115, 1.48), m["gris"], 0.01),
         caja("display", (0.08, 0.01, 0.03), (0.33, -0.122, 1.63), m["pantalla"], 0.004),
         caja("pared", (2.4, 0.05, 2.2), (0, 0.15, 1.1), mat("pared", (0.06, 0.1, 0.17, 1), 0.8), 0)]
    return agrupar("aire", p)


def microondas(m):
    p = [caja("cuerpo", (0.5, 0.38, 0.3), (0, 0, 0.15 + 0.9), m["inox"], 0.02),
         caja("puerta", (0.36, 0.01, 0.24), (-0.06, -0.192, 1.05), m["negro"], 0.01),
         caja("panel", (0.1, 0.01, 0.24), (0.19, -0.192, 1.05), m["negro"], 0.01),
         caja("display", (0.07, 0.008, 0.03), (0.19, -0.199, 1.13), m["pantalla"], 0.003),
         caja("encimera", (1.4, 0.6, 0.9), (0, 0.05, 0.45), mat("encimera", (0.75, 0.73, 0.7, 1), 0.35), 0.02)]
    return agrupar("microondas", p)


def radiador(m):
    p = [caja("panel", (1.0, 0.1, 0.55), (0, 0, 0.45), m["esmalte"], 0.03)]
    for i in range(9):
        p.append(caja(f"aleta{i}", (0.02, 0.015, 0.45), (-0.4 + i * 0.1, -0.055, 0.45), m["blanco_mate"], 0.005))
    p.append(caja("termostato", (0.05, 0.03, 0.08), (0.42, -0.07, 0.62), m["led_naranja"], 0.005))
    p.append(caja("pared", (2.4, 0.05, 2.0), (0, 0.15, 1.0), mat("pared", (0.06, 0.1, 0.17, 1), 0.8), 0))
    return agrupar("calefaccion", p)


PROCEDURALES = {"tv": tv, "aire": split, "microondas": microondas, "calefaccion": radiador, "nevera": nevera, "nevera2": nevera, "congelador": congelador, "lavadora": lavadora,
                "secadora": lambda m: lavadora(m, True), "lavavajillas": lavavajillas, "termo": termo,
                "deshumidificador": deshumidificador, "medidor": contador}

# aparato -> (modelo de Poly Haven, altura en metros)
POLYHAVEN = {"cocina": ("electric_stove", 0.9), "ventiladores": ("ceiling_fan", 0.45),
             "luz": ("lightbulb_led", 0.25)}


def cargar_polyhaven(nombre, altura):
    d = R3D / nombre
    gltf = next(d.glob("*.gltf"))
    antes = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=str(gltf))
    nuevos = [o for o in bpy.data.objects if o not in antes]
    raiz = agrupar(nombre, [o for o in nuevos if o.parent is None])
    bpy.context.view_layer.update()
    pts = [o.matrix_world @ Vector(c) for o in nuevos if o.type == "MESH" for c in o.bound_box]
    zmin, zmax = min(p.z for p in pts), max(p.z for p in pts)
    cx = (min(p.x for p in pts) + max(p.x for p in pts)) / 2
    cy = (min(p.y for p in pts) + max(p.y for p in pts)) / 2
    k = altura / (zmax - zmin)
    raiz.scale = (k, k, k)
    raiz.location = (-cx * k, -cy * k, -zmin * k)
    return raiz


# ---------- plató ----------

def plato():
    sc = bpy.context.scene
    # suelo y fondo curvo (ciclorama) en azul noche
    bpy.ops.mesh.primitive_plane_add(size=1)
    o = bpy.context.object
    me = o.data
    import bmesh
    bm = bmesh.new()
    perfil = [(y, 0.0) for y in [-6, -2, 0.5, 1.5]] + [(1.5 + 1.2 * math.sin(a), 1.2 - 1.2 * math.cos(a))
                                                     for a in [math.pi / 8 * i for i in range(1, 5)]] + [(2.7, 4.0)]
    filas = [[bm.verts.new((x, y, z)) for x in (-8, 8)] for (y, z) in perfil]
    for a, b in zip(filas, filas[1:]):
        bm.faces.new((a[0], a[1], b[1], b[0]))
    bm.to_mesh(me)
    bm.free()
    o.name = "ciclorama"
    o.data.materials.clear()
    o.data.materials.append(mat("fondo", (0.008, 0.018, 0.04, 1), 0.7))
    bpy.ops.object.shade_smooth()
    # línea de luz naranja en el suelo (detalle de marca)
    caja("tira", (3.0, 0.03, 0.005), (0, -0.9, 0.003), mat("tira", (0, 0, 0, 1), 0.3, emision=NARANJA, fuerza=8), 0)
    # luces: principal, contra naranja, relleno azul
    def luz(nombre, tipo, pos, energia, color, tam=1.0):
        bpy.ops.object.light_add(type=tipo, location=pos)
        l = bpy.context.object
        l.name = nombre
        l.data.energy = energia
        l.data.color = color[:3]
        if tipo == "AREA":
            l.data.size = tam
        d = Vector((0, 0, 0.8)) - l.location
        l.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()
        return l
    luz("principal", "AREA", (-2.5, -3.0, 3.2), 700, (1, 0.96, 0.9), 2.0)
    luz("contra", "AREA", (2.2, 1.6, 2.6), 450, NARANJA, 1.0)
    luz("relleno", "AREA", (3.0, -2.5, 1.2), 160, AZUL, 2.0)
    # entorno HDRI suave
    w = bpy.data.worlds.new("mundo")
    sc.world = w
    w.use_nodes = True
    nt = w.node_tree
    env = nt.nodes.new("ShaderNodeTexEnvironment")
    env.image = bpy.data.images.load(str(R3D / "studio_small_09_1k.hdr"))
    nt.links.new(env.outputs["Color"], nt.nodes["Background"].inputs["Color"])
    nt.nodes["Background"].inputs["Strength"].default_value = 0.08


def camara(caja_obj, fotogramas, giro=0.5):
    sc = bpy.context.scene
    (x0, x1), (z0, z1) = caja_obj
    objetivo_alto = z1
    alto_vis = max(0.9, max(z1 - z0, (x1 - x0) * 0.5625) * 1.4)  # margen alrededor del aparato
    dist = alto_vis / (2 * math.tan(math.radians(22.9) / 2))
    centro = Vector(((x0 + x1) / 2, 0, (z0 + z1) / 2))
    bpy.ops.object.empty_add(location=centro)
    obj = bpy.context.object
    bpy.ops.object.camera_add()
    cam = bpy.context.object
    cam.data.lens = 50
    cam.data.dof.use_dof = True
    cam.data.dof.focus_object = obj
    cam.data.dof.aperture_fstop = 4.0
    tr = cam.constraints.new("TRACK_TO")
    tr.target = obj
    tr.track_axis = "TRACK_NEGATIVE_Z"
    tr.up_axis = "UP_Y"
    sc.camera = cam
    for f, k in [(1, 0.0), (fotogramas, 1.0)]:
        ang = -math.pi / 2 - giro / 2 + giro * k  # gira de izquierda a derecha por delante
        d = dist * (1.0 - 0.12 * k)               # y se acerca un poco
        cam.location = (centro.x + math.cos(ang) * d, math.sin(ang) * d, centro.z + (z1 - z0) * 0.25 + 0.2)
        cam.keyframe_insert("location", frame=f)
    for fc in cam.animation_data.action.fcurves:
        for kp in fc.keyframe_points:
            kp.interpolation = "SINE"
    return cam


def render_cfg(salida, fotogramas, ancho=1280, alto=720, muestras=8):
    sc = bpy.context.scene
    sc.render.engine = "CYCLES"
    c = sc.cycles
    c.device = "CPU"
    c.samples = muestras
    c.use_adaptive_sampling = True
    c.use_denoising = True
    c.denoiser = "OPENIMAGEDENOISE"
    c.max_bounces, c.diffuse_bounces, c.glossy_bounces, c.transmission_bounces = 4, 2, 2, 2
    sc.render.use_persistent_data = True
    sc.render.resolution_x, sc.render.resolution_y = ancho, alto
    sc.render.fps = 30
    sc.frame_start, sc.frame_end = 1, fotogramas
    sc.view_settings.view_transform = "AgX"
    sc.view_settings.look = "AgX - Medium High Contrast"
    sc.render.image_settings.file_format = "PNG"
    sc.render.filepath = str(Path(salida) / "f_")


def construir(aparato, fotogramas):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    plato()
    m = M()
    if aparato in PROCEDURALES:
        raiz = PROCEDURALES[aparato](m)
    else:
        nombre, altura = POLYHAVEN[aparato]
        raiz = cargar_polyhaven(nombre, altura)
        if aparato == "ventiladores":
            raiz.location.z += 1.0
    bpy.context.view_layer.update()
    pts = [o.matrix_world @ Vector(c) for o in bpy.data.objects
           if o.type == "MESH" and o.name not in ("ciclorama", "tira") and not o.name.startswith(("pared", "mueble", "encimera"))
           for c in o.bound_box]
    camara(((min(p.x for p in pts), max(p.x for p in pts)), (min(p.z for p in pts), max(p.z for p in pts))), fotogramas)
    return raiz


if __name__ == "__main__":
    args = sys.argv[sys.argv.index("--") + 1:]
    aparato, salida = args[0], args[1]
    n = int(args[args.index("--fotogramas") + 1]) if "--fotogramas" in args else 120
    construir(aparato, n)
    render_cfg(salida, n)
    if "--fijo" in args:
        f = int(args[args.index("--fijo") + 1])
        bpy.context.scene.frame_set(f)
        bpy.context.scene.render.filepath = str(Path(salida) / f"fijo_{aparato}.png")
        bpy.ops.render.render(write_still=True)
    else:
        bpy.ops.render.render(animation=True)
