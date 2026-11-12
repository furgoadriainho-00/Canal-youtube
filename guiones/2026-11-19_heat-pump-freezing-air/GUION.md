# Guion · How a Heat Pump Pulls Heat Out of Freezing Air

| | |
|---|---|
| **Formato** | Vídeo largo · 16:9 |
| **Duración objetivo** | 9–10 min (narración de unas 1.500 palabras, a 164 por minuto) |
| **Publicar** | Jueves 19 de noviembre de 2026 |
| **Estructura** | Paso a paso (los tres largos anteriores fueron comparaciones) |
| **Fuentes y cálculos** | `fuentes.md` y `datos/calculo.py` → `datos/resultados.txt` |

Indicaciones en español; narración en inglés de EE. UU., literal. **La voz dice exactamente las cifras de la pantalla.** Escenas solo del motor (sin stock). Clips 3D: `aire.mp4` (la bomba de calor), `calefaccion.mp4` (radiador eléctrico), `nevera.mp4` (para la comparación con la nevera) y `medidor.mp4`. Para el ciclo del refrigerante, un diagrama con iconos y flechas: unidad exterior → compresor → unidad interior → válvula de expansión, con la casa en corte de fondo.

---

## 1 · Gancho (0:00–0:20)
**Narración**
> It's zero degrees outside. Your heat pump is pulling heat out of that freezing air and pushing it into your house.
> That sounds impossible. It isn't. And understanding how it works explains why it can cut an electric heating bill by more than half.

**Imagen:** termómetro exterior a **0°F** con nieve (iconos). Clip `aire.mp4` y flechas naranjas que van de fuera hacia dentro de la casa en corte. Rótulo con `?` que late.
**Texto en pantalla:** `0°F outside → heat inside?`

## 2 · Promesa (0:20–0:45)
**Narración**
> In this video, I'll walk through it step by step: why freezing air still holds heat, how a heat pump moves it, and what that means in dollars compared with electric baseboard heaters, using official efficiency ratings and real energy prices.

**Imagen:** cuatro iconos numerados que se encienden uno a uno: 1 copo de nieve con calor, 2 compresor, 3 casa caliente y 4 monedas. Tarjetas de fuente: DOE (10 CFR 430), ENERGY STAR y EIA.
**Texto en pantalla:** `Step by step`

## 3 · Paso 1: el aire helado todavía tiene calor (0:45–2:00)
**Narración**
> Step one: cold air still has heat in it.
> Cold just means less heat, not none. To find true zero heat, you'd have to go all the way down to absolute zero, which is minus four hundred fifty-nine point six seven degrees Fahrenheit.
> Measured from that point, air at zero degrees still has about eighty-seven percent of the heat energy of air at seventy degrees.
> At thirty-two degrees, it's about ninety-three percent. At forty-seven degrees, a mild winter day, about ninety-six percent.
> Even at five degrees, it's still about eighty-eight percent.
> Think about that for a second. The difference between a mild day and a brutal one feels huge to you, but for the air itself, it's a small drop in total heat.
> So the outdoor air in winter isn't empty. It's full of heat. The problem is that it's at a lower temperature than your living room, and heat naturally flows from warm to cold, not the other way.
> A heat pump's whole job is to make that heat flow uphill.

**Imagen**
- Regla vertical de temperatura con la marca **−459.67°F** (absolute zero) abajo del todo, y **0°F**, **32°F** y **70°F** arriba, muy juntas.
- Anillos: **96%** (47°F), **93%** (32°F), **88%** (5°F) y **87%** (0°F) del calor del aire a 70°F, uno tras otro.
- Flecha de calor de la casa hacia fuera (lo natural), y después una flecha que «sube» de fuera hacia dentro, con el rótulo «uphill».

**Texto en pantalla:** `0°F air: 87% of the heat energy of 70°F air`

