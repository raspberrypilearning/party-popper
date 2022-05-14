## Introduction

اصنع مفرقعات حفلة قابل لإعادة الاستخدام يكافئك بعرض ضوئي وصوتي عند سحبه.

In the [LED firefly project](https://projects.raspberrypi.org/en/projects/led-firefly){:target="_blank"}, you used a single-colour LED. بالنسبة لحفلتك، ستستخدم نوعًا مختلفًا من الاضوية LED، يسمى RGB LED الذي يمكنه عرض ألوان متعددة.

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 10px;">
<div style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px; display:flex; margin-bottom: 27px;"><p><span style="color: #0faeb0">مفرقعات الحفلة</span> مشهورة تستخدم للاحتفال بالمناسبات الخاصة في جميع أنحاء العالم. They usually have a piece of string that can be pulled to make a loud sound and release some confetti into the air. إذا لم تكن قد رأيت واحدة من قبل ، فقد تتعرف على الرموز التعبيرية لمفرقعات الحفلة!</p>
</div>
<div>
! [الرمز التعبيري لمفرقعات الحفلة.] (images / party-popper.png) {: width = "300px"}
</div>
</div>
</div>

You will:

+ Code an **RGB LED** to light in different colours and fade out
+ Create a sound effect on a buzzer
+ Make a contact switch out of card, foil, and string

To complete this project you will need:

**Hardware:**

You can purchase all the required hardware for this project and the other projects in this path from the [Pimoroni web store.](https://shop.pimoroni.com/products/pico-intro-kit?variant=39893512945747){:target='_blank'}

+ A Raspberry Pi Pico with pin headers soldered on
+ A **data** USB A to micro USB cable
+ A **passive** buzzer
+ 3× 100Ω resistors (any resistor from 75Ω to 220Ω will work)
+ 1× common cathode RGB LED
+ 6× socket–socket jumper wires
+ 2× socket–pin jumper wires
+ Craft items such as corrugated card, kitchen foil, string, ribbon, coloured paper, and sticky tape or duct tape

**Software:**
+ Thonny – this project can be completed using the Thonny Python editor, which can be installed on a Linux, Windows, or Mac computer.

[[[thonny-install]]]

[[[change-theme-thonny]]]


--- no-print --- --- task ---

**شاهد**: يُظهر هذا المثال مفرقعات الحفلة الذي يقوم بتشغيل عرض ضوئي ملون مع بعض الأصوات.

![يتم سحب قطعة صغيرة من الرقائق المعدنية من مفتاح المفرقعات ويضيء مؤشر LED ويتم تشغيل الصوت.](images/full-popper-test.gif)

--- /task --- --- /no-print ---

--- print-only ---

![مفرقعات الحفلة مصنوعة من الورق المقوى مع ذيل الشريط.](images/add-ribbon.jpg)

--- /print-only ---
