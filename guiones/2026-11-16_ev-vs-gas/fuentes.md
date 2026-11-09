# Fuentes · EV vs Gas: What Charging at Home Really Costs, by State

1. **Millas al año:** AFDC, «Average Annual Vehicle Miles Traveled by Major Vehicle Category»: turismo (Car) **11.026**; furgoneta o camioneta ligera 11.360. Cita FHWA Highway Statistics 2024, tabla VM-1. https://afdc.energy.gov/data/10309
2. **Gasolina:** EPA Automotive Trends: «The average model year 2024 new vehicle increased fuel economy by 0.1 mpg to a record high 27.2 mpg» (valor real). https://www.epa.gov/automotive-trends/highlights-automotive-trends-report
3. **Coches eléctricos, consumo EPA combinado de 2025** (fueleconomy.gov, buscador de modelos de 2025): Tesla Model Y Long Range RWD 27 kWh/100 mi · Model Y Long Range AWD 29 · Hyundai Ioniq 5 Standard Range 29 · Ioniq 5 RWD 30 · Chevrolet Equinox EV FWD 31 · Ford Mustang Mach-E RWD Extended 31. Se usa **30**. https://www.fueleconomy.gov
   - Definición en fueleconomy.gov: «This value tells you how many kilowatt-hours the vehicle would use to travel 100 miles.» No dice de forma explícita si incluye las pérdidas de carga; por eso hay un caso prudente.
4. **Pérdidas de carga:** fueleconomy.gov (ORNL): «Battery charging efficiency can vary, but it is often 84% to 93%, based on published studies.» Caso prudente: coste del eléctrico ÷ 0,84. https://www.fueleconomy.gov/feg/evtech.shtml
5. **Gasolina normal, EIA (media anual, impuestos incluidos, $/galón):** EE. UU. 2020 2,168 · 2021 3,008 · 2022 3,951 · 2023 3,519 · 2024 3,304 · 2025 **3,097**. Estados en 2025: CA 4,410 · CO 2,868 · FL 2,957 · MA 2,970 · MN 2,963 · NY 3,056 · OH 2,960 · TX 2,660 · WA 4,132.
   https://www.eia.gov/dnav/pet/pet_pri_gnd_dcus_nus_a.htm · https://www.eia.gov/dnav/pet/pet_pri_gnd_a_epmr_pte_dpgal_a.htm
6. **Luz residencial, EIA:** EE. UU. ene–ago 2026 **18,19 ¢/kWh**; anual 2020 13,15 · 2021 13,66 · 2022 15,04 · 2023 16,00 · 2024 16,48 · 2025 17,23 (EPM 5.3). Estados, ene–ago 2026 (EPM 5.6.B): WA 14,42 · CA 32,58 · TX 16,03 · FL 15,32 · CO 16,80 · MN 16,44 · OH 18,81 · NY 29,26 · MA 30,19.
7. **Hogar medio:** 10.791 kWh/año (EIA FAQ 97, datos de 2022). **RECS 2020, CE5.3a:** carga de eléctricos 2.363 kWh/año por hogar que carga uno.

## Cifras en pantalla, tal como salen (todas en `datos/resultados.txt`)
11.026 · 27,2 · 27 · 29 · 30 · 31 · 3,10 (3,097) · 18,2 (18,19) · 3,7 gal · 11,39 · 5,46 · 405 · 3.308 · 1.255 · 602 · 654 · 84 % · 84–93 % · 716 · 539 · WA 1.675 / 477 / 1.198 / 1.107 · FL 1.199 / 507 / 692 / 595 · MN 1.201 / 544 / 657 / 554 · CO 1.163 / 556 / 607 / 501 · TX 1.078 / 530 / 548 / 447 · OH 1.200 / 622 / 578 / 459 · CA 1.788 / 1.078 / 710 / 505 · NY 1.239 / 968 / 271 / 87 · MA 1.204 / 999 / 205 / 15 · precios de estado 14,4 · 4,13 · 15,3 · 2,96 · 16,4 · 16,8 · 2,87 · 16,0 · 2,66 · 18,8 · 32,6 · 4,41 · 29,3 · 3,06 · 30,2 · 2,97 · 38,0 · 31,9 · 31 % · 10.791 · 276 · 50 · 2.363 · 430 · 2,17 · 3,95 · 13,2 · 7,97 · 3,94 · 14,53 · 4,51 · 542 · 622.

## Supuestos
- Gasolina de 2025 frente a luz de 2026 (lo último publicado de cada uno). Se dice en la descripción.
- Solo carga en casa y coste de la energía: sin carga pública, sin precio del coche, seguro ni mantenimiento. Se dice en el vídeo.
- «Real households vary in how much they drive and where they plug in» explica en general la diferencia con la RECS, sin dar una causa concreta.
