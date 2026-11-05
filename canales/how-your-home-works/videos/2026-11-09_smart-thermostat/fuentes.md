# Fuentes · Does a Smart Thermostat Actually Save Money?

1. **ENERGY STAR, smart thermostats** (https://www.energystar.gov/products/smart_thermostats), citas literales:
   - «For the average American household, almost half of the annual energy bill goes to heating and cooling – that's more than $900 a year.»
   - «Smart thermostats that earn the ENERGY STAR label have been independently certified, based on actual field data, to deliver energy savings.»
   - Geofencing: «This feature allows your thermostat to detect when you've left for the day to 'set back' your HVAC system…». Learning: «Certain ENERGY STAR certified smart thermostats can learn your preferences automatically and establish a schedule that adjusts to energy-saving temperatures when you are asleep or away.»
2. **ENERGY STAR, connected thermostat criteria** (https://www.energystar.gov/products/smart_thermostats/key_product_criteria), tabla 2:
   - Reducción anual del tiempo de funcionamiento en calefacción: límite inferior del IC 95 % de la media nacional ponderada **≥ 8 %**; media de los percentiles 20 **≥ 4 %**.
   - En refrigeración: **≥ 10 %** y **≥ 5 %**.
   - «The 20th percentile means that 4 out of 5 homes in the sample saved at least that much.» Datos: «a year of data from hundreds of their customers' homes», analizados con software de la EPA.
3. **U.S. DOE (EERE), boletín del 2 de febrero de 2024**: «Setting back your thermostat for at least 8 hours per day can save you as much as 10% per year on heating and cooling costs.» https://content.govdelivery.com/accounts/USEERE/bulletins/3883189
4. **EIA RECS 2020, tabla HC6.1** (millones de hogares; copia en `datos/hc6.1.xlsx`): termostato inteligente 12,78 · programable 52,59 · no programable 44,08. Cómo se controla la calefacción: una temperatura fija la mayor parte del tiempo 50,69 · a mano 31,04 · el termostato la ajusta solo 19,79.
   https://www.eia.gov/consumption/residential/data/2020/index.php?view=characteristics
5. **EIA RECS 2020, consumos por hogar**: gas de calefacción 44,897 MMBtu (CE5.4; por región NE 52,352 · MW 62,852 · S 33,725 · W 29,696); aire acondicionado 2.318 kWh + ventilador 457 (CE5.3a; por región NE 1.395+323 · MW 1.522+299 · S 3.304+588 · W 2.059+402); calefacción eléctrica 2.484 + ventilador 233.
6. **Precios EIA**: luz residencial 18,19 ¢/kWh (ene–ago 2026, EPM 5.3); gas residencial 15,34 $/Mcf (2025); 1 Mcf = 1,036 MMBtu.

## Cifras en pantalla, tal como salen (todas en `datos/resultados.txt`)
$900+ · $665 · $505 · 8 % · 10 % · 4 % · 5 % · $53 · $50 · $104 · $52 · $90 · $72–$90 · $50–$100 · 65M (65,4) · 52.6M · 12.8M · 19.8M · 20M · 30 % (19,79 ÷ 65,37) · 50.7M (50,7; 50,69 redondeado) · 31.0M · 44M · 12 % (12,78 ÷ 109,45) · $117 · NE $93 · MW $108 · S $111 · W $80 (y los parciales de la tabla de regiones).

## Supuestos
- Menos tiempo de funcionamiento ≈ menos energía, en la misma proporción. Se dice en el vídeo.
- El precio de $150 del termostato es un ejemplo, no un dato: se rotula «example» en pantalla.
- «La guía del DOE va en sentido contrario» al mito: es una interpretación del boletín, que dice que bajarlo ahorra. No se da ninguna otra cifra.
