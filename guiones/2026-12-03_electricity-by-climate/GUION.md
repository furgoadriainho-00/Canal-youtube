# Guion · What Uses the Most Electricity in Your Climate

| | |
|---|---|
| **Formato** | Vídeo largo · 16:9 |
| **Duración objetivo** | 9–10 min (narración de unas 1.550 palabras, a 164 por minuto) |
| **Publicar** | Jueves 3 de diciembre de 2026 |
| **Estructura** | Lista (los largos anteriores: historia, comparación y mito vs realidad) |
| **Fuentes y cálculos** | `fuentes.md` y `datos/calculo.py` → `datos/resultados.txt` |

Indicaciones en español; narración en inglés de EE. UU., literal. **La voz dice exactamente las cifras de la pantalla.** Escenas solo del motor (sin stock). Recurso fijo: **mapa de EE. UU.** que resalta la zona de cada clima con su icono (copo, gota, sol, cactus, ola) y un **ranking de tres puestos** por clima. Clips 3D: `aire.mp4`, `calefaccion.mp4`, `termo.mp4`, `deshumidificador.mp4`, `nevera.mp4` y `medidor.mp4`.

---

## 1 · Gancho (0:00–0:20)
**Narración**
> In Miami, the biggest electricity user in a typical home is the air conditioner. In Seattle, it's not heating and it's not cooling. It's the water heater.
> Where you live changes what's eating your electric bill. Let's go climate by climate.

**Imagen:** mapa con Miami (naranja, sol) y Seattle (azul, ola). Puesto 1 en Miami: clip `aire.mp4`; puesto 1 en Seattle: clip `termo.mp4`.
**Texto en pantalla:** `#1 in Miami ≠ #1 in Seattle`

## 2 · Promesa y método (0:20–1:15)
**Narración**
> I'll use the government's household energy survey, which breaks down electricity use by appliance for each of five climate regions.
> For each one, I'll show you the top three electricity users, and what they cost a year.
> Two things to keep in mind. First, each number is the average for homes that actually have that use. So the heating number is for homes that heat with electricity, and the water heater number is for homes with an electric water heater.
> Second, I'll price everything at the same national average, eighteen point one nine cents per kilowatt-hour, so you're comparing how much electricity each climate uses, not local prices. To get your own number, multiply the kilowatt-hours by the price on your bill.
> The climate regions come from the Department of Energy's Building America program, which sorts every county by temperature, rainfall and how much heating it needs.

**Imagen:** tarjetas de fuente: EIA RECS 2020 (tablas CE5.3a y CE5.3b) y U.S. DOE / PNNL «Climate Regions by County». Iconos: casa con rayo y el rótulo «homes that have it». Contador de luz `medidor.mp4` con **18.19¢/kWh**. Mapa con cinco zonas que se colorean una a una. Fórmula: **kWh × 18.19¢ = $ a year**.
**Texto en pantalla:** `5 climates · top 3 each`

## 3 · La media nacional (1:15–2:10)
**Narración**
> First, the national picture.
> Across all US homes that have them, three uses are almost tied at the top.
> Air conditioning, including its fan: about two thousand seven hundred seventy-five kilowatt-hours a year, or about five hundred five dollars.
> Electric heating, with its fan: about two thousand seven hundred seventeen kilowatt-hours, about four hundred ninety-four dollars.
> And an electric water heater: about two thousand seven hundred six kilowatt-hours, about four hundred ninety-two dollars.
> Nothing else comes close. Number four is the dehumidifier, at about nine hundred ninety-nine kilowatt-hours, about one hundred eighty-two dollars.
> Now watch how much that order changes once you split the country by climate.

**Imagen:** ranking nacional con tres puestos casi empatados: **AC $505**, **Heating $494**, **Water heating $492** (clips `aire`, `calefaccion`, `termo`). Cuarto puesto aparte, más pequeño: **Dehumidifier $182** (`deshumidificador.mp4`).
**Texto en pantalla:** `US: $505 · $494 · $492`

