"""Secadora de gas frente a eléctrica.
- RECS 2020 CE5.3a: electricidad de secadoras 2,319 MMBtu por hogar que la usa. CE5.4: gas natural de secadoras 2,064 MMBtu.
- DOE, 10 CFR 430 subparte B, apéndice D2: 283 ciclos al año (4.5.1(1)); desde 2028, 236 (4.5.1(2)); carga de prueba estándar 8,45 lb.
- 10 CFR 430.32(h): CEF mínimo desde 2015: eléctrica ventilada estándar 3,73 lb/kWh, gas 3,30; desde el 1/3/2028: 3,93 y 3,48. 1994: EF 3,01 y 2,67.
- Precios: luz EIA EPM 5.3/5.6.B (ene–ago 2026); gas EIA, residencial 2025 ($/Mcf); 1 Mcf = 1,036 MMBtu; 1 MMBtu = 293,07 kWh.
- RECS 2020 HC3.1: hogares con secadora por combustible.
"""
KWH = 293.07
E_KWH = 2.319 * KWH
G_MMBTU = 2.064
CICLOS = 283
EST = [("Florida", 15.32, 25.48), ("Arizona", 15.36, 18.58), ("Washington", 14.42, 17.62), ("Georgia", 15.48, 20.42),
       ("Minnesota", 16.44, 10.98), ("Illinois", 19.23, 11.25), ("US average", 18.19, 15.34)]
print(f"eléctrica: {E_KWH:.1f} kWh/año → {E_KWH/CICLOS:.2f} kWh por carga (283 cargas)")
print(f"gas: {G_MMBTU} MMBtu/año → {G_MMBTU/1.036:.3f} Mcf → {G_MMBTU*1e6/CICLOS:,.0f} Btu por carga")
print("estado,luz_¢,gas_$Mcf,eléctrica_$año,gas_$año,eléctrica_$carga,gas_$carga,diferencia_$año")
for e, c, g in EST:
    ea, ga = E_KWH * c / 100, G_MMBTU / 1.036 * g
    print(f"{e},{c},{g},{ea:.0f},{ga:.0f},{ea/CICLOS:.2f},{ga/CICLOS:.2f},{ea-ga:.0f}")
print("\nprueba del DOE (carga 8,45 lb):")
for n, cef in (("eléctrica 1994 (EF)", 3.01), ("eléctrica 2015", 3.73), ("eléctrica 2028", 3.93), ("gas 2015", 3.30), ("gas 2028", 3.48)):
    print(f"  {n}: {cef} lb/kWh → {8.45/cef:.2f} kWh por carga (máximo)")
print(f"eléctrica 2015 en la prueba: {8.45/3.73:.2f} kWh × 18,19 ¢ = {8.45/3.73*0.1819:.2f} $ por carga")
print(f"mejora 2015→2028 eléctrica: {1-3.73/3.93:.1%} menos energía por carga")
print(f"\nhogares (M): con secadora 102,32 · eléctrica 82,21 ({82.21/102.32:.0%}) · gas 18,89 ({18.89/102.32:.0%}) · propano 1,22 · sin secadora 21,20 de 123,53")
print("cargas por semana (M): 0 → 1,92 · 1–4 → 67,48 · 5–9 → 25,93 · 10–15 → 6,06 · >15 → 0,93")
print(f"1–4 cargas: {67.48/102.32:.0%} de los hogares con secadora")
print(f"283 cargas/año = {283/52:.1f} por semana; 236 = {236/52:.1f}")
for e, c, g in EST[-1:]:
    print(f"10 años, media EE. UU.: eléctrica {E_KWH*c/100*10:.0f} $, gas {G_MMBTU/1.036*g*10:.0f} $ (sin la luz del motor de la de gas ni subidas de precio)")
print("\nprecio de la misma energía (1 MMBtu):")
for e, c, g in EST:
    pe, pg = c / 100 * KWH, g / 1.036
    print(f"  {e}: luz {pe:.2f} $ · gas {pg:.2f} $ · luz/gas {pe/pg:.1f}×")
print(f"energía al año: eléctrica 2,319 MMBtu frente a gas 2,064 MMBtu ({2.064/2.319:.0%})")
viejas = 17.68 + 7.03 + 4.89
print(f"\nsecadoras de 10 años o más en 2020: {viejas:.2f} M ({viejas/102.32:.0%} de las secadoras)")
print(f"prueba: norma de 1994 {8.45/3.01:.2f} kWh frente a 2015 {8.45/3.73:.2f} kWh → {1-3.01/3.73:.0%} menos energía con la de 2015")
print("\nuna carga de prueba en una eléctrica nueva (2,27 kWh):")
for e, c in (("Washington", 14.42), ("US average", 18.19), ("Illinois", 19.23)):
    print(f"  {e}: {8.45/3.73*c/100:.2f} $")
