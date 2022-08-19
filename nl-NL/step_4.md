## Activeer je feestknaller

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Je moet je feestknaller kunnen activeren vanuit de Raspberry Pi Pico. In deze stap maak je een prototype van je schakelaar met behulp van jumperdraden. 
</div>
<div>
![Afbeelding met een feestknaller project met een schakelaar gemaakt van een paar jumper draden.](images/switch-buzzer-led.jpg){:width="300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
<span style="color: #0faeb0">Licht- en geluidsvoorstellingen</span> met technologie worden wereldwijd gebruikt voor vieringen. Deze **duurzame** en **herbruikbare** opties zorgen voor leuke displays en interactief amusement. In plaats van wegwerp voorwerpen zoals plastic feestknallers of chemisch vuurwerk, vieren mensen tegenwoordig met drones, lasers en projectieshows!
</p>

--- task ---

Pak **twee bus–pen** jumperdraden die voor je trekschakelaar gebruikt kunnen worden.

**Sluit** een jumperdraad aan op **GP18** en de andere op de **GND** pen ernaast.

![Een bedradingsschema met een jumperdraad die is aangesloten op GP18 en een andere jumperdraad die is aangesloten op GND.](images/jumper-switch.png)

--- /task ---

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>Er zijn twee manieren waarop je code kunt uitvoeren op basis van de status van een ingang (zoals een schakelaar of sensor). De eerste is om een lus te gebruiken en de status te blijven controleren, dit heet <span style="color: #0faeb0">polling</span>. Je hebt polling gebruikt in je vuurvliegproject. De tweede is om een functie aan te roepen wanneer een ingang van status verandert, met behulp van <span style="color: #0faeb0">events (gebeurtenissen)</span> die veranderingen detecteren wanneer ze plaatsvinden. 
</p>

--- task ---

Wijzig je code om `picozero` te vertellen om de `knal` functie aan te roepen wanneer de trekschakelaar wordt geopend (losgekoppeld).

Wanneer je een gebeurtenis gebruikt zoals `when_opened`, wordt de functie uitgevoerd totdat deze is voltooid en kun je deze niet onderbreken. Dit is wat je wilt in dit geval, je wilt dat het hele geluidseffect en kleurveranderingeffect plaats vinden wanneer de feestknaller wordt geactiveerd.

**Vergeet niet** dat je ook `Switch` moet importeren van `picozero` op regel 1.

--- code ---
---
language: python
filename: party_popper.py 
line_numbers: true
line_number_start: 1
line_highlights: 1, 5, 19
---
from picozero import RGBLED, Speaker, Switch
from time import sleep

rgb = RGBLED(red=1, green=2, blue=3) # Pennummers 
trek = Switch(18)
luidspreker = Speaker(5)

def knal():
    print("Knal") # Toon in de terminal
    rgb.color = (255, 0, 255) # Paars
    luidspreker.play(523, 0.1) # 523 = noot C4, 0.1 seconden
    rgb.color = (0, 0, 0) # LED geen kleur – uit
    sleep(0.1)
    rgb.color = (255, 0, 255) # Paars
    luidspreker.play(523, 0.6) # Noot C4, 0.6 seconden
    rgb.off()
        
trek.when_opened = pop # De pop-functie wordt opgeroepen wanneer de trekschakelaar wordt geopend

--- /code ---

**Tip:** Zorg ervoor dat je **niet** `()` toevoegt aan het einde van `trek.when_opened = knal`. Deze regel vertelt `picozero` dat telkens wanneer de `when_opened` gebeurtenis plaatsvindt, de `knal` functie wordt aangeroepen.

--- /task ---

--- task ---

**Test**: Voer de code uit om ervoor te zorgen dat de RGB-LED brandt en het geluid wordt afgespeeld telkens wanneer de schakelaar **geopend** is.

**Fouten oplossen**:

--- collapse ---

---
title: Ik zie het bericht `Switch is not defined`
---

Voeg `, Switch` toe aan het einde van regel 1.

--- /collapse ---

--- collapse ---

---
title: De code loopt voordat ik aan de schakelaar trek
---

+ Controleer of de kabels van de trekschakelaar op de juiste pennen zijn aangesloten
+ Controleer of de kabels van de trekschakelaar goed met elkaar zijn verbonden
+ Controleer of je de regel `knal()` hebt verwijderd en deze hebt vervangen door `trek.when_opened = knal`

--- /collapse ---

--- collapse ---

---
title: Het "Knal" bericht verschijnt niet in de shell
---

Controleer de Thonny-console op foutberichten en herstel je code zodat het er precies zo uitziet als het voorbeeld.

--- /collapse ---

--- collapse ---

---
title: De RGB LED of zoemer werkt niet meer
---

+ Controleer of de juiste pootjes zijn aangesloten op de juiste pennen
+ Controleer op losse verbindingen
+ Controleer of de LED niet is doorgebrand

--- /collapse ---

--- /task ---
