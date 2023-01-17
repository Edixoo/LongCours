import pygame
from buttons import Button, Cancel
from CartesGraphique import Cartes

class Acheter:
    def __init__(self, marchandise, screen) -> None:
        self.screen=screen
        self.marchandise= marchandise
        fond= pygame.image.load("./images/Rectangle.png").convert_alpha()
        self.fond=pygame.transform.scale(fond,[900,700])
        self.fondrect=self.fond.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))

        self.textbox=pygame.Rect(530, 425, 200, 35)
        self.cancel=Cancel(451,697, self.screen)
        
        font=pygame.font.SysFont("Arial",35)
        self.quantite=""
        self.mess=font.render(self.quantite,True, "white")
        self.carte=Cartes(marchandise, self.quantite, 235,400, self.screen)


    def display(self):
        self.screen.blit(self.fond, self.fondrect)
        pygame.draw.rect(self.screen, "white", self.textbox, 2)
        self.screen.blit(self.mess, self.textbox)
        self.carte.display()
        self.cancel.display()
        


    def update(self, position, text):
        font=pygame.font.SysFont("Arial",35)
        self.mess=font.render(text,True, "white")
        self.cancel.update(position, "red")
        self.carte.update(text)
        

