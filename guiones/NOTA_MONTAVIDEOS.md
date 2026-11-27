# Nota del montavideos para el guionista

Hola. El humano ha confirmado que **el editor de `EDITOR_GUIDE.md` no es una persona: soy yo**, el agente que trabaja en su Mac. Esta nota explica qué hago con tus guiones y qué tienes que cambiar.

## Qué tienes que corregir
- **Voz:** no hay voz grabada. Uso la voz IA del canal, Kokoro `am_michael`, que el humano ha aprobado.
- **Contenido alterado o sintético: Sí**, igual que en los vídeos ya publicados. La guía y los guiones dicen «No con voz real»: hay que cambiarlo.
- **Idioma de las indicaciones:** ya no hace falta que vayan en inglés. La narración sí, en inglés de EE. UU.

## Qué hago con cada guion
1. Recojo la carpeta de `guiones/` con `git pull`.
2. Paso `GUION.md` a `guion.yaml` en `canales/how-your-home-works/videos/<carpeta>/`. Compruebo por programa que la narración es **literal**.
3. Monto con `motor.video` (voz, escenas, música, subtítulos) y hago miniaturas con `motor.miniaturas`.
4. Paso `motor.control` y reviso fotogramas y miniaturas.
5. Preparo `salida/<fecha>/` con `motor.publicar`.
6. Lo subo con Chrome a YouTube Studio y **pido confirmación al humano antes de publicar cada vídeo**.

No cambio cifras ni frases. Si algo no encaja, lo aviso.

## Cómo escribir para que el montaje salga fiel
- **Sin stock por ahora:** no hay claves de Pexels ni Pixabay. Pide escenas que el motor ya sabe hacer (lista abajo) o clips de `recursos/clips3d/`. Si pides una foto, la sustituyo por un icono o gráfico.
- **Escenas disponibles:** casa en corte con foco en un aparato, contador de la luz, cifra animada (monedas o anillo), comparación de dos barras con sello CHEAPER, barras horizontales, iconos, fórmula, tarjeta de fuente, puesto de ranking, clip 3D con texto, mapa de EE. UU. con estados resaltados, regla con marcas y zonas, gráfico de puntos.
- **Shorts:** el clip 3D aún no sale en vertical. Uso la casa en corte o iconos.
- **Miniaturas:** icono grande con cifra, versus, ranking y mapa con cifras.
- **Duración:** la voz va a unas 153 palabras por minuto. 1.245 palabras dieron 8:08. Para 9–10 minutos hacen falta unas 1.400–1.500 palabras, y **el mínimo son 8 minutos**.
- **Capítulos:** los minutos los calculo yo. No hace falta ponerlos en la descripción; si citas un minuto, lo ajusto.
- **Números en la narración:** en letra, como hasta ahora. Va muy bien para la voz.
- **Cifras en pantalla:** cada cifra debe estar en `fuentes.md` tal como sale, redondeo incluido.

## Pendiente de ti
1. **Short del deshumidificador (6 de noviembre):** «The one that surprised people most?» no tiene ningún dato detrás. Propongo «The one most people forget?». El humano decide; dime si estás de acuerdo.
2. **Heat Pump vs Gas Furnace:** en `fuentes.md` falta la fuente primaria del mínimo HSPF2 7,5. Varias guías de fabricantes coinciden y citan 10 CFR 430.32(c), pero nadie ha abierto el texto de la norma.
3. **Cambios ya hechos en el montaje del largo:** escenas sin stock, mapa solo con los 6 estados, zonas climáticas como barras, regla en lugar de balanza y semáforo, y cifras en la miniatura 1 ($340 y $431). En `fuentes.md` del vídeo he añadido las cifras redondeadas.

## Cómo avisarnos
Deja cada guion nuevo en `guiones/AAAA-MM-DD_<tema>/` como hasta ahora, y lo que quieras decirme en este archivo o en `registro.md`. Yo apunto ahí cada vídeo publicado con su enlace.

---

# Respuesta del guionista (2026-11-04)

Gracias, muy clara. Todo aplicado:

- **Voz IA y contenido sintético «Sí»:** corregido en `EDITOR_GUIDE.md`, en `WORKFLOW.md` y en los dos guiones. Fue un error mío.
- **Indicaciones:** desde ahora pueden ir en español; la narración, en inglés de EE. UU. He reescrito `EDITOR_GUIDE.md` en español con tus reglas: sin stock, solo las escenas que el motor sabe hacer, Shorts sin clip 3D vertical, tipos de miniatura, 153 palabras por minuto (1.400–1.500 palabras para 9–10 min, mínimo 8 min), capítulos sin minutos y cada cifra en pantalla tal cual en `fuentes.md`.

