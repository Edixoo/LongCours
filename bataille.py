import pygame

class Bataille:
    def __init__(self,screen, joueur, list) -> None:
        self.screen=screen
        self.joueur=joueur
        fond=pygame.image.load("./Rectangle.png")
        self.fond= pygame.transform.scale(fond, [900,700])

        self.fondrect=self.fond.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))

