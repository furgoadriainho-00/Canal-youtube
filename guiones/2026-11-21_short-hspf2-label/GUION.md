# Guion · Short · What Does HSPF2 on a Heat Pump Mean?

| | |
|---|---|
| **Formato** | Short · 9:16 · 1080×1920 |
| **Duración** | 35–45 s |
| **Publicar** | Sábado 21 de noviembre de 2026 |
| **Estructura** | Pregunta-respuesta (los anteriores: historia, comparación y mito vs realidad) |
| **Sale de** | `guiones/2026-11-19_heat-pump-freezing-air/` (apartado 8b) y `datos/resultados.txt` de esta carpeta |

Narración en inglés, literal. Subtítulos grandes palabra a palabra. Imagen nueva cada 2–3 s. Sin clip 3D: etiqueta de eficiencia con iconos, fórmula, contador de luz y barras. La voz dice las mismas cifras que la pantalla. El final enlaza con el principio para que se repita, y el Short se entiende solo.

| # | Narración (EN) | Imagen | Texto en pantalla |
|---|---|---|---|
| 1 | What does that HSPF2 number on a heat pump actually mean? | Etiqueta de eficiencia (iconos) con **HSPF2** resaltado y un `?` que late | `*HSPF2?*` |
| 2 | It's how many B T U of heat you get for each watt-hour of electricity, over a whole heating season. | Fórmula con iconos: rayo (1 Wh) → llamas (BTU); calendario de invierno | `BTU of heat per Wh` |
| 3 | An electric heater turns one watt-hour into three point four one two B T U. That's the baseline. | Radiador en la casa en corte; cifra **3.412** | `1 Wh = 3.412 BTU` |
| 4 | The federal minimum for a new heat pump is seven point five. Divide by three point four one two, and it gives about two point two times the heat of a heater, for about forty-five percent of the electricity. | Fórmula animada **7.5 ÷ 3.412 ≈ 2.2**; anillo **45%** | `7.5 → 2.2× · 45%` |
| 5 | A model rated nine gives about two point six four, about thirty-eight percent. | Fórmula **9 ÷ 3.412 ≈ 2.64**; anillo **38%** | `9 → 2.64× · 38%` |
| 6 | In a typical Minnesota home, that's about one thousand sixty-five dollars a year versus about eight hundred eighty-eight. About one hundred seventy-eight dollars saved. | Comparación de dos barras: **$1,065** (7.5) frente a **$888** (9, CHEAPER); cifra **−$178/yr** | `$1,065 vs $888` |
| 7 | So next time you see HSPF2 on a heat pump, you'll know what that number actually means… | Corte al plano 1 | `Higher = less electricity` |

Palabras de narración: unas 140.

**Cálculo** (`datos/calculo.py` → `datos/resultados.txt`): COP = HSPF2 ÷ 3,412 (7,5 → 2,20; 9 → 2,64). Casa típica de clima frío (RECS 2020 CE5.4 × 0,80 = 14.244 kWh de calor) × 16,44 ¢ (EIA, MN) → 1.065 $ y 888 $ al año; diferencia 178 $.

## Metadatos
- **Título:** `What Does HSPF2 on a Heat Pump Mean? #shorts`
- **Descripción:**
  ```
  HSPF2 = BTU of heat per watt-hour of electricity over a heating season. 1 Wh = 3.412 BTU, so HSPF2 ÷ 3.412 = units of heat per unit of electricity. Federal minimum HSPF2 7.5 (10 CFR 430.32) → about 2.2, or 45% of the electricity of a baseboard heater. HSPF2 9 → about 2.64 (38%). Typical cold-climate home in Minnesota: $1,065 vs $888 a year (EIA RECS 2020 heating needs, EIA MN electricity 16.44¢/kWh, Jan–Aug 2026). Running costs only.
  ```
- **Etiquetas:** `hspf2, heat pump efficiency, heat pump rating explained, heat pump label, heat pump cost, shorts, home by the numbers`
- **Ajustes:** no es para niños · contenido sintético: **Sí** (voz IA).
