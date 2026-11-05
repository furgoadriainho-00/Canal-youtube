"""Termostato inteligente: cuánto puede ahorrar, con datos oficiales.

- ENERGY STAR (criterios de certificación): reducción anual del tiempo de funcionamiento ≥ 8 % en calefacción y ≥ 10 % en
  refrigeración (límite inferior del IC 95 % de la media nacional); percentil 20: ≥ 4 % y ≥ 5 % («4 de cada 5 hogares»).
- ENERGY STAR: el hogar medio gasta «more than $900 a year» en calefacción y refrigeración.
- DOE (boletín 2/2/2024): bajar el termostato al menos 8 h al día puede ahorrar «as much as 10%» al año en calefacción y refrigeración.
- RECS 2020: gas de calefacción 44,897 MMBtu por hogar (CE5.4); aire acondicionado y su ventilador 2.318 + 457 kWh (CE5.3a);
  calefacción eléctrica y su ventilador 2.484 + 233 kWh. Precios EIA: luz 0,1819 $/kWh (2026), gas 15,34 $/Mcf (2025).
- Supuesto: menos tiempo de funcionamiento ≈ menos energía, en la misma proporción (equipos de una sola etapa).
"""
GAS_MMBTU = 15.34 / 1.036
gas_cal = 44.897 * GAS_MMBTU
aire = (2318 + 457) * 0.1819
elec_cal = (2484 + 233) * 0.1819
print(f"calefacción de gas ${gas_cal:.0f} · aire acondicionado ${aire:.0f} · calefacción eléctrica ${elec_cal:.0f}")
print(f"casa de gas con aire: mínimo certificado {gas_cal*0.08:.0f} + {aire*0.10:.0f} = ${gas_cal*0.08 + aire*0.10:.0f}/año")
print(f"  4 de cada 5 hogares, al menos: {gas_cal*0.04:.0f} + {aire*0.05:.0f} = ${gas_cal*0.04 + aire*0.05:.0f}/año")
print(f"casa eléctrica con aire: {elec_cal*0.08:.0f} + {aire*0.10:.0f} = ${elec_cal*0.08 + aire*0.10:.0f}/año")
print(f"sobre los $900 de ENERGY STAR: 8 % = ${900*0.08:.0f} · 10 % = ${900*0.10:.0f}")
print(f"DOE, hasta un 10 % (casa de gas con aire): ${(gas_cal + aire)*0.10:.0f}/año")
# RECS HC6.1, millones de hogares
smart, prog, noprog = 12.78, 52.59, 44.08
una, manual, auto = 50.69, 31.04, 19.79
print(f"programable o inteligente: {smart+prog:.1f} M · lo dejan ajustar solo: {auto} M ({auto/(smart+prog):.0%})")
print(f"una temperatura fija: {una} M · ajuste a mano: {manual} M")
print(f"ejemplo de amortización: termostato de $X → X / {gas_cal*0.08 + aire*0.10:.0f} años")

# Por región (RECS 2020): gas de calefacción por hogar (CE5.4, MMBtu) y aire acondicionado + ventilador (CE5.3a, kWh)
REG = {"Northeast": (52.352, 1395 + 323), "Midwest": (62.852, 1522 + 299), "South": (33.725, 3304 + 588), "West": (29.696, 2059 + 402)}
print("\nregión: calefacción de gas $ → 8 % · aire $ → 10 % · total")
for r, (g, a) in REG.items():
    cg, ca = g * GAS_MMBTU, a * 0.1819
    print(f"{r:9s} ${cg:4.0f} → ${cg*0.08:3.0f} · ${ca:4.0f} → ${ca*0.10:3.0f} · ${cg*0.08 + ca*0.10:4.0f}")
