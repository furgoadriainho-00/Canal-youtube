# Fuentes · Heat Pump vs Gas Furnace

1. **EIA, Residential Energy Consumption Survey 2020, tabla CE5.4** («Detailed household natural gas and propane end-use consumption — averages»). Gas de calefacción por hogar que lo usa, en millones de BTU: hot-humid 20,804 · mixed-dry/hot-dry 19,009 · marine 30,236 · mixed-humid 44,010 · very cold/cold 60,753. Copia en `datos/ce5.4.xlsx`.
   https://www.eia.gov/consumption/residential/data/2020/index.php?view=consumption
2. **EIA, Electric Power Monthly, tabla 5.6.B**: precio residencial de la electricidad por estado, enero–agosto de 2026 (preliminar). FL 15,32 · AZ 15,36 · WA 14,42 · GA 15,48 · MN 16,44 · IL 19,23 ¢/kWh. Media de EE. UU.: 18,19 (tabla 5.3).
   https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_b
3. **EIA, Natural Gas Prices**: gas residencial 2025, en $ por cada mil pies cúbicos. EE. UU. 15,34 · FL 25,48 · AZ 18,58 · WA 17,62 · GA 20,42 · MN 10,98 · IL 11,25.
   https://www.eia.gov/dnav/ng/ng_pri_sum_a_EPG0_PRS_DMcf_a.htm
4. **ENERGY STAR, calderas (key product criteria)**: al menos 95 % AFUE en el sur y 97 % en el norte (versión 5.0, en vigor desde el 31/07/2026).
   https://www.energystar.gov/products/furnaces/key_product_criteria
5. **Mínimo federal para bombas de calor split (2023)**: HSPF2 de 7,5 o más. Varias fuentes del sector coinciden; falta la fuente primaria del DOE (10 CFR 430.32). ENERGY STAR para bombas de calor: COP de 1,75 o más a 5 °F en las de clima frío.
   https://www.energystar.gov/products/air_source_heat_pumps/key-product-criteria · https://www.nahb.org/blog/2022/05/upcoming-changes-to-efficiency-standards-for-ac-units-and-heat-pumps

## Supuestos (dichos en el vídeo o en la descripción)
- Calor que necesita la casa = gas de RECS × 0,80, que es la eficiencia supuesta de las calderas que tenían esos hogares en 2020.
- Caldera nueva al 95 % en todos los estados. En el norte el mínimo de ENERGY STAR es 97 %, así que el supuesto favorece un poco a la bomba de calor en MN e IL.
- Bomba de calor: COP estacional = HSPF2 ÷ 3,412 = 2,2. Es el valor de ensayo para un clima moderado; en climas fríos el real es menor, y por eso se muestra también COP 1,75.
- Conversiones: 1 MMBtu = 293,07 kWh; 1 Mcf = 1,036 MMBtu; 1 therm = 29,307 kWh.
- Solo costes de uso. No incluye compra, instalación ni la refrigeración que también da la bomba de calor.

## Cálculo
`python3 datos/calculo.py` → `datos/resultados.txt`. Todas las cifras de la narración salen de ahí.

## Añadidos
6. **Evolución de los precios desde 2020**: electricidad residencial 13,15 ¢ (2020) → 18,19 ¢ (2026, ene–ago), +38 % (EIA EPM tabla 5.3); gas residencial 10,78 $/Mcf (2020) → 15,34 (2025), +42 % (EIA, serie anual de precios).
   https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_03 · https://www.eia.gov/dnav/ng/ng_pri_sum_dcu_nus_a.htm
- El sistema híbrido (dual fuel) se explica con la lógica del punto de empate. No se da ninguna cifra de ahorro, porque no hay una fuente.

## Cifras redondeadas en pantalla
18,2 ¢/kWh (18,19) · 53,3 y 14,8 $/MMBtu · relación 3,6 · empate nacional 3,4 · 2,4 en Washington (2,36) · 4,9 en Illinois (4,93) · 2,2 mínimo federal · coste 431, 340, 287, 311, 433, 465, 730, 727, 542, 1.065, 1.338, 556, 1.246 $ (ver `datos/resultados.txt`). +19 % caldera vieja (95 ÷ 80). 3,3 en el ejemplo (3,34).
