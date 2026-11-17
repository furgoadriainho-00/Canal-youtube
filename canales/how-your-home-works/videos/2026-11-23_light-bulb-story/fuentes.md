# Fuentes · The Light Bulb Story: From Edison to LEDs

1. **Thomas A. Edison Papers (Rutgers University), «The Carbon-Filament Lamp»:** «In the early morning hours of October 22 1879, they began … experiments on straight carbons made from cotton thread»; Batchelor: «… we carbonized it in a closed chamber»; «After the lamp had been left burning for 13 1/2 hours, they added enough battery cells…»; «this caused the bulb to overheat and crack after another hour, the laboratory staff had for the first time produced a lamp that showed true commercial promise».
   https://edison.rutgers.edu/life-of-edison/biographical-essays/lighting/the-carbon-filament-lamp
2. **Edison Papers, cronología 1871–1880:** «Oct 22 — Conducts the first successful experiment with a high-resistance carbon filament.» · «Nov 1 — Executes his first patent application for a high-resistance carbon filament (U.S. Pat. 223,898).» · «Dec 31 — Holds the first public demonstration of his incandescent electric lighting system at Menlo Park.» · 1880: «July 19 — Makes the first lamp tests using bamboo filaments, which become standard in Edison lamps.»
   https://edison.rutgers.edu/life-of-edison/chronology/1871-1880
3. **National Park Service, Thomas Edison NHP, biografía:** «After one and a half years of work, success was achieved when an incandescent lamp with a filament of carbonized sewing thread burned for thirteen and a half hours» (confirma 13,5 h y el año y medio de trabajo).
   https://www.nps.gov/edis/learn/historyculture/edison-biography.htm
4. **IEEE (ETHW), Milestone Pearl Street Station, 1882:** «On 4 September 1882, Edison's direct current (dc) generating station at 257 Pearl Street, began supplying electricity»; «only some 85 customers having a total of about 400 lamps on the first day of operation»; «grew to about 10,000 lamps serving 513 customers within a year».
   https://ethw.org/Milestones:Pearl_Street_Station,_1882
5. **FTC, «Shopping for light bulbs» (agosto de 2023):** «a traditional 60-watt incandescent bulb produces about 800 lumens of light… an LED … that produces that same 800 lumens but uses only about 9 watts»; «lumens = brightness», «watts = energy».
   https://consumer.ftc.gov/articles/shopping-light-bulbs
6. **10 CFR 430.32 (CFR edición 2025, GovInfo), apartado (dd) y (s)/(dd)(1)(iii):**
   - (dd): «Beginning July 25, 2022, the sale of any general service lamp that does not meet a minimum efficacy standard of 45 lumens per watt is prohibited.» → 800 ÷ 45 = **17,8 W**.
   - (dd)(1)(i), incandescentes de uso general, potencia máxima: 1490–2600 lm **72 W** (1/1/2012) · 1050–1489 lm **53 W** (1/1/2013) · 750–1049 lm **43 W** (1/1/2014) · 310–749 lm 29 W (1/1/2014).
   - (dd)(1)(iii): CFL de casquillo medio fabricadas desde el 1 de enero de 2006, desnudas de ≥ 15 W: al menos **60 lm/W**.
   - (dd)(1)(iv): bombillas fabricadas desde el 25 de julio de 2028; LED integrada omnidireccional corta, sin standby: 123 / (1,2 + e^(−0,005 × (lm − 200))) + 25,9 → a 800 lm, **124,3 lm/W** → **6,4 W**.
   https://www.govinfo.gov/content/pkg/CFR-2025-title10-vol3/xml/CFR-2025-title10-vol3-sec430-32.xml
7. **EIA, RECS 2020, tabla HC5.1** (millones de hogares; copia en `datos/hc5.1.xlsx`): total 123,53. LED todas 26,08 + la mayoría 31,61 = **57,7 M** (**47 %**). CFL todas 5,35 + la mayoría 9,55 = 14,90 (**12 %**). Incandescente o halógena todas 8,50 + la mayoría 10,19 = 18,69 (**15 %**); al menos una: **75,22 M** → **75,2 M** (**61 %**). Exterior toda la noche: al menos una 51,12; incandescente o halógena **13,62 M**.
   https://www.eia.gov/consumption/residential/data/2020/
   EIA, Today in Energy, 31/03/2022, «Nearly half of U.S. households use LED bulbs for all or most of their indoor lighting»: «47% report using LEDs for most or all of their indoor lighting in 2020»; en 2015 «only 4% of households used LEDs»; CFL «fell from 32% in 2015 to 12% in 2020»; incandescente o halógena «fell from 31% … to 15% in 2020». https://www.eia.gov/todayinenergy/detail.php?id=51858
8. **EIA, RECS 2015, tabla HC5.1** (118,2 M): LED todas 1,2 + la mayoría 4,1 = 5,3 (4,5 %; la EIA lo publica como **4 %**, y es lo que se dice); CFL 11,6 + 25,9 = 37,5 (**32 %**); incandescente 13,2 + 23,4 = 36,6 (**31 %**).
   https://www.eia.gov/consumption/residential/data/2015/hc/php/hc5.1.php
9. **EIA, Today in Energy, 23/03/2026 (RECS 2024):** «Over one-third of households (37%) used LED bulbs for all indoor lighting.» https://www.eia.gov/todayinenergy/detail.php?id=67368
10. **EIA, Electric Power Monthly:** luz residencial ene–ago 2026: EE. UU. **18,19 ¢/kWh** (tabla 5.3); WA **14,42** y CA **32,58** ¢/kWh (tabla 5.6.B).
    https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_03

## Supuestos (se dicen en el vídeo)
- Todas las bombillas comparadas dan 800 lúmenes.
- 3 horas al día (1.095 h al año) en el interior; 12 horas por noche en la luz del porche. Se dicen como supuestos y el apartado 11 avisa de que el ahorro depende de las horas reales.
- «Almost five times»: 43 W ÷ 9 W = 4,8.
- «About fifteen percent of the electricity»: 9 ÷ 60 = 15 %.
- No se cita la duración de los filamentos de bambú (no se ha encontrado en fuentes fiables).

## Cálculo
`python3 datos/calculo.py` → `datos/resultados.txt`.

## Cifras en pantalla, tal como salen (todas en `datos/resultados.txt` o arriba)
1879 · 13,5 · 60 W · 9 W · 15 % · 1882 · 2006 · 2014 · 2022 · 2028 · Oct 22 · Nov 1 · Dec 31 · 1880 · 400 · 85 · 10.000 · 513 · 800 · 3 h · 18,19 · 11,95 · 1.095 · 65,7 · 60 lm/W · 32 % · 31 % · 4 % · 1.490–2.600 · 72 W · 2012 · 2013 · 53 W · 43 W · 8,56 · 47 % · 57,7 M · 12 % · 45 lm/W · 17,8 W · 1,79 · 37 % · 2024 · 124,3 · 6,4 W · 1,28 · 3,54 · 10,16 · 102 · 14,42 · 8,05 · 32,58 · 18,19 · 61 % · 75,2 M · 13,62 M · 12 h · 47,80 · 7,17 · 40,63.
