## Laat je RGB LED branden

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In het vuurvliegjes LED-project heb je een LED met één kleur gebruikt. Voor je feestknaller sluit je een RGB (full colour) LED aan op je Raspberry Pi Pico en toon je een kleur die je zelf kiest.
</div>
<div>
![Er is een RGB-LED bevestigd aan een Raspberry Pi Pico en deze licht op in paars.](images/led-purple.gif){:width="300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
RGB staat voor Rood Groen Blauw. Met <span style="color: #ff2416"><b>RGB LED's</b></span> kun je code gebruiken om te bepalen hoeveel van elke kleur wordt uitgestraald.
</p>

[[[generic-theory-simple-colours]]]

--- task ---

Zorg ervoor dat de Raspberry Pi Pico **losgekoppeld** is van de computer voordat je onderdelen aansluit, omdat de verbindingen anders overbelast, kortgesloten of beschadigd kunnen raken.

--- /task ---

--- task ---

Sluit de **RGB-LED** aan op de Pico aan de hand van de instructies hier:

[[[rgb-led-resistor-electrical-tape]]]

[[[rgb-led-resistor-solder-heat-shrink]]]

--- /task ---

--- task ---

Een RGB LED heeft **vier** poten, een voor elke kleur en een voor een gedeelde verbinding met **GND**.

![Een diagram van een RGB LED met de poten gekleurd en in de volgorde rood, aarde, groen, blauw.](images/rgb-led-legs.png)

Kijk naar je RGB LED en zorg ervoor dat je de vier poten kunt ontdekken. In het bovenstaande diagram, van links naar rechts, is het eerste pootje voor **Rood**, het tweede pootje voor **GND** (aarde), het derde pootje voor **Groen** en het laatste voor **Blauw**.

**Let op:** het **GND** (aarde) pootje is het langste.

--- /task ---

--- task ---

Draai je Raspberry Pi Pico om en zoek de pinnen met de naam **GP1**, **GND**, **GP2** en **GP3**.

**Verbind** de jumperdraad die is aangesloten op het rode pootje van je RGB LED aan op **GP1**, de aarde (negatief) aan op **GND**, groen aan op **GP2**, en blauw aan op **GP3**:

![Een diagram van een RGB LED met weerstanden die zijn aangesloten op pennen GP1, GND, GP2 en GP3.](images/rgb-led-diagram.png)

--- /task ---

--- task ---

**Sluit de Raspberry Pi Pico** aan op de computer met de micro-USB-kabel.

--- /task ---

--- task ---

Maak een nieuw bestand in Thonny door op **File** > **New** in de bovenste menubalk te klikken. Er wordt een leeg bestand geopend. Sla het bestand op als `party_popper.py`.

![Afbeelding van het File-menu in Thonny met het menu-item New.](images/new_thonny.png)

--- /task ---

--- task ---

Voeg code toe voor de `import` van `RGBLED` en gebruik deze om een `rgb` variabele te maken, zodat je de RGB LED kunt programmeren die je hebt aangesloten op de pennen **GP1**, **GND**, **GP2** en **GP3**.

--- code ---
---
language: python filename: party_popper.py line_numbers: true line_number_start: 1
line_highlights:
---
from picozero import RGBLED from time import sleep

rgb = RGBLED(red=1, green=2, blue=3) # Pin numbers

--- /code ---

**Tip:** `RGBLED(red=1, green=2, blue=3)` kan ook worden geschreven als `RGBLED(1, 2, 3)`, waarbij alleen de pennummers worden gebruikt die op elk kanaal zijn aangesloten.

--- /task ---

--- task ---

Maak nu een `knal` functie om de RGB LED te laten branden en een bericht te tonen in de Thonny shell zodat je weet wanneer de functie wordt aangeroepen.

Je moet de functie ook **aanroepen (call)** met `knal()`.

--- code ---
---
language: python filename: party_popper.py line_numbers: true line_number_start: 1
line_highlights: 6-12
---
from picozero import RGBLED from time import sleep

rgb = RGBLED(red=1, green=2, blue=3) # Pin numbers

def pop(): print("Pop") # Print to the shell rgb.color = (255, 0, 255) # Purple sleep(2) rgb.off()

pop() # Call the pop function

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je script uit en controleer of de RGB-LED gedurende twee seconden paars (maximaal rood en maximaal blauw) wordt en vervolgens uitgaat. Controleer ook of je het woord "Knal" ziet staan in de Thonny-shell telkens wanneer je je script uitvoert.

![Er is een RGB-LED aangesloten op een Raspberry Pi Pico en deze licht op in de kleur paars.](images/led-purple.gif){:width="300px"}

**Fouten oplossen:**

--- collapse ---

---
title: Ik zie het bericht `RGBLED is not defined`
---

Zorg ervoor dat in regel 1 `from picozero import RGBLED` staat

--- /collapse ---

--- collapse ---

---
title: Het "Knal" bericht verschijnt niet in de shell
---

Controleer de Thonny-console op foutberichten en herstel je code zodat het er precies zo uitziet als het voorbeeld.

--- /collapse ---

--- collapse ---

---
title: Het "Knal" bericht verschijnt, maar de RGB gaat niet branden
---

Als de RGB-LED niet gaat branden:
+ Controleer of de jumperdraden op de juiste pennen zijn aangesloten
+ Controleer op losse verbindingen
+ Controleer of de LED niet is doorgebrand (of gebroken) door deze te verwisselen met een andere LED

--- /collapse ---

--- collapse ---

---
title: De RGB LED gaat aan, maar is niet paars
---

Mogelijk zijn de LED-poten aangesloten op de verkeerde pennen. Probeer de RGB LED in te stellen op de volgende kleuren en zorg ervoor dat de RGB LED de juiste kleur toont: rood `(255, 0, 0)`, groen `(0, 255, 0)`, blauw `(0, 0, 255)`. Verwissel de jumperdraden als dat nodig is. Als slechts één kleur werkt, dan kan het zijn dat de aarde is aangesloten op de kleur voor die pen.

--- /collapse ---

**Tip:** het gebruik van `print` om berichten te tonen in de Thonny-shell is handig als je scripts voor de Raspberry Pi Pico debugt.

--- /task ---

--- task ---

**Kies:** als je een andere kleur wilt, wijzig dan de getallen die de kleur instellen:

+ Rood: (255, 0, 0)
+ Groen: (0, 255, 0)
+ Blauw: (0, 0, 255)
+ Cyaan: (0, 255, 255)
+ Geel: (255, 255, 0)
+ Roze: (255, 0, 50)

Probeer de getallen aan te passen om de juiste balans te krijgen.

**Tip:** door rood, groen en blauw te mengen, krijg je wit.

**Tip:** als je vindt dat de LED te helder is, kun je een lagere waarde gebruiken. Bijvoorbeeld `(100, 0, 0)` zal nog steeds een rode kleur weergeven, maar deze zal niet zo helder zijn als `(255, 0, 0)`.

--- /task ---
