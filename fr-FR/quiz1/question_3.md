
--- question ---
---
legend: Question 3 sur 3
---

Tu as utilisé un événement `when_opened` pour exécuter du code chaque fois que ta bombe de fête a été tirée.

Quelle ligne de code configure correctement l'événement afin que la fonction `pop` soit appelée à chaque fois que la connexion est ouverte.

--- choices ---

- (x) `pull.when_opened = pop`

  --- feedback ---

Correct ! Lors de l'utilisation d'événements, nous n'utilisons pas les parenthèses `()` car la fonction ne doit être appelée que lorsque l'événement se produit. Ajouter `()` à la fin appellera la fonction **une fois** ; dès que la ligne de code est exécutée.

  --- /feedback ---

- ( ) `pull.when_opened = pop()`

  --- feedback ---

Non, mais c'est une erreur très courante ! Ce code appellera la fonction `pop` **une fois** lorsque cette ligne de code s'exécutera. Au lieu de cela, tu dois indiquer à `pico_zero` quelle fonction exécuter lorsque l'événement se produit et `pico_zero` appellera la fonction pour toi **chaque fois** que l'événement se produit.

  --- /feedback ---

--- /choices ---

--- /question ---