## 4 · Paso 2: el refrigerante absorbe el calor de fuera (2:00–3:00)
**Narración**
> Step two: grab the heat outside.
> A heat pump circulates a special fluid called a refrigerant through two coils, one outdoors and one indoors.
> In the outdoor coil, the refrigerant is kept at very low pressure, which makes it even colder than the winter air around it.
> Because the refrigerant is colder than the air, heat flows from the air into the refrigerant. That's the normal direction: warm to cold.
> As it soaks up that heat, the refrigerant boils and turns into a gas. That's the trick. Boiling absorbs a lot of energy, so the gas now carries the heat it took from outside.
> It's the same thing that happens when water boils on your stove. The pot keeps taking in heat while the water turns to steam. Except the refrigerant boils at a temperature far below freezing, so the winter air is enough to do it.
> A fan on the outdoor unit keeps pushing fresh outdoor air across the coil, so there's always more heat to grab.

**Imagen:** diagrama del ciclo con la unidad exterior encendida (clip `aire.mp4` en pequeño). Flechas naranjas del aire hacia un tubo azul; gotas que se convierten en burbujas («liquid → gas»). Rótulo «low pressure = very cold».
**Texto en pantalla:** `Refrigerant colder than the air → heat flows in`

## 5 · Paso 3: el compresor lo calienta (3:00–3:45)
**Narración**
> Step three: squeeze it.
> The gas goes into a compressor, the part that actually uses electricity.
> Squeezing a gas into a smaller space raises its temperature. It's the same reason a bike pump gets warm when you use it.
> After the compressor, the refrigerant is now hotter than the air inside your home.
> And here's the key detail: the electricity the compressor uses isn't wasted. It also ends up as heat in the refrigerant. So everything that went in, the heat from outside plus the compressor's own energy, is now ready to be delivered indoors.

**Imagen:** icono de compresor con un rayo (la electricidad); el tubo pasa de azul a naranja. Icono de bomba de bicicleta con una pequeña ola de calor. Termómetro: el refrigerante supera los **70°F** de dentro.
**Texto en pantalla:** `Compressor: squeeze → hotter than indoors`

## 6 · Paso 4: suelta el calor dentro (3:45–4:30)
**Narración**
> Step four: release the heat indoors.
> The hot refrigerant flows through the indoor coil. Now it's warmer than your room, so heat flows out of it and into your house, again from warm to cold, the natural direction.
> A fan pushes that warm air through your home. And as the refrigerant gives up its heat, it turns back into a liquid.

**Imagen:** casa en corte con la unidad interior; flechas naranjas que salen hacia las habitaciones; burbujas que vuelven a ser gotas («gas → liquid»).
**Texto en pantalla:** `Hot refrigerant → heat into your home`

## 7 · Paso 5: reinicia el ciclo (4:30–5:15)
**Narración**
> Step five: reset the loop.
> The liquid passes through an expansion valve, a small opening that drops its pressure suddenly. That makes it very cold again, ready to go back outside and soak up more heat.
> And the loop runs over and over.
> If this sounds familiar, it should. Your refrigerator does exactly the same thing. It pumps heat out of the box and releases it into your kitchen. That's why the coils on the back of an older fridge feel warm. A heat pump is basically a refrigerator that cools the outdoors and heats your house.

**Imagen:** el ciclo completo animado en bucle: exterior (azul) → compresor → interior (naranja) → válvula → exterior. Corte al clip `nevera.mp4` con flechas de calor que salen por detrás, y comparación de dos iconos: «Fridge: box → kitchen» y «Heat pump: outdoors → home».
**Texto en pantalla:** `A heat pump = a fridge for your whole house`

## 8 · Paso 6: por qué da más calor que la luz que gasta (5:15–6:30)
**Narración**
> Step six: why this beats an electric heater.
> An electric baseboard heater turns electricity directly into heat. One unit of electricity gives you one unit of heat. That's it.
> A heat pump uses its electricity to move heat, not to make it. So it can deliver more heat than the electricity it uses.
> Under federal rules, a new heat pump has to reach a heating rating that works out to about two point two units of heat for every unit of electricity, averaged over a season.
> In other words, it uses about forty-five percent of the electricity of a baseboard heater for the same warmth.
> In very cold weather, it works harder, because the gap between outdoor and indoor air is bigger. ENERGY STAR's cold-climate heat pumps have to deliver at least one point seven five units of heat per unit of electricity at five degrees Fahrenheit.
> Even then, that's about fifty-seven percent of the electricity of a baseboard heater.

