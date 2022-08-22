## Faire du bruit

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Une bombe de fête fait aussi du bruit ! Dans cette étape, tu vas connecter un buzzer **passif** à ton Raspberry Pi Pico et le coder pour qu'il émette un son lorsque ta bombe est tirée. 
</div>
<div>
![Image montrant un buzzer piézo passif connecté à un Raspberry Pi Pico.](images/rgb-buzzer.gif){:width="300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
Il existe deux principaux types de buzzer, un buzzer **actif** et un buzzer **passif**. Un buzzer **actif** joue toujours la même tonalité. Un buzzer **passif** peut jouer une variété de tonalités. Il nécessite une connexion à établir et un signal spécifique pour jouer la tonalité choisie. 
</p>

[[[buzzers-speakers]]]

--- task ---

Note que ton buzzer a une patte longue et une patte courte. Comme pour les LED, la patte longue est la patte positive (+) et la patte courte est la patte de masse (-). Si tes pattes de buzzer sont assez similaires en hauteur, jette un coup d'œil en haut du buzzer et trouve le symbole (+).

![Un buzzer passif noir à deux pattes. L'une est légèrement plus courte indiquant qu'il s'agit de la patte négative.](images/buzzer.png){:width="300px"}

--- /task ---

--- task ---

**Connecte** le buzzer à ton Raspberry Pi Pico à l'aide de deux fils de liaison **prise–prise**. Connecte la patte longue à **GP5**et la patte courte à la broche **GND** (masse) à proximité.

![Un schéma de câblage montrant une LED RVB attachée à côté d'un buzzer passif attaché au GP5 et aux broches de masse.](images/rgb-led-buzzer-diagram.png)

--- /task ---

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
Les humains peuvent entendre des sons dans la plage de 20 Hz (très bas) à 20 000 Hz (très élevé). Les enfants et les jeunes peuvent entendre des sons plus aigus que les personnes âgées. Les notes de musique correspondent à des **fréquences** sonores spécifiques ; par exemple, le Do médian (C4) est d'environ 262 Hz. Hz, abréviation de Hertz, est le nombre de vibrations par seconde. Envoyer le bon signal à un buzzer le fera vibrer à une fréquence particulière, que tu entendras comme une note de musique. </p>

--- task ---

**Test :** Mets à jour ton script `bombe_fete.py` pour correspondre à ce qui suit, puis exécute ton code pour tester le buzzer. **Rappelle-toi** d'importer également `Speaker` sur la **ligne 1**.

--- code ---
---
language: python
filename: bombe_fete.py
line_numbers: true
line_number_start: 1
line_highlights: 1, 5, 10
---
from picozero import RGBLED, Speaker
from time import sleep

rvb = RGBLED(rouge=1, vert=2, bleu=3) # Numéros des broches 
hautparleur = Speaker(5)

def boum():
    print("Boum") # Imprimer sur la console
    rvb.color = (255, 0, 255) # Violet
    hautparleur.play(262, 1) # 262 = note C4, pendant 1 seconde
    rvb.off()

boum()
--- /code ---

--- /task ---

Ta bombe de fête a de la lumière et du son. Ensuite, crée une combinaison intéressante de lumières et de sons qui s'activeront lorsque ta bombe de fête sera déclenchée. Dans cet exemple, nous créons un son « Ta-da ! » de célébration et avec une LED violette clignotant au rythme de l'effet.

--- task ---

Modifie ton script `bombe_fete.py` pour qu'il corresponde à ce qui suit :

--- code ---
---
language: python
filename: bombe_fete.py
line_numbers: true
line_number_start: 1
line_highlights:  10-15
---
from picozero import RGBLED, Speaker
from time import sleep

rvb = RGBLED(rouge=1, vert=2, bleu=3) # Numéros des broches
hautparleur = Speaker(5)

def boum():
    print("Boum") # Imprimer sur la console
    rvb.color = (255, 0, 255) # Violet
    hautparleur.play(262, 0.1) # 262 = note C4, 0,1 seconde
    rvb.color = (0, 0, 0) # LED sans couleur – éteinte
    sleep(0.1)
    rvb.color = (255, 0, 255) # Violet
    hautparleur.play(262, 0.6) # Note C4, 0,6 seconde
    rvb.off()

boum()

--- /code ---

--- /task ---

--- task ---

**Test :** Exécute ton code pour voir si l'effet sonore joue le « Ta-da ! » et ta LED clignote à temps.

![Image montrant un buzzer piezo passif connecté à un Raspberry Pi Pico.](images/rgb-buzzer.gif){:width="300px"}

--- /task ---

--- task ---

**Déboguer :**

--- collapse ---

---
title: je vois le message `Speaker is not defined`
---

Ajoute `, Speaker` à la fin de la ligne 1.

--- /collapse ---

--- collapse ---

---
title: Le message "Pop" n'apparaît pas dans la console
---

Vérifie que la console Thonny ne contient pas de messages d'erreur et corrige ton code pour qu'il ressemble exactement à l'exemple.

--- /collapse ---

--- collapse ---

---
title: La LED RVB ne s'allume pas
---

Si la LED RVB ne s'allume pas :
+ Vérifie que les fils de liaison sont connectés aux bonnes broches
+ Vérifie les connexions mal fixées
+ Vérifie que la LED n'a pas grillé

--- /collapse ---

--- collapse ---

---
title: Le buzzer ne fait pas de bruit
---

Si le buzzer ne fait pas de bruit :
+ Vérifie que les bonnes pattes sont connectées aux bonnes broches
+ Vérifie les connexions mal fixées
+ Vérifie que tu joues sur une fréquence que tu peux entendre : les valeurs doivent être comprises entre 15 et 15 000
+ Vérifie que tu utilises un buzzer **passif**

--- /collapse ---

--- /task ---
