import pygame
from buttons import Cancel,Button
from CartesGraphique import Cartes
import marchandises
from joueurs import joueur
import copy
class Vendre:
    def __init__(self, screen) -> None:
        self.screen=screen
        self.marchandise: marchandises.marchandises = marchandises.cereale(1)
        self.joueur: joueur = joueur(81,"tempo","b")
        
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
        self.marchandise=marchandise
        self.dispo=self.font.render("Quantité disponible de " + marchandise.nom+ ": "+str(self.joueur.bateau.inventaire.getMarchandiseByName(marchandise)), True, "white")
        self.screen.blit(self.fond, self.fondrect)
        pygame.draw.rect(self.screen, "white", self.textbox, 2)
        self.screen.blit(self.mess, self.textbox)
        self.screen.blit(self.dispo, (475,235))
        self.carte=Cartes(marchandise, self.quantite, 235, 400, self.screen)
        self.carte.display()
        if self.ventecheck:
            self.vendre.display()
        self.cancel.display()
        
    def checkforInput(self, position, march):
        if self.cancel.checkForInput(position):
            return (1,self.joueur)

        elif self.quantite!='' and self.vendre.checkForInput(position) and self.marchandise.nom==march.nom:
            march= copy.copy(self.marchandise)
            march.qttachete=int(self.quantite)
            print (march.qttachete)
            self.joueur.ajout_monnaie(march.qttachete*march.prix_achat)
            self.joueur.bateau.inventaire.retirergraph(march.qttachete, march)
            self.ventecheck=False
            return (1, self.joueur)
        else:
            return (0, self.joueur)


    def update(self, position, text):
        self.mess=self.font.render(text,True, "white")
        self.cancel.update(position, "red")
        self.quantite=str(text)
        self.vendre.update(position, "grey")
        if text!='':
            if self.joueur.bateau.inventaire.getMarchandiseByName(self.marchandise)!="Vide":
                print(int(self.joueur.bateau.inventaire.getMarchandiseByName(self.marchandise)))
                if int(self.joueur.bateau.inventaire.getMarchandiseByName(self.marchandise))<int(text):
                    self.ventecheck=True
                else:
                    self.ventecheck=False
            else:
                self.ventecheck=False
        else:
            self.ventecheck=False
        

