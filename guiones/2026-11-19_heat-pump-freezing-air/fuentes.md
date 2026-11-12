# Fuentes · How a Heat Pump Pulls Heat Out of Freezing Air

1. **Mínimo federal de las bombas de calor (fuente primaria):** 10 CFR 430.32(c)(5), bombas de calor partidas fabricadas desde el 1 de enero de 2023: SEER2 14,3 y **HSPF2 7,5**. Texto oficial (CFR, edición 2025, GovInfo), comprobado el 2026-11-04 para el vídeo del 5 de noviembre.
   https://www.govinfo.gov/content/pkg/CFR-2025-title10-vol3/xml/CFR-2025-title10-vol3-sec430-32.xml
   - HSPF2 = BTU de calor por Wh de luz en la temporada; 1 Wh = 3,412 BTU → COP estacional 7,5 ÷ 3,412 = 2,198 ≈ **2,2** → usa 1 ÷ 2,198 = **45 %** de la luz de la resistencia.
2. **ENERGY STAR, bombas de calor de aire (key product criteria):** las de clima frío deben dar un **COP de 1,75** o más a **5 °F** → 1 ÷ 1,75 = **57 %**.
   https://www.energystar.gov/products/air_source_heat_pumps/key-product-criteria
3. **EIA, RECS 2020, tabla CE5.4:** gas de calefacción por hogar que lo usa (MMBtu): hot-humid 20,804 · mixed-humid 44,010 · very cold/cold 60,753. Calor que llega a la casa = × 0,80 (eficiencia supuesta de las calderas de esos hogares, igual que en el vídeo del 5 de noviembre). Copia en `../2026-11-05_heat-pump-vs-gas/datos/ce5.4.xlsx`.
   https://www.eia.gov/consumption/residential/data/2020/
4. **EIA, RECS 2020, tabla HC6.1** (equipo principal de calefacción, millones de hogares): bomba de calor central 16,13 · minisplit 1,06 → **17,2 M** (17,19); resistencia eléctrica: equipos fijos 7,65 + radiadores portátiles 3,03 → **10,7 M** (10,68) de 123,53 M → **8,6 %**. Copia en `datos/hc6.1.xlsx`.
5. **EIA, Electric Power Monthly, tabla 5.6.B:** luz residencial ene–ago 2026: FL 15,32 · GA 15,48 · MN 16,44 ¢/kWh.
   https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_b
6. **Física:** cero absoluto = −459,67 °F. La energía térmica del aire es proporcional a su temperatura absoluta (Rankine = °F + 459,67): (0 + 459,67) ÷ (70 + 459,67) = 0,868 → **87 %**; 32 °F → **93 %**; 47 °F → **96 %**; 5 °F → **88 %**. Es una simplificación (calor sensible del aire a presión constante), y así se dice: «heat energy … measured from that point».
7. **Calderas de gas (sección 11):** del vídeo del 5 de noviembre (`../2026-11-05_heat-pump-vs-gas/datos/resultados.txt`): caldera nueva al 95 %, gas de 2025: MN **542 $**, FL **431 $** al año.

## Ciclo del refrigerante (pasos 2–5)
Explicación cualitativa sin cifras: evaporador, compresor, condensador y válvula de expansión. Es la descripción estándar del ciclo de compresión de vapor (la misma que el DOE usa para las bombas de calor y las neveras). No se da ninguna cifra de desescarche, temperatura del refrigerante ni capacidad.

## Supuestos (se dicen en el vídeo o en la descripción)
- Solo coste de funcionamiento. Sin compra ni instalación.
- Resistencia eléctrica: COP 1.
- 1.338 $ en MN = el COP de 1,75 durante todo el invierno, un supuesto pesimista que se dice como tal («even if we assume»).

## Cálculo
`python3 datos/calculo.py` → `datos/resultados.txt`.

## Cifras en pantalla, tal como salen (todas en `datos/resultados.txt` o arriba)
0 °F · 5 °F · 32 °F · 47 °F · 70 °F · −459,67 · 87 % · 88 % · 93 % · 96 % · 1,0 · 0,45 · 1,75 · 2,2 · 45 % · 57 % · 7,5 · 3,412 · FL 747 / 340 / 407 · GA 1.597 / 727 / 871 · MN 2.342 / 1.065 / 1.276 / 1.338 · 17,2 M · 10,7 M · 8,6 % · gas MN 542 · gas FL 431.
