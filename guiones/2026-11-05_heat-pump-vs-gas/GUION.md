# Guion · Heat Pump vs Gas Furnace

| | |
|---|---|
| **Canal** | Home By The Numbers (@HomeByTheNumbers) |
| **Formato** | Vídeo largo · 16:9 · 1920×1080 · 30 fps |
| **Duración objetivo** | 9–10 min (unas 1.350 palabras de narración) |
| **Publicar** | Jueves 5 de noviembre de 2026 |
| **Estructura** | Comparación (el vídeo anterior era una lista) |
| **Idioma** | Narración en inglés (EE. UU.). Las indicaciones para el editor van en español. |
| **Fuentes y cálculos** | `fuentes.md` y `datos/calculo.py` en esta carpeta. **No cambies ninguna cifra sin avisar.** |

## Indicaciones generales para el editor
- **Estilo del canal:** fondo azul noche `#0F1B2D`, acento naranja `#FF7A1A` (calor, gas, coste) y azul `#2EC4F1` (frío, electricidad, ahorro). Tipografía Montserrat ExtraBold para cifras y títulos, Inter para el resto.
- **Ritmo:** cambio de imagen cada 2–4 s. **Nada de pantallas de solo texto** salvo frases cortas de transición (menos de 2 s).
- **Cifras:** cada cifra en dólares aparece contando desde 0, con monedas o barras animadas. Las fuentes van en pantalla, abajo y en pequeño, la primera vez que sale cada dato.
- **Recursos que ya tenemos** (en el repositorio):
  - Clips 3D de 3 s en `recursos/clips3d/`. Para este vídeo sirven `aire.mp4` (split, como bomba de calor), `calefaccion.mp4` (radiador), `termo.mp4` y `medidor.mp4` (contador de luz).
  - Logo, banner y marca de agua en `canales/how-your-home-works/marca/`.
- **Lo que falta y tienes que conseguir:** imagen de una caldera de gas, de una unidad exterior de bomba de calor y de una llama de gas; un mapa de EE. UU. con los 6 estados. Usa solo stock con licencia libre (Pexels o Pixabay), gráficos propios o 3D propio. **Nada de clips de otros youtubers, películas o noticias.**
- **Voz:** sintética o grabada, en inglés de EE. UU., ritmo tranquilo. Si es voz de IA, en YouTube hay que marcar «Contenido alterado o sintético: Sí».
- **Música:** solo de la Biblioteca de audio de YouTube, entre 18 y 20 dB por debajo de la voz. Volumen final en torno a −14 LUFS.

---

## 1 · Gancho (0:00–0:15)
**Narración**
> In Florida, a heat pump heats a typical home for about ninety dollars a year less than a gas furnace.
> In Illinois, the same heat pump costs about seven hundred dollars a year *more*.
> Same machines. Same physics. Completely different answer.

**Imagen**
- Pantalla partida: Florida (palmeras, sol) a la izquierda e Illinois (nieve) a la derecha.
- En cada lado, un contador de dólares: Florida **−$90/yr**, en verde, e Illinois **+$690/yr**, en naranja.
- «Same machines» → clip 3D `aire.mp4` girando, entre las dos mitades.

**Texto en pantalla:** `Florida: heat pump saves ~$90/yr` · `Illinois: heat pump costs ~$690/yr more`

---

## 2 · Promesa (0:15–0:40)
**Narración**
> So is a heat pump actually cheaper to run than gas where you live?
> I ran the numbers for six states, using government data on energy prices and on how much heat homes really use.
> By the end, you'll know the one number that decides it for your own house.
> Quick note: this is about running costs only, not the price of buying or installing either system.

**Imagen**
- Mapa de EE. UU. en el estilo del canal. Se iluminan uno a uno Florida, Arizona, Washington, Georgia, Minnesota e Illinois.
- «Government data»: tarjeta con «U.S. Energy Information Administration» y el sello «OFFICIAL DATA».
- «The one number»: un `?` grande que late.
- «Running costs only»: icono de factura mensual, y una etiqueta de precio de instalación tachada.

