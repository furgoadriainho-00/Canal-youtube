"""Coste anual por uso final: kWh medios por hogar que lo usa (EIA RECS 2020) x precio residencial medio 2026 (EIA)."""
import csv, pathlib
PRECIO = 0.1819  # $/kWh, EIA Electric Power Monthly tabla 5.3, media residencial EE. UU. enero-agosto 2026 (preliminar)
# (nombre en pantalla, kWh/año por hogar que lo usa, tabla RECS)
USOS = [
    ("Air conditioning (incl. its fan)", 2318 + 457, "CE5.3a"),
    ("Electric space heating (incl. its fan)", 2484 + 233, "CE5.3a"),
    ("Electric water heater", 2706, "CE5.3a"),
    ("Pool pump", 2384, "CE5.3b"),
    ("EV charging", 2363, "CE5.3a"),
    ("Hot tub (heater + pump)", 1479 + 484, "CE5.3b"),
    ("Dehumidifier", 999, "CE5.3a"),
    ("Main refrigerator", 617, "CE5.3b"),
    ("Clothes dryer", 680, "CE5.3a"),
    ("Lighting", 654, "CE5.3a"),
    ("TVs and related devices", 632, "CE5.3b"),
    ("Separate freezer", 570, "CE5.3b"),
    ("Second refrigerator", 494, "CE5.3b"),
    ("Cooking (range/oven)", 290, "CE5.3b"),
    ("Ceiling fans", 226, "CE5.3a"),
    ("Humidifier", 139, "CE5.3a"),
    ("Dishwasher (machine only)", 112, "CE5.3b"),
    ("Microwave", 107, "CE5.3b"),
    ("Clothes washer (machine only)", 69, "CE5.3a"),
]
out = pathlib.Path(__file__).with_name("costes.csv")
with out.open("w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["uso", "kwh_anual", "coste_anual_usd", "tabla"])
    for n, k, t in sorted(USOS, key=lambda x: -x[1]):
        w.writerow([n, k, round(k * PRECIO), t])
        print(f"{n:42s} {k:5d} kWh  ${k*PRECIO:5.0f}")
