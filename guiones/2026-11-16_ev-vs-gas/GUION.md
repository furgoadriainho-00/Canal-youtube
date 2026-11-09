# Guion · EV vs Gas: What Charging at Home Really Costs, by State

| | |
|---|---|
| **Formato** | Vídeo largo · 16:9 |
| **Duración objetivo** | 9–10 min (narración de unas 1.550 palabras, a 164 por minuto) |
| **Publicar** | Lunes 16 de noviembre de 2026 |
| **Estructura** | Comparación (los anteriores: comparación, pregunta-respuesta, comparación) |
| **Fuentes y cálculos** | `fuentes.md` y `datos/calculo.py` → `datos/resultados.txt` |

Indicaciones en español; narración en inglés de EE. UU., literal. **La voz dice exactamente las cifras de la pantalla.** Escenas solo del motor (sin stock). No hay clip 3D de coche: usa iconos (`ev_station`, coche, surtidor), el contador de luz (`medidor.mp4`), la casa en corte con foco `coche` (el garaje), el mapa y las barras.

---

## 1 · Gancho (0:00–0:20)
**Narración**
> In Washington State, charging an electric car at home instead of buying gas saves about one thousand one hundred ninety-eight dollars a year.
> In Massachusetts, it saves about two hundred five.
> Same car. Same miles. So what's going on?

**Imagen:** mapa con WA (azul) y MA (naranja). Cifras con monedas: **$1,198/yr** y **$205/yr**. Icono de coche eléctrico que pasa entre los dos.
**Texto en pantalla:** `WA: $1,198/yr · MA: $205/yr`

## 2 · Promesa (0:20–0:50)
**Narración**
> In this video, I'll work out what it really costs to drive an electric car charged at home, compared with a gas car, for the whole country and for nine states.
> I'll use official numbers for how far Americans drive, how efficient the cars are, and what electricity and gasoline cost.
> And at the end, I'll give you a two-line formula to check your own state.

**Imagen:** casa en corte con foco `coche` (garaje con el cargador). Tarjetas de fuente: EPA, U.S. DOT / FHWA y EIA. Mapa con 9 estados que se encienden uno a uno.
**Texto en pantalla:** `9 states · official data · your own formula`

## 3 · Los ingredientes (0:50–2:20)
**Narración**
> First, the ingredients. There are only four.
> One: how far you drive. According to the Federal Highway Administration, the average car in America covers about eleven thousand twenty-six miles a year.
> Two: how efficient a gas car is. The EPA says the average new vehicle from model year twenty twenty-four gets about twenty-seven point two miles per gallon in real-world driving. That's a record high.
> Three: how efficient an electric car is. Popular twenty twenty-five models are rated by the EPA at between twenty-seven and thirty-one kilowatt-hours per hundred miles. For example, the Tesla Model Y Long Range rear-wheel drive is rated at twenty-seven, and the Chevrolet Equinox EV front-wheel drive at thirty-one. I'll use thirty, a middle value.
> And four: what you pay for energy. Nationally, regular gasoline averaged about three dollars and ten cents a gallon in twenty twenty-five, and home electricity is about eighteen point two cents per kilowatt-hour in twenty twenty-six.
> That's everything we need.

**Imagen**
- Cifra **11,026 mi/yr** con un cuentakilómetros (icono). Fuente: FHWA, Highway Statistics 2024.
- Surtidor con **27.2 mpg**. Fuente: EPA Automotive Trends.
- Barras horizontales de modelos de 2025 (kWh/100 mi): Model Y LR RWD **27**, Model Y LR AWD **29**, Ioniq 5 **29**, Equinox EV FWD **31**, Mach-E RWD Ext **31**; línea marcada **30** («used here»). Fuente: fueleconomy.gov.
- Dos cifras: gasolina **$3.10/gal** y luz **18.2¢/kWh**. Fuente: EIA.

**Texto en pantalla:** `11,026 mi · 27.2 mpg · 30 kWh/100 mi · $3.10/gal · 18.2¢/kWh`

## 4 · Cada 100 millas (2:20–3:10)
**Narración**
> Let's start small, with every hundred miles.
> A gas car at twenty-seven point two miles per gallon needs about three point seven gallons to go a hundred miles. At the national price, that's about eleven dollars and thirty-nine cents.
> An electric car at thirty kilowatt-hours per hundred miles, at the national electricity price, costs about five dollars and forty-six cents for the same hundred miles.
> So charging at home costs less than half as much per mile, on average.

