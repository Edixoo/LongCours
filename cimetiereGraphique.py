import pygame
import cimetiere
from InventaireGraphique import InventaireGraphique
from buttons import Cancel, Button

class CimetiereGraphique:

    def __init__(self, position, cimetiere: cimetiere.cimetiere, screen) -> None:
        self.screen= screen
        self.cimetiere=cimetiere
        self.rect=self.port=pygame.Rect(position[0],position[1],20,20)
        self.cimeclicked=False
        self.invclick=False
        self.couleur="red"
        self.inventaire= InventaireGraphique(self.screen, self.cimetiere.inventaire)
        self.cancel=Cancel(self.screen.get_width()/2-75, self.screen.get_height()/2+125,self.screen)
        self.bouton=Button([503, 527], [100,50], "Montrer", self.screen, 20)

    def display(self):
        pygame.draw.rect(self.screen, self.couleur, self.rect)

    def update(self,position):
        self.bouton.update(position, "grey")
        self.inventaire.update(position)
        self.cancel.update(position, "red")


    def checkforInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.cimeclicked=True
        if self.bouton.checkForInput(position)==1:
            self.invclick=True
        elif self.invclick==True and self.inventaire.cancel.checkForInput(position):
            self.invclick=False
        if self.cimeclicked==True and self.invclick==False and self.cancel.checkForInput(position):
            self.cimeclicked=False

    def afficher_interface(self):
        rectangle=pygame.image.load("./images/Rectangle.png").convert_alpha()
        rect=rectangle.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
        self.screen.blit(rectangle,rect)

        self.fontTitre=pygame.font.SysFont("Arial", 25, True)

        self.titre=self.fontTitre.render("Cimetière", True, "white")
        self.screen.blit(self.titre, [420,241])
        self.cancel.display()
        self.bouton.display()
        
        

        