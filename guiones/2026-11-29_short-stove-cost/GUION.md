# Guion · Short · Gas vs Electric Stove: The Yearly Cost

| | |
|---|---|
| **Formato** | Short · 9:16 · 1080×1920 |
| **Duración** | 35–45 s |
| **Publicar** | Domingo 29 de noviembre de 2026 |
| **Estructura** | Comparación (los anteriores: mito vs realidad, lista y pregunta-respuesta) |
| **Datos** | `datos/calculo.py` → `datos/resultados.txt` (RECS 2020 y precios EIA) |

Narración en inglés, literal. Subtítulos grandes palabra a palabra. Imagen nueva cada 2–3 s. Sin clip 3D: casa en corte con foco en la cocina, iconos de cocina eléctrica (rayo, naranja) y de gas (llama, azul), monedas y barras. La voz dice las mismas cifras que la pantalla. El final enlaza con el principio para que se repita, y el Short se entiende solo.

| # | Narración (EN) | Imagen | Texto en pantalla |
|---|---|---|---|
| 1 | A gas stove uses about twice the energy of an electric one. And it still costs less to run. | Casa en corte con foco en la cocina; dos iconos: llama (azul) y rayo (naranja); cifra **2×** | `2× the energy, less money?` |
| 2 | In the government's household energy survey, the average electric range, cooktop and oven used about two hundred ninety point four kilowatt-hours a year. | Contador de luz que gira hasta **290.4 kWh** | `290.4 kWh a year` |
| 3 | At the US average electricity price, that's about fifty-two dollars and eighty-three cents. | Cifra **$52.83** con monedas (naranja) | **$52.83/yr** |
| 4 | The average gas stove used about twice that energy. But at the average gas price, it cost about twenty-nine dollars and ninety-five cents. | Comparación de dos barras: **$52.83** (eléctrica) frente a **$29.95** (gas, CHEAPER) | `$52.83 vs $29.95` |
| 5 | Either way, cooking is a small part of the bill. Fifty-nine percent of homes with a range cook on electric. Thirty-one percent on gas. | Barras horizontales: eléctrica **59%**, gas **31%** | `59% electric · 31% gas` |
| 6 | Gas energy is just cheaper per unit, so a gas stove uses about twice the energy of an electric one… | Corte al plano 1 | `Cheaper energy` |

Palabras de narración: unas 120.

**Cálculo** (`datos/calculo.py`): RECS 2020 CE5.3b, cocina eléctrica 0,991 MMBtu = 290,4 kWh × 18,19 ¢ = 52,83 $; CE5.4, cocina de gas 2,023 MMBtu ÷ 1,036 × 15,34 $/Mcf = 29,95 $; 2,023 ÷ 0,991 = 2,0×. HC3.1: cocinas (range) por combustible.

## Metadatos
- **Título:** `Gas vs Electric Stove: The Yearly Cost #shorts`
- **Descripción:**
  ```
  EIA Residential Energy Consumption Survey 2020, average per home that uses each: electric cooking (ranges, cooktops, ovens; microwaves excluded) about 290.4 kWh a year = $52.83 at 18.19¢/kWh (EIA, Jan–Aug 2026); natural gas cooking about 2.023 million BTU = $29.95 at $15.34 per thousand cubic feet (EIA, 2025). Of homes with a range, 59% cook mostly on electric and 31% on natural gas.
  ```
- **Etiquetas:** `gas vs electric stove, stove energy cost, cost to cook, electric range cost, gas range cost, shorts, home by the numbers`
- **Ajustes:** no es para niños · contenido sintético: **Sí** (voz IA).