**Imagen:** comparación de dos barras de electricidad para el mismo calor: radiador `calefaccion.mp4` **1.0** frente a bomba de calor **0.45** (sello CHEAPER). Después, regla de eficiencia con las marcas **1.0** (baseboard), **1.75** (5°F, ENERGY STAR) y **2.2** (federal minimum). Anillos **45%** y **57%**. Fuentes: 10 CFR 430.32(c)(5) y ENERGY STAR.
**Texto en pantalla:** `Same heat: 45% of the electricity (57% at 5°F)`

## 8b · Cómo leer la etiqueta (6:30–7:15)
**Narración**
> Where does that two point two come from? From the rating on every heat pump's label, called HSPF2.
> It measures how many B T U of heat the heat pump delivers for each watt-hour of electricity, over a whole heating season.
> One watt-hour of electricity turned straight into heat gives three point four one two B T U. That's what a baseboard heater does.
> The federal minimum for a new heat pump is an HSPF2 of seven point five. Divide seven point five by three point four one two, and you get about two point two.
> So when you shop, the higher that number, the less electricity it needs for the same heat. And if you live somewhere with hard winters, look for a model that meets ENERGY STAR's cold-climate criteria.

**Imagen:** etiqueta de eficiencia (iconos) con **HSPF2 7.5** resaltado. Fórmula animada: **7.5 ÷ 3.412 ≈ 2.2**. Después, regla con 7.5 (mínimo) y la flecha «higher = less electricity». Tarjeta: 10 CFR 430.32(c)(5).
**Texto en pantalla:** `HSPF2 7.5 ÷ 3.412 ≈ 2.2`

## 9 · Paso 7: lo que vale en dólares (7:15–8:45)
**Narración**
> Now let's put dollars on it.
> I started with how much energy typical homes in three different climates use for heating, from the government's household energy survey, and worked out how much heat actually reaches the rooms. Then I priced that heat with each state's average electricity price.
> In Florida, heating a typical home with electric baseboard heaters costs about seven hundred forty-seven dollars a year. With a heat pump, about three hundred forty. That's about four hundred seven dollars saved.
> In Georgia, about one thousand five hundred ninety-seven dollars with baseboard heat, and about seven hundred twenty-seven with a heat pump. About eight hundred seventy-one saved.
> And in Minnesota, where winters are long, baseboard heat costs about two thousand three hundred forty-two dollars a year. A heat pump at the federal minimum, about one thousand sixty-five. That's about one thousand two hundred seventy-six dollars saved.
> Even if we assume the heat pump only manages the cold-weather rating all winter long, it would cost about one thousand three hundred thirty-eight dollars in Minnesota. Still about a thousand dollars less than baseboard heat.
> The colder the climate, the more heat you need, and the more a heat pump saves over electric resistance.
> Notice that the percentage is the same everywhere. The heat pump always uses about forty-five percent of the electricity. What changes is the size of the bill it's cutting.

**Imagen:** gráfico recurrente de dos barras por estado (radiador en naranja y bomba de calor en azul, sello CHEAPER), con el ahorro debajo:
- Florida: **$747** frente a **$340** → **−$407**
- Georgia: **$1,597** frente a **$727** → **−$871**
- Minnesota: **$2,342** frente a **$1,065** → **−$1,276**; barra extra **$1,338** («cold rating all winter»)
Mapa con los 3 estados.

**Texto en pantalla:** `Minnesota: $2,342 → $1,065 (−$1,276/yr)`

| Estado | Resistencia | Bomba de calor (2,2) | Bomba de calor (1,75) | Ahorro |
|---|---|---|---|---|
| Florida | $747 | $340 | $427 | $407 |
| Georgia | $1,597 | $727 | $913 | $871 |
| Minnesota | $2,342 | $1,065 | $1,338 | $1,276 |

## 10 · Quién usa qué (8:00–8:45)
**Narración**
> So how many American homes already heat this way?
> According to the government's household energy survey, about seventeen point two million homes use a heat pump as their main heating, counting ductless mini-splits.
> And about ten point seven million homes still rely mainly on electric resistance heat, from built-in electric units to portable heaters.
> That's about eight point six percent of all homes, the group with the most to gain from switching.

**Imagen:** tarjeta «EIA · RECS 2020». Barras horizontales (millones de hogares): «Heat pump + mini-split» **17.2M** (azul) y «Electric resistance» **10.7M** (naranja). Anillo **8.6%** de todos los hogares.
**Texto en pantalla:** `10.7M homes still heat with electric resistance`

