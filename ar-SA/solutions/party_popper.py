from picozero import RGBLED, Speaker, Switch
from time import sleep

rgb = RGBLED(red=1, green=2, blue=3) # أرقام دبوس 
pull = Switch(18)
speaker = Speaker(5)

def pop():
    print("فرقعة") # اطبع على الغلاف
    rgb.color = (255, 0, 255) # بنفسجي "purple"
    speaker.play(523, 0.1) # 523 = النغمة C4 ، لمدة ثانية واحدة
    rgb.color = (0, 0, 0) # LED لا لون - معطلة
    sleep(0.1)
    rgb.color = (255, 0, 255) # بنفسجي "purple"
    speaker.play(523, 0.6) # النغمة C4، لمدة 0.6 ثانية
    rgb.off()
        
pull.when_opened = pop # سيتم استدعاء دالة pop عندما يتم سحب مفتاح التشغيل