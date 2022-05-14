## قم بتنشيط مفرقعات الحفلة

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
يجب أن تكون قادرًا على تنشيط مفرقعات الحفلة من Raspberry Pi Pico. In this step, you will prototype your switch using jumper wires. 
</div>
<div>
! [صورة تظهر مشروع مفرقعات للحفلة بمفتاح مصنوع من زوج من الأسلاك.] (images / switch-buzzer-led.jpg) {: width = "300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
<span style="color: #0faeb0">Light and sound shows</span> using technology are being used in celebrations worldwide. These **sustainable** and **reusable** options create fun displays and interactive entertainments. الآن ، بدلاً من العناصر التي يمكن التخلص منها مثل المفرقعات البلاستيكية أو الألعاب النارية الكيميائية، يحتفل الناس بالطائرات بدون طيار والليزر وعروض الإسقاط!
</p>

--- task ---

Get **two socket–pin** jumper wires to be used for your pull switch.

**Connect** one jumper wire to **GP18** and one to the **GND** pin next to it.

![A wiring diagram showing a jumper wire attached to GP18 and another jumper wire attached to GND.](images/jumper-switch.png)

--- /task ---

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>There are two ways that you can run code based on the state of an input (like a switch or sensor). The first is to use a loop and keep checking the state, this is called <span style="color: #0faeb0">polling</span>. You used polling in your LED firefly project. The second is to call a function when an input changes state, using <span style="color: #0faeb0">events</span> that detect changes when they happen. 
</p>

--- task ---

Change your code to tell `picozero` to call the `pop` function whenever the pull switch is opened (disconnected).

When you use an event such as `when_opened`, the function will run until it is completed and you won't be able to interrupt it. هذا ما تريده في هذه الحالة ، فأنت تريد أن يحدث تأثير الصوت بالكامل وتأثير تغيير اللون عند تنشيط مفرقعات الحفلة.

**Remember** that you will also need to import `Switch` from `picozero` on line 1.

--- code ---
---
language: python filename: party_popper.py line_numbers: true line_number_start: 1
line_highlights: 1, 5, 19
---
from picozero import RGBLED, Speaker, Switch from time import sleep

rgb = RGBLED(red=1, green=2, blue=3) # Pin numbers pull = Switch(18) speaker = Speaker(5)

def pop(): print("Pop") # Print to the shell rgb.color = (255, 0, 255) # Purple speaker.play(523, 0.1) # 523 = note C4, 0.1 seconds rgb.color = (0, 0, 0) # LED no colour – off sleep(0.1) rgb.color = (255, 0, 255) # Purple speaker.play(523, 0.6) # Note C4, 0.6 seconds rgb.off()

pull.when_opened = pop # The pop function will be called when the pull switch is opened

--- /code ---

**Tip:** Make sure you **don't** add `()` to the end of `pull.when_opened = pop`. This line tells `picozero` that every time the `when_opened` event happens, the `pop` function is called.

--- /task ---

--- task ---

**Test**: Run your code to make sure your RGB LED lights and the sound plays each time that the switch is **opened**.

**Debug**:

--- collapse ---

---
title: I see the message `Switch is not defined`
---

Add `, Switch` to the end of line 1.

--- /collapse ---

--- collapse ---

---
title: The code runs before I pull the switch
---

+ Check to make sure your pull switch cables are connected to the correct pins
+ Check to make sure your pull switch cables have a good connection with each other
+ Check that you have removed the `pop()` line and replaced it with `pull.when_opened = pop`

--- /collapse ---

--- collapse ---

---
title: The "Pop" message doesn't appear in the shell
---

Check the Thonny console for any error messages and fix your code so it looks exactly like the example.

--- /collapse ---

--- collapse ---

---
title: The RGB LED or buzzer has stopped working
---

+ Check that the correct legs are connected to the correct pins
+ Check for any loose connections
+ Check the LED has not blown

--- /collapse ---

--- /task ---
