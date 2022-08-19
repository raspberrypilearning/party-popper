
--- question ---
---
legend: Vraag 3 van 3
---

Je hebt een `when_opened`-gebeurtenis gebruikt om code uit te voeren wanneer je feestknaller wordt getrokken.

Welke regel code zorgt ervoor dat de gebeurtenis correct wordt ingesteld zodat de `knal` functie wordt aangeroepen telkens wanneer de verbinding wordt geopend.

--- choices ---

- (x) `trek.when_opened = knal`

  --- feedback ---

Juist! Wanneer we gebeurtenissen gebruiken, gebruiken we de `()` haakjes niet, omdat de functie alleen moet worden aangeroepen wanneer de gebeurtenis plaatsvindt. Als je aan het einde `()` toevoegt, wordt de functie **eenmaal** aangeroepen; zodra de regel code wordt uitgevoerd.

  --- /feedback ---

- ( ) `trek.when_opened = knal()`

  --- feedback ---

Nee, maar dit is echt een veel voorkomende fout! Deze code zal de `trek` functie **eenmaal** aanroepen wanneer deze regel code wordt uitgevoerd. In plaats daarvan moet je `pico_zero` vertellen welke functie moet worden uitgevoerd wanneer de gebeurtenis plaatsvindt en `pico_zero` zal de functie voor je aanroepen **elke keer** dat de gebeurtenis plaatsvindt.

  --- /feedback ---

--- /choices ---

--- /question ---
