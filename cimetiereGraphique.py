import pygame
import cimetiere
from InventaireGraphique import InventaireGraphique

class CimetiereGraphique:

    def __init__(self, position, cimetiere: cimetiere.cimetiere, screen) -> None:
        self.screen= screen
        self.cimetiere=cimetiere
        self.rect=self.port=pygame.Rect(position[0],position[1],50,50)
        self.cimeclicked=False
        self.inventaire= InventaireGraphique(self.screen, self.cimetiere.inventaire[0])
    
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.cimeclicked=True
        