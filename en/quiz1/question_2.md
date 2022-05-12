
--- question ---
---
legend: Question 2 of 3
---

You are helping someone with a project. 

They are trying to play a sound on a buzzer that is correctly connected to pin GP5 and GND on their Raspberry Pi Pico. 

This is their code:

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

speaker = Speaker(5)

def play_sound():
    speaker.pitch(523, 1) # 523 = note C4, 1 second
    sleep(0.1)

play_sound()

--- /code ---

Thonny gives the error: "**NameError: name 'Speaker' isn't defined**".

Which line of code should they edit to fix the problem?

--- choices ---

- (x) Line 1

  --- feedback ---
  
Correct! Line 1 needs to have `, Speaker` added to the end of it so that `Speaker` is imported from `picozero`.
  
  --- /feedback ---

- ( ) Line 4

  --- feedback ---
  
Try again. It's a good idea to check that the correct pin is used but in this case, that is right. 
  
  --- /feedback ---

- ( ) Line 7

  --- feedback ---
  
Try again. `speaker.pitch(523, 1)` will play a note for 1 second. There is something missing on a different line. 
  
  --- /feedback ---

- ( ) Line 11

  --- feedback ---
  
Try again. Calling the `play_sound()` function with open and close brackets is needed to play the sound. 
  
  --- /feedback ---
  
--- /choices ---

--- /question ---
