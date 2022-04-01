## Make your switch

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Make a switch to activate your party popper using corrugated card, glue, and kitchen foil.
</div>
<div>
![Image showing a cardboard contact switch in the style of a pin and socket connection.](images/add-ribbon.jpg){:width="300px"}
</div>
</div>

--- task ---

Now that you know your code works, you need to make the switch that will set off your party popper! 

Gather your materials:

- A pair of scissors
- Corrugated card
- Kitchen foil
- A glue stick
- Some sticky tape

**Optional**:

- A pencil and a ruler (if you want to be more precise with your make)
- Some ribbon, string, coloured paper/card, or plain paper that you have coloured in

![A piece of corrugated card, some foil, a pencil, a ruler, a glue stick, a pair of scissors, and a piece of rainbow-coloured ribbon.](images/switch-gather-materials.jpeg)

--- /task ---

--- task ---

Cut the **corrugated card** into three rectangles that are the same size. You can decide on the size of your party popper. The example is 3cm × 5cm. 

**Tip**: If you don't have a pencil and a ruler, then cut the first one and use it as a template for the other two. 

![Three pieces of corrugated card cut into equal-sized rectangles.](images/three-rectangles.jpg)

--- /task ---

--- task ---

Cut a section out of the centre of one of your rectangles. Keep the piece of card that you have cut out as this will be used later. 

![Three rectanglar pieces of corrugated card. The middle piece has had a centre strip removed so that it forms an n shape. The removed piece is placed next to it.](images/centre-cut.jpg)

--- /task ---

--- task ---

Take the **kitchen foil** and cut it to the same size as the un-cut rectangles.

**Glue** the cardboard and attach the foil. 

**Tip:** Make sure you don't get too much glue on the outside of the foil as it will affect the contacts of the switch. 

![Three rectanglar pieces of corrugated card. The pieces to the left and right have foil glued onto them.](images/add-foil.jpg)

--- /task ---

--- task ---

Take the piece of card that you removed from the centre rectangle and cut the top into a V shape or a point to make it easier to place it inside your popper.

**Trim** the sides by a few millimetres to make sure that it will easily fit into your popper.

![Three rectanglar pieces of corrugated card. The pieces to the left and right have foil glued onto them. An additional, smaller piece of card is underneath and has a V shape cut at one end to form a point.](images/trim-piece.jpg)

--- /task ---

--- task ---

Cover the removed piece in **kitchen foil**. It is very important that you use one piece of foil and that it wraps all the way around. This is what will make the switch close and allow the current to flow.

![Three rectanglar pieces of corrugated card. The pieces to the left and right have aluminium foil glued onto them. An additional, smaller piece of card is underneath and has a V shape cut out of one end. The smaller pieces has been covered with aluminum foil.](images/foil-cover.gif)

--- /task ---

--- task ---

**Disconnect your Raspberry Pi Pico from your computer.**

**Remove** the two jumper wires attached to the **GP18** and **GND** pins. 

Use some sticky tape to secure them to the top of each rectangle. 

**Tip:** It is important that the pins make a secure contact with the kitchen foil. Make sure that each pin is lying flat against the foil with the plastic part of the jumper wire against the edge of the cardboard. 

![A rectanglar piece of card is covered with foil. The pin end of a jumper wire has been stuck to the top section with sticky tape.](images/pin-sticky-tape-1.jpg)

Add more tape to secure the jumper wire and stop it from accidentally coming loose.

![A rectanglar piece of card is covered with foil. The pin end of a jumper wire has been stuck to the top section with sticky tape. A further piece of sticky tape has been used to secure the jumper wire in place.](images/pin-sticky-tape-2.jpg)

--- /task ---

--- task ---

**Test**: Reattach your jumper wires to **GP18** and **GND** and your Raspberry Pi Pico back to your computer, then **run** your code. 

Close and open the switch by touching the two foiled rectangles together, foil to foil. The RGB LED and buzzer will play when the switch is open. 

![Two foil pads are placed together to make a connection. When the pads are disconnected, the LED lights and the buzzer sounds.](images/foil-pad-test.gif)

--- /task ---

--- task ---

**Debug:** 

--- collapse ---

---
title: The popper is constantly going off
---

+ Check that your wires are really secure
+ Make sure that your fingers aren't touching the foil during testing as your body can complete and break the circuit and cause it to go off
+ If this error keeps happening, try remaking the rectangle cards and foil covers 

--- /collapse ---

--- collapse ---

---
title: The switch doesn't activate the popper
---

+ Check that the jumper wires are attached to the correct pins
+ Check the connections between the pins on the jumper wires and the foil are solid on both sides
+ Close and open your switch to make sure you are triggering the event
+ Make sure your code matches the example and that you have clicked **Run**

--- /collapse ---

--- /task ---

--- task ---

**Disconnect your Raspberry Pi Pico from your computer.**

**Remove** the jumper wires from the **GP18** and **GND** pins again so that you can complete your popper.

Add glue to one side of the piece of cardboard you removed the middle from and stick it to the foil-covered side of the left rectangle. 

This layer will create a barrier between the two pieces of foil and allow space for your centre piece to be placed inside. 

![The middle piece of cardboard has now been glued onto the left rectangle.](images/glue-left.jpg)

--- /task ---

--- task ---

Add glue to the other side of the piece of cardboard you removed the middle from, and stick the foil face of your other rectangle on top. Make sure that the two pieces of foil **are not** touching. You may need to trim your foil if it is overlapping.

![The right-hand piece of cardboard has now been glued onto the left rectangle, face down.](images/glue-right.jpg)

--- /task ---

--- task ---

**Test**: 

- Connect your Raspberry Pi Pico to your computer
- Reattach your jumper wires  to **GP18** and **GND**
- Place the centre piece inside the popper to form a connection (close the switch)
- **Run** your code
- The code should run when you remove the centre piece from the popper

![A small piece of foil is pulled out of the popper switch and an LED lights up and a sound plays.](images/full-popper-test.gif)

--- /task ---

--- task ---

**Debug**:

--- collapse ---

---
title: The switch doesn't activate the popper
---

+ Check that the jumper wires are attached to the correct pins
+ Check the connections between the pins on the jumper wires and the foil are solid on both sides
+ Push the middle piece inside your popper and pull it out again to trigger the event
+ Check the bits of foil on the outer pieces of card aren't permanently touching
+ Make sure that you have clicked **Run**

--- /collapse ---

--- /task ---

--- task ---

**Optional**: Add some ribbon, coloured card, string, or anything colourful to the end of your centre piece. This will make it more fun to pull your party popper!

![The completed party popper with a piece of rainbow ribbon attached.](images/add-ribbon.jpg)

--- /task ---
