from picozero import RGBLED, Speaker, Switch
from time import sleep

rvb = RGBLED(red=1, green=2, blue=3) # Numéros des broches 
tirer = Switch(18)
hautparleur = Speaker(5)

def boum():
    print("Boum") # Imprimer sur la console
    rvb.color = (255, 0, 255) # Violet
    hautparleur.play(523, 0.1) # 523 = note C4, 0,1 seconde
    rvb.color = (0, 0, 0) # LED sans couleur – éteinte
    sleep(0.1)
    rvb.color = (255, 0, 255) # Violet
    hautparleur.play(523, 0.6) # Note C4, 0,6 seconde
    rvb.off()
        
tirer.when_opened = boum # La fonction pop sera appelée lorsque l'interrupteur à tirette est ouvert