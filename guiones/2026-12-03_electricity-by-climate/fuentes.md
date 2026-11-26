# Fuentes · What Uses the Most Electricity in Your Climate

1. **EIA, RECS 2020, tablas CE5.3a y CE5.3b** («Detailed household site electricity end-use consumption — averages, 2020», revisadas en marzo de 2024): MMBtu por hogar **que tiene ese uso**, filas «Climate region». Copias en `datos/ce5.3a.xlsx` y `datos/ce5.3b.xlsx`. Conversión × 293,07 kWh/MMBtu. Calefacción = «Space heating» + «Air handlers for heating»; aire acondicionado = «Air conditioning» + «Air handlers for cooling»; jacuzzi = calentador + bomba. Algunas divisiones censales salen «Q» (sin dato publicado); no se usan.
   https://www.eia.gov/consumption/residential/data/2020/
2. **PNNL para el DOE, «Building America Best Practices Series, Vol. 7.3: Guide to Determining Climate Regions by County»** (agosto de 2015). Definiciones citadas: hot-humid «more than 20 inches (50 cm) of annual precipitation» y temperatura húmeda alta en verano; hot-dry y mixed-dry «less than 20 inches (50 cm) of annual precipitation»; cold «between 5,400 and 9,000 heating degree days»; very cold «between 9,000 and 12,600»; marine: invierno suave y «a dry season in summer». Condados comprobados en la tabla: Miami-Dade FL y Harris TX → Hot-Humid; Maricopa AZ, Clark NV y Los Angeles CA → Hot-Dry; Fulton GA y St. Louis MO → Mixed-Humid; Hennepin MN y Cook IL → Cold; King WA, Multnomah OR y San Francisco CA → Marine.
   https://www.energy.gov/sites/prod/files/2015/10/f27/ba_climate_region_guide_7.3.pdf
   EIA, glosario de la RECS: «In 2009, RECS began using Building America Climate Regions». https://www.eia.gov/consumption/residential/terminology.php
3. **EIA, Electric Power Monthly, tabla 5.3:** luz residencial EE. UU. ene–ago 2026, **18,19 ¢/kWh** (precio único para todos los climas; se dice en el vídeo).
   https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_03
4. **Remisiones a otros guiones:** bomba de calor COP 2,2 → **45 %** de la luz (`../2026-11-19_heat-pump-freezing-air/fuentes.md`); termo con bomba de calor ENERGY STAR **72 %** menos que el termo eléctrico (`../2026-11-12_water-heaters/datos/resultados.txt`: 1 − 137/492) → 559 × 0,7215 = **403 $**; DOE, termostato 8 h al día → hasta **10 %** (`../2026-11-09_smart-thermostat/fuentes.md`, punto 3).

## Cálculo
`python3 -I datos/calculo.py` → `datos/resultados.txt`. Comprobaciones: 4.893 ÷ 2.775 − 1 = **76 %**; 574 + 532 + 499 = **1.605**; 465 + 360 = **825** < 890; 1.580 ÷ 2.775 = **57 %**; 4.893 ÷ 1.097 = **4,5** («almost four and a half»).

## Supuestos y frases sin cifra
- «Dry heat takes less work to cool, because there's less moisture to pull out of the air»: explicación física general (carga latente); sin cifra.
- «The survey doesn't say why water heating is higher here»: no se da ninguna causa.

## Cifras en pantalla, tal como salen (todas en `datos/resultados.txt` o arriba)
18,19 · 505 · 494 · 492 · 182 · 890 · 465 · 360 · 4.893 · 2.775 · 76 % · 825 · 249 · 366 · 67 · 111 · 580 · 376 · 191 · 574 · 532 · 499 · 1.605 · 3.644 · 663 · 8 h · 10 % · 595 · 485 · 287 · 57 % · 1,0 · 0,45 · 45 % · 559 · 521 · 200 · 72 % · 403 · 434 · 521 · 357 · 430 · 104 · 122 · 773–912 · 571–713 · 550–680 · 1.097–4.893 · 4,5.
