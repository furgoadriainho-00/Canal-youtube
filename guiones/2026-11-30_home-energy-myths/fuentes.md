# Fuentes · 7 Home Energy Myths That Cost You Money

Vídeo recopilatorio: cada cifra sale de una fuente primaria ya comprobada en otro guion del canal (se indica cuál) o de `datos/calculo.py`.

## Mito 1 · bajar la calefacción
- **U.S. DOE (EERE), boletín del 2/2/2024:** «Setting back your thermostat for at least 8 hours per day can save you as much as 10% per year on heating and cooling costs.» https://content.govdelivery.com/accounts/USEERE/bulletins/3883189
- **ENERGY STAR, smart thermostats:** «almost half of the annual energy bill goes to heating and cooling – that's more than $900 a year.» https://www.energystar.gov/products/smart_thermostats → 900 × 10 % = hasta **90 $**.
- **ENERGY STAR, criterios de termostatos conectados:** reducción del tiempo de calefacción ≥ **8 %** (límite inferior del IC 95 % de la media nacional), con datos de hogares reales. https://www.energystar.gov/products/smart_thermostats/key_product_criteria
- **RECS 2020 HC6.1:** temperatura fija la mayor parte del tiempo **50,69 M** → 50,7 M.
- Todo en `../2026-11-09_smart-thermostat/fuentes.md` (puntos 1–4).
- «A cooler house loses heat to the outdoors more slowly»: física básica (la pérdida de calor crece con la diferencia de temperatura entre dentro y fuera); sin cifra.

## Mito 2 · bombas de calor bajo cero
- Cero absoluto −459,67 °F; aire a 0 °F **87 %** y a 32 °F **93 %** de la energía térmica del aire a 70 °F. ENERGY STAR clima frío: COP ≥ **1,75** a **5 °F**; resistencia COP 1.
- Casa típica: MN **2.342 $** (resistencia) frente a **1.065 $** (bomba, HSPF2 7,5); GA **1.597 $** frente a **727 $**.
- `../2026-11-19_heat-pump-freezing-air/fuentes.md` (puntos 1, 2, 3, 5 y 6) y su `datos/resultados.txt`.

## Mito 3 · calentador sin depósito
- Casa eléctrica: termo **492 $** · sin depósito al mínimo federal **498 $** · bomba de calor ENERGY STAR **137 $** (1 − 137/492 = **72 %**). Casa de gas: depósito al mínimo **269 $** · sin depósito al mínimo **187 $** → **82 $**.
- RECS 2020 HC8.1: sin depósito 8,03 M de 123,53 M = **6,5 %**.
- `../2026-11-12_water-heaters/fuentes.md` y `../2026-11-12_water-heaters/datos/resultados.txt` (UEF mínimos de 10 CFR 430.32(d)(1), ENERGY STAR, RECS CE5.3a/CE5.4/HC8.1, precios EIA).
- «Both turn electricity into heat almost one to one»: UEF mínimo del termo eléctrico 0,921 (10 CFR 430.32(d)(1)).

## Mito 4 · radiador portátil
- 1.500 W (ejemplo, «a fifteen-hundred-watt heater») → **1,5 kWh** por hora × 18,19 ¢ = **0,27 $** (27 ¢). 8 h × 30 días: EE. UU. **65 $** · WA **52 $** (14,42 ¢) · CA **117 $** (32,58 ¢).
- Bomba de calor COP 2,2 → **45 %** de la luz para el mismo calor.
- `../2026-11-22_short-space-heater-cost/fuentes.md` y `datos/calculo.py` de esta carpeta.
- «One of the most expensive ways to heat with electricity»: la resistencia es COP 1, el mínimo posible para un aparato eléctrico; la bomba de calor da 2,2.

## Mito 5 · lavadora
- **ENERGY STAR, clothes washers:** «Water heating consumes about 90% of the energy it takes to operate a clothes washer.» · «Switching your temperature setting from hot to warm can cut energy use in half.» · «Using the cold cycle reduces energy use even more.» https://www.energystar.gov/products/clothes_washers (citado en el Short del 29/10, `canales/how-your-home-works/videos/2026-10-29_short-washer-myth/fuentes.md`).
- **RECS 2020 HC3.1** (temperatura habitual de lavado, millones): caliente **8,72** · templada **53,11** · fría **42,13**. Copia en `../2026-11-26_gas-vs-electric-dryer/datos/hc3.1.xlsx`.

## Mito 6 · LED
- FTC: 60 W ≈ 800 lm; LED de 800 lm ≈ 9 W. 3 h al día × 18,19 ¢: **11,95 $** frente a **1,79 $** → **10,16 $** por bombilla, **102 $** por 10. Porche 12 h por noche: **47,80 $** frente a **7,17 $**.
- 10 CFR 430.32(dd): desde el **25 de julio de 2022**, prohibida la venta de bombillas de uso general de menos de **45 lm/W** (60 W ÷ 800 lm = 13,3 lm/W).
- RECS 2020 HC5.1: al menos una incandescente o halógena **75,22 M** → 75,2 M.
- `../2026-11-23_light-bulb-story/fuentes.md` y su `datos/resultados.txt`.

## Mito 7 · aparatos de gas
- RECS 2020: cocina eléctrica 0,991 MMBtu (290,4 kWh) → **52,83 $**; cocina de gas 2,023 MMBtu → **29,95 $** (2,0×). Secadora eléctrica 2,319 MMBtu → **124 $**; gas 2,064 MMBtu → **31 $**. 1 MMBtu: luz **53,31 $**, gas **14,81 $**.
- `../2026-11-29_short-stove-cost/fuentes.md` y `../2026-11-26_gas-vs-electric-dryer/fuentes.md`.
- Caldera nueva (95 %) frente a bomba de calor: MN **542 $** frente a **1.065 $**; FL **431 $** frente a **340 $**. `../2026-11-05_heat-pump-vs-gas/datos/resultados.txt`.

## Precios
- EIA EPM 5.3, luz residencial EE. UU. ene–ago 2026: **18,19 ¢/kWh**; 5.6.B: WA 14,42 · CA 32,58 · MN 16,44 · GA 15,48 · FL 15,32. EIA gas residencial 2025: **15,34 $/Mcf**.

## Cifras en pantalla, tal como salen
10 % · 900 · 90 · 8 % · 50,7 M · −459,67 · 87 % · 93 % · 0 °F · 32 °F · 5 °F · 1,75 · 1,0 · 2.342 · 1.065 · 1.597 · 727 · 6,5 % · 492 · 498 · 137 · 72 % · 269 · 187 · 82 · 1.500 W · 1,5 kWh · 27 · 65 · 52 · 117 · 0,45 · 45 % · 90 % · 8,72 M · 53,11 M · 42,13 M · 800 · 60 W · 9 W · 11,95 · 1,79 · 10,16 · 102 · 45 lm/W · 12 h · 47,80 · 7,17 · 75,2 M · 52,83 · 29,95 · 124 · 31 · 53,31 · 14,81 · 542 · 340 · 431.
