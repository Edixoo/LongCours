import pygame
import joueurs
import portgraphique

class joueurGraphique:
    def __init__(self, screen, joueur) -> None:
        self.joueur=joueur
        self.screen=screen
        self.imagejoueur=pygame.image.load("./images/joueurbase.png")
        self.imagejoueur=pygame.transform.scale(self.imagejoueur, (80,60))
 
    def display(self,port: portgraphique.Portgraphique):
        self.screen.blit(self.imagejoueur, (port.port.x+10, port.port.y+10))