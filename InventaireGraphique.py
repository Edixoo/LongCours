import pygame
import inventaire
from buttons import Button, Cancel

class InventaireGraphique:
    def __init__(self, screen, inventaire: inventaire.inventaire) -> None:
        self.screen=screen
        self.bouton=Button([165, 753], [150, 75], "Inventaire", self.screen, 30)
        self.inventaire=inventaire
        self.isclickedinv=False
        self.cancel=Cancel(451,697, self.screen)
        
    
    def display(self):
        self.bouton.display()

    def update(self, position):
        self.bouton.update(position, "grey")
        self.cancel.update(position, "grey")

    def checkforInput(self,position):
        if self.bouton.checkForInput(position)==1:
            self.isclickedinv=True
        if self.isclickedinv==True and self.cancel.checkForInput(position):
            self.isclickedinv=False

    def afficher_inv(self):
        fond= pygame.image.load("./images/Rectangle.png").convert_alpha()
        fond=pygame.transform.scale(fond,[900,700])
        fondrect=fond.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
        self.screen.blit(fond,fondrect)

        self.font=pygame.font.SysFont("Arial", 30)
        self.fonttitre=pygame.font.SysFont("Arial", 40, True)

        self.titre=self.fonttitre.render("Inventaire", True, "white")
        self.screen.blit(self.titre, [382, 80])

        self.contenu=self.font.render("Or :     " + self.inventaire.getGold(), True, "white")
        self.screen.blit(self.contenu, [145, 251])

        self.contenu=self.font.render("Textile :     " + self.inventaire.getTextile(), True, "white")
        self.screen.blit(self.contenu, [145, 413])

        self.contenu=self.font.render("Bois :     " + self.inventaire.getBois(), True, "white")
        self.screen.blit(self.contenu, [145, 601])

        self.contenu=self.font.render("Céréales :     " + self.inventaire.getCereale(), True, "white")
        self.screen.blit(self.contenu, [555, 251])

        self.contenu=self.font.render("Machines et Outils :     " + self.inventaire.getMachineOutils(), True, "white")
        self.screen.blit(self.contenu, [555, 413])

        self.contenu=self.font.render("Pétrole :     " + self.inventaire.getPetrole(), True, "white")
        self.screen.blit(self.contenu, [555, 601])

        self.cancel.display()