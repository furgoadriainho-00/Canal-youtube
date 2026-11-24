# Guion · Short · Space Heater vs Heat Pump: The Hourly Cost

| | |
|---|---|
| **Formato** | Short · 9:16 · 1080×1920 |
| **Duración** | 35–45 s |
| **Publicar** | Martes 1 de diciembre de 2026 |
| **Estructura** | Comparación (los anteriores: pregunta-respuesta, comparación y mito vs realidad) |
| **Sale de** | `guiones/2026-11-30_home-energy-myths/` (mito 4) y `datos/resultados.txt` de esta carpeta |

Narración en inglés, literal. Subtítulos grandes palabra a palabra. Imagen nueva cada 2–3 s. Sin clip 3D: dos habitaciones en corte, radiador portátil (naranja) y bomba de calor (azul), contador de luz y monedas. La voz dice las mismas cifras que la pantalla. El final enlaza con el principio para que se repita, y el Short se entiende solo.

| # | Narración (EN) | Imagen | Texto en pantalla |
|---|---|---|---|
| 1 | Same heat, two machines. A fifteen-hundred-watt space heater, and a heat pump at the federal minimum. | Dos habitaciones en corte lado a lado: radiador **1,500 W** (naranja) y bomba de calor (azul) | `Same heat, 2 machines` |
| 2 | The space heater turns one point five kilowatt-hours of electricity into one point five kilowatt-hours of heat, every hour. | Contador de luz: **1.5 kWh** entra, **1.5 kWh** de calor sale | `1.5 kWh in → 1.5 out` |
| 3 | The heat pump moves heat from outside. For the same heat, it needs only about zero point six eight kilowatt-hours. | Flechas de calor de fuera hacia dentro; contador: **0.68 kWh** | `0.68 kWh` |
| 4 | At the US average electricity price, that's about twenty-seven cents an hour, versus about twelve. | Comparación de dos barras: **27¢** frente a **12¢** (CHEAPER) | `27¢ vs 12¢ an hour` |
| 5 | Eight hours a day for a month: about sixty-five dollars, versus about thirty. | Calendario de un mes; barras **$65** frente a **$30** (CHEAPER) | `$65 vs $30 a month` |
| 6 | A space heater is fine for a quick warm-up. For hours of heat, the heat pump gives the same heat… | Corte al plano 1 | `Same heat, less power` |

Palabras de narración: unas 110.

**Cálculo** (`datos/calculo.py`): bomba de calor COP 2,2 (HSPF2 7,5 ÷ 3,412, 10 CFR 430.32(c)(5)) → 1,5 ÷ 2,198 = 0,68 kWh. × 18,19 ¢ (EIA): 0,27 $ frente a 0,12 $ la hora; × 240 h: 65 $ frente a 30 $.

## Metadatos
- **Título:** `Space Heater vs Heat Pump: The Hourly Cost #shorts`
- **Descripción:**
  ```
  For the heat a 1,500 W space heater gives in an hour (1.5 kWh), a heat pump at the federal minimum (HSPF2 7.5 ≈ 2.2 units of heat per unit of electricity, 10 CFR 430.32) needs about 0.68 kWh. At the US average electricity price (18.19¢/kWh, EIA, Jan–Aug 2026): about 27¢ vs 12¢ an hour, or $65 vs $30 a month at 8 hours a day. Running costs only.
  ```
- **Etiquetas:** `space heater vs heat pump, space heater cost, heat pump cost, cheapest way to heat, electric heating cost, shorts, home by the numbers`
- **Ajustes:** no es para niños · contenido sintético: **Sí** (voz IA).
