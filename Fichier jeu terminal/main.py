import world
import os
import sys
import time

while True:
    longcours = world.world() 
    longcours.jouerpartie()
    print("_________________________")
    print("_________________________")
    print("Souhaitez vous lancer une nouvelle partie ? [oui/non]")
    choix=input()
    if choix=="oui":
        time.sleep(5)
    else:
        print("_________________________")
        print("Merci d'avoir joué à notre jeu !")
        print("_________________________")
        time.sleep(5)
        break
    
