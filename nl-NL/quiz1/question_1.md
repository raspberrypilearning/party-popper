## Reflectie

Goed gedaan. Je hebt een herbruikbare elektronische feestknaller gemaakt die je kunt gebruiken wanneer je wilt vieren. Nu is het tijd om na te denken over wat je hebt geleerd om je te helpen onthouden.

Beantwoord de drie onderstaande vragen.

Je wordt naar het juiste antwoord geleid. Je kunt deze activiteit zo vaak doen als je wilt.

Veel plezier!

--- question ---

---
legend: Vraag 1 van 3
---

In het feestknaller-project heb je een RGB LED geprogrammeerd om de kleur paars te laten zien door rood en blauw te mengen:

--- code ---
---
language: python filename: party_popper.py line_numbers: true line_number_start: 1
line_highlights: 3
---
from picozero import RGBLED

rgb = RGBLED(red=1, green=2, blue=3) # Pin numbers

rgb.color = (255, 0, 255) # Purple

--- /code ---

Welk diagram toont de pennen die correct zijn aangesloten om deze code te laten werken:

--- choices ---

- (x) ![Een diagram van een RGB LED met weerstanden die zijn aangesloten op pennen GP1, GND, GP2 en GP3.](images/rgb-led-quiz.png)

  --- feedback ---

Ja. Het is echt belangrijk dat de jumperdraden die zijn aangesloten op de LED-benen zijn aangesloten op de vermelde pinnen die worden gebruikt voor je `RGBLED`. In dit geval, rood naar pen GP1, aarde (negatief) naar GND, groen naar pen GP2, en blauw naar pen GP3.

  --- /feedback ---

- ( ) ![Een diagram van een RGB LED met weerstanden die zijn aangesloten op GP0, GP1, GND en GP2.](images/rgb-reverse.png)

  --- feedback ---

Probeer het opnieuw. De LED is niet aangesloten op de pennen die in de code worden gebruikt, dus het instellen van de kleuren werkt niet goed.

  --- /feedback ---

--- /choices ---

--- /question ---
