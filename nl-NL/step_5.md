## Maak je schakelaar

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Maak een schakelaar om je feestknaller te activeren met golfkarton, lijm en keukenfolie.
</div>
<div>
![Afbeelding met een kartonnen schakelaar in de stijl van een pen- en bus-aansluiting.](Images/add-ribbon.jpg){:width="300px"}
</div>
</div>

--- task ---

Nu je weet dat je code werkt, moet je de schakelaar maken die je feestknaller zal starten!

Verzamel je materialen:

- Een schaar
- Golfkarton
- Keukenfolie
- Een lijmstift
- Wat plakband

**Optioneel**:

- Een potlood en een liniaal (als je nauwkeuriger wilt zijn)
- Een lint, touw, gekleurd papier/karton of gewoon papier dat je hebt ingekleurd

![Een stuk golfkarton, wat folie, een potlood, een liniaal, een lijmstok, een schaar en een stuk regenboog-gekleurd lint.](images/switch-gather-materials.jpeg)

--- /task ---

--- task ---

Snijd het **golfkarton** in drie rechthoeken van dezelfde grootte. Je kunt zelf de grootte van je feestknaller bepalen. Het voorbeeld is 3 cm × 5 cm.

**Tip**: Als je geen potlood en een liniaal hebt, knip dan de eerste en gebruik deze als sjabloon voor de andere twee.

![Drie stukken golfkarton in rechthoeken van gelijke grootte geknipt.](images/three-rectangles.jpg)

--- /task ---

--- task ---

Knip een gedeelte uit het midden van een van je rechthoeken. Bewaar het stukje karton dat je hebt uitgeknipt, omdat dit later zal worden gebruikt.

![Drie rechthoekige stukjes golfkarton. Het middenstuk heeft een middenstrook verwijderd zodat het een n vorm vormt. Het verwijderde stuk wordt ernaast geplaatst.](images/centre-cut.jpg)

--- /task ---

--- task ---

Neem de **keukenfolie** en snijd deze op dezelfde grootte als de ongesneden rechthoeken.

**Lijm** het karton en bevestig de folie.

**Tip:** Zorg ervoor dat je niet te veel lijm op de buitenkant van de folie krijgt, omdat dit de contacten van de schakelaar zal beïnvloeden.

![Drie rechthoekige stukjes golfkarton. Op de stukken links en rechts is folie gelijmd.](images/add-foil.jpg)

--- /task ---

--- task ---

Pak het stuk karton dat je uit de middelste rechthoek hebt verwijderd en snijd de bovenkant in een V-vorm of een punt om het makkelijker te maken om het in je kanon te plaatsen.

**Snijd** de zijkanten een paar millimeter bij om ervoor te zorgen dat deze gemakkelijk in je knaller past.

![Drie rechthoekige stukjes golfkarton. Op de stukken links en rechts is folie gelijmd. Een extra, kleiner stuk karton is eronder en heeft een V-vorm die aan het ene uiteinde wordt gesneden om een punt te vormen.](images/trim-piece.jpg)

--- /task ---

--- task ---

Pak het verwijderde stuk in met **keukenfolie**. Het is erg belangrijk dat je één stuk folie gebruikt en dat het helemaal rond wordt gewikkeld. Dit is wat de schakelaar sluit en de stroom laat stromen.

![Drie rechthoekige stukjes golfkarton. Op de stukken links en rechts is aluminiumfolie gelijmd. Een extra, kleiner stuk karton zit eronder en heeft een V-vorm die uit één uiteinde is gesneden. De kleinere stukken zijn bedekt met aluminiumfolie.](images/foil-cover.gif)

--- /task ---

--- task ---

**Koppel de Raspberry Pi Pico los van de computer.**

**Verwijder** de twee verbindingsdraden die zijn aangesloten op de **GP18** en **GND** pennen.

Gebruik plakband om ze aan de bovenkant van elke rechthoek te bevestigen.

**Tip:** het is belangrijk dat de pinnen goed contact maken met de keukenfolie. Zorg ervoor dat elke pen plat tegen de folie ligt met het plastic gedeelte van de verbindingsdraad tegen de rand van het karton.

![Een rechthoekig stukje karton is bedekt met folie. Het penuiteinde van een jumperdraad is met plakband aan het bovenste gedeelte bevestigd.](images/pin-sticky-tape-1.jpg)

Voeg meer plakband toe om de jumperdraad vast te zetten en te voorkomen dat deze per ongeluk loskomt.

