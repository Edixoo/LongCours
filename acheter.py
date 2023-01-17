import pygame
from buttons import Cancel
from CartesGraphique import Cartes
from joueurs import joueur

class Acheter:
    def __init__(self, marchandise, screen) -> None:
        self.screen=screen
        self.marchandise= marchandise
        self.joueur: joueur
        fond= pygame.image.load("./images/Rectangle.png").convert_alpha()
        self.fond=pygame.transform.scale(fond,[900,700])
        self.fondrect=self.fond.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))

        self.cancel=Cancel(451,697, self.screen)

        font=pygame.font.SysFont("Arial",25)
        self.quantite=""
        self.mess=font.render(self.quantite,True, "white")
        self.carte=Cartes(marchandise, self.quantite, 235,400, self.screen)

        self.premierphrase=font.render("Entrez le nombre de "+marchandise.nom, True, "white")
        self.deuxiemephrase=font.render("que vous voulez acheter", True, "white")
        self.textbox=pygame.Rect(530, self.screen.get_height()/2+5, 200, 35)
        

    def display(self,joueur):
        self.screen.blit(self.fond, self.fondrect)
        pygame.draw.rect(self.screen, "white", self.textbox, 2)
        self.screen.blit(self.mess, self.textbox)
        self.screen.blit(self.premierphrase, (475,self.screen.get_height()/2-60))
        self.screen.blit(self.deuxiemephrase, (475, self.screen.get_height()/2-30))
        self.carte.display()
        self.cancel.display()
        


    def update(self, position, text):
        font=pygame.font.SysFont("Arial",35)
        self.mess=font.render(text,True, "white")
        self.cancel.update(position, "red")
        self.carte.update(text)
        self.textbox.w=max(100,self.mess.get_width()+10)
        

