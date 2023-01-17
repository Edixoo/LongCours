import pygame
from buttons import Cancel
from CartesGraphique import Cartes
from marchandises import marchandises
from joueurs import joueur
class Vendre:
    def __init__(self, screen) -> None:
        self.screen=screen
        self.marchandise: marchandises
        self.joueur: joueur
        
        fond= pygame.image.load("./images/Rectangle.png").convert_alpha()
        self.fond=pygame.transform.scale(fond,[900,700])
        self.fondrect=self.fond.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))

        self.textbox=pygame.Rect(530, 425, 200, 35)
        self.cancel=Cancel(451,697, self.screen)

        self.font=pygame.font.SysFont("Arial",25)
        self.quantite=""
        self.mess=self.font.render(self.quantite,True, "white")
        self.carte: Cartes

        self.dispo=""


    def display(self, joueur, marchandise):
        self.joueur=joueur
        self.dispo=self.font.render("Quantité disponible de " + marchandise.nom+ ":", True, "white")
        self.
        self.screen.blit(self.fond, self.fondrect)
        pygame.draw.rect(self.screen, "white", self.textbox, 2)
        self.screen.blit(self.mess, self.textbox)
        self.screen.blit(self.dispo, (475,235))
        self.carte.display()
        self.cancel.display()
        


    def update(self, position, text):
        self.mess=self.font.render(text,True, "white")
        self.cancel.update(position, "red")
        self.carte.update(text)
        