## 4 · Clima 1: cálido y húmedo (2:10–3:20)
**Narración**
> Climate one: hot-humid. Think Miami and Houston. The Building America definition is more than twenty inches of rain a year, with long, very muggy summers.
> Number one, by a mile: air conditioning. About four thousand eight hundred ninety-three kilowatt-hours a year, about eight hundred ninety dollars. That's about seventy-six percent more than the national average for air conditioning.
> Number two: the electric water heater, about two thousand five hundred fifty-nine kilowatt-hours, about four hundred sixty-five dollars.
> Number three: electric heating, about one thousand nine hundred eighty-one kilowatt-hours, about three hundred sixty dollars. Yes, even here.
> Put another way, air conditioning alone costs more here than the water heater and the heating combined.
> And a bonus: dehumidifiers work harder in this climate than anywhere else, about one thousand three hundred sixty-eight kilowatt-hours, about two hundred forty-nine dollars, in homes that have one.
> Ceiling fans, too: about three hundred sixty-six kilowatt-hours a year here, about sixty-seven dollars, compared with about one hundred eleven kilowatt-hours in the marine climate.
> So in this climate, the first place to look is the cooling system: its efficiency, its thermostat settings, and how much humid air leaks into the house.

**Imagen**
- Mapa: zona cálida-húmeda resaltada (gota + sol), con **Miami** y **Houston**.
- Ranking: **1 · AC $890** (barra larga, `aire.mp4`) · **2 · Water heating $465** · **3 · Heating $360**.
- Comparación de dos barras: AC aquí **4,893 kWh** frente a media **2,775 kWh**; anillo **+76%**.
- Barra **$890** (AC) frente a la suma **$465 + $360 = $825**.
- Cifra extra: **Dehumidifier $249** (`deshumidificador.mp4`).
- Ventiladores de techo: **366 kWh ($67)** frente a **111 kWh** en el clima marino.

**Texto en pantalla:** `Hot-humid #1: AC, $890 a year`

## 5 · Clima 2: cálido y seco (3:20–4:20)
**Narración**
> Climate two: hot-dry and mixed-dry. Think Phoenix, Las Vegas and Los Angeles. Less than twenty inches of rain a year.
> Number one is still air conditioning: about three thousand one hundred eighty-nine kilowatt-hours, about five hundred eighty dollars. A lot, but well below the hot-humid climate. Dry heat takes less work to cool, because there's less moisture to pull out of the air.
> Number two: the water heater, about two thousand sixty-five kilowatt-hours, about three hundred seventy-six dollars. That's the lowest water heating number of any climate.
> And number three: electric heating, about one thousand fifty kilowatt-hours, about one hundred ninety-one dollars. Also the lowest of any climate.
> And notice what's not in the top three here: the dehumidifier. In homes that have one, it uses about seven hundred seventy-three kilowatt-hours a year, the lowest of the five climates, and the refrigerators pass it, at about eight hundred sixty-eight.

**Imagen**
- Mapa: zona seca resaltada (cactus + sol), con **Phoenix**, **Las Vegas** y **Los Angeles**.
- Ranking: **1 · AC $580** · **2 · Water heating $376** · **3 · Heating $191**.
- Comparación de barras de aire acondicionado: hot-humid **$890** frente a hot-dry **$580**; icono de gota de humedad tachada.
- Sello «LOWEST» junto a **$376** y **$191**.

**Texto en pantalla:** `Hot-dry #1: AC, $580 a year`

## 6 · Clima 3: mixto y húmedo (4:20–5:20)
**Narración**
> Climate three: mixed-humid. Think Atlanta and St. Louis. Real winters and real summers.
> This is the most balanced climate on the list, and the top three are close together.
> Number one: electric heating, about three thousand one hundred fifty-eight kilowatt-hours, about five hundred seventy-four dollars.
> Number two: the water heater, about two thousand nine hundred twenty-seven kilowatt-hours, about five hundred thirty-two dollars.
> Number three: air conditioning, about two thousand seven hundred forty-five kilowatt-hours, about four hundred ninety-nine dollars.
> Add those three up, and a home that does all three with electricity spends about one thousand six hundred five dollars a year on just heating, cooling and hot water.
> This climate also has the highest electric car charging number in the survey: about three thousand six hundred forty-four kilowatt-hours a year, about six hundred sixty-three dollars, in homes that charge at home.
> That balance is why the thermostat matters so much here. It controls two of the top three. The Department of Energy says setting it back for at least eight hours a day can save up to ten percent a year on heating and cooling.

