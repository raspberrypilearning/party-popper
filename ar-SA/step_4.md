## قم بتنشيط مفرقعات الحفلة

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
يجب أن تكون قادرًا على تنشيط مفرقعات الحفلة من Raspberry Pi Pico. في هذه الخطوة ، ستقوم بعمل نموذج أولي لمفتاحك باستخدام أسلاك التوصيل. 
</div>
<div>
! [صورة تظهر مشروع مفرقعات للحفلة بمفتاح مصنوع من زوج من الأسلاك.] (images / switch-buzzer-led.jpg) {: width = "300px"}
</div>
</div>

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>
<span style="color: #0faeb0">عروض ضوئية وصوتية</span> تستخدم التكنولوجيا في الاحتفالات في جميع أنحاء العالم. تعمل هذه الخيارات ** المستدامة ** و ** القابلة لإعادة الاستخدام ** على إنشاء عروض ممتعة ووسائل ترفيه تفاعلية. الآن ، بدلاً من العناصر التي يمكن التخلص منها مثل المفرقعات البلاستيكية أو الألعاب النارية الكيميائية، يحتفل الناس بالطائرات بدون طيار والليزر وعروض الإسقاط!
</p>

--- task ---

احصل على **سلك توصيل ثنائي المقبس - دبوس** لاستخدامه في مفتاح السحب.

**قم بتوصيل** سلك توصيل واحد بـ **GP18** وواحد إلى **دبوس GND** المجاور له.

![A wiring diagram showing a jumper wire attached to GP18 and another jumper wire attached to GND.](images/jumper-switch.png)

--- /task ---

<p style='border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;'>هناك طريقتان يمكنك من خلالهما تشغيل التعليمات البرمجية بناءً على حالة الإدخال (مثل مفتاح أو جهاز استشعار). الأول هو استخدام حلقة ومواصلة التحقق من الحالة ، وهذا ما يسمى <span style="color: #0faeb0">الاقتراع</span>. لقد استخدمت الاقتراع في مشروع LED اليراع. والثاني هو استدعاء دالة عندما تتغير حالة الإدخال ، باستخدام <span style="color: #0faeb0">أحداث</span> التي تكتشف التغييرات عند حدوثها. 
</p>

--- task ---

قم بتغيير الكود الخاص بك لإخبار `picozero` باستدعاء وظيفة `pop` كلما تم فتح مفتاح السحب (غير متصل).

عند استخدام حدث مثل `when_opened`، ستعمل الوظيفة حتى تكتمل ولن تتمكن من مقاطعتها. هذا ما تريده في هذه الحالة ، فأنت تريد أن يحدث تأثير الصوت بالكامل وتأثير تغيير اللون عند تنشيط مفرقعات الحفلة.

**تذكر** أنك ستحتاج أيضًا إلى استيراد `Switch` من `picozero` على السطر 1.

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
