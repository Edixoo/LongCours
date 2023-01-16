import pygame
import cimetiere
from InventaireGraphique import InventaireGraphique

class CimetiereGraphique:

    def __init__(self, position, cimetiere: cimetiere.cimetiere, screen) -> None:
        self.screen= screen
        self.cimetiere=cimetiere
        self.rect=self.port=pygame.Rect(position[0],position[1],50,50)
        self.cimeclicked=False
        self.inventaire= InventaireGraphique(self.screen, self.cimetiere.inventaire)
    

    def display(self):
        pygame.draw.rect(self.screen, "red", self.rect)


    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.cimeclicked=True
    

    def afficher_interface(self):
        rectangle=pygame.image.load("./images/Rectangle.png").convert_alpha()
        rect=rectangle.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
        self.screen.blit(rectangle,rect)

        self.fontTitre=pygame.font.SysFont("Arial", 25, True)

        self.titre=self.fontTitre.render("Cimetière", True, "white")
        self.screen.blit(self.titre, [420,241])