**Imagen**
- Mapa: zona mixta-húmeda (copo + sol), con **Atlanta** y **St. Louis**.
- Ranking con tres barras casi iguales: **1 · Heating $574** · **2 · Water heating $532** · **3 · AC $499**.
- Fórmula **$574 + $532 + $499 = $1,605/yr**.
- Icono de coche eléctrico: **3,644 kWh · $663/yr** (sello «HIGHEST»).
- Termostato que baja de noche: **8 h/day → up to 10%** (tarjeta del DOE).

**Texto en pantalla:** `Mixed-humid: $574 · $532 · $499`

## 7 · Clima 4: frío y muy frío (5:20–6:20)
**Narración**
> Climate four: cold and very cold. Think Minneapolis and Chicago.
> No surprise at number one: electric heating, about three thousand two hundred seventy-one kilowatt-hours, about five hundred ninety-five dollars. The highest heating number of any climate.
> Number two: the water heater, about two thousand six hundred sixty-eight kilowatt-hours, about four hundred eighty-five dollars.
> Number three: air conditioning, about one thousand five hundred eighty kilowatt-hours, about two hundred eighty-seven dollars. Even in cold country, summers still add up, although that's only about fifty-seven percent of the national average for air conditioning.
> One caveat: this heating number is only for homes that use electricity for heat. Homes that heat with gas or other fuels aren't in it.
> If that's you, and you heat with baseboards or space heaters, a heat pump is the big lever. Using the federal minimum rating, it gives the same heat for about forty-five percent of the electricity. I ran the full Minnesota numbers in my heat pump video.

**Imagen**
- Mapa: zona fría (copo de nieve), con **Minneapolis** y **Chicago**.
- Ranking: **1 · Heating $595** (`calefaccion.mp4`) · **2 · Water heating $485** · **3 · AC $287** (anillo **57%** de la media nacional).
- Icono de llama de gas tachada con el rótulo «electric heat only».
- Comparación de dos barras de electricidad para el mismo calor: baseboard **1.0** frente a heat pump **0.45** (CHEAPER); anillo **45%**.

**Texto en pantalla:** `Cold #1: heating, $595 a year`

## 8 · Clima 5: marino (6:20–7:30)
**Narración**
> Climate five: marine. Think Seattle, Portland and San Francisco. Mild winters, cool, dry summers.
> And here's the surprise from the start of the video. Number one is the water heater: about three thousand seventy-three kilowatt-hours, about five hundred fifty-nine dollars. That's the highest water heating number of any climate.
> Number two: electric heating, about two thousand eight hundred sixty-two kilowatt-hours, about five hundred twenty-one dollars.
> Number three: air conditioning, way down at about one thousand ninety-seven kilowatt-hours, about two hundred dollars. The lowest of any climate.
> The survey doesn't say why water heating is higher here. But it does mean that if you live in a marine climate with an electric water heater, that's the first appliance to look at.
> In my water heater video, an ENERGY STAR heat pump water heater used about seventy-two percent less electricity than a regular electric tank for the same hot water. On a five-hundred-fifty-nine-dollar water heating bill, that would be about four hundred three dollars a year.

**Imagen**
- Mapa: zona marina (ola), con **Seattle**, **Portland** y **San Francisco**.
- Ranking: **1 · Water heating $559** (`termo.mp4`, sello «HIGHEST») · **2 · Heating $521** · **3 · AC $200** (sello «LOWEST»).
- Anillo **−72%** (heat pump water heater) sobre la barra de **$559** → **−$403/yr**.

**Texto en pantalla:** `Marine #1: water heater, $559`

## 9 · Los que no salen en el top 3 (7:30–8:20)
**Narración**
> Some appliances don't make any climate's top three, simply because most homes don't have them. But if you do, they're big.
> A pool pump, in homes that have one, uses about two thousand three hundred eighty-four kilowatt-hours a year nationally, about four hundred thirty-four dollars. In the hot-humid climate, about five hundred twenty-one.
> A hot tub, heater plus pump, about one thousand nine hundred sixty-three kilowatt-hours, about three hundred fifty-seven dollars.
> And charging an electric car at home, about two thousand three hundred sixty-three kilowatt-hours, about four hundred thirty dollars.
> A separate freezer is another quiet one. Nationally, about five hundred seventy kilowatt-hours a year, about one hundred four dollars. In the hot-humid climate, about six hundred seventy-two, about one hundred twenty-two dollars, the most of any climate.
> Any one of those can sit right next to your air conditioner on the bill.

