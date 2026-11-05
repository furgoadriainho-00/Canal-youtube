# Fuentes · Tank vs Tankless vs Heat Pump Water Heater

1. **Mínimos federales, 10 CFR 430.32(d)(1)** (Code of Federal Regulations, edición 2025, GovInfo; vigentes hasta las normas nuevas de 2029):
   - Gas con depósito, de 20 a 55 gal, uso medio: UEF = 0,6483 − 0,0017 × Vr → con 50 gal, **0,563**.
   - Eléctrico con depósito, de 20 a 55 gal, uso medio: UEF = 0,9307 − 0,0002 × Vr → con 50 gal, **0,921**.
   - Gas sin depósito (menos de 2 gal, más de 50.000 Btu/h), uso medio: **0,81**. Eléctrico sin depósito, uso medio: **0,91**.
   https://www.govinfo.gov/content/pkg/CFR-2025-title10-vol3/xml/CFR-2025-title10-vol3-sec430-32.xml
2. **ENERGY STAR, criterios de los termos** (https://www.energystar.gov/products/water_heaters/residential_water_heaters_key_product_criteria):
   - Gas con depósito de 20 a 55 gal: «Medium Draw Pattern: UEF ≥ 0.81».
   - Gas sin depósito: «UEF ≥ 0.95»; «Max GPM ≥ 2.8 over a 67° rise».
   - Bomba de calor: «Integrated HPWH — UEF ≥ 3.30».
   - Definición: «Uniform Energy Factor (UEF): … The higher the UEF value is, the more efficient the water heater. UEF is determined by the Department of Energy's test method outlined in 10 CFR Part 430, Subpart B, Appendix E.»
3. **ENERGY STAR, gas tankless** (https://www.energystar.gov/products/whole_home_tankless_gas_water_heaters): caudales típicos «Shower and Bathtub - 2.5 GPM», «Clothes Washer - 3.3 GPM», «Kitchen and Bathroom Sink - 2.2 GPM».
4. **ENERGY STAR, termos con bomba de calor** (https://www.energystar.gov/products/heat_pump_water_heaters): necesitan un espacio de «40° to 90° F» y unos «1,000 cubic feet of air space».
5. **EIA RECS 2020**: termo eléctrico 2.706 kWh por hogar (CE5.3a); termo de gas 18,154 MMBtu por hogar (CE5.4, copia en `datos/ce5.4.xlsx`); HC8.1 (copia en `datos/hc8.1.xlsx`): gas 59,33 M de hogares, eléctrico 57,04 M, sin depósito 8,03 M de 123,53 M (6,5 %).
   https://www.eia.gov/consumption/residential/data/2020/
6. **Precios EIA**: luz 18,19 ¢/kWh en EE. UU. (ene–ago 2026, EPM 5.3). Por estado (EPM 5.6.B): WA 14,42 · FL 15,32 · TX 16,03 · IL 19,23 · NY 29,26 · CA 32,58. Gas: 15,34 $/Mcf (2025), con 1 Mcf = 1,036 MMBtu.
7. **ENERGY STAR, lavadoras**: «Water heating consumes about 90% of the energy it takes to operate a clothes washer.» https://www.energystar.gov/products/clothes_washers (ya usada en el primer vídeo).

## Cifras en pantalla, tal como salen (todas en `datos/resultados.txt`)
$492 · $498 · $137 · −$355 · 72 % (355 ÷ 492) · 59.3M · 57.0M · UEF 0.92 · 0.91 · 3.30 · 3.6× (3,6; 3,30 ÷ 0,921) · 2.8 GPM (2,8) · 0.56 · 0.81 · 0.95 · $269 · $187 · $159 · $165 · ~$100 (104–110) · −$80 a −$110 (82–110) · WA $281 · FL $299 · TX $313 · IL $375 · NY $571 · CA $636 · 1,950 kWh (1.951) · 2.5 · 2.2 · 3.3 · 2.8 GPM · 4.7 GPM (2,5 + 2,2) · 40–90 °F · 1,000 ft³ · 6.5 % · 90 %.

## Supuestos
- Agua caliente que necesita el hogar = consumo RECS × eficiencia del termo normal (0,921 eléctrico; 0,563 gas). Las eficiencias UEF son de ensayo: el uso real varía.
- Termo de 50 galones con patrón de uso medio. RECS 2020: 46,85 M de hogares con termo de 50 gal o más y 55,37 M con termo de 31 a 49 gal.
- Solo costes de uso. No incluye compra ni instalación.
- «Electric resistance can't get much better than one unit of heat per unit of electricity» es física básica (rendimiento máximo de 1,0 en la resistencia) y coincide con el UEF de 0,92 / 0,91.