## 11 · ¿Y frente al gas? (8:45–9:20)
**Narración**
> One honest caveat. Beating electric baseboard heat is easy. Beating a gas furnace is a different question.
> A gas furnace doesn't use electricity for heat at all, so the comparison depends on two prices instead of one.
> In Minnesota, where gas is cheap, a new gas furnace heats that same typical home for about five hundred forty-two dollars a year, less than the heat pump.
> In Florida, the heat pump wins against gas too. It all comes down to the price of gas versus electricity where you live, and I worked that out state by state in my heat pump versus gas furnace video.

**Imagen:** tres barras para Minnesota: baseboard **$2,342**, heat pump **$1,065** y gas furnace **$542** (sello CHEAPER en el gas). Después, Florida: heat pump **$340** frente a gas **$431**.
**Texto en pantalla:** `vs gas: depends on your prices`

## 12 · Resumen y cierre (9:20–10:00)
**Narración**
> So that's how a heat pump pulls heat out of freezing air.
> Freezing air still holds plenty of heat. The refrigerant soaks it up outside, the compressor makes it hotter than your home, the indoor coil releases it, and the loop starts again.
> Because it moves heat instead of making it, it uses about forty-five percent of the electricity of baseboard heat at the federal minimum, and about fifty-seven percent even at five degrees.
> In a cold state like Minnesota, that's about one thousand two hundred seventy-six dollars a year compared with electric baseboard heaters.
> So if you heat with baseboards or space heaters today, the cold outside isn't a reason to rule out a heat pump. It's the reason the savings get bigger.
> The full heat pump versus gas furnace comparison is right here on the channel.

**Imagen:** el ciclo animado una última vez, con las cifras **45%**, **57%** y **−$1,276/yr**. Pantalla final hacia «Heat Pump vs Gas Furnace: Which Is Cheaper to Run?».

---

## Miniaturas
1. **Icono grande con cifra:** bomba de calor con nieve y **«0°F»**. Texto: **«HEAT FROM ICE?»**
2. **Versus:** radiador eléctrico frente a bomba de calor. Texto: **«$2,342 vs $1,065»**
3. **Mapa con cifras:** Minnesota resaltado. Texto: **«−$1,276/YR»**

## Metadatos para YouTube
**Título** (menos de 60 caracteres): `How a Heat Pump Pulls Heat Out of Freezing Air`

**Descripción**
```
How can a heat pump heat your home when it's 0°F outside? Step by step: freezing air still holds heat (0°F air has about 87% of the heat energy of 70°F air, measured from absolute zero), a refrigerant soaks it up outside, a compressor makes it hotter than your home, and an indoor coil releases it.

Because it moves heat instead of making it, a heat pump at the federal minimum (HSPF2 7.5, about 2.2 units of heat per unit of electricity) uses about 45% of the electricity of baseboard heat; ENERGY STAR cold-climate models must reach 1.75 at 5°F.

Yearly heating cost, baseboard vs heat pump: Florida $747 vs $340; Georgia $1,597 vs $727; Minnesota $2,342 vs $1,065.

How the numbers work: heating needs from the EIA Residential Energy Consumption Survey 2020 (by climate); state electricity prices from the EIA (Jan–Aug 2026). Running costs only.

Sources:
Federal heat pump standard, 10 CFR 430.32(c)(5): https://www.govinfo.gov/content/pkg/CFR-2025-title10-vol3/xml/CFR-2025-title10-vol3-sec430-32.xml
ENERGY STAR heat pump criteria: https://www.energystar.gov/products/air_source_heat_pumps/key-product-criteria
EIA Residential Energy Consumption Survey 2020 (CE5.4, HC6.1): https://www.eia.gov/consumption/residential/data/2020/
EIA electricity prices by state: https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_b
```
**Etiquetas:** `how does a heat pump work, heat pump cold weather, heat pump vs baseboard heat, heat pump explained, heat pump efficiency, cold climate heat pump, electric heating cost, home by the numbers`
**Ajustes:** idioma inglés · lista «Home energy costs, explained» · no es para niños · contenido sintético: **Sí** (voz IA).
