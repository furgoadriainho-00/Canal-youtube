"""Termos: depósito normal, sin depósito (tankless) y con bomba de calor. Coste anual con eficiencias oficiales.

Eficiencias (UEF):
- Mínimo federal, 10 CFR 430.32(d)(1), termo de 50 galones con patrón de uso medio:
  gas con depósito 0,6483 − 0,0017×50 = 0,563 · eléctrico con depósito 0,9307 − 0,0002×50 = 0,921 ·
  gas sin depósito 0,81 · eléctrico sin depósito 0,91.
- ENERGY STAR: gas con depósito ≥ 0,81 · gas sin depósito ≥ 0,95 · termo con bomba de calor integrado ≥ 3,30.
Agua caliente que necesita el hogar = consumo RECS 2020 × eficiencia del termo normal:
- hogares con termo eléctrico: 2.706 kWh (CE5.3a) × 0,921
- hogares con termo de gas: 18,154 MMBtu (CE5.4) × 0,563
Precios EIA: luz 0,1819 $/kWh (2026, ene–ago), gas 15,34 $/Mcf (2025) = 14,81 $/MMBtu.
"""
KWH = 0.1819; GAS = 15.34 / 1.036; KWH_MMBTU = 293.07
gas_tank, elec_tank = 0.6483 - 0.0017 * 50, 0.9307 - 0.0002 * 50
print(f"UEF mínimos 50 gal: gas {gas_tank:.3f} · eléctrico {elec_tank:.3f}")
# casa con termo eléctrico
util_e = 2706 * elec_tank  # kWh de agua caliente útil
print(f"\nCASA ELÉCTRICA (agua caliente útil {util_e:.0f} kWh)")
for n, uef in [("termo eléctrico normal", elec_tank), ("eléctrico sin depósito (mín. federal)", 0.91), ("bomba de calor (ENERGY STAR)", 3.30)]:
    kwh = util_e / uef
    print(f"  {n:38s} {kwh:6.0f} kWh  ${kwh*KWH:4.0f}")
# casa con termo de gas
util_g = 18.154 * gas_tank  # MMBtu útiles
print(f"\nCASA DE GAS (agua caliente útil {util_g:.2f} MMBtu = {util_g*KWH_MMBTU:.0f} kWh)")
for n, uef in [("gas con depósito (mín. federal)", gas_tank), ("gas con depósito ENERGY STAR", 0.81),
               ("gas sin depósito (mín. federal)", 0.81), ("gas sin depósito ENERGY STAR", 0.95)]:
    print(f"  {n:38s} {util_g/uef:6.2f} MMBtu ${util_g/uef*GAS:4.0f}")
kwh_bc = util_g * KWH_MMBTU / 3.30
print(f"  {'bomba de calor (ENERGY STAR), con luz':38s} {kwh_bc:6.0f} kWh   ${kwh_bc*KWH:4.0f}")
print(f"\nbomba de calor frente a termo eléctrico: {3.30/elec_tank:.1f} veces más eficiente")
print(f"RECS HC8.1: sin depósito 8,03 M de 123,53 M hogares = {8.03/123.53:.1%}; gas 59,33 M; eléctrico 57,04 M")

# Ahorro del termo con bomba de calor frente al eléctrico normal, según el precio de la luz del estado (EIA EPM 5.6.B, ene–ago 2026)
ahorro_kwh = 2706 - util_e / 3.30
print(f"\nkWh ahorrados al año: {ahorro_kwh:.0f}")
for e, c in [("Washington", 14.42), ("Florida", 15.32), ("Texas", 16.03), ("EE. UU.", 18.19), ("Illinois", 19.23), ("New York", 29.26), ("California", 32.58)]:
    print(f"  {e:11s} {c:5.2f}¢ → ${ahorro_kwh*c/100:4.0f}/año")
