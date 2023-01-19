import pygame
from buttons import Cancel,Button
from CartesGraphique import Cartes
import marchandises
from joueurs import joueur
class Vendre:
    def __init__(self, screen) -> None:
        self.screen=screen
        self.marchandise: marchandises.marchandises = marchandises.cereale(1)
        self.joueur: joueur
        
        fond= pygame.image.load("./images/Rectangle.png").convert_alpha()
        self.fond=pygame.transform.scale(fond,[900,700])
        self.fondrect=self.fond.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
        self.ventecheck=False
        self.vendre=Button((self.screen.get_width()/2+65, 697),(100,50),"Vendre",self.screen, 20)
        self.textbox=pygame.Rect(530, 425, 200, 35)
        self.cancel=Cancel(self.screen.get_width()/2-65,697, self.screen)

        self.font=pygame.font.SysFont("Arial",25)
        self.quantite=""
        self.mess=self.font.render(self.quantite,True, "white")
        self.carte=Cartes(self.marchandise, 1, 235, 400, self.screen)


    def display(self, joueur, marchandise):
        self.joueur=joueur
        self.dispo=self.font.render("Quantité disponible de " + marchandise.nom+ ":", True, "white")
        self.screen.blit(self.fond, self.fondrect)
        pygame.draw.rect(self.screen, "white", self.textbox, 2)
        self.screen.blit(self.mess, self.textbox)
        self.screen.blit(self.dispo, (475,235))
        self.carte=Cartes(marchandise, self.quantite, 235, 400, self.screen)
        self.carte.display()
        if self.ventecheck:
            self.vendre.display()
        self.cancel.display()
        


    def update(self, position, text):
        self.mess=self.font.render(text,True, "white")
        self.cancel.update(position, "red")
        self.quantite=str(text)
        self.textbox.w=max(100,self.mess.get_width()+10)
        

