# Fuentes · Short · What Does HSPF2 on a Heat Pump Mean?

1. **10 CFR 430.32(c)(5):** bombas de calor partidas desde 2023, **HSPF2 7,5** como mínimo. Ver `../2026-11-19_heat-pump-freezing-air/fuentes.md` (punto 1), comprobado en GovInfo.
   https://www.govinfo.gov/content/pkg/CFR-2025-title10-vol3/xml/CFR-2025-title10-vol3-sec430-32.xml
2. **Definición de HSPF2:** calor total de la temporada (BTU) ÷ luz consumida (Wh), 10 CFR 430, subparte B, apéndice M1. Conversión: 1 Wh = **3,412** BTU. Mismo planteamiento que en el largo del 19 (apartado 8b).
3. **Casa típica de clima frío:** RECS 2020 CE5.4 (60,753 MMBtu de gas × 0,80) = 14.244 kWh de calor; luz MN 16,44 ¢/kWh (EIA EPM 5.6.B, ene–ago 2026). Ver puntos 3 y 5 del largo del 19.
4. **HSPF2 9:** ejemplo de un modelo más eficiente, solo para el cálculo (no se cita ningún producto).

## Cálculo
`python3 datos/calculo.py` → `datos/resultados.txt`: 7,5 → COP 2,20, 45 %, 1.065 $; 9 → COP 2,64, 38 %, 888 $; diferencia 178 $.

## Cifras en pantalla, tal como salen
3,412 · 7,5 · 2,2 · 45 % · 9 · 2,64 · 38 % · 1.065 · 888 · 178
