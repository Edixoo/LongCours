import pygame
from buttons import Cancel, Button
from acheter import Acheter

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
        self.cancel=Cancel(self.screen.get_width()/2-75, self.screen.get_height()/2+125,self.screen)

        self.achat=Button([518,522],[100,50], "Acheter", self.screen, 25)

        self.acheter=Acheter(port.marchandise, self.screen)
        self.port=pygame.Rect(posx,posy,50,50)
        self.isclicked=False
        self.clickachat=False
    
    def display(self):
        pygame.draw.rect(self.screen, self.couleur, self.port)

    def checkforInput(self,position):
        if position[0] in range(self.port.left, self.port.right) and position[1] in range(self.port.top, self.port.bottom):
            self.isclicked=True
        if self.achat.checkForInput(position)==1:
            self.clickachat=True
        elif self.clickachat==True and self.acheter.cancel.checkForInput(position):
            self.clickachat=False
        if self.cancel.checkForInput(position)==1 and self.isclicked==True and self.clickachat==False:
            self.isclicked=False
    
    def update(self, position, text):
        self.cancel.update(position, "red")
        self.acheter.update(position, text)
        self.achat.update(position, "grey")

    def afficher_interface(self):
            rectangle=pygame.image.load("./images/Rectangle.png").convert_alpha()
            rect=rectangle.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
            self.screen.blit(rectangle,rect)
            
            self.screen.blit(self.marchandisenom, self.rectmarchnom)
            self.screen.blit(self.marchandiseprix, self.rectprix)
            self.screen.blit(self.nom, self.rectnom)
            self.cancel.display()
            self.achat.display()

            