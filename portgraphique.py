import pygame
from buttons import Cancel, Button
from acheter import Acheter
from vendre import Vendre
import joueurs


main_font = pygame.font.SysFont("cambria", 20)

class Portgraphique:
    def __init__(self, port, posx, posy, screen) -> None:
        self.screen: pygame.Surface =screen
        self.marchandisenom=main_font.render("Nom: " +port.marchandise.nom, True, "white")
        self.rectmarchnom=self.marchandisenom.get_rect(center=(self.screen.get_width()/2, (self.screen.get_height()/2-75)))
        self.marchandiseprix= main_font.render("prix: " +str(port.marchandise.prix_achat), True, "white")
        self.rectprix= self.marchandiseprix.get_rect(center=(self.screen.get_width()/2, (self.screen.get_height()/2-20)))
        self.nom=main_font.render(port.nom, True, "white")
        self.rectnom=self.nom.get_rect(center=(self.screen.get_width()/2, (self.screen.get_height()/2-150)))
        self.couleur=port.couleur
        self.cancel=Cancel(340, 522,self.screen)
        self.portbase=port
        self.joueur: joueurs.joueur = joueurs.joueur(81,"tempo","b")
        self.achat=Button([455,522],[100,50], "Acheter", self.screen, 25)
        self.vente=Button([570,522], [100,50], "Vendre", self.screen, 25)

        self.acheter=Acheter(port.marchandise, self.screen)
        self.vendre=Vendre(self.screen)
        self.rect=pygame.Rect(posx,posy,20,20)
        self.isclicked=False
        self.clickachat=False
        self.clickvente=False
        self.updatejoueur=False
    
    def display(self, joueur):
        pygame.draw.rect(self.screen, self.couleur, self.rect)
        self.joueur=joueur

    def checkforInput(self,position):

        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.isclicked=True

        if self.achat.checkForInput(position):
            self.clickachat=True
        if self.clickachat==True:
            checkachat= self.acheter.checkforInput(position)
            if checkachat[0]:
                self.joueur=checkachat[1]
                self.updatejoueur=True
                self.clickachat=False
                checkachat=(False,self.joueur)

        if self.vente.checkForInput(position):
            self.clickvente=True
        if self.clickvente==True:
            checkvente=self.vendre.checkforInput(position, self.portbase.marchandise)
            if checkvente[0]:
                self.joueur=checkvente[1]
                self.updatejoueur=True
                self.clickvente=False
                checkvente=(False, self.joueur)

        if self.cancel.checkForInput(position)==1 and self.isclicked==True and self.clickachat==False:
            self.isclicked=False
            self.updatejoueur=False
    
    def update(self, position, text):
        self.cancel.update(position, "red")
        self.acheter.update(position, text)
        self.achat.update(position, "grey")
        self.vente.update(position, "grey")
        self.vendre.update(position, text)

    def afficher_interface(self, joueur):
            rectangle=pygame.image.load("./images/Rectangle.png").convert_alpha()
            rect=rectangle.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
            self.screen.blit(rectangle,rect)
            self.screen.blit(self.marchandisenom, self.rectmarchnom)
            self.screen.blit(self.marchandiseprix, self.rectprix)
            self.screen.blit(self.nom, self.rectnom)
            self.cancel.display()
            self.achat.display()
            self.vente.display()
            self.joueur=joueur

            