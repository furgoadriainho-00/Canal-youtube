"""Coste de un calefactor de 1.500 W a plena potencia, por estado.
Luz residencial ene–ago 2026, EIA EPM 5.6.B (estados) y 5.3 (EE. UU.), ¢/kWh, ya citados en los guiones del 12 y del 16 de noviembre.
"""
P = 1.5  # kW
PRECIOS = [("Washington", 14.42), ("Florida", 15.32), ("Texas", 16.03), ("Minnesota", 16.44),
           ("US average", 18.19), ("New York", 29.26), ("Massachusetts", 30.19), ("California", 32.58)]
print("estado,¢/kWh,$/hora,$/mes (8 h al día, 30 días)")
for e, c in PRECIOS:
    print(f"{e},{c},{P*c/100:.2f},{P*8*30*c/100:.0f}")
