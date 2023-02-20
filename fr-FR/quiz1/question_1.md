## Réflexion

Bien joué. Tu as créé un dispositif de bombe de fête électronique réutilisable que tu peux utiliser lorsque tu veux célébrer quelque chose. Il est maintenant temps de réfléchir à ce que tu as appris pour t'aider à t'en souvenir.

Réponds aux trois questions ci-dessous.

Tu seras guidé vers la bonne réponse. Tu peux faire cette activité autant de fois que tu le souhaites.

Amuse-toi bien !

--- question ---

---
legend: Question 1 sur 3
---

Dans le projet bombe de fête, tu as programmé une LED RVB pour afficher la couleur violette en mélangeant le rouge et le bleu :

--- code ---
---
language: python
filename: party_popper.py
line_numbers: true
line_number_start: 1
line_highlights: 3
---
from picozero import RGBLED

rgb = RGBLED(red=1, green=2, blue=3) # Numéros des broches 

rgb.color = (255, 0, 255) # Violet

--- /code ---

Quel schéma montre les broches câblées correctement pour que ce code fonctionne :

--- choices ---

- (x) ![Un schéma d'une LED RVB avec des résistances connectées aux broches GP1, GND, GP2 et GP3.](images/rgb-led-quiz.png)

  --- feedback ---

Oui. Il est vraiment important que les fils de liaison connectés aux pattes de la LED soient connectés aux broches indiquées utilisées pour ta `RGBLED`. Dans ce cas, rouge à la broche GP1, masse (négatif) à GND, vert à la broche GP2 et bleu à la broche GP3.

  --- /feedback ---

- ( ) ![Un schéma d'une LED RVB avec des résistances connectées à GP0, GP1, GND et GP2.](images/rgb-reverse.png)

  --- feedback ---

Réessaie, la LED n'est pas connectée aux broches utilisées dans le code, donc le réglage des couleurs ne fonctionnera pas correctement.

  --- /feedback ---

--- /choices ---

--- /question ---