**Texto en pantalla:** `6 states · official data` · `Running costs only`

---

## 3 · Cómo funciona cada uno (0:40–2:00)
**Narración**
> First, the key difference.
> A gas furnace makes heat by burning natural gas. A new high-efficiency furnace turns at least ninety-five percent of the energy in that gas into heat for your home.
> A heat pump doesn't burn anything. It moves heat that's already outside, even in cold air, into your house, using electricity to run a compressor.
> That's why it can deliver more heat than the electricity it uses.
> The federal minimum efficiency for a new heat pump works out to about two point two units of heat for every unit of electricity, averaged over a heating season.
> So on efficiency, the heat pump wins. Easily.
> But you don't pay for efficiency. You pay for energy. And gas and electricity have very different prices.

**Imagen**
- Caldera: llama, y una barra que se llena hasta el **95 %**, en naranja. Fuente: ENERGY STAR.
- Bomba de calor: unidad exterior, flechas de calor que entran desde fuera aunque nieve, compresor girando. Clip `aire.mp4`.
- «Two point two»: ecuación animada `1 unit of electricity → 2.2 units of heat`, con 1 rayo y 2,2 llamas pequeñas. Fuente: DOE, mínimo federal 2023 (HSPF2 7,5).
- «You pay for energy»: corte rápido a dos facturas, una de gas y otra de luz.

**Texto en pantalla:** `Gas furnace: ≥95% efficient` · `Heat pump: ~2.2× (federal minimum)`

---

## 4 · El precio de cada energía (2:00–3:15)
**Narración**
> Here's the catch.
> In twenty twenty-six, the average American home pays about eighteen cents per kilowatt-hour for electricity.
> For natural gas, the average residential price in twenty twenty-five was fifteen dollars and thirty-four cents per thousand cubic feet.
> Put both in the same unit of energy, and the same amount of energy costs about three and a half times more as electricity than as gas.
> That gives us the number that decides everything: the break-even efficiency.
> If your heat pump delivers more heat per unit of electricity than that number, the heat pump is cheaper to run. If it delivers less, gas wins.
> At national average prices, the break-even is about three point four. And a minimum-efficiency heat pump is about two point two.
> So on average, across the country, gas is still cheaper to run.
> But nobody pays the national average. And this is where it gets interesting.

**Imagen**
- Contador de luz (`medidor.mp4`) y una cifra que cuenta hasta **18.2¢/kWh**. Fuente: EIA, 2026.
- Llama y cifra **$15.34 per 1,000 cubic feet**. Fuente: EIA, 2025.
- «Same unit»: dos barras con el mismo bloque de energía. La de la electricidad crece hasta **3.6×** la del gas: $53.3 frente a $14.8 por millón de BTU.
- «Break-even efficiency»: una balanza, con «heat pump efficiency» en un lado y «price ratio» en el otro.
- «3.4 vs 2.2»: dos marcas sobre una regla, 2.2 en azul y 3.4 en naranja, con un hueco entre ellas.
- «Nobody pays the average»: el mapa de EE. UU. con cada estado cambiando de color según su precio.

**Texto en pantalla:** `Electricity ≈ 3.6× the price of gas (same energy)` · `Break-even: 3.4 · Heat pump: 2.2`

---

## 5 · Cuánto calor necesita cada casa (3:15–4:00)
**Narración**
> The other half of the math is how much heat your home actually needs.
> The government's Residential Energy Consumption Survey measured how much gas homes burn for heating in each climate zone.
> A gas-heated home in a very cold or cold climate burns about three times as much as one in a hot, humid climate.
> I turned that into the heat those homes actually need, then worked out what it costs to supply it with a new gas furnace, or with a heat pump, at each state's own prices.

