# Sources · Heat Pump vs Gas Furnace

1. **EIA, Residential Energy Consumption Survey 2020, table CE5.4** ("Detailed household natural gas and propane end-use consumption — averages"). Space-heating gas per household that uses it, million BTU: hot-humid 20.804 · mixed-dry/hot-dry 19.009 · marine 30.236 · mixed-humid 44.010 · very cold/cold 60.753. Copy in `datos/ce5.4.xlsx`.
   https://www.eia.gov/consumption/residential/data/2020/index.php?view=consumption
2. **EIA, Electric Power Monthly, table 5.6.B**: residential electricity price by state, January–August 2026 (preliminary). FL 15.32 · AZ 15.36 · WA 14.42 · GA 15.48 · MN 16.44 · IL 19.23 ¢/kWh. US average: 18.19 (table 5.3).
   https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_b
3. **EIA, Natural Gas Prices**: residential gas, 2025, $ per thousand cubic feet. US 15.34 · FL 25.48 · AZ 18.58 · WA 17.62 · GA 20.42 · MN 10.98 · IL 11.25.
   https://www.eia.gov/dnav/ng/ng_pri_sum_a_EPG0_PRS_DMcf_a.htm
4. **ENERGY STAR, furnaces (key product criteria)**: at least 95% AFUE in the South and 97% in the North (version 5.0, in effect since July 31, 2026).
   https://www.energystar.gov/products/furnaces/key_product_criteria
5. **Federal minimum for split heat pumps — primary source:** 10 CFR 430.32(c)(5): "Central air conditioners and central air conditioning heat pumps manufactured on or after January 1, 2023, must have a Seasonal Energy Efficiency Ratio 2 and a Heating Seasonal Performance Factor 2 not less than: … (ii) Split systems—heat pumps: SEER2 14.3, HSPF2 7.5." Checked in the official text (Code of Federal Regulations, 2025 edition, GovInfo) on 2026-11-04.
   https://www.govinfo.gov/content/pkg/CFR-2025-title10-vol3/xml/CFR-2025-title10-vol3-sec430-32.xml
   ENERGY STAR cold-climate heat pumps: COP of 1.75 or higher at 5 °F. https://www.energystar.gov/products/air_source_heat_pumps/key-product-criteria
6. **Price changes since 2020**: residential electricity 13.15¢ (2020) → 18.19¢ (Jan–Aug 2026), +38% (EIA EPM table 5.3); residential gas $10.78/Mcf (2020) → $15.34 (2025), +42% (EIA annual price series).
   https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_03 · https://www.eia.gov/dnav/ng/ng_pri_sum_dcu_nus_a.htm

## Assumptions (stated in the video or the description)
- Heat a home needs = RECS gas × 0.80, the assumed efficiency of the furnaces those homes had in 2020.
- New furnace at 95% in every state. In the North the ENERGY STAR minimum is 97%, so this assumption slightly favors the heat pump in MN and IL.
- Heat pump: seasonal COP = HSPF2 ÷ 3.412 = 2.2. That is the rating for a moderate climate; real-world efficiency is lower in cold climates, which is why COP 1.75 is also shown.
- Conversions: 1 MMBtu = 293.07 kWh; 1 Mcf = 1.036 MMBtu; 1 therm = 29.307 kWh.
- Running costs only. Purchase, installation and the cooling a heat pump also provides are not included.
- Dual fuel is explained with the break-even logic only. No savings figure is given, because there is no source for one.

## Calculation
`python3 datos/calculo.py` → `datos/resultados.txt`. Every number in the narration comes from there.