**Imagen:** fórmula `100 ÷ 27.2 = 3.7 gal × $3.10 ≈ $11.39` y `30 kWh × $0.182 ≈ $5.46`. Comparación de dos barras: **$11.39** (gasolina, naranja) frente a **$5.46** (eléctrico, azul, sello CHEAPER).
**Texto en pantalla:** `Per 100 miles: $11.39 vs $5.46`

## 5 · Un año entero (3:10–4:00)
**Narración**
> Now scale that up to a full year of driving.
> At eleven thousand twenty-six miles, the gas car burns about four hundred five gallons, which costs about one thousand two hundred fifty-five dollars.
> The electric car uses about three thousand three hundred eight kilowatt-hours, which costs about six hundred two dollars.
> That's a difference of about six hundred fifty-four dollars a year, on national averages.

**Imagen:** dos contadores que corren a la vez: galones (**405**) y kWh (**3,308**) con el contador de luz. Después, comparación de dos barras: **$1,255** frente a **$602**. Cifra **−$654/yr** con monedas.
**Texto en pantalla:** `U.S.: $1,255 vs $602 → $654 a year`

## 6 · La parte prudente (4:00–4:50)
**Narración**
> Before going further, here's a cautious check.
> Charging a battery always wastes a bit of energy as heat. Oak Ridge National Laboratory says charging efficiency is often between eighty-four and ninety-three percent.
> The government's fuel economy site defines the EPA number as the electricity the car uses to travel a hundred miles, but it doesn't spell out how charging losses are counted.
> So let's take the worst case. If we add charging losses on top, at eighty-four percent efficiency, the electric car would cost about seven hundred sixteen dollars a year.
> It still saves about five hundred thirty-nine dollars. So the result holds either way.

**Imagen:** batería que se carga con un poco de «calor» que se escapa (icono). Anillo hasta **84%** (rótulo «84–93%»). Fuente: ORNL vía fueleconomy.gov. Barras: «EV (EPA rating)» **$602**, «EV (worst case)» **$716** y «Gas» **$1,255**.
**Texto en pantalla:** `Worst case: $716 · still saves $539`

## 7 · Estado por estado (4:50–7:00)
> Gráfico recurrente: **dos barras por estado** (gasolina en naranja, eléctrico en azul) que crecen contando dólares, con el ahorro debajo. Arriba, el nombre del estado; en pequeño, el precio de su gasolina y de su luz.

**Narración**
> But nobody pays the national average. Let's go state by state.
>
> Washington has relatively cheap electricity, about fourteen point four cents, and expensive gas, about four dollars and thirteen cents.
> That's the best combination for an electric car. Gas costs about one thousand six hundred seventy-five dollars a year, and charging at home about four hundred seventy-seven. That saves about one thousand one hundred ninety-eight dollars.
>
> In Florida, gas costs about one thousand one hundred ninety-nine dollars a year, and electricity about five hundred seven. That saves about six hundred ninety-two.
>
> Minnesota lands close to the national picture, saving about six hundred fifty-seven dollars. Colorado saves about six hundred seven.
>
> Texas has the cheapest gas of these states, about two dollars and sixty-six cents. Even so, an electric car saves about five hundred forty-eight dollars a year. Ohio saves about five hundred seventy-eight.
>
> California is the interesting one. Its electricity is the most expensive here, at about thirty-two point six cents. But its gas is also very expensive, about four dollars and forty-one cents. So the electric car still saves about seven hundred ten dollars a year.
>
> Now the two states where it gets tight. In New York, with electricity near twenty-nine point three cents, the savings drop to about two hundred seventy-one dollars a year.
> And in Massachusetts, with electricity near thirty point two cents, it's about two hundred five dollars.
> In the worst-case check with charging losses added, Massachusetts drops to about fifteen dollars a year. Basically a tie.

| Estado | Gasolina $/año | Eléctrico $/año | Ahorro | Caso prudente | Precios en pantalla |
|---|---|---|---|---|---|
| Washington | **$1,675** | **$477** | **$1,198** | $1,107 | 14.4¢ · $4.13 |
| Florida | **$1,199** | **$507** | **$692** | $595 | 15.3¢ · $2.96 |
| Minnesota | $1,201 | $544 | **$657** | $554 | 16.4¢ · $2.96 |
| Colorado | $1,163 | $556 | **$607** | $501 | 16.8¢ · $2.87 |
| Texas | $1,078 | $530 | **$548** | $447 | 16.0¢ · $2.66 |
| Ohio | $1,200 | $622 | **$578** | $459 | 18.8¢ · $2.96 |
| California | $1,788 | $1,078 | **$710** | $505 | 32.6¢ · $4.41 |
| New York | $1,239 | $968 | **$271** | $87 | 29.3¢ · $3.06 |
| Massachusetts | $1,204 | $999 | **$205** | **$15** | 30.2¢ · $2.97 |

