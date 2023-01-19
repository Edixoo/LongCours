import pygame
import joueurs
import portgraphique

class joueurGraphique:
    def __init__(self, screen, joueur, port) -> None:
        self.joueur=joueur
        self.screen=screen
        self.imagejoueur=pygame.image.load("./images/joueurbase.png")
        self.imagejoueur=pygame.transform.scale(self.imagejoueur, (80,60))
        self.rect=self.imagejoueur.get_rect(center=(port.port.x+5, port.port.y+5))
 
    def display(self):
        self.screen.blit(self.imagejoueur, self.rect)


    def move(self, port:portgraphique.Portgraphique):
        self.rect=self.imagejoueur.get_rect(center=(port.port.x+5, port.port.y+5))