**Imagen**
- Tarjeta de fuente: «Residential Energy Consumption Survey · EIA · 2020».
- Mapa de zonas climáticas, con una barra de calor por zona, de menos a más: hot-humid 20.8, mixed-dry 19.0, marine 30.2, mixed-humid 44.0 y very cold/cold 60.8 millones de BTU de gas al año.
- «Three times»: comparación de dos casas, una pequeña llama en la de Florida y tres llamas en la de Minnesota.

**Texto en pantalla:** `Cold climates: ~3× the heating of hot-humid ones`

---

## 6 · Estado por estado (4:00–6:45)
> Gráfico recurrente para todo el bloque: **dos barras por estado**, gas en naranja y bomba de calor en azul, que crecen contando dólares. Arriba, el nombre del estado y un icono de su clima. Abajo y en pequeño, los precios del estado. Gana la barra más baja: se ilumina con la etiqueta «CHEAPER».

**Narración**
> Let's go state by state, from warm to cold.
>
> Florida. Electricity is about fifteen cents, but gas is expensive, around twenty-five dollars per thousand cubic feet.
> Heating a typical gas-heated home in Florida's climate costs about four hundred thirty dollars a year with a new gas furnace.
> With a heat pump, about three hundred forty.
> The heat pump wins by roughly ninety dollars a year. And in Florida, that same heat pump also works as your air conditioner.
>
> Arizona. Heating needs are small here. Gas furnace: about two hundred ninety dollars a year. Heat pump: about three hundred ten.
> Nearly a tie, with gas slightly ahead at minimum efficiency.
>
> Washington State has relatively cheap electricity, about fourteen cents.
> Gas: about four hundred thirty dollars a year. Heat pump: about four hundred sixty-five.
> Close again. The break-even here is about two point four, just above the federal minimum.
>
> Georgia, in the mixed-humid zone. Gas: about seven hundred thirty dollars. Heat pump: about seven hundred twenty-seven.
> That's a dead heat.
>
> Now the cold states. Minnesota. Gas is cheap here, about eleven dollars, and homes need a lot of heat.
> Gas furnace: about five hundred forty dollars a year. Heat pump at the federal minimum: about one thousand sixty-five.
> Why does the cold matter? A heat pump has to pull heat out of the outdoor air. The colder that air is, the harder the compressor works for every unit of heat it moves.
> So on the coldest days, efficiency drops further. ENERGY STAR's cold-climate heat pumps only have to reach one point seven five at five degrees Fahrenheit. At that level, the heat pump would cost over thirteen hundred dollars a year.
>
> Illinois is even more lopsided. Gas: about five hundred fifty-five. Heat pump: about twelve hundred forty-five.
> The break-even efficiency in Illinois is almost five. That's more than double the federal minimum.

| Estado | Gas (furnace 95 %) | Bomba de calor (COP 2,2) | Gana | Precios en pantalla |
|---|---|---|---|---|
| Florida | **$431** | **$340** | Bomba de calor | 15.3¢/kWh · $25.48/Mcf |
| Arizona | **$287** | **$311** | Gas (casi empate) | 15.4¢ · $18.58 |
| Washington | **$433** | **$465** | Gas (casi empate) | 14.4¢ · $17.62 |
| Georgia | **$730** | **$727** | Empate | 15.5¢ · $20.42 |
| Minnesota | **$542** | **$1,065** (y $1,338 con COP 1,75) | Gas | 16.4¢ · $10.98 |
| Illinois | **$556** | **$1,246** | Gas | 19.2¢ · $11.25 |

**Imagen extra**
- Florida: después de «air conditioner», la bomba de calor (clip `aire.mp4`) con copos de nieve, porque también enfría.
- Minnesota: con «coldest days», termómetro a **5 °F** y la barra azul que crece de $1,065 a $1,338.
- Illinois: con «almost five», la regla de antes con una marca en **4.9**, muy lejos de 2.2.

---

