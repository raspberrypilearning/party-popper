
--- question ---
---
legend: Question 2 sur 3
---

Tu aides quelqu'un avec un projet.

Ils essaient de jouer un son sur un buzzer correctement connecté aux broches GP5 et GND de leur Raspberry Pi Pico.

Voici leur code :

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

hautparleur = Speaker(5)

def jouer_son():
    hautparleur.pitch(523, 1) # 523 = note C4, 1 seconde
    sleep(0.1)

jouer_son()

--- /code ---

Thonny donne l'erreur : "**NameError : name 'Speaker' isn't defined**".

Quelle ligne de code doivent-ils modifier pour résoudre le problème ?

--- choices ---

- (x) Ligne 1

  --- feedback ---

Correct ! La ligne 1 doit avoir `, Speaker` ajouté à la fin de sorte que `Speaker` soit importé de `picozero`.

  --- /feedback ---

- ( ) Ligne 4

  --- feedback ---

Réessaie. C'est une bonne idée de vérifier que la bonne broche est utilisée, mais dans ce cas, c'est bon.

  --- /feedback ---

- ( ) Ligne 7

  --- feedback ---

Réessaie. `hautparleur.pitch(523, 1)` jouera une note pendant 1 seconde. Il manque quelque chose sur une autre ligne.

  --- /feedback ---

- ( ) Ligne 11

  --- feedback ---

Réessaie. L'appel de la fonction `jouer_son()` avec des parenthèses ouvrantes et fermantes est nécessaire pour jouer le son.

  --- /feedback ---

--- /choices ---

--- /question ---
