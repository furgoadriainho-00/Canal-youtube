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