## 7 · El patrón (6:45–7:30)
**Narración**
> So here's the pattern.
> The heat pump wins where gas is expensive and winters are mild. Gas wins where gas is cheap and winters are long and cold.
> And notice: the cold states aren't losing mainly because heat pumps stop working in the cold. They're losing because gas is so cheap there.
> Minnesota pays less than half what Florida pays for the same gas.
> Two more things move the result.
> If you're comparing against an old furnace that's only eighty percent efficient, gas costs about nineteen percent more than with a new one.
> And better insulation shrinks both bills, but it doesn't change which one is cheaper.

**Imagen**
- Gráfico de dispersión: eje X «precio del gas», eje Y «frío del clima». Los 6 estados como puntos, azules donde gana la bomba de calor y naranjas donde gana el gas.
- «Less than half»: dos montones de monedas, **$10.98** en Minnesota frente a **$25.48** en Florida.
- «Old furnace 80 %»: barra de eficiencia que baja de 95 % a 80 % y factura de gas que sube **+19 %**.
- «Insulation»: casa que se envuelve en aislante y dos facturas que bajan a la vez.

**Texto en pantalla:** `Cheap gas + cold winters → gas wins` · `Pricey gas + mild winters → heat pump wins`

---

## 7b · ¿Y si combinas los dos? (7:30–8:15)
**Narración**
> There's also a middle path, and it follows straight from the break-even idea.
> Some homes use a hybrid setup, often called dual fuel: a heat pump paired with a gas furnace.
> On mild days, the heat pump does the heating at its best efficiency. When it gets really cold and its efficiency drops below your break-even line, the furnace takes over.
> In a state like Georgia or Washington, where the two are nearly tied on average, that switch point is where the savings come from.
> One more thing to keep in mind: prices move.
> Since twenty twenty, the average residential electricity price rose about thirty-eight percent, and natural gas rose about forty-two percent.
> Because both went up by a similar amount, the overall picture hasn't flipped. But in your state, a big change in either price can move your break-even.

**Imagen**
- Termómetro que baja poco a poco. Por encima de una línea marcada «break-even», trabaja la bomba de calor (azul, `aire.mp4`); al cruzarla hacia abajo, se enciende la caldera (llama naranja).
- Rótulo: `Dual fuel: heat pump on mild days, furnace on the coldest`.
- «Prices move»: dos líneas de 2020 a 2026. Electricidad **13.15¢ → 18.19¢ (+38%)**, fuente EIA EPM 5.3; gas **$10.78 → $15.34 (+42%)**, fuente EIA.

**Texto en pantalla:** `Electricity +38% · Gas +42% (since 2020)`

---

## 8 · Tu número (8:15–9:15) — la recompensa
**Narración**
> Now let's find the answer for your own home. You need two numbers from your bills.
> One: what you pay per kilowatt-hour of electricity. Two: what you pay for gas, per therm.
> Divide your electricity price by your gas price, then multiply by twenty-seven point eight.
> That's the efficiency your heat pump needs to beat a new ninety-five percent furnace.
> For example, eighteen cents per kilowatt-hour and a dollar fifty per therm gives about three point three.
> If your number comes out around two or lower, a typical heat pump should be cheaper to run. If it's above three, gas will most likely win on running costs.
> And if you heat with electric baseboard heaters, which turn one unit of electricity into one unit of heat, a heat pump at the federal minimum uses less than half the electricity for the same warmth.

**Imagen**
- Calculadora en pantalla, paso a paso:
  `$/kWh ÷ $/therm × 27.8 = break-even`
  `0.18 ÷ 1.50 × 27.8 = 3.3`
- Semáforo: **≤ 2** en verde («heat pump likely cheaper»), **2–3** en amarillo («check carefully») y **> 3** en naranja («gas likely cheaper»).
- Radiador eléctrico (clip `calefaccion.mp4`) frente a bomba de calor: barras de electricidad **1.0** frente a **0.45**.

**Texto en pantalla:** `Break-even = (¢/kWh ÷ 100) ÷ ($/therm) × 27.8`

