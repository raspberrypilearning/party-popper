
--- question ---
---
legend: السؤال 2 من 3
---

أنت تساعد شخصًا ما في مشروع.

إنهم يحاولون تشغيل صوت على جرس متصل بشكل صحيح بدبوس GP5 و GND على Raspberry Pi Pico.

هذه هي التعليمات البرمجية الخاصة بهم:

--- code ---
---
language: python filename: sound.py line_numbers: true line_number_start: 1
line_highlights:
---
from picozero import RGBLED from time import sleep

speaker = Speaker(5)

def play_sound(): speaker.play(523, 1) # 523 = note C4, 1 second sleep(0.1)

play_sound()

--- /code ---

يعطي Thonny الخطأ:"**NameError: name 'Speaker' isn't defined**".

أي سطر من التعليمات البرمجية يجب عليهم تعديله لإصلاح المشكلة؟

--- choices ---

- (×) السطر 1

  --- feedback ---

صحيح! يجب أن يحتوي السطر 1 على `, speaker` مضافاً إلى نهايته بحيث يتم استيراد `, speaker` من `picozero`.

  --- /feedback ---

- (×) السطر 4

  --- feedback ---

حاول مرة أخرى. من الجيد التحقق من استخدام الدبوس الصحيح ولكن في هذه الحالة ، هذا صحيح.

  --- /feedback ---

- (×) السطر 7

  --- feedback ---

حاول مرة أخرى. `speaker.play(523, 1)` will play a note for 1 second. هناك شيء مفقود في سطر مختلف.

  --- /feedback ---

- (×) السطر 11

  --- feedback ---

حاول مرة أخرى. يلزم استدعاء دالة `() play_sound` مع أقواس الفتح والإغلاق لتشغيل الصوت.

  --- /feedback ---

--- /choices ---

--- /question ---
