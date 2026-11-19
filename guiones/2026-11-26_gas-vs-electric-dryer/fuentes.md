# Fuentes · Gas vs Electric Dryer: The Real Yearly Cost

1. **EIA, RECS 2020, tabla CE5.3a** (electricidad por uso final, media por hogar que usa ese uso): secadoras **2,319 MMBtu** → × 293,07 = **679,6 kWh**. Copia en `datos/ce5.3a.xlsx`.
2. **EIA, RECS 2020, tabla CE5.4** (gas natural y propano por uso final): secadoras de gas natural **2,064 MMBtu** (propano 1,883, no se usa). 2,064 ÷ 2,319 = **89 %**. Copia en `datos/ce5.4.xlsx`. La cifra de gas no incluye la electricidad del tambor y el ventilador de la secadora de gas (se dice en el vídeo y en la descripción).
3. **EIA, RECS 2020, tabla HC3.1** (millones de hogares; copia en `datos/hc3.1.xlsx`): total 123,53; con secadora **102,32**; eléctrica **82,21** (**80 %**); gas natural **18,89** (**18 %**); propano **1,22**; sin secadora **21,2**. Cargas por semana: 0 → 1,92 · 1–4 → 67,48 (**66 %** de 102,32) · 5–9 → **25,93** · 10–15 → 6,06 · más de 15 → 0,93. Edad: 10–14 años **17,68** · 15–19 **7,03** · 20 o más **4,89** → **29,6 M** (**29 %**).
   https://www.eia.gov/consumption/residential/data/2020/
4. **10 CFR 430.32(h)** (CFR edición 2025, GovInfo):
   - (h)(2), fabricadas del 14/5/1994 al 1/1/2015: eléctrica estándar EF **3,01** lb/kWh; gas 2,67.
   - (h)(3), desde el 1/1/2015: eléctrica ventilada estándar CEF **3,73** lb/kWh; gas ventilada **3,30**.
   - (h)(4), desde el **1/3/2028** (apéndice D2): eléctrica estándar **3,93**; gas ventilada estándar **3,48**.
   https://www.govinfo.gov/content/pkg/CFR-2025-title10-vol3/xml/CFR-2025-title10-vol3-sec430-32.xml
5. **10 CFR 430, subparte B, apéndice D2** (eCFR, versión de 2025-10-01): tabla 1, carga de prueba de secadora estándar **8,45 lb**; 4.5.1, «Representative average number of clothes dryer cycles in a year»: (1) **283**; (2) **236**, que se aplica desde el 1 de marzo de 2028 según la nota introductoria. 283 ÷ 52 = **5,4** por semana; 236 ÷ 52 = **4,5**.
   https://www.ecfr.gov/current/title-10/chapter-II/subchapter-D/part-430/subpart-B/appendix-Appendix%20D2%20to%20Subpart%20B%20of%20Part%20430
6. **EIA, Electric Power Monthly**, luz residencial ene–ago 2026 (¢/kWh): EE. UU. **18,19** (tabla 5.3); FL 15,32 · AZ 15,36 · WA **14,42** · GA 15,48 · MN 16,44 · IL **19,23** (tabla 5.6.B).
   https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_b
7. **EIA, Natural Gas Prices**, gas residencial 2025 ($/Mcf): EE. UU. 15,34 · FL 25,48 · AZ 18,58 · WA 17,62 · GA 20,42 · MN 10,98 · IL 11,25. 1 Mcf = 1,036 MMBtu. (Los mismos que en `../2026-11-05_heat-pump-vs-gas/fuentes.md`, punto 3.)
   https://www.eia.gov/dnav/ng/ng_pri_sum_a_EPG0_PRS_DMcf_a.htm

## Supuestos (se dicen en el vídeo o en la descripción)
- Coste anual = energía media de la RECS × precio de cada estado. Solo coste de funcionamiento, sin instalación.
- La cifra de la secadora de gas no incluye su electricidad (tambor, ventilador y controles).
- «About four times»: 124 ÷ 31 = 4,0.
- La norma de 1994 (EF) y la de 2015 (CEF) se miden de forma algo distinta; se dice en el vídeo («not a perfect comparison»).
- 10 años = coste anual × 10, sin cambios de precio (se dice).
- Carga de prueba en una eléctrica nueva: 8,45 ÷ 3,73 = 2,27 kWh → WA 0,33 $ · EE. UU. 0,41 $ · IL 0,44 $ («up to», porque es el máximo permitido).

## Cálculo
`python3 datos/calculo.py` → `datos/resultados.txt`.

## Cifras en pantalla, tal como salen (todas en `datos/resultados.txt` o arriba)
2,319 · 2,064 · 124 · 31 · 102,32 · 82,21 M · 18,89 M · 1,22 M · 80 % · 66 % · 25,93 M · 21,2 · 679,6 · 89 % · 53,31 · 14,81 · 3,6 · 1,8 · 5,2 · 93 · 131 · 22 · 108 · 112 · 90 · 104 · 37 · 67 · 105 · 41 · 65 · 98 · 35 · 63 · 51 · 53 · 8,45 · 3,73 · 2,27 · 18,19 · 0,41 · 3,30 · 3,48 · 3,93 · 5,1 % · 283 · 5,4 · 236 · 4,5 · 17,68 M · 7,03 M · 4,89 M · 29,6 M · 29 % · 3,01 · 2,81 · 1.236 · 306 · 0,33 · 0,44.
