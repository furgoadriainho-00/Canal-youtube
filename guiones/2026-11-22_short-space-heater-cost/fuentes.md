# Fuentes · Short · What a Space Heater Costs Per Hour, by State

1. **EIA, Electric Power Monthly, tabla 5.6.B:** luz residencial por estado, ene–ago 2026 (provisional): WA 14,42 · FL 15,32 · TX 16,03 · MN 16,44 · NY 29,26 · MA 30,19 · CA 32,58 ¢/kWh. **Tabla 5.3:** EE. UU. 18,19 ¢/kWh. Ya citados en `../2026-11-16_ev-vs-gas/fuentes.md` (punto 6) y `../2026-11-12_water-heaters/fuentes.md` (punto 6).
   https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_b
2. **1.500 W:** potencia de ejemplo, la de la etiqueta del calefactor (la voz dice «a fifteen-hundred-watt space heater», no que todos lo sean). Referencia: según la CPSC, los calefactores eléctricos de pared más vendidos son de 1.500 W (CPSC, *Final Report on Fixed-Position Electric Heaters*, 2002: «Wall heaters for residential use typically range from 500 watts to 2,500 watts, with the most popular units at 1,500 watts»). https://www.cpsc.gov/s3fs-public/pdfs/blk_media_fpheater.pdf
3. **Física:** 1.500 W durante 1 hora = 1,5 kWh. Toda la luz que consume un calefactor de resistencia se convierte en calor («same heater, same heat»).
4. **Supuesto «8 hours a day for a month»:** 8 h × 30 días a plena potencia, dicho como supuesto. La descripción avisa de que con termostato el consumo real suele ser menor.

## Cálculo
`python3 datos/calculo.py` → `datos/resultados.txt`.

## Cifras en pantalla, tal como salen
1.500 W · 22 · 23 · 24 · 25 · 27 · 44 · 45 · 49 · 52 · 117 · 1,5 kWh
