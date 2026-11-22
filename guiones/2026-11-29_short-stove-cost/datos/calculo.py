"""Cocina eléctrica frente a gas: coste al año (RECS 2020).
CE5.3b: cocina eléctrica 0,991 MMBtu por hogar que la usa (cocinas, placas y hornos; sin microondas). Microondas 0,364.
CE5.4: cocina de gas natural 2,023 MMBtu. HC3.1: combustible de la cocina (range) más usada.
Precios: luz 18,19 ¢/kWh (EIA EPM 5.3, ene–ago 2026); gas 15,34 $/Mcf (EIA, 2025); 1 Mcf = 1,036 MMBtu; 1 MMBtu = 293,07 kWh.
"""
e = 0.991 * 293.07
print(f"eléctrica: {e:.1f} kWh → {e*0.1819:.2f} $/año")
print(f"gas: 2,023 MMBtu → {2.023/1.036*15.34:.2f} $/año · {2.023/0.991:.1f}× la energía de la eléctrica")
print(f"microondas: {0.364*293.07:.1f} kWh → {0.364*293.07*0.1819:.2f} $/año")
print(f"hogares con cocina (range) 110,32 M: eléctrica 65,56 ({65.56/110.32:.0%}) · gas 34,68 ({34.68/110.32:.0%}) · propano 4,82 · mixta 5,26")
