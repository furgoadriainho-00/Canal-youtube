"""Bomba de calor frente a calefacción eléctrica de resistencia (radiadores, zócalos), con datos oficiales.

- Calor que necesita una casa: gas de calefacción RECS 2020 (CE5.4) × 0,80 (igual que en Heat Pump vs Gas).
- Resistencia eléctrica: 1 kWh de calor por kWh de luz (COP 1).
- Bomba de calor: COP 2,2 (HSPF2 7,5 ÷ 3,412, mínimo federal, 10 CFR 430.32(c)(5)); COP 1,75 a 5 °F (mínimo ENERGY STAR clima frío).
- Luz por estado: EIA EPM 5.6.B, ene–ago 2026.
- Física: cero absoluto = −459,67 °F.
"""
KWH_MMBTU = 293.07
ZONA = {"Hot-humid": 20.804, "Mixed-humid": 44.01, "Very cold/Cold": 60.753}
EST = [("Florida", "Hot-humid", 15.32), ("Georgia", "Mixed-humid", 15.48), ("Minnesota", "Very cold/Cold", 16.44)]
COP = 7.5 / 3.412
print("estado,calor_kWh,resistencia_$,bomba_2.2_$,bomba_1.75_$,ahorro_$")
for e, z, c in EST:
    kwh = ZONA[z] * 0.80 * KWH_MMBTU
    r, b, f = kwh * c / 100, kwh / COP * c / 100, kwh / 1.75 * c / 100
    print(f"{e},{kwh:.0f},{r:.0f},{b:.0f},{f:.0f},{r-b:.0f}")
print(f"\nCOP 2,2 → la bomba de calor usa {1/COP:.0%} de la luz de la resistencia; COP 1,75 → {1/1.75:.0%}")
# Calor que aún tiene el aire frío, medido desde el cero absoluto (escala Rankine)
for f in (47, 32, 5, 0):
    print(f"aire a {f} °F: {(f+459.67)/(70+459.67):.0%} de la energía térmica del aire a 70 °F (en temperatura absoluta)")
# RECS HC6.1 (millones de hogares, equipo principal de calefacción)
print(f"\nbomba de calor 16,13 M + minisplit 1,06 M = {16.13+1.06:.2f} M; resistencia (equipos fijos 7,65 + portátiles 3,03) = {7.65+3.03:.2f} M de 123,53 M ({(7.65+3.03)/123.53:.1%})")
