
--- question ---
---
legend: Question 3 of 3
---

لقد استخدمت حدثًا `when_opened` لتشغيل التعليمات البرمجية كلما تم سحب مفرقعات الحفلة.

Which line of code correctly sets up the event so that the `pop` function gets called every time the connection is opened.

--- choices ---

- (x) `pull.when_opened = pop`

  --- feedback ---

Correct! When using events, we don't use the `()` brackets because the function should only be called when the event happens. Adding `()` at the end will call the function **once**; as soon as the line of code is executed.

  --- /feedback ---

- ( ) `pull.when_opened = pop()`

  --- feedback ---

No, but this is a really common mistake! This code will call the `pop` function **once** when this line of code runs. Instead you need to tell `pico_zero` which function to run when the event occurs and `pico_zero` will call the function for you **every time** the event happens.

  --- /feedback ---

--- /choices ---

--- /question ---
