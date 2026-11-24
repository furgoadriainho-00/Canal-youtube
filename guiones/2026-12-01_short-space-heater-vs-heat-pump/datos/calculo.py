"""Mismo calor que un radiador de 1.500 W durante una hora: radiador (COP 1) frente a bomba de calor al mínimo federal (COP 2,2 = HSPF2 7,5 ÷ 3,412). Luz 18,19 ¢/kWh (EIA EPM 5.3, ene–ago 2026). Mes = 8 h × 30 días."""
cop = 7.5 / 3.412
for n, kwh in (("radiador", 1.5), ("bomba de calor", 1.5 / cop)):
    print(f"{n}: {kwh:.2f} kWh por hora → {kwh*0.1819:.2f} $/h · {kwh*0.1819*240:.0f} $/mes")