![Een rechthoekig stukje karton is bedekt met folie. Het penuiteinde van een jumperdraad is met plakband aan het bovenste gedeelte bevestigd. Er is nog een stukje plakband gebruikt om de jumperdraad op zijn plaats vast te zetten.](images/pin-sticky-tape-2.jpg)

--- /task ---

--- task ---

**Test**: Bevestig de verbindingsdraden weer aan **GP18** en **GND** en de Raspberry Pi Pico terug op de computer, en **voer** je code uit.

Sluit en open de schakelaar door de twee ingepakte rechthoeken samen aan te raken. De RGB-LED en -zoemer worden afgespeeld wanneer de schakelaar aan staat.

![Er worden twee foliepads bij elkaar geplaatst om een verbinding te maken. Wanneer de pads worden losgekoppeld, gaan de LED-lampjes branden en klinkt de zoemer.](images/foil-pad-test.gif)

--- /task ---

--- task ---

**Fouten oplossen:**

--- collapse ---

---
title: De popper gaat constant af
---

+ Controleer of de draden goed vastzitten
+ Zorg ervoor dat je vingers de folie niet raken tijdens het testen, omdat je lichaam het circuit kan sluiten en breken en ervoor kan zorgen dat het afgaat
+ Als deze fout blijft optreden, probeer dan de rechthoekige kaarten en foliehoezen opnieuw te maken

--- /collapse ---

--- collapse ---

---
title: De schakelaar activeert de knaller niet
---

+ Controleer of de jumperdraden op de juiste pennen zijn aangesloten
+ Controleer of de aansluitingen tussen de pennen op de jumperdraden en de folie aan beide zijden stevig zijn
+ Sluit en open je schakelaar om ervoor te zorgen dat je de gebeurtenis activeert
+ Zorg ervoor dat de code overeenkomt met het voorbeeld en dat je op **Run** hebt geklikt

--- /collapse ---

--- /task ---

--- task ---

**Koppel de Raspberry Pi Pico los van de computer.**

**Verwijder** de verbindingsdraden van de **GP18** en **GND** pinnen opnieuw zodat je de knaller kunt voltooien.

Voeg lijm toe aan één kant van het stuk karton waarvan je het midden hebt verwijderd en plak het aan de met folie bedekte kant van de linker rechthoek.

Deze laag zal een barrière tussen de twee stukken folie creëren en ruimte laten om je middenstuk binnenin te plaatsen.

![Het middenstuk karton is nu op de linker rechthoek gelijmd.](images/glue-left.jpg)

--- /task ---

--- task ---

Voeg lijm toe aan de andere kant van het stuk karton waaruit je het midden hebt verwijderd en plak het folieoppervlak van je andere rechthoek erop. Zorg ervoor dat de twee stukken folie elkaar **niet** raken. Mogelijk moet je de folie bijsnijden als deze elkaar overlapt.

![Het rechter stuk karton is nu met de bedrukte zijde naar beneden op de linker rechthoek gelijmd.](images/glue-right.jpg)

--- /task ---

--- task ---

**Test**:

- Sluit je Raspberry Pi Pico aan op je computer
- Bevestig de verbindingsdraden weer aan **GP18** en **GND**
- Plaats het middenstuk in het kanon om een verbinding te maken (sluit de schakelaar)
- **Run** je code
- De code moet worden uitgevoerd wanneer je het middenstuk uit het kanon verwijdert

![Er wordt een klein stukje folie uit de knaller-schakelaar getrokken en een LED licht op en er wordt een geluid afgespeeld.](images/full-popper-test.gif)

--- /task ---

--- task ---

**Fouten oplossen**:

--- collapse ---

---
title: De schakelaar activeert de knaller niet
---

+ Controleer of de jumperdraden op de juiste pennen zijn aangesloten
+ Controleer of de aansluitingen tussen de pennen op de jumperdraden en de folie aan beide zijden stevig zijn
+ Druk het middenstuk in je kanon en trek het weer naar buiten om de gebeurtenis te activeren
+ Controleer of de stukjes folie op de buitenste stukjes kaart elkaar niet permanent raken
+ Zorg ervoor dat je op **Run** hebt geklikt

--- /collapse ---

--- /task ---

--- task ---

**Optioneel**: Voeg wat lint, gekleurd katron, touw of iets kleurrijks toe aan het einde van je middenstuk. Dit zal het leuker maken om je feestknaller te laten afgaan!

![De voltooide feestknaller met een stuk regenbooglint.](images/add-ribbon.jpg)

--- /task ---
