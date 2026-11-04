# Script · Heat Pump vs Gas Furnace

| | |
|---|---|
| **Channel** | Home By The Numbers (@HomeByTheNumbers) |
| **Format** | Long video · 16:9 · 1920×1080 · 30 fps |
| **Target length** | 9–10 min (about 1,250 words of narration) |
| **Publish** | Thursday, November 5, 2026 |
| **Structure** | Comparison (the previous video was a list) |
| **Language** | Narration in US English |
| **Sources & math** | `fuentes.md` and `datos/calculo.py` in this folder. **Do not change any number without checking with us first.** |

## General notes for the editor
- **Channel style:** midnight-blue background `#0F1B2D`, orange accent `#FF7A1A` (heat, gas, cost) and blue `#2EC4F1` (cold, electricity, savings). Montserrat ExtraBold for numbers and titles, Inter for everything else.
- **Pace:** change the picture every 2–4 seconds. **No text-only screens**, except short transition lines (under 2 seconds).
- **Numbers:** every dollar figure counts up from 0, with coins or animated bars. Show the source small at the bottom the first time each figure appears.
- **Assets we already have** (in the repository):
  - 3-second 3D clips in `recursos/clips3d/`. For this video: `aire.mp4` (wall-mounted unit, use it as the heat pump), `calefaccion.mp4` (electric radiator), `termo.mp4` (water heater) and `medidor.mp4` (electric meter).
  - Logo, banner and watermark in `canales/how-your-home-works/marca/`.
- **What you need to source:** a gas furnace, an outdoor heat pump unit, a gas flame, and a US map with the 6 states. Use only free-license stock (Pexels or Pixabay), your own graphics or your own 3D. **No clips from other YouTubers, movies or news.**
- **Voice:** US English, calm and clear pace, using the narration exactly as written (numbers are spelled out the way they should be said). With an AI voice, set "Altered or synthetic content: Yes".
- **Music:** YouTube Audio Library only, 18–20 dB below the voice. Final loudness around −14 LUFS.

---

## 1 · Hook (0:00–0:15)
**Narration**
> In Florida, a heat pump heats a typical home for about ninety dollars a year less than a gas furnace.
> In Illinois, the same heat pump costs about seven hundred dollars a year *more*.
> Same machines. Same physics. Completely different answer.

**Visuals**
- Split screen: Florida (palm trees, sun) on the left and Illinois (snow) on the right.
- A dollar counter on each side: Florida **−$90/yr** in green, Illinois **+$690/yr** in orange.
- "Same machines" → 3D clip `aire.mp4` rotating between the two halves.

**On-screen text:** `Florida: heat pump saves ~$90/yr` · `Illinois: heat pump costs ~$690/yr more`

---

## 2 · Promise (0:15–0:40)
**Narration**
> So is a heat pump actually cheaper to run than gas where you live?
> I ran the numbers for six states, using government data on energy prices and on how much heat homes really use.
> By the end, you'll know the one number that decides it for your own house.
> Quick note: this is about running costs only, not the price of buying or installing either system.

**Visuals**
- US map in the channel style. Florida, Arizona, Washington, Georgia, Minnesota and Illinois light up one by one.
- "Government data": a card reading "U.S. Energy Information Administration" with an "OFFICIAL DATA" stamp.
- "The one number": a big pulsing `?`.
- "Running costs only": a monthly-bill icon, plus an installation price tag that gets crossed out.

**On-screen text:** `6 states · official data` · `Running costs only`

---

## 3 · How each one works (0:40–2:00)
**Narration**
> First, the key difference.
> A gas furnace makes heat by burning natural gas. A new high-efficiency furnace turns at least ninety-five percent of the energy in that gas into heat for your home.
> A heat pump doesn't burn anything. It moves heat that's already outside, even in cold air, into your house, using electricity to run a compressor.
> That's why it can deliver more heat than the electricity it uses.
> The federal minimum efficiency for a new heat pump works out to about two point two units of heat for every unit of electricity, averaged over a heating season.
> So on efficiency, the heat pump wins. Easily.
> But you don't pay for efficiency. You pay for energy. And gas and electricity have very different prices.

**Visuals**
- Furnace: a flame, and a bar that fills to **95%** in orange. Source: ENERGY STAR.
- Heat pump: outdoor unit, heat arrows coming in from outside even with snow falling, spinning compressor. Clip `aire.mp4`.
- "Two point two": animated equation `1 unit of electricity → 2.2 units of heat`, with 1 lightning bolt and 2.2 small flames. Source: DOE, 2023 federal minimum (HSPF2 7.5).
- "You pay for energy": quick cut to two bills, one for gas and one for electricity.

**On-screen text:** `Gas furnace: ≥95% efficient` · `Heat pump: ~2.2× (federal minimum)`

---

