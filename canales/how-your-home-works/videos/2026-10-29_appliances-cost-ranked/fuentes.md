# Fuentes · Which appliances really use the most electricity

## Datos principales
1. **EIA, Residential Energy Consumption Survey (RECS) 2020**, tablas CE5.3a y CE5.3b, «Detailed household site electricity end-use consumption — averages, 2020» (publicadas en junio de 2023, revisadas en marzo de 2024). Son kWh al año **por hogar que usa ese aparato**. Copias en `datos/ce5.3a.xlsx` y `datos/ce5.3b.xlsx`.
   https://www.eia.gov/consumption/residential/data/2020/index.php?view=consumption
   - Aire acondicionado 2.318 + su ventilador 457 · calefacción eléctrica 2.484 + su ventilador 233 · termo eléctrico 2.706 · bomba de piscina 2.384 · carga de coche eléctrico 2.363 · jacuzzi (calentador 1.479 + bomba 484) · deshumidificador 999 · frigorífico principal 617 · segundo frigorífico 494 · congelador aparte 570 · secadora 680 · iluminación 654 · televisores y aparatos conectados 632 · cocina (fuegos/horno) 290 · ventiladores de techo 226 · humidificador 139 · lavavajillas 112 · microondas 107 · lavadora 69.
   - La EIA aclara que «televisores y aparatos conectados» incluye descodificadores, consolas, dispositivos de streaming y equipos de audio, y que «cocina» no incluye el microondas.
2. **EIA, Electric Power Monthly, tabla 5.3**: precio medio residencial en EE. UU. **18,19 ¢/kWh** en enero–agosto de 2026 (preliminar). En 2025 fue 17,23 ¢ y en 2020, 13,15 ¢.
   https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_03
3. **EIA, FAQ «How much electricity does an American home use?»**: 10.791 kWh al año por cliente residencial en 2022.
   https://www.eia.gov/tools/faqs/faq.php?id=97&t=3

## Datos de apoyo
4. **ENERGY STAR, Clothes Washers**: «Water heating consumes about 90% of the energy it takes to operate a clothes washer.» y «Switching your temperature setting from hot to warm can cut energy use in half.»
   https://www.energystar.gov/products/clothes_washers
5. **U.S. Department of Energy (Building Science Education)**: los termos con bomba de calor «can be two to three times more efficient than conventional electric-resistance water heaters».
   https://bsesc.energy.gov/energy-basics/water-heaters-heat-pumps

## Cálculo propio (el ángulo del vídeo)
Coste al año = kWh de RECS 2020 × 0,1819 $/kWh. Script: `datos/calcular.py` → `datos/costes.csv`.
- **Limitación, dicha en el vídeo:** son medias nacionales con datos de uso de 2020 (la última encuesta publicada) y precios de 2026. Cada casa es distinta según clima, tamaño y aparatos.
- Termo con bomba de calor: 492 $ ÷ 2 a 3 = de **164 a 246 $** al año. Es una estimación que sale de la fuente 5, no un dato medido.

## Datos añadidos al ampliar el guion
6. **RECS 2020, tabla CE5.3a por región** (kWh por hogar que lo usa):
   - Aire acondicionado + ventilador: Noreste 1.395 + 323 = 1.718 → **313 $** · Sur 3.304 + 588 = 3.892 → **708 $** · West South Central (TX, OK, AR, LA, división estándar del censo) 3.873 + 693 = 4.566 → **831 $**.
   - Calefacción eléctrica: Medio Oeste 3.109 frente a 2.484 de media nacional (**+25 %**); con el ventilador, 3.109 + 432 = 3.541 → **644 $**.
7. **U.S. DOE (EERE), boletín del 2 de febrero de 2024**: «Setting back your thermostat for at least 8 hours per day can save you as much as 10% per year on heating and cooling costs.»
   https://content.govdelivery.com/accounts/USEERE/bulletins/3883189
   - Cálculo propio: (505 + 494) × 10 % ≈ **100 $/año** como máximo. En el vídeo se dice «up to».
8. **Consumo medio del hogar**: 10.791 kWh (EIA, FAQ 97, datos de 2022) × 0,1819 = **1.963 $**.

## Cálculos derivados (todos a 0,1819 $/kWh)
- Al mes: aire acondicionado 505/12 = 42 · termo 492/12 = 41 · deshumidificador 182/12 = 15 · iluminación 119/12 = 9,9 · televisores 115/12 = 9,6 · congelador 104/12 = 8,7 · cocina 53/12 = 4,4.
- Segundo frigorífico en 10 años, con el precio constante: 90 × 10 = **900 $**. Frente al frigorífico principal: 90/112 = **80 %**.
- Del 2020 al 2026 el precio sube 18,19/13,15 = **+38 %**.
- Deshumidificador frente al frigorífico principal: 182/112 = **+62 %**. Secadora frente a lavadora: 124/13 = **9,5×**. Aire acondicionado frente a ventiladores de techo: 505/41 = **12,3×**.
- Puestos 4 a 15 sumados = **992 $**. Cada uno de los 3 primeros vale aproximadamente la mitad (492 a 505).
- Los 3 primeros sumados: 505 + 494 + 492 = **1.491 $**.

## Descartado por no poder verificarlo
- «Las LED gastan hasta un 90 % menos». No he podido abrir la página oficial de ENERGY STAR.
- Qué estados forman la subdivisión «Mountain South» de RECS. Uso la división West South Central, que es la estándar del censo.
