
--- question ---
---
legend: Vraag 2 van 3
---

Je helpt iemand met een project.

Ze proberen een geluid af te spelen op een zoemer die correct is aangesloten op pin GP5 en GND op hun Raspberry Pi Pico.

Dit is hun code:

--- code ---
---
language: python
filename: sound.py
line_numbers: true
line_number_start: 1
line_highlights: 
---
from picozero import RGBLED
from time import sleep

luidspreker = Speaker(5)

def speel_geluid():
    luidspreker.pitch(523, 1) # 523 = noot C4, 0.1 seconden
    sleep(0.1)

speel_geluid()

--- /code ---

Thonny geeft de fout: "**NameError: name 'Speaker' isn't defined**".

Welke regel code moeten ze bewerken om het probleem op te lossen?

--- choices ---

- (X) Regel 1

  --- feedback ---

Juist! In regel 1 moet `, Speaker` aan het einde toegevoegd zijn, zodat `Speaker` wordt geïmporteerd uit `picozero`.

  --- /feedback ---

- ( ) Regel 4

  --- feedback ---

Probeer het opnieuw. Het is een goed idee om te controleren of de juiste pen wordt gebruikt, maar in dit geval is dat juist.

  --- /feedback ---

- ( ) Regel 7

  --- feedback ---

Probeer het opnieuw. `luidspreker.pitch(523, 1)` speelt gedurende 1 seconde een noot af. Er ontbreekt iets op een andere regel.

  --- /feedback ---

- ( ) Regel 11

  --- feedback ---

Probeer het opnieuw. Om het geluid af te spelen is het nodig om de `speel_geluid()` functie met open- en sluithaakjes aan te roepen.

  --- /feedback ---

--- /choices ---

--- /question ---
