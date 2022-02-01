## Make your switch

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Create a pull switch to activate your party popper.
</div>
<div>
![Image showing a party popper project with a switch made from a pair of jumper wires.](images/image.png){:width="300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
Technology is finding its way into all sorts of celebrations worldwide, creating lots of sustainable and reuable options for all kinds of fun displays and interactive entertainments. Now instead of disposable items like plastic party poppers or chemical fireworks, people are celebrating with drones, lasers and projection shows!
</p>

--- task ---

Get 2 x socket-pin jumper wires to be used for your pull switch. 

**Connect:** Connect one jumper wire to **GP18** and one to the **GND** pin next to it. 

![A wiring diagram showing a jumper wire attached to GP18 and another jumper wire attached to GND.](images/jumper-switch.png)

--- /task ---

In the LED Firefly project you checked `is_closed` in a loop to run different code if your switch was closed or open. Instead of checking in a loop, you can get `picozero` to call a function when a switch is opened or closed using `when_opened` and `when_closed`. 

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>There are two ways that you can run code based on the state of an input such as a Switch. You can use a loop and keeping checking the state of the input to see if it `is_open` or `is_closed`, this is called <span style="color: #0faeb0">polling</span>. Or, you can ask `picozero` to call a function when an input changes state, using <span style="color: #0faeb0">events</span> such as `when_opened` and `when_closed`. Using events can make your code simpler to write and understand and means that input changes can be detected when they happen and won't be missed if you don't poll (check) the input at the right time. 
</p>

--- task ---

Add code to call the `pop` function when the pull switch is opened (disconnected).

--- code ---
---
language: python
filename: main.py 
line_numbers: true
line_number_start: 1
line_highlights: 1, 5, 19
---
from picozero import RGBLED, Speaker, Switch
from time import sleep

rgb = RGBLED(red=1, green=2, blue=3) # pin numbers 
pull = Switch(18)
speaker = Speaker(5)

def pop():
    print("pulled")
    c_note = 523
    rgb.color = (255, 125, 0)
    speaker.play(c_note, 0.1)
    rgb.color = (0, 0, 0)
    sleep(0.1)
    rgb.color = (255, 125, 0)
    speaker.play(c_note, 0.6)
    rgb.off()
        
pull.when_opened = pop # The pop function will be called when the pull switch is opened (disconnected)

--- /code ---

**Tip:** Make sure you **don't** add `()` to the end of `pull.when_opened = pop`. This line tells `picozero` that every time the `when_opened` event happens, the `pop` function is called. 


--- /task ---

--- task ---

Now that you know your code is working, you can go ahead and make the party popper switch! First, you need to gather your materials:

- A pair of scissors
- Corrugated card
- Aluminium foil
- A glue stick

**Optional**:

- A pencil and a ruler (if you want to be more precise with your make)
- Some nice ribbon OR string OR coloured paper/card OR plain paper that you have coloured in

![The image shows a piece of corrugated card, some aluminium foil, a pencil, a ruler, a glue stick, a pair of scissors and a piece of rainbow coloured ribbon.](images/switch-gather-materials.jpeg)

--- /task ---

--- task ---

Cut the **corrugated card** into three rectangles that are the same size. You can decide on the size of your party popper. The example is 3cm x 5cm. 

**Tip**: If you don't have a pencil and a ruler then cut the first one and then use it as a template for the other two. 

![Three pieces of corrugated card cut into equal sized rectangles.](images/three-rectangles.jpg)

**Optional**: You don't have to use a rectangle shape, you could do a circle or a rocket or anything you like! You will need to make sure though that you follow similar steps to make the switch close and open as expected. 

--- /task ---

--- task ---

**Cut** a section out of the centre of one of your rectangles. Keep the piece of card that you have cut out as this will be used later. 

![Three pieces of rectangle corrugated card. The middle piece has the centre removed. The removed piece is placed next to it.](images/centre-cut.jpg)

--- /task ---

--- task ---

Take the **aluminium foil** and cut it to the same size as the un-cut rectangles. 

Next, **glue** the foil to the rectangles.

![Three pieces of rectangle corrugated card. The pieces to the left and right have aluminium foil glued onto them.](images/add-foil.jpg)

--- /task ---

--- task ---

Now take the piece of card that you removed from the centre rectangle and cut a V shape out of the top to make it easier to place it inside your popper.

Next, **trim** the sides by a few millimetres to make sure that it will easily fit into your popper.

![Three pieces of rectangle corrugated card. The pieces to the left and right have aluminium foil glued onto them. An additional, smaller piece of card is underneath and has a V shape cut out of one end.](images/trim-piece.jpg)

--- /task ---

--- task ---

Now, cover the removed piece in **aluminium foil**. It is very important that you use a continuous piece of foil and that it goes all the way around. This is what will make the switch close and allow the current to flow.

![Three pieces of rectangle corrugated card. The pieces to the left and right have aluminium foil glued onto them. An additional, smaller piece of card is underneath and has a V shape cut out of one end. The smaller pieces has been covered with alumium foil.](images/foil-cover.gif)

--- /task ---


--- save ---


