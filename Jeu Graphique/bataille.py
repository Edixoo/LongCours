import pygame
from joueurs import joueur as j
from buttons import Button, Cancel
from InterfaceChoixJoueur import ChoixJoueur
from InterfaceCombat import Combat


class Bataille:
    def __init__(self,screen, joueur, listejoueur) -> None:
        self.screen=screen
        self.joueurUn=joueur
        self.joueurDeux=j(0,"pseudo","")
        self.choixjoueur=ChoixJoueur(self.screen, listejoueur, self.joueurUn)
        self.combatint=Combat(self.joueurUn, self.joueurDeux,self.screen)
        self.choix=True
        self.combat=False

    def update(self, position):
        if self.choix:
            self.choixjoueur.update(position)
        if self.combat:
            self.combatint.update(position)
    
    def display(self):
        if self.choix:
            self.choixjoueur.display()
        elif self.combat:
            self.combatint.display()
    
    def checkforInput(self, position):
        if self.choixjoueur.checkForInput(position)!=0:
            self.choix=False
            if self.choixjoueur.checkForInput(position)!=1:
                self.joueurDeux=self.choixjoueur.checkForInput(position)
                self.combatint=Combat(self.joueurUn, self.joueurDeux,self.screen)
                self.choix=False
                self.combat=True
        if self.combatint.checkForInput(position)!=0:
            j1, j2=self.combatint.checkForInput(position)
            self.combat=False
            return j1, j2
        return 0