> ✅ **Comprobación de la fórmula:** 1 therm = 29,307 kWh; 29,307 × 0,95 = 27,84. Está en `datos/resultados.txt`.

---

## 9 · Resumen y cierre (9:15–10:00)
**Narración**
> So, is a heat pump cheaper to run than gas?
> In Florida, yes. In Georgia, it's a tie. In Minnesota and Illinois, no, not at today's prices.
> The heat pump is the more efficient machine almost everywhere. Whether it's cheaper depends on what you pay for each kind of energy.
> If you want to see what every other appliance in your home costs per year, my full ranking of fifteen appliances is right here.

**Imagen**
- Repaso rápido: los 6 estados con su ganador (iconos de bomba de calor o de llama) sobre el mapa.
- Pantalla final (últimos 10–15 s): tarjeta del vídeo «Which Appliances Use the Most Electricity? Ranked by Cost» y botón de suscripción.

---

## Miniaturas (haz las 3 y súbelas a «Probar y comparar»)
1. **Versus:** bomba de calor (azul) a la izquierda y llama de gas (naranja) a la derecha, con «VS» en el centro. Texto: **«WHICH IS CHEAPER?»**
2. **Mapa:** EE. UU. con Florida en azul y Minnesota en naranja. Texto: **«$340 vs $1,065»**
3. **Cifra:** bomba de calor grande con una etiqueta roja **«+$690/YR?»**. Texto: **«DEPENDS WHERE»**

Máximo 4 palabras, alto contraste y que se lea en el móvil.

## Metadatos para YouTube
**Título** (menos de 60 caracteres):
`Heat Pump vs Gas Furnace: Which Is Cheaper to Run?`

**Descripción:**
```
Heat pump vs gas furnace: which one is actually cheaper to run? I calculated the yearly heating cost in 6 states, from Florida to Illinois, using official U.S. government data on energy prices and home heating use.

In Florida a heat pump saves about $90 a year. In Illinois it costs about $690 more. The difference comes down to one number: your break-even efficiency, and you can calculate yours in 30 seconds (see 8:15).

This video covers running costs only, not purchase or installation.

Chapters:
0:00 Florida vs Illinois
0:15 What we're comparing
0:40 How each system makes heat
2:00 The price of gas vs electricity
3:15 How much heat homes need
4:00 State by state
6:45 The pattern
7:30 Hybrid systems and changing prices
8:15 Calculate your own break-even
9:15 Summary

How the numbers work: heating demand from the EIA Residential Energy Consumption Survey (2020) by climate zone; new furnace at 95% efficiency (ENERGY STAR minimum, South); heat pump at the 2023 federal minimum (HSPF2 7.5 ≈ 2.2 seasonal efficiency); residential prices from the EIA (electricity Jan–Aug 2026, gas 2025). Your own costs depend on your home, climate and rates.

Sources:
EIA Residential Energy Consumption Survey 2020, table CE5.4: https://www.eia.gov/consumption/residential/data/2020/index.php?view=consumption
EIA electricity prices by state, Table 5.6.B: https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_b
EIA natural gas residential prices by state: https://www.eia.gov/dnav/ng/ng_pri_sum_a_EPG0_PRS_DMcf_a.htm
ENERGY STAR furnace criteria: https://www.energystar.gov/products/furnaces/key_product_criteria
ENERGY STAR heat pump criteria: https://www.energystar.gov/products/air_source_heat_pumps/key-product-criteria
```
> Ajusta los minutos de los capítulos a los del montaje final.

**Etiquetas:**
`heat pump vs gas furnace, heat pump cost, gas furnace cost, is a heat pump cheaper, heating cost comparison, heat pump cold climate, home heating, energy bills, break even, home by the numbers`

**Ajustes:** idioma inglés · lista «Home energy costs, explained» · no es para niños · contenido sintético: **Sí** si la voz es de IA.
