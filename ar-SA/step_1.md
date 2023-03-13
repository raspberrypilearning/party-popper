## You will make

اصنع مفرقعات حفلة قابل لإعادة الاستخدام يكافئك بعرض ضوئي وصوتي عند سحبه.

في مشروع [LED اليراعة المضيئة](https://projects.raspberrypi.org/en/projects/led-firefly){: target = "_ blank"} ، استخدمت مصباح LED أحادي اللون. بالنسبة لحفلتك، ستستخدم نوعًا مختلفًا من الاضوية LED، يسمى RGB LED الذي يمكنه عرض ألوان متعددة.

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 10px;">
<div style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px; display:flex; margin-bottom: 27px;"><p><span style="color: #0faeb0">مفرقعات الحفلة</span> مشهورة تستخدم للاحتفال بالمناسبات الخاصة في جميع أنحاء العالم. عادة ما يكون لديهم قطعة من الخيط يمكن سحبها لإصدار صوت مرتفع وإطلاق بعض القصاصات في الهواء. إذا لم تكن قد رأيت واحدة من قبل ، فقد تتعرف على الرموز التعبيرية لمفرقعات الحفلة!</p>
</div>
<div>
! [الرمز التعبيري لمفرقعات الحفلة.] (images / party-popper.png) {: width = "300px"}
</div>
</div>
</div>

سوف تفعلها:

+ قم ببرمجة **RGB LED** للإضاءة بألوان مختلفة وتتلاشى
+ قم بإنشاء تأثير صوتي على الجرس
+ قم بصنع مفتاح تشغيل من البطاقة والرقائق المعدنية والسلسلة

لإكمال هذا المشروع: ستحتاج إلى:

**الأجهزة:**

يمكنك شراء جميع الأجهزة المطلوبة لهذا المشروع والمشاريع الأخرى في هذا المسار من [متجر Pimoroni. ](https://shop.pimoroni.com/products/pico-intro-kit?variant=39893512945747){:target='_blank'}

إذا كان لديك Raspberry Pi Pico بالفعل ، يمكنك شراء المكونات الإلكترونية التي تحتاجها لهذا المشروع والمشاريع الأخرى في المسار من [متجر الويب Kitronik.](https://kitronik.co.uk/products/5343-raspberry-pi-foundation-pico-pathway-pack)

+ Raspberry Pi Pico مع رؤوس دبوس ملحومة
+ وصلة تحويل سلك USB الى سلك USB مصغر
+ جرس **سلبي**
+ مقاومات 3 × 100 أوم (أي مقاوم من 75 درجة إلى 220 درجة سيعمل)
+ 1 × الكاثود RGB LED
+ 6 × مأخذ توصيل الأسلاك
+ 2 × المقبس - دبوس الأسلاك الطائر
+ العناصر الحرفية مثل البطاقات المموجة ، ورقائق المطبخ ، والخيط ، والشريط ، والورق الملون ، والشريط اللاصق أو الشريط اللاصق

**Software:**
+ Thonny - يمكن إكمال هذا المشروع باستخدام محرر Thonny Python ، والذي يمكن تثبيته على كمبيوتر Linux أو Windows أو Mac.

[[[thonny-install]]]

[[[change-theme-thonny]]]


--- no-print --- --- task ---

**شاهد**: يُظهر هذا المثال مفرقعات الحفلة الذي يقوم بتشغيل عرض ضوئي ملون مع بعض الأصوات.

![يتم سحب قطعة صغيرة من الرقائق المعدنية من مفتاح المفرقعة ويضيء مؤشر مصباح LED ويتم تشغيل الصوت.](images/full-popper-test.gif)

--- /task --- --- /no-print ---

--- print-only ---

![مفرقعات الحفلة مصنوعة من الورق المقوى مع ذيل الشريط.](images/add-ribbon.jpg)

--- /print-only ---
