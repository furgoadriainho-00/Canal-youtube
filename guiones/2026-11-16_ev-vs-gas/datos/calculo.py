"""Cargar un coche eléctrico en casa frente a llenar el depósito: coste anual por estado.

- Consumo del eléctrico: 30 kWh/100 millas (EPA 2025: Model Y LR RWD 27 · Model Y LR AWD 29 · Ioniq 5 29–30 · Equinox EV FWD 31 · Mach-E RWD Ext 31).
- Gasolina: 27,2 mpg, media real de los coches nuevos de 2024 (EPA Automotive Trends).
- Millas al año: 11.026 por coche (FHWA Highway Statistics 2024, tabla VM-1, vía AFDC).
- Precios: gasolina normal 2025 (EIA, $/galón); luz residencial ene–ago 2026 (EIA EPM 5.6.B, ¢/kWh).
- Caso prudente: si el consumo EPA no incluyera las pérdidas de carga, se suman con la peor eficiencia de carga citada por ORNL (84 %).
"""
MILLAS, KWH100, MPG = 11026, 30, 27.2
EST = [("U.S.", 18.19, 3.097), ("Washington", 14.42, 4.132), ("California", 32.58, 4.410), ("Texas", 16.03, 2.660),
       ("Florida", 15.32, 2.957), ("Colorado", 16.80, 2.868), ("Minnesota", 16.44, 2.963), ("Ohio", 18.81, 2.960),
       ("New York", 29.26, 3.056), ("Massachusetts", 30.19, 2.970)]
print(f"galones/año {MILLAS/MPG:.0f} · kWh/año {MILLAS*KWH100/100:.0f}")
print("estado,gasolina_$,eléctrico_$,ahorro_$,eléctrico_84%_$,ahorro_84%_$,gas_$/100mi,ev_$/100mi")
for e, c, g in EST:
    gas = MILLAS / MPG * g
    ev = MILLAS * KWH100 / 100 * c / 100
    ev84 = ev / 0.84
    print(f"{e},{gas:.0f},{ev:.0f},{gas-ev:.0f},{ev84:.0f},{gas-ev84:.0f},{100/MPG*g:.2f},{KWH100*c/100:.2f}")
# precio de la luz al que el eléctrico empata con la gasolina (EE. UU.)
g = 3.097
print(f"empate en EE. UU.: luz a {100/MPG*g/KWH100*100:.1f} ¢/kWh (con 84 %: {100/MPG*g/KWH100*100*0.84:.1f} ¢)")
for m, k in [("Model Y LR RWD", 27), ("Equinox EV FWD", 31)]:
    print(f"{m}: {MILLAS*k/100*0.1819:.0f} $/año en EE. UU.")

# Evolución de precios: gasolina normal EE. UU. (EIA, $/galón) y luz residencial (EIA EPM 5.3, ¢/kWh)
GAS = {2020: 2.168, 2021: 3.008, 2022: 3.951, 2023: 3.519, 2024: 3.304, 2025: 3.097}
LUZ = {2020: 13.15, 2026: 18.19}
print("\ncada 100 millas: gasolina 2020 ${:.2f} · 2022 ${:.2f} · 2025 ${:.2f}".format(*(100 / MPG * GAS[a] for a in (2020, 2022, 2025))))
print("cada 100 millas: eléctrico 2020 ${:.2f} · 2026 ${:.2f}".format(KWH100 * LUZ[2020] / 100, KWH100 * LUZ[2026] / 100))
print(f"subida 2020→2025 gasolina {GAS[2025]/GAS[2020]-1:.0%} · luz 2020→2026 {LUZ[2026]/LUZ[2020]-1:.0%}")
# Efecto en la factura de la luz de casa
print(f"\nel coche suma {MILLAS*KWH100/100:.0f} kWh/año = {MILLAS*KWH100/100/10791:.0%} de los 10.791 kWh de un hogar medio (EIA, 2022)")
print(f"al mes: {MILLAS*KWH100/100/12:.0f} kWh ≈ ${MILLAS*KWH100/100/12*0.1819:.0f}")
print(f"RECS 2020: hogares que cargan un eléctrico, 2.363 kWh/año de carga = ${2363*0.1819:.0f}/año a 18,19 ¢")
# Luz residencial anual (EIA EPM 5.3): 2021 13,66 · 2022 15,04 · 2023 16,00 · 2024 16,48 · 2025 17,23
LUZ_A = {2020: 13.15, 2021: 13.66, 2022: 15.04, 2023: 16.00, 2024: 16.48, 2025: 17.23}
print("\naño: gasolina $/100mi · eléctrico $/100mi · proporción")
for a in range(2020, 2026):
    gg, ee = 100 / MPG * GAS[a], KWH100 * LUZ_A[a] / 100
    print(f"{a}: {gg:.2f} · {ee:.2f} · {ee/gg:.2f}")
