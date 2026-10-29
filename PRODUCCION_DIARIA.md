# Producción diaria

Este es el procedimiento que sigue cada sesión automática (y cualquier sesión a mano). Las reglas de fondo están en `CLAUDE.md`; aquí solo va el cómo.

## 0. Preparar el entorno (sesión nueva)
```bash
./instalar.sh            # crea .venv y descarga el modelo de voz si falta
. .venv/bin/activate
```

## 1. Decidir qué toca hoy
- Calendario por canal: **1 Short al día** y **2 vídeos largos por semana (lunes y jueves)**.
- Mira `canales/<canal>/publicados.csv` y `salida/` para saber qué está ya hecho y qué falta.
- Antes de producir Shorts nuevos, usa los derivados del último largo (2–3 por largo) que aún no estén hechos.
- Los lunes, además: informe semanal (sección 9 de CLAUDE.md) en `informes/AAAA-MM-DD.md`. Sin acceso a YouTube Analytics, pide las cifras al humano en el informe.

## 2. Producir un vídeo
1. Elige la idea de `ideas.csv` con más puntuación y estado `pendiente`. Comprueba en `publicados.csv` que la estructura no repite las 3 últimas.
2. Crea `canales/<canal>/videos/AAAA-MM-DD_<slug>/`.
3. Investiga con un mínimo de 3 fuentes fiables. Guarda los datos originales en `datos/` si son tablas, y apunta cada cifra y cada cálculo en `fuentes.md`.
4. Escribe `guion.yaml`: gancho, promesa, bloques con mini-gancho, recompensa y cierre. Los tipos de escena están en `motor/escenas.py`:
   `casa` (la casa en corte: `foco` = un aparato de `motor/casa.py` APARATOS, o `todos`; `lineas` opcional), `contador` (contador de la luz), `puesto`, `numero` (con `$` caen monedas; con `%` sale un anillo), `comparar`, `barras`, `iconos`, `formula`, `fuente`, `titulo` y `texto`.
   **Regla de estilo (petición del humano):** el vídeo tiene que ser visual. Nada de pantallas de solo texto salvo transiciones de menos de 2 s, como máximo un 10 % de las frases. Cada aparato que se nombra se enseña en la casa o con su icono animado, y cada cifra en dólares lleva monedas.
   Los iconos son nombres de Material Symbols (`recursos/iconos/*.codepoints`). En los largos, pon `capitulo:` en las frases donde empieza cada capítulo y añade `miniaturas:` con 3 variantes.
5. Escribe `licencias.md` (copia el de un vídeo anterior si los recursos son los mismos) y `metadatos.json`.
6. Monta el vídeo y las miniaturas:
   ```bash
   python -m motor.video canales/<canal>/videos/<carpeta>            # --prueba 6 para revisar solo el principio
   python -m motor.miniaturas canales/<canal>/videos/<carpeta>       # solo los largos
   ```
7. Control de calidad:
   ```bash
   python -m motor.control canales/<canal>/videos/<carpeta>
   ```
   Además, **mira** `visuales/mosaico_qc.png` (texto cortado, solapes, elementos fuera del cuadro) y las miniaturas. Si algo falla, corrígelo y repite. No publiques nada que no pase.
8. Prepara la subida:
   ```bash
   python -m motor.publicar canales/<canal>/videos/<carpeta> AAAA-MM-DD
   ```
   Esto crea `salida/AAAA-MM-DD/<carpeta>/` con el vídeo, las miniaturas, los subtítulos y `subir.txt`, y lo apunta en `publicados.csv`.
9. Marca la idea como `hecha` en `ideas.csv` y añade ideas nuevas para que siempre haya 20 pendientes.

## 3. Entregar y guardar
- Envía al humano los archivos de `salida/AAAA-MM-DD/` (vídeo y miniaturas) con un mensaje corto: qué es, cuándo publicarlo y qué ajustes poner (está en `subir.txt`).
- Apunta una línea por tarea en `registro.md`.
- Haz commit y push a `master` de todo menos los `.mp4` y `.wav` (ya están en `.gitignore`).

## Si algo se rompe
- Si falla el montaje, `--sin-cache` regenera la voz y las escenas desde cero.
- Si un dato no se puede verificar, quítalo del guion. No lo inventes.
- Si hay que gastar dinero, crear cuentas o tocar ajustes de YouTube o Google, no lo hagas: apúntalo y pregunta al humano.
