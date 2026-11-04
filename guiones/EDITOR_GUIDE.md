# Guía de los guiones · Home By The Numbers

Guiones de **Home By The Numbers** (@HomeByTheNumbers), canal en inglés para público de EE. UU. Los escribe el **guionista** (Claude, en la nube). Los monta y los publica el **montavideos** (el agente de Claude que trabaja en el Mac del humano) con el motor del repositorio. Las notas entre los dos van en `guiones/NOTA_MONTAVIDEOS.md` o en `registro.md`.

## Dónde está todo
- Repositorio: **github.com/furgoadriainho-00/Canal-youtube**, carpeta `guiones/`. Hay una carpeta por vídeo, `AAAA-MM-DD_<tema>`, con la fecha de publicación.
- En cada carpeta: `GUION.md` (narración e imagen), `fuentes.md` (de dónde sale cada cifra) y `datos/` (cálculos).
- Clips 3D de 15 aparatos en `recursos/clips3d/`. Logo, banner y marca de agua en `canales/how-your-home-works/marca/`.

## Reglas para escribir (guionista)
- **Narración en inglés de EE. UU.**, con los números escritos como se dicen. Las indicaciones pueden ir en español.
- **Duración:** la voz va a unas **153 palabras por minuto**. Un largo de 9–10 min necesita **1.400–1.500 palabras**, y el mínimo son 8 min. Un Short, 80–150 palabras.
- **Cifras en pantalla:** cada una tiene que estar en `fuentes.md` **tal como sale**, redondeo incluido.
- **Capítulos:** no hace falta poner los minutos; los calcula el montavideos.
- **Sin stock por ahora** (no hay claves de Pexels ni Pixabay). Pide solo escenas que el motor sabe hacer:
  - casa en corte con foco en un aparato · contador de la luz · cifra animada (monedas o anillo)
  - comparación de dos barras con sello CHEAPER · barras horizontales · iconos · fórmula · tarjeta de fuente
  - puesto de ranking · clip 3D con texto · mapa de EE. UU. con estados resaltados · regla con marcas y zonas · gráfico de puntos
- **Shorts:** el clip 3D todavía no sale en vertical. Usa la casa en corte, iconos o cifras.
- **Miniaturas:** icono grande con cifra, versus, ranking, o mapa con cifras. Máximo 4 palabras.
- **Variedad:** no más de 3 vídeos seguidos con la misma estructura, la misma miniatura base o la misma frase de inicio.

## Reglas de montaje y publicación (montavideos)
- **Voz:** la IA del canal, Kokoro `am_michael`, aprobada por el humano. La narración se usa **literal**.
- **YouTube «Altered or synthetic content»: Sí**, siempre que la voz sea de IA.
- Nada de material con derechos. Música generada por el motor o de la Biblioteca de audio de YouTube.
- Volumen en torno a −14 LUFS y música entre 18 y 20 dB por debajo de la voz.
- No se cambian cifras ni frases. Si algo no encaja, se avisa en `NOTA_MONTAVIDEOS.md`.
- Antes de publicar cada vídeo se pide confirmación al humano. El enlace publicado se apunta en `registro.md` y en `canales/how-your-home-works/publicados.csv`.

## Calendario
**1 Short cada día** y **2 vídeos largos a la semana** (lunes y jueves). Los guiones van siempre con al menos una semana de antelación.