## 4 · The price of each energy (2:00–3:15)
**Narration**
> Here's the catch.
> In twenty twenty-six, the average American home pays about eighteen cents per kilowatt-hour for electricity.
> For natural gas, the average residential price in twenty twenty-five was fifteen dollars and thirty-four cents per thousand cubic feet.
> Put both in the same unit of energy, and the same amount of energy costs about three and a half times more as electricity than as gas.
> That gives us the number that decides everything: the break-even efficiency.
> If your heat pump delivers more heat per unit of electricity than that number, the heat pump is cheaper to run. If it delivers less, gas wins.
> At national average prices, the break-even is about three point four. And a minimum-efficiency heat pump is about two point two.
> So on average, across the country, gas is still cheaper to run.
> But nobody pays the national average. And this is where it gets interesting.

**Visuals**
- Electric meter (`medidor.mp4`) with a number counting up to **18.2¢/kWh**. Source: EIA, 2026.
- Flame with **$15.34 per 1,000 cubic feet**. Source: EIA, 2025.
- "Same unit": two bars for the same block of energy. The electricity bar grows to **3.6×** the gas bar: $53.3 vs $14.8 per million BTU.
- "Break-even efficiency": a balance scale, "heat pump efficiency" on one side and "price ratio" on the other.
- "3.4 vs 2.2": two marks on a ruler, 2.2 in blue and 3.4 in orange, with a gap between them.
- "Nobody pays the average": the US map with each state changing color by its prices.

**On-screen text:** `Electricity ≈ 3.6× the price of gas (same energy)` · `Break-even: 3.4 · Heat pump: 2.2`

---

## 5 · How much heat each home needs (3:15–4:00)
**Narration**
> The other half of the math is how much heat your home actually needs.
> The government's Residential Energy Consumption Survey measured how much gas homes burn for heating in each climate zone.
> A gas-heated home in a very cold or cold climate burns about three times as much as one in a hot, humid climate.
> I turned that into the heat those homes actually need, then worked out what it costs to supply it with a new gas furnace, or with a heat pump, at each state's own prices.

**Visuals**
- Source card: "Residential Energy Consumption Survey · EIA · 2020".
- Climate-zone map with one heat bar per zone, smallest to largest: hot-humid 20.8, mixed-dry 19.0, marine 30.2, mixed-humid 44.0, very cold/cold 60.8 million BTU of gas per year.
- "Three times": two houses side by side, one small flame on the Florida house and three flames on the Minnesota house.

**On-screen text:** `Cold climates: ~3× the heating of hot-humid ones`

---

## 6 · State by state (4:00–6:45)
> Recurring graphic for the whole section: **two bars per state**, gas in orange and heat pump in blue, growing as the dollars count up. State name and a climate icon at the top; that state's prices small at the bottom. The lower bar wins: it lights up with a "CHEAPER" label.

**Narration**
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

| State | Gas (95% furnace) | Heat pump (COP 2.2) | Winner | Prices on screen |
|---|---|---|---|---|
| Florida | **$431** | **$340** | Heat pump | 15.3¢/kWh · $25.48/Mcf |
| Arizona | **$287** | **$311** | Gas (near tie) | 15.4¢ · $18.58 |
| Washington | **$433** | **$465** | Gas (near tie) | 14.4¢ · $17.62 |
| Georgia | **$730** | **$727** | Tie | 15.5¢ · $20.42 |
| Minnesota | **$542** | **$1,065** ($1,338 at COP 1.75) | Gas | 16.4¢ · $10.98 |
| Illinois | **$556** | **$1,246** | Gas | 19.2¢ · $11.25 |

**Extra visuals**
- Florida: after "air conditioner", the heat pump (clip `aire.mp4`) with snowflakes, because it also cools.
- Minnesota: on "coldest days", a thermometer at **5 °F** and the blue bar growing from $1,065 to $1,338.
- Illinois: on "almost five", the ruler from before with a mark at **4.9**, far from 2.2.

---

## 7 · The pattern (6:45–7:30)
**Narration**
> So here's the pattern.
> The heat pump wins where gas is expensive and winters are mild. Gas wins where gas is cheap and winters are long and cold.
> And notice: the cold states aren't losing mainly because heat pumps stop working in the cold. They're losing because gas is so cheap there.
> Minnesota pays less than half what Florida pays for the same gas.
> Two more things move the result.
> If you're comparing against an old furnace that's only eighty percent efficient, gas costs about nineteen percent more than with a new one.
> And better insulation shrinks both bills, but it doesn't change which one is cheaper.

**Visuals**
- Scatter plot: X axis "gas price", Y axis "how cold the climate is". The 6 states as dots, blue where the heat pump wins and orange where gas wins.
- "Less than half": two coin stacks, **$10.98** in Minnesota vs **$25.48** in Florida.
- "Old furnace 80%": efficiency bar dropping from 95% to 80% and the gas bill rising **+19%**.
- "Insulation": a house wrapping itself in insulation and both bills shrinking together.

