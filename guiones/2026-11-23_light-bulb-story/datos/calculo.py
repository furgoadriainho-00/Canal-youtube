"""Historia de la bombilla: coste anual de una bombilla de 800 lúmenes según la tecnología/norma.
- 60 W incandescente ≈ 800 lm; LED de 800 lm ≈ 9 W (FTC, «Shopping for light bulbs»).
- 2014: bombillas de 750–1049 lm, máximo 43 W (10 CFR 430.32(dd)(1)(i), fila C).
- 2022: mínimo 45 lm/W (10 CFR 430.32(dd)).
- 2028: LED integrada omnidireccional corta, sin standby: 123/(1,2 + e^(−0,005·(lm−200))) + 25,9 lm/W (10 CFR 430.32(dd)(1)(iv)).
- Uso supuesto: 3 horas al día. Luz: 18,19 ¢/kWh (EIA EPM 5.3, ene–ago 2026).
- RECS 2020 HC5.1 y RECS 2015 HC5.1 (millones de hogares).
"""
import math
LM, H, C = 800, 3 * 365, 0.1819
w45 = LM / 45
ef28 = 123 / (1.2 + math.exp(-0.005 * (LM - 200))) + 25.9
w28 = LM / ef28
casos = [("incandescente 60 W", 60), ("halógena máx. 2014 (43 W)", 43), ("límite 2022 (45 lm/W)", w45),
         ("LED (FTC, 9 W)", 9), ("límite 2028", w28)]
print(f"horas al año: {H}; 2022: 800 lm ≤ {w45:.1f} W; 2028: {ef28:.1f} lm/W → ≤ {w28:.1f} W")
print("bombilla,W,kWh/año,$/año,$/año×10 bombillas")
for n, w in casos:
    k = w * H / 1000
    print(f"{n},{w:.1f},{k:.1f},{k*C:.2f},{k*C*10:.0f}")
print(f"LED frente a 60 W: {9/60:.0%} de la luz, ahorro {(60-9)*H/1000*C:.2f} $/año por bombilla, {(60-9)*H/1000*C*10:.0f} $ por 10")
# RECS
print(f"2020 todo o casi todo LED: {26.08+31.61:.2f} M de 123,53 ({(26.08+31.61)/123.53:.0%})")
print(f"2015 todo o casi todo LED: {1.2+4.1:.1f} M de 118,2 ({(1.2+4.1)/118.2:.1%}; EIA lo publica como 4 %)")
print(f"2020 todo o casi todo incandescente/halógena: {8.5+10.19:.2f} M ({(8.5+10.19)/123.53:.0%}); 2015: {13.2+23.4:.1f} M ({(13.2+23.4)/118.2:.0%})")
print(f"2020 al menos una incandescente/halógena: 75,22 M ({75.22/123.53:.0%})")
print(f"CFL todo o casi todo: 2020 {5.35+9.55:.2f} M ({(5.35+9.55)/123.53:.0%}); 2015 {11.6+25.9:.1f} M ({(11.6+25.9)/118.2:.0%})")
# Por estado (EIA EPM 5.6.B, ene–ago 2026): ahorro de cambiar una de 60 W por una LED de 9 W, 3 h al día
for e, c in (("Washington", 14.42), ("California", 32.58)):
    print(f"ahorro 60→9 W en {e} ({c} ¢): {(60-9)*H/1000*c/100:.2f} $/año")
# Exterior toda la noche: RECS 2020 HC5.1; supuesto 12 h al día
print(f"exterior toda la noche: 51,12 M hogares con al menos una; 13,62 M con incandescente/halógena ({13.62/123.53:.0%} de todos)")
for w in (60, 9):
    print(f"exterior {w} W, 12 h al día: {w*12*365/1000*C:.2f} $/año")
print(f"diferencia exterior: {(60-9)*12*365/1000*C:.2f} $/año")
