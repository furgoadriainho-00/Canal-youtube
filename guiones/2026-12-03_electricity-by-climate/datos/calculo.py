"""Lo que más electricidad gasta en cada clima (RECS 2020, CE5.3a y CE5.3b).
Medias por hogar QUE TIENE ese uso (MMBtu → kWh × 293,07). Precio único: 18,19 ¢/kWh (EIA EPM 5.3, ene–ago 2026), para comparar solo el consumo.
Calefacción = calefacción + ventilador de calefacción; aire acondicionado = AC + ventilador de refrigeración.
"""
import sys, openpyxl
from pathlib import Path
D = Path(sys.argv[0]).resolve().parent
def filas(f):
    ws = openpyxl.load_workbook(D / f, data_only=True).active
    rows = list(ws.iter_rows(values_only=True))
    return rows[3], {str(r[0]).strip(): r for r in rows if r[0]}
ha, a = filas("ce5.3a.xlsx"); hb, b = filas("ce5.3b.xlsx")
CLIMAS = ["All homes", "Very cold and Cold", "Mixed-humid", "Hot-humid", "Mixed-dry and Hot-dry", "Marine"]
USOS = {
    "Heating (with its fan)": lambda A, B: A[1] + A[2],
    "Air conditioning (with its fan)": lambda A, B: A[3] + A[4],
    "Water heating": lambda A, B: A[8],
    "Clothes dryer": lambda A, B: A[10],
    "Lighting": lambda A, B: A[11],
    "All refrigerators": lambda A, B: B[1],
    "Separate freezer": lambda A, B: B[4],
    "TVs and related": lambda A, B: B[8],
    "Dehumidifier": lambda A, B: A[6],
    "Ceiling fans": lambda A, B: A[5],
    "Cooking": lambda A, B: B[5],
}
EXTRA = {"Pool pump": lambda A, B: B[12], "Hot tub (heater + pump)": lambda A, B: B[13] + B[14], "EV charging": lambda A, B: A[12]}
C = 0.1819
for cl in CLIMAS:
    A, B = a[cl], b[cl]
    res = sorted(((n, f(A, B) * 293.07) for n, f in USOS.items()), key=lambda x: -x[1])
    print(f"\n== {cl}")
    for i, (n, k) in enumerate(res, 1):
        print(f"  {i}. {n}: {k:,.0f} kWh → {k*C:,.0f} $")
    for n, f in EXTRA.items():
        try:
            k = f(A, B) * 293.07; print(f"  (solo quien lo tiene) {n}: {k:,.0f} kWh → {k*C:,.0f} $")
        except TypeError:
            print(f"  (solo quien lo tiene) {n}: dato no publicado (Q)")