**Imagen:** tres iconos con sello «IF YOU HAVE ONE»: piscina **$434** (y **$521** en hot-humid), jacuzzi **$357**, coche eléctrico **$430**. Después, una barra junto a la del aire acondicionado nacional (**$505**) para comparar.
**Texto en pantalla:** `Pool pump: $434 a year`

Después: congelador aparte **$104** (US) frente a **$122** (hot-humid).

## 10 · Lo que es igual en todas partes (8:20–8:55)
**Narración**
> And some things barely change with the climate. All the refrigerators in a home use between about seven hundred seventy-three and nine hundred twelve kilowatt-hours a year in every climate. Lighting, between about five hundred seventy-one and seven hundred thirteen.
> TVs and everything plugged into them, from streaming boxes to game consoles, between about five hundred fifty and six hundred eighty.
> Your fridge doesn't care much about the weather outside. Your heating, cooling and hot water do.
> Air conditioning, by comparison, ranges from about one thousand ninety-seven kilowatt-hours in the marine climate to about four thousand eight hundred ninety-three in the hot-humid one. That's almost four and a half times as much.

**Imagen:** reglas horizontales estrechas: frigoríficos **773–912 kWh** (`nevera.mp4`), luz **571–713 kWh** y TV **550–680 kWh**, frente a la regla ancha del aire acondicionado **1,097–4,893 kWh** (**4.5×**).
**Texto en pantalla:** `Fridges: 773–912 kWh everywhere`

## 11 · Resumen y cierre (8:55–9:35)
**Narración**
> So, climate by climate. Hot-humid: air conditioning, about eight hundred ninety dollars. Hot-dry: air conditioning, about five hundred eighty. Mixed-humid: heating, about five hundred seventy-four, with hot water and cooling right behind. Cold: heating, about five hundred ninety-five. Marine: the water heater, about five hundred fifty-nine.
> Find your climate, find your number one, and start there.
> If your number one is the water heater, my comparison of tank, tankless and heat pump water heaters is right here on the channel.

**Imagen:** mapa completo con los cinco puestos 1 a la vez: **$890**, **$580**, **$574**, **$595** y **$559**, cada uno con su icono. Pantalla final hacia «Tank vs Tankless vs Heat Pump Water Heater».

---

## Miniaturas
1. **Mapa con cifras:** mapa de EE. UU. con los cinco puestos 1. Texto: **«YOUR #1?»**
2. **Versus:** Miami (aire acondicionado) frente a Seattle (termo). Texto: **«MIAMI vs SEATTLE»**
3. **Icono grande con cifra:** aire acondicionado con sol. Texto: **«$890/YR»**

## Metadatos para YouTube
**Título** (menos de 60 caracteres): `What Uses the Most Electricity in Your Climate`

**Descripción**
```
The top three electricity users in five US climates, from the EIA Residential Energy Consumption Survey 2020 (average per home that has each use, priced at the US average of 18.19¢/kWh, EIA Jan–Aug 2026):
Hot-humid (Miami, Houston): AC $890 · water heating $465 · heating $360
Hot-dry/mixed-dry (Phoenix, Las Vegas, Los Angeles): AC $580 · water heating $376 · heating $191
Mixed-humid (Atlanta, St. Louis): heating $574 · water heating $532 · AC $499
Cold/very cold (Minneapolis, Chicago): heating $595 · water heating $485 · AC $287
Marine (Seattle, Portland, San Francisco): water heating $559 · heating $521 · AC $200
Heating and AC include their fans. Climate regions: DOE Building America, by county (PNNL).

Sources:
EIA RECS 2020, tables CE5.3a and CE5.3b: https://www.eia.gov/consumption/residential/data/2020/
PNNL / DOE, Guide to Determining Climate Regions by County (2015): https://www.energy.gov/sites/prod/files/2015/10/f27/ba_climate_region_guide_7.3.pdf
EIA electricity prices: https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_03
```
**Etiquetas:** `what uses the most electricity, electric bill by climate, home energy use, air conditioning cost, water heater cost, electric heating cost, home by the numbers`
**Ajustes:** idioma inglés · lista «Home energy costs, explained» · no es para niños · contenido sintético: **Sí** (voz IA).
