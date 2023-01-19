import pygame

class joueurGraphique:
    def __init__(self, screen, joueur, port) -> None:
        self.joueur=joueur
        self.screen=screen
        self.imagejoueur=pygame.image.load("./images/joueurbase.png")
        self.imagejoueur=pygame.transform.scale(self.imagejoueur, (80,60))
        self.rect=self.imagejoueur.get_rect(center=(port.rect.x+5, port.rect.y+5))
        self.port=port
 
    def display(self):
        self.screen.blit(self.imagejoueur, self.rect)


    def move(self, port):
        self.port=port
        self.rect=self.imagejoueur.get_rect(center=(port.rect.x+5, port.rect.y+5))