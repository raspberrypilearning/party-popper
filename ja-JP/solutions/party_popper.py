from picozero import RGBLED, Speaker, Switch
from time import sleep

rgb = RGBLED(red=1, green=2, blue=3) # pin numbers 
pull = Switch(18)
speaker = Speaker(5)

def pop():
    print("Pop") # print to the shell
    rgb.color = (255, 0, 255) # purple
    speaker.play(523, 0.1) # 523 = note C4, 0.1 seconds
    rgb.color = (0, 0, 0) # led no colour - off
    sleep(0.1)
    rgb.color = (255, 0, 255) # purple
    speaker.play(523, 0.6) # note C4, 0.6 seconds
    rgb.off()
        
pull.when_opened = pop # The pop function will be called when the pull switch is opened