"""HSPF2 → COP y coste anual en Minnesota (casa típica de clima frío, del largo del 19 de noviembre).
Calor: RECS 2020 CE5.4 very cold/cold 60,753 MMBtu × 0,80 × 293,07 kWh/MMBtu. Luz MN 16,44 ¢ (EIA EPM 5.6.B, ene–ago 2026).
"""
kwh = 60.753 * 0.80 * 293.07
for h in (7.5, 9):
    cop = h / 3.412
    print(f"HSPF2 {h}: COP {cop:.2f} · {1/cop:.0%} de la luz de un radiador · MN {kwh/cop*0.1644:.0f} $/año")
print(f"diferencia MN: {kwh/(7.5/3.412)*0.1644 - kwh/(9/3.412)*0.1644:.0f} $/año")