**On-screen text:** `Cheap gas + cold winters → gas wins` · `Pricey gas + mild winters → heat pump wins`

---

## 7b · What if you combine both? (7:30–8:15)
**Narration**
> There's also a middle path, and it follows straight from the break-even idea.
> Some homes use a hybrid setup, often called dual fuel: a heat pump paired with a gas furnace.
> On mild days, the heat pump does the heating at its best efficiency. When it gets really cold and its efficiency drops below your break-even line, the furnace takes over.
> In a state like Georgia or Washington, where the two are nearly tied on average, that switch point is where the savings come from.
> One more thing to keep in mind: prices move.
> Since twenty twenty, the average residential electricity price rose about thirty-eight percent, and natural gas rose about forty-two percent.
> Because both went up by a similar amount, the overall picture hasn't flipped. But in your state, a big change in either price can move your break-even.

**Visuals**
- A thermometer slowly dropping. Above a line marked "break-even", the heat pump runs (blue, `aire.mp4`); once it crosses below, the furnace kicks in (orange flame).
- Caption: `Dual fuel: heat pump on mild days, furnace on the coldest`.
- "Prices move": two lines from 2020 to 2026. Electricity **13.15¢ → 18.19¢ (+38%)**, source EIA EPM 5.3; gas **$10.78 → $15.34 (+42%)**, source EIA.

**On-screen text:** `Electricity +38% · Gas +42% (since 2020)`

---

## 8 · Your number (8:15–9:15) — the payoff
**Narration**
> Now let's find the answer for your own home. You need two numbers from your bills.
> One: what you pay per kilowatt-hour of electricity. Two: what you pay for gas, per therm.
> Divide your electricity price by your gas price, then multiply by twenty-seven point eight.
> That's the efficiency your heat pump needs to beat a new ninety-five percent furnace.
> For example, eighteen cents per kilowatt-hour and a dollar fifty per therm gives about three point three.
> If your number comes out around two or lower, a typical heat pump should be cheaper to run. If it's above three, gas will most likely win on running costs.
> And if you heat with electric baseboard heaters, which turn one unit of electricity into one unit of heat, a heat pump at the federal minimum uses less than half the electricity for the same warmth.

**Visuals**
- On-screen calculator, step by step:
  `$/kWh ÷ $/therm × 27.8 = break-even`
  `0.18 ÷ 1.50 × 27.8 = 3.3`
- Traffic light: **≤ 2** green ("heat pump likely cheaper"), **2–3** yellow ("check carefully"), **> 3** orange ("gas likely cheaper").
- Electric radiator (clip `calefaccion.mp4`) vs heat pump: electricity bars **1.0** vs **0.45**.

**On-screen text:** `Break-even = (¢/kWh ÷ 100) ÷ ($/therm) × 27.8`

> ✅ **Formula check:** 1 therm = 29.307 kWh; 29.307 × 0.95 = 27.84. See `datos/resultados.txt`.

---

## 9 · Recap and close (9:15–10:00)
**Narration**
> So, is a heat pump cheaper to run than gas?
> In Florida, yes. In Georgia, it's a tie. In Minnesota and Illinois, no, not at today's prices.
> The heat pump is the more efficient machine almost everywhere. Whether it's cheaper depends on what you pay for each kind of energy.
> If you want to see what every other appliance in your home costs per year, my full ranking of fifteen appliances is right here.

**Visuals**
- Quick recap: the 6 states with their winner (heat pump or flame icon) on the map.
- End screen (last 10–15 s): card for the video "Which Appliances Use the Most Electricity? Ranked by Cost" and the subscribe button.

---

## Thumbnails (make all 3 and use YouTube's "Test & compare")
1. **Versus:** heat pump (blue) on the left, gas flame (orange) on the right, "VS" in the middle. Text: **"WHICH IS CHEAPER?"**
2. **Map:** US with Florida in blue and Minnesota in orange. Text: **"$340 vs $1,065"**
3. **Number:** big heat pump with a red tag **"+$690/YR?"**. Text: **"DEPENDS WHERE"**

Maximum 4 words, high contrast, readable on a phone.

## YouTube metadata
**Title** (under 60 characters):
`Heat Pump vs Gas Furnace: Which Is Cheaper to Run?`

**Description:**
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
> Update the chapter timestamps to match the final edit.

**Tags:**
`heat pump vs gas furnace, heat pump cost, gas furnace cost, is a heat pump cheaper, heating cost comparison, heat pump cold climate, home heating, energy bills, break even, home by the numbers`

**Settings:** language English · playlist "Home energy costs, explained" · not made for kids · altered or synthetic content: **Yes** with an AI voice (**No** only if a real person records it).
