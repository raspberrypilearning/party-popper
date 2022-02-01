## Reflection

Well done, you have learned a lot! Now it's time to reflect - reflecting is an important part of learning because it helps make new connections in your brain.

Answer the three questions below to reflect on what you've learned.

After each question, press submit. You will be guided towards the correct answer. You can do this activity as many times as you want to.

Have fun!

--- question ---

---
legend: Question 1 of 3
---

In the party popper project you programmed an RGB LED to show the colour purple by mixing red and blue:

--- code ---
---
language: python
filename: partypopper.py
line_numbers: true
line_number_start: 1
line_highlights: 3
---
from picozero import RGBLED

rgb = RGBLED(red=1, green=2, blue=3) # pin numbers 

rgb.color = (255, 0, 255) # purple

--- /code ---

Which diagram shows the pins wired correctly for this code to work:

--- choices ---

- (x) [correctly wired]

  --- feedback ---

Yes. It's really important that the jumper wires connected to the LED legs are connected to the stated pins used for your `RGBLED`. In this case, red to pin GP1, ground (negative) to ground, green to pin GP2 and blue to pin GP3. 

  --- /feedback ---

- ( ) [jumpers in reverse order]

  --- feedback ---

Try again, the jumper wires in this diagram have been placed in the reverse order. 

  --- /feedback ---

--- /choices ---

--- /question ---