**Imagen extra:** al final del bloque, el mapa con los 9 estados coloreados según el ahorro (azul fuerte en WA, claro en MA) y las cifras encima.

## 7b · Lo que suma a tu factura de la luz (7:00–7:50)
**Narración**
> Here's another way to see it: what an electric car adds to your home's electric bill.
> At eleven thousand twenty-six miles a year, charging at home adds about three thousand three hundred eight kilowatt-hours.
> The average American home uses about ten thousand seven hundred ninety-one kilowatt-hours a year. So the car adds about thirty-one percent to the household's electricity use.
> Month by month, that's about two hundred seventy-six kilowatt-hours, or about fifty dollars, at the national price.
> And the government's household survey has a real-world number too. Homes that charge an electric car used about two thousand three hundred sixty-three kilowatt-hours a year for charging. At today's price, that's about four hundred thirty dollars.
> That's below our estimate, a reminder that real households vary in how much they drive and where they plug in.

**Imagen**
- Casa en corte con foco `coche` y el contador de luz (`medidor.mp4`) que sube **+3,308 kWh**.
- Anillo que se llena hasta **31%** sobre la cifra **10,791 kWh** del hogar medio. Fuente: EIA.
- Cifras al mes: **276 kWh** y **$50/mo** con monedas.
- Tarjeta «EIA · RECS 2020» y cifra **2,363 kWh → $430/yr**.

**Texto en pantalla:** `+31% household electricity · ~$50/month`

## 7c · Los precios cambian (7:50–8:30)
**Narración**
> One more thing: both prices move.
> In twenty twenty, regular gas averaged about two dollars and seventeen cents a gallon. In twenty twenty-two, it spiked to about three dollars and ninety-five cents. In twenty twenty-five, it was back to about three dollars and ten cents.
> Home electricity rose more steadily, from about thirteen point two cents in twenty twenty to about eighteen point two cents today.
> Per hundred miles, gas went from about seven dollars and ninety-seven cents in twenty twenty, to about fourteen fifty-three at the twenty twenty-two peak, and about eleven thirty-nine now. Electricity went from about three ninety-four to about five forty-six.
> In twenty twenty, and again today, charging at home cost about half as much per mile as gas. At the twenty twenty-two peak, with electricity at about fifteen cents, it cost about four dollars and fifty-one cents per hundred miles, less than a third of gas.
> Gas simply swings a lot more than electricity.

**Imagen:** dos líneas de 2020 a 2026: gasolina **$2.17 → $3.95 (2022) → $3.10** (naranja, con el pico marcado) y luz **13.2¢ → 18.2¢** (azul, constante). Después, barras cada 100 millas: 2020 **$7.97 vs $3.94**, 2022 **$14.53 vs $4.51**, hoy **$11.39 vs $5.46**. Fuente: EIA.
**Texto en pantalla:** `2022 peak: $14.53 vs $4.51 per 100 mi`

## 8 · El precio de la luz que empata (8:30–9:10)
**Narración**
> So here's the pattern. The savings depend on two prices: gas and electricity. Cheap power and expensive gas, like Washington, is the jackpot. Expensive power and average gas, like Massachusetts, shrinks the gap.
> On national gas prices, electricity would have to cost about thirty-eight cents per kilowatt-hour before charging at home stopped being cheaper.
> In the worst case, with charging losses added, that line drops to about thirty-one point nine cents.
> Most states are far below that line. A few in the Northeast and California are getting close.

**Imagen:** regla de ¢/kWh de 0 a 40 con una línea **38.0¢** («break-even») y otra punteada **31.9¢** («worst case»). Marcas para WA **14.4**, US **18.2**, NY **29.3**, MA **30.2** y CA **32.6**.
**Texto en pantalla:** `Break-even power price: 38.0¢ (worst case 31.9¢)`

