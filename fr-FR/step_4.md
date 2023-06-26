## Activer ta bombe de fête

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Tu dois pouvoir activer ta bombe de fête depuis le Raspberry Pi Pico. Dans cette étape, tu prototyperas ton interrupteur à l'aide de fils de liaison. 
</div>
<div>
![Image montrant un projet de bombe de fête avec un interrupteur fabriqué à partir d'une paire de fils de liaison.](images/switch-buzzer-led.jpg){:width="300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
<span style="color: #0faeb0">Des spectacles son et lumière</span> utilisant la technologie sont utilisés dans les célébrations du monde entier. Ces options **durables** et **réutilisables** créent des présentations amusantes et des divertissements interactifs. Aujourd'hui, au lieu d'utiliser des objets jetables comme des pétards en plastique ou des feux d'artifice chimiques, les gens font la fête avec des drones, des lasers et des projections !
</p>

--- task ---

Procurez-vous deux fils de liaison **prise–broche** à utiliser pour ton interrupteur à tirette.

**Connecte** un fil à **GP18** et l'autre à **GND** à côté.

![Un schéma de câblage montrant un fil de liaison attaché à GP18 et un autre fil de liaison connecté à GND.](images/jumper-switch.png)

--- /task ---

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>Il existe deux manières d'exécuter du code en fonction de l'état d'une entrée (comme un interrupteur ou un capteur). La première est d'utiliser une boucle et de continuer à vérifier l'état, c'est ce qu'on appelle <span style="color: #0faeb0">polling</span>. Tu as utilisé le polling dans ton projet luciole LED. La seconde consiste à appeler une fonction lorsqu'une entrée change d'état, en utilisant <span style="color: #0faeb0">events</span> qui détectent les changements lorsqu'ils se produisent. 
</p>

--- task ---

Change ton code pour indiquer à `picozero` d'appeler la fonction `pop` chaque fois que l'interrupteur à tirette est ouvert (déconnecté).

Lorsque tu utilises un événement tel que `when_opened`, la fonction s'exécutera jusqu'à ce qu'elle soit terminée et tu ne pourras pas l'interrompre. C'est ce que tu veux dans ce cas, tu veux que tout l'effet sonore et l'effet de changement de couleur se produisent lorsque la bombe de fête est activée.

**Rappelle-toi** que tu devras également importer `Switch` from `picozero` sur la ligne 1.

--- code ---
---
language: python filename: party_popper.py line_numbers: true line_number_start: 1
line_highlights: 1, 5, 19
---
from picozero import RGBLED, Speaker, Switch from time import sleep

rgb = RGBLED(red=1, green=2, blue=3) # Pin numbers pull = Switch(18) speaker = Speaker(5)

def boum(): print("Boum") # Imprimer sur la console rvb.color = (255, 0, 255) # Violet hautparleur.play(523, 0.1) # 523 = note C4, 0,1 seconde rvb.color = (0, 0, 0) # LED sans couleur – éteinte sleep(0.1) rvb.color = (255, 0, 255) # Violet hautparleur.play(523, 0.6) # Note C4, 0,6 seconde rvb.off()

pull.when_opened = pop # The pop function will be called when the pull switch is opened

--- /code ---

**Astuce :** Assure-toi de **ne pas** ajouter `()` à la fin de `pull.when_opened = pop`. Cette ligne indique à `picozero` que chaque fois que l'événement `when_opened` se produit, la fonction `pop` est appelée.

--- /task ---

--- task ---

**Test**: Exécute ton code pour t'assurer que ta LED RVB s'allume et que le son est émis à chaque fois que l'interrupteur est **ouvert**.

**Déboguer** :

--- collapse ---

---
title: Je vois le message `Switch is not defined`
---

Ajouter `, Switch` à la fin de la ligne 1.

--- /collapse ---

--- collapse ---

---
title: Le code s'exécute avant que j'actionne l'interrupteur
---

+ Vérifie que les câbles de ton interrupteur à tirette sont connectés aux bonnes broches
+ Vérifie que tes câbles d'interrupteur à tirette ont une bonne connexion les uns avec les autres
+ Vérifie que tu as supprimé la ligne `pop()` et l'as remplacée par `pull.when_opened = pop`

--- /collapse ---

--- collapse ---

---
title: Le message "Pop" n'apparaît pas dans la console
---

Vérifie que la console Thonny ne contient pas de messages d'erreur et corrige ton code pour qu'il ressemble exactement à l'exemple.

--- /collapse ---

--- collapse ---

---
title: La LED RVB ou le buzzer a cessé de fonctionner
---

+ Vérifie que les bonnes pattes sont connectées aux bonnes broches
+ Vérifie les connexions mal fixées
+ Vérifie que la LED n'a pas grillé

--- /collapse ---

--- /task ---
