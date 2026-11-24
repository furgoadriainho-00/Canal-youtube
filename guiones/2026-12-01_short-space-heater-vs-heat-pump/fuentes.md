# Fuentes · Short · Space Heater vs Heat Pump: The Hourly Cost

- **10 CFR 430.32(c)(5):** bomba de calor partida, HSPF2 ≥ 7,5 → COP estacional 7,5 ÷ 3,412 = 2,198 (ver `../2026-11-19_heat-pump-freezing-air/fuentes.md`, punto 1).
- **Radiador de resistencia:** COP 1, 1.500 W → 1,5 kWh por hora (ver `../2026-11-22_short-space-heater-cost/fuentes.md`).
- **EIA EPM 5.3:** luz residencial EE. UU. ene–ago 2026, 18,19 ¢/kWh.
- Supuesto: 8 h al día × 30 días (se dice en la voz).

## Cálculo
`python3 datos/calculo.py` → `datos/resultados.txt`: radiador 1,50 kWh → 0,27 $/h → 65 $/mes; bomba de calor 0,68 kWh → 0,12 $/h → 30 $/mes.


## Cifras en pantalla, tal como salen
1.500 W · 1,5 kWh · 0,68 kWh · 27 · 12 · 65 · 30