## 9 · Tu fórmula (9:10–10:10) — la recompensa
**Narración**
> Now let's do your own state, in two lines.
> Line one, the electric car: multiply its rating in kilowatt-hours per hundred miles by your electricity price. Thirty times eighteen point two cents is about five dollars and forty-six cents per hundred miles.
> Line two, the gas car: divide one hundred by its miles per gallon, then multiply by your gas price. One hundred divided by twenty-seven point two, times three dollars and ten cents, is about eleven dollars and thirty-nine cents.
> The difference, times the miles you drive divided by a hundred, is your yearly savings.
> And the car itself matters. A Tesla Model Y Long Range rear-wheel drive, at twenty-seven kilowatt-hours per hundred miles, costs about five hundred forty-two dollars a year to charge at the national price. An Equinox EV front-wheel drive, at thirty-one, about six hundred twenty-two.

**Imagen:** fórmula paso a paso:
`EV: kWh/100 mi × $/kWh` → `30 × $0.182 = $5.46`
`Gas: 100 ÷ mpg × $/gal` → `100 ÷ 27.2 × $3.10 = $11.39`
`(gas − EV) × miles ÷ 100 = yearly savings`
Después, barras: Model Y LR RWD **$542/yr** y Equinox EV FWD **$622/yr**.
**Texto en pantalla:** `EV = kWh/100 × price · Gas = 100 ÷ mpg × price`

## 10 · Lo que no entra (10:10–10:40)
**Narración**
> A few things are not in these numbers.
> This is home charging only. Public charging prices vary a lot, and they're not included here.
> It also leaves out the price of the car, insurance and maintenance. This is purely the cost of energy to drive.
> And these are averages. If you drive more than eleven thousand miles a year, the savings grow with every mile.

**Imagen:** tres iconos tachados: cargador público, etiqueta de precio del coche y llave inglesa. Después, cuentakilómetros que sube y monedas que crecen.
**Texto en pantalla:** `Home charging · energy cost only`

## 11 · Resumen y cierre (10:40–11:10)
**Narración**
> So, is charging an electric car at home cheaper than buying gas? On national averages, yes, by about six hundred fifty-four dollars a year.
> In Washington, by about one thousand one hundred ninety-eight. In Massachusetts, only about two hundred five, and close to a tie in the worst case.
> Check your own two prices with the formula, and you'll know where your state lands.
> And if you're wondering what else charging adds to your home's electric bill, my ranking of fifteen home appliances is on this channel.

**Imagen:** repaso: el mapa con las cifras de los 9 estados y **$654** en el centro. Pantalla final hacia «Which Appliances Use the Most Electricity? Ranked by Cost».

---

## Miniaturas
1. **Mapa con cifras:** WA en azul y MA en naranja. Cifras: **«$1,198 vs $205»**
2. **Versus:** icono de cargador frente a surtidor. Texto: **«$602 vs $1,255»**
3. **Icono grande con cifra:** coche eléctrico y **«−$654/YR»**. Texto: **«EV VS GAS»**

## Metadatos para YouTube
**Título** (menos de 60 caracteres): `EV vs Gas: Real Cost of Charging at Home, by State`

**Descripción**
```
Is charging an electric car at home really cheaper than gas? Using official data for miles driven (FHWA), fuel economy (EPA) and energy prices (EIA), I calculated the yearly cost for the U.S. and 9 states.

U.S. average: gas about $1,255 a year vs about $602 charging at home, about $654 saved. Washington saves about $1,198; Massachusetts only about $205.

How the numbers work: 11,026 miles a year (FHWA Highway Statistics 2024); gas car at 27.2 mpg (EPA, model year 2024 average); EV at 30 kWh/100 mi (EPA ratings of popular 2025 models: 27–31); regular gasoline 2025 and residential electricity Jan–Aug 2026 (EIA). Worst-case check adds charging losses at 84% efficiency (ORNL). Home charging only; car price, insurance and maintenance not included.

Sources:
FHWA via AFDC, annual miles by vehicle type: https://afdc.energy.gov/data/10309
EPA Automotive Trends: https://www.epa.gov/automotive-trends/highlights-automotive-trends-report
EPA ratings: https://www.fueleconomy.gov
EIA gasoline prices: https://www.eia.gov/dnav/pet/pet_pri_gnd_a_epmr_pte_dpgal_a.htm
EIA electricity prices by state: https://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=epmt_5_6_b
Charging efficiency (ORNL, via fueleconomy.gov): https://www.fueleconomy.gov/feg/evtech.shtml
```
**Etiquetas:** `ev vs gas, cost to charge electric car at home, ev charging cost, electric car savings, ev cost by state, home ev charging, gas vs electric car, home by the numbers`
**Ajustes:** idioma inglés · lista «Home energy costs, explained» · no es para niños · contenido sintético: **Sí** (voz IA).
