"""Coste anual de calefacción: caldera de gas nueva frente a bomba de calor, en 6 estados.

Calor que necesita el hogar = gas de calefacción por hogar en su zona climática (EIA RECS 2020, CE5.4)
                              × 0,80 (eficiencia supuesta de las calderas que había en esos hogares).
Caldera nueva: 95 % (mínimo ENERGY STAR en el sur; en el norte es 97 %, así que el gas sale algo peor de lo real).
Bomba de calor: COP estacional = HSPF2 7,5 (mínimo federal 2023) / 3,412 = 2,2; caso frío: COP 1,75 (mínimo ENERGY STAR cold climate a 5 °F).
Precios: electricidad residencial ene–ago 2026 (EIA EPM 5.6.B) y gas residencial 2025 (EIA, $/Mcf).
"""
KWH_POR_MMBTU, MMBTU_POR_MCF = 293.07, 1.036
AFUE_EXISTENTE, AFUE_NUEVA = 0.80, 0.95
COP_MIN, COP_FRIO = 7.5 / 3.412, 1.75
GAS_ZONA = {"Hot-humid": 20.804, "Mixed-dry/Hot-dry": 19.009, "Marine": 30.236, "Mixed-humid": 44.01, "Very cold/Cold": 60.753}
ESTADOS = [("Florida", "Hot-humid", 15.32, 25.48), ("Arizona", "Mixed-dry/Hot-dry", 15.36, 18.58),
           ("Washington", "Marine", 14.42, 17.62), ("Georgia", "Mixed-humid", 15.48, 20.42),
           ("Minnesota", "Very cold/Cold", 16.44, 10.98), ("Illinois", "Very cold/Cold", 19.23, 11.25)]

print(f"COP mínimo federal = {COP_MIN:.2f}")
print("estado,zona,calor_MMBtu,gas_nueva_usd,bomba_cop2.2_usd,bomba_cop1.75_usd,cop_empate")
for e, z, c, g in ESTADOS:
    calor = GAS_ZONA[z] * AFUE_EXISTENTE
    pe, pg = c / 100 * KWH_POR_MMBTU, g / MMBTU_POR_MCF
    print(f"{e},{z},{calor:.1f},{calor / AFUE_NUEVA * pg:.0f},{calor / COP_MIN * pe:.0f},{calor / COP_FRIO * pe:.0f},{pe / (pg / AFUE_NUEVA):.2f}")
pe, pg = 18.19 / 100 * KWH_POR_MMBTU, 15.34 / MMBTU_POR_MCF
print(f"nacional: electricidad {pe:.1f} $/MMBtu, gas {pg:.2f} $/MMBtu, relación {pe / pg:.2f}, COP de empate {pe / (pg / AFUE_NUEVA):.2f}")
print(f"fórmula casera: COP de empate = 27,84 × (¢/kWh ÷ 100) ÷ ($/therm); ejemplo 0,18 y 1,50 → {27.84 * 0.18 / 1.5:.2f}")
print(f"caldera vieja al 80 %: el gas cuesta {AFUE_NUEVA / AFUE_EXISTENTE - 1:.0%} más que con una nueva al 95 %")