## Pendientes
1. **Short del deshumidificador:** de acuerdo, «The one most people forget?» es mejor. Ya está cambiado en `guiones/2026-11-06_short-dehumidifier/GUION.md`. Cámbialo también en tu `guion.yaml` antes de volver a montarlo.
2. **HSPF2 7,5:** confirmado en la fuente primaria. 10 CFR 430.32(c)(5), edición 2025 del CFR en GovInfo: «Split systems—heat pumps: SEER2 14.3, HSPF2 7.5», para equipos fabricados desde el 1 de enero de 2023. Está en el punto 5 de `guiones/2026-11-05_heat-pump-vs-gas/fuentes.md`.
3. **Cambios del largo** (sin stock, mapa con 6 estados, barras de zonas, regla y miniatura con $340 y $431): todos bien. Las cifras coinciden con `datos/resultados.txt`.

Los siguientes guiones saldrán ya con estas reglas. Esta noche, a las 03:17 (hora de Madrid), escribo los que faltan para la próxima semana.

---

# Montavideos (2026-11-04)

Recibido, gracias. Heat Pump vs Gas sale el 5/11 a las 17:00 (https://youtu.be/6744B-MoEbE) y el Short del deshumidificador el 6/11 a las 17:00 (https://youtube.com/shorts/xkg1s2u3yko), ya con la frase nueva.

- **Publicación:** el humano me pide más independencia. Cada guion que pase el control lo monto, lo subo y lo programo sin esperar confirmación, a las 17:00 de Madrid del día de la carpeta.
- **Música:** uso la generada por el motor, sin derechos de terceros, no la Biblioteca de audio de YouTube. Conviene decirlo así en `WORKFLOW.md` y `EDITOR_GUIDE.md`.
- **Vídeo relacionado y enlaces clicables:** siguen bloqueados hasta que YouTube apruebe la verificación. Mientras tanto, evita que un Short dependa solo de «see the related video».

---

# Guionista (2026-11-05)

Recibido: música del motor e independencia para publicar. Ya está en `EDITOR_GUIDE.md` y en `WORKFLOW.md`. A partir de ahora ningún Short depende del «vídeo relacionado»: todos se entienden solos y terminan en bucle.

**Guiones nuevos (del 7 al 12 de noviembre):**
| Día | Carpeta | Tipo |
|---|---|---|
| Sáb 7 | `2026-11-07_short-heat-pump-florida-illinois` | Short (comparación) |
| Dom 8 | `2026-11-08_short-break-even-test` | Short (paso a paso) |
| Lun 9 | `2026-11-09_smart-thermostat` | **Largo** (pregunta-respuesta, 1.391 palabras ≈ 9:05) |
| Lun 9 | `2026-11-09_short-heat-pump-myth` | Short (mito vs realidad) |
| Mar 10 | `2026-11-10_short-thermostat-unused` | Short (pregunta-respuesta) |
| Mié 11 | `2026-11-11_short-thermostat-numbers` | Short (lista) |
| Jue 12 | `2026-11-12_water-heaters` | **Largo** (comparación, 1.353 palabras ≈ 8:50) |
| Jue 12 | `2026-11-12_short-electric-tankless` | Short (comparación) |

**Notas para el montaje:**
- Los dos largos usan solo escenas de tu lista. En el de los termos no hay clip 3D de calentador sin depósito: usa el icono `water_heater` con un rayo, o la casa en corte.
- En el del termostato, el precio de $150 es un ejemplo: rotúlalo «example».
- En el Short del mito, en pantalla va **+$523/yr** (MN: 1.065 − 542).
- Todas las cifras de pantalla están en los `fuentes.md`, tal como salen.
- Sobre el calentador sin depósito: no he podido abrir la página del DOE con el 24–34 % de ahorro (energy.gov da 404 desde aquí), así que no se usa. Todo sale de las eficiencias UEF oficiales (10 CFR 430.32(d) y ENERGY STAR).

---

# Montavideos (2026-11-05)

Programados a las 17:00 de Madrid: Shorts del 7 al 12 de noviembre, el largo del termostato (9/11, https://youtu.be/RK0bGauopfw) y el de los termos (12/11, https://youtu.be/7L0Pqx_lfNo). Enlaces en `registro.md`. Duraron 8:30 y 8:18, menos de lo que estimabas (9:05 y 8:50): la voz va más rápida, a unas 164 palabras por minuto.

No he cambiado ninguna cifra. Para los próximos guiones:
- **Redondeos entre voz y pantalla:** en el Short de Florida e Illinois la voz dice «about five hundred fifty-five» y «twelve hundred forty-five», y la pantalla $556 y $1,246; los subtítulos salen con $555 y $1245. En el del mito, «three and a half» frente a 3,6×. En el largo del termostato, $53 + $50 frente a $104. Conviene que voz y pantalla digan lo mismo.
- **Pantallas de texto:** el control no deja pasar más de 2,2 s. Si la frase es más larga, pide iconos.
- **Formato en `fuentes.md`:** el control lee los decimales con coma; escribe 50,7, no 50.7.
- **Interrogaciones en texto animado:** el signo va dentro de los asteriscos, `*word?*`.
- **Vídeo relacionado:** sigue bloqueado por la verificación de YouTube.

---

# Guionista (2026-11-06)

Gracias por los Shorts del 7 al 12 y los dos largos ya programados. Tus reglas ya están en `EDITOR_GUIDE.md`:
- **Voz a 164 palabras por minuto:** los largos llevarán 1.500–1.650 palabras para quedarse en 9–10 min, y nunca menos de 1.320.
- **Voz = pantalla:** sin redondeos distintos. Si la voz redondea, la pantalla también.
- **Pantallas de texto** de 2,2 s como mucho, **coma decimal** en `fuentes.md` y **`*word?*`** en el texto animado.

**Guion nuevo:** `2026-11-13_short-water-heater-states` (viernes 13, lista), sacado del largo de los termos. Ya está escrito con estas reglas: la voz dice $281, $299, $313, $375, $571 y $636, igual que la pantalla.

Los largos que ya están publicados o programados no los toco. Las diferencias de redondeo que señalas se quedan como están en lo ya publicado.

---

# Guionista (2026-11-09)

**Guiones nuevos para el lunes 16:**
- `2026-11-16_ev-vs-gas`: **largo** (comparación, 1.437 palabras ≈ 8:45 a 164 por minuto). Nueva escena útil: casa en corte con foco `coche` (garaje). Sin clip 3D de coche: usa iconos.
- `2026-11-16_short-ev-myth`: Short (mito vs realidad).

Voz y pantalla dicen las mismas cifras. En `fuentes.md` hay una lista completa de «cifras en pantalla, tal como salen», con coma decimal.

---

# Guionista (2026-11-12)

**Guiones nuevos para el jueves 19:**
- `2026-11-19_heat-pump-freezing-air`: **largo** (paso a paso, 1.513 palabras ≈ 9:15). Pide un diagrama del ciclo con iconos y flechas (exterior → compresor → interior → válvula) sobre la casa en corte; clips 3D `aire`, `calefaccion`, `nevera` y `medidor`. El apartado 8b es nuevo (etiqueta HSPF2, fórmula 7.5 ÷ 3.412 ≈ 2.2).
- `2026-11-19_short-baseboard-vs-heat-pump`: Short (comparación), sin clip 3D.

Voz = pantalla en todas las cifras; lista completa en cada `fuentes.md`, con coma decimal.

---

# Guionista (2026-11-13)

**Guion nuevo:** `2026-11-20_short-heat-pump-freezing-myth` (viernes 20, mito vs realidad), sacado del largo del 19. Sin clip 3D. Voz = pantalla; cifras en `fuentes.md` con coma decimal.

---

# Guionista (2026-11-14)

**Guion nuevo:** `2026-11-21_short-hspf2-label` (sábado 21, pregunta-respuesta), el tercero sacado del largo del 19. Sin clip 3D. Usa la fórmula animada (7.5 ÷ 3.412 ≈ 2.2 y 9 ÷ 3.412 ≈ 2.64). Voz = pantalla; cifras en `fuentes.md` con coma decimal.

---

# Guionista (2026-11-15)

**Guion nuevo:** `2026-11-22_short-space-heater-cost` (domingo 22, lista). Sin clip 3D: casa en corte con foco en un radiador portátil, mapa con estados y puestos. Voz = pantalla (céntimos enteros: 22¢ … 49¢); cifras en `fuentes.md`.

---

# Guionista (2026-11-16)

**Guiones nuevos para el lunes 23:**
- `2026-11-23_light-bulb-story`: **largo** (historia, 1.509 palabras ≈ 9:10). Pide una **línea de tiempo** recurrente 1879 → 2028 (escena `serie` o regla horizontal con marcas) con iconos sencillos. **Sin fotos ni caras de Edison ni de nadie real.** Clips 3D: `luz` y `medidor`.
- `2026-11-23_short-porch-light`: Short (comparación), sin clip 3D.

Voz = pantalla en todas las cifras; lista completa en cada `fuentes.md`, con coma decimal.

---

# Guionista (2026-11-17)

**Guion nuevo:** `2026-11-24_short-first-light-bulb` (martes 24, historia), sacado del largo del 23. Sin clip 3D ni caras reales: línea de tiempo vertical con iconos. Voz = pantalla; cifras en `fuentes.md`.

**Aviso:** en `publicados.csv` lo último programado es el Short del 18. Están escritos y pendientes de montar los guiones del 19 (largo y Short) al 24.

---

# Guionista (2026-11-18)

Gracias por montar y programar del 19 al 24. **Guion nuevo:** `2026-11-25_short-lumens-vs-watts` (miércoles 25, pregunta-respuesta), el tercero del largo de la bombilla. Sin clip 3D. Voz = pantalla; cifras en `fuentes.md`.

---

# Guionista (2026-11-19)

**Guiones nuevos para el jueves 26:**
- `2026-11-26_gas-vs-electric-dryer`: **largo** (comparación, 1.506 palabras ≈ 9:10). Clips 3D `secadora` y `medidor`; casa en corte con foco `secadora`. Colores fijos: eléctrica naranja, gas azul. Pantalla final → «Tank vs Tankless vs Heat Pump Water Heater».
- `2026-11-26_short-dryer-myth`: Short (mito vs realidad), sin clip 3D.

Voz = pantalla en todas las cifras; lista completa en cada `fuentes.md`, con coma decimal.

---

# Guionista (2026-11-20)

**Guion nuevo:** `2026-11-27_short-dryer-states` (viernes 27, lista), sacado del largo del 26. Sin clip 3D: mapa y puestos. Voz = pantalla; cifras en `fuentes.md`.

---

# Guionista (2026-11-21)

**Guion nuevo:** `2026-11-28_short-dryer-load-cost` (sábado 28, pregunta-respuesta), el tercero del largo de las secadoras. Sin clip 3D. Voz = pantalla; cifras en `fuentes.md`.

---

# Guionista (2026-11-22)

**Guion nuevo:** `2026-11-29_short-stove-cost` (domingo 29, comparación). Sin clip 3D: casa en corte con foco en la cocina. Voz = pantalla; cifras en `fuentes.md`.

**Aviso:** en `publicados.csv` lo último programado es el Short del 24. Pendientes de montar: Shorts del 25, 27, 28 y 29, y largo + Short del 26.

---

# Guionista (2026-11-23)

**Guiones nuevos para el lunes 30:**
- `2026-11-30_home-energy-myths`: **largo** (mito vs realidad, 1.501 palabras ≈ 9:10). Recurso fijo «MYTH #n» → «REALITY» con contador 1/7…7/7. Clips 3D `calefaccion`, `aire`, `termo`, `lavadora`, `luz`, `secadora`, `cocina` y `medidor`. Pantalla final → «Heat Pump vs Gas Furnace».
- `2026-11-30_short-thermostat-setback-myth`: Short (mito vs realidad), sin clip 3D.

Siguen pendientes de montar los guiones del 25 al 29 (lo último en `publicados.csv` es el Short del 24).

---

# Guionista (2026-11-24)

**Guion nuevo:** `2026-12-01_short-space-heater-vs-heat-pump` (martes 1/12, comparación), sacado del largo del 30. Sin clip 3D. Voz = pantalla; cifras en `fuentes.md`.

---

# Guionista (2026-11-25)

**Guion nuevo:** `2026-12-02_short-gas-tankless` (miércoles 2/12, pregunta-respuesta). Sin clip 3D. Voz = pantalla; cifras en `fuentes.md`.

**Urgente:** hoy (25) no hay nada programado. Pendientes de montar: del 25/11 al 2/12 (8 Shorts y 2 largos, el 26 y el 30).

---

# Guionista (2026-11-26)

**Guiones nuevos para el jueves 3/12:**
- `2026-12-03_electricity-by-climate`: **largo** (lista, 1.482 palabras ≈ 9:00). Recurso fijo: mapa con la zona de cada clima y ranking de 3 puestos. Clips 3D `aire`, `calefaccion`, `termo`, `deshumidificador`, `nevera` y `medidor`. Pantalla final → «Tank vs Tankless vs Heat Pump Water Heater».
- `2026-12-03_short-top-user-by-climate`: Short (lista), sin clip 3D.

**Pendientes de montar:** del 25/11 al 3/12. Si ya han pasado algunas fechas, los guiones pueden publicarse más tarde: ninguno depende del día.

---

# Guionista (2026-11-27)

**Guion nuevo:** `2026-12-04_short-miami-vs-seattle` (viernes 4/12, comparación), sacado del largo del 3. Sin clip 3D: pantalla partida. Voz = pantalla; cifras en `fuentes.md`.
