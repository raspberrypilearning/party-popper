## Make a noise

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
A party popper also makes a noise! Connect a speaker to play a sound when activated. 
</div>
<div>
Image, gif or video showing what they will achieve by the end of the step. ![](images/image.png){:width="300px"}
</div>
</div>

--- task ---

Another step of tasks to complete.

--- /task ---

--- code ---
---
language: python
filename: partypopper.py
line_numbers: true
line_number_start: 1
line_highlights: 
---

from picozero import *
from time import sleep

pico_led.on()
sleep(1)
pico_led.off()

speaker = Speaker(5)
rgb = RGBLED(red=2, green=1, blue=0)
pull = Button(18)

def tada():
    print("pulled")
    c_note = 523
    rgb.color = (250,125,0)
    speaker.play(c_note, 0.1)
    rgb.color = (0,0,0)
    sleep(0.1)
    rgb.color = (250,125,0)
    speaker.play(c_note, 0.4)
    for i in range(100, 0, -1):
        speaker.play(c_note, 0.01, i/100)
    rgb.off()
        
pull.when_released = tada



--- /code ---
--- task ---

Step content... 
Can use:
**Test:**
**Choose:**
**Tip:**

--- /task ---

--- save ---