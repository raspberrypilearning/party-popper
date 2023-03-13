## Quick quiz

Answer the three questions. There are hints to guide you to the correct answer.

When you have answered each question, click on **Check my answer**.

Have fun!

--- question ---

---
legend: Question 1 sur 3
---

In the party popper project you programmed an RGB LED to show the colour purple by mixing red and blue:

--- code ---
---
language: python filename: party_popper.py line_numbers: true line_number_start: 1
line_highlights: 3
---
from picozero import RGBLED

rgb = RGBLED(red=1, green=2, blue=3) # Pin numbers

rgb.color = (255, 0, 255) # Purple

--- /code ---

Which diagram shows the pins wired correctly for this code to work:

--- choices ---

- (x) ![Un schéma d'une LED RVB avec des résistances connectées aux broches GP1, GND, GP2 et GP3.](images/rgb-led-quiz.png)

  --- feedback ---

Yes. It's really important that the jumper wires connected to the LED legs are connected to the stated pins used for your `RGBLED`. In this case, red to pin GP1, ground (negative) to GND, green to pin GP2, and blue to pin GP3.

  --- /feedback ---

- ( ) ![Un schéma d'une LED RVB avec des résistances connectées à GP0, GP1, GND et GP2.](images/rgb-reverse.png)

  --- feedback ---

Try again, the LED is not connected to the pins that are used in the code so setting the colours will not work correctly.

  --- /feedback ---

--- /choices ---

--- /question ---
