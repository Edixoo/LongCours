import pygame
import port
from buttons import Button
from buttons import Cancel

pygame.init()
main_font = pygame.font.SysFont("cambria", 20)

class Portgraphique:
    def __init__(self, port, posx, posy, screen) -> None:
        self.screen: pygame.Surface =screen
        self.marchandisenom=main_font.render(port.marchandise.nom, True, "white")
        self.rectnom=self.marchandisenom.get_rect(center=(self.screen.get_width()/2, (self.screen.get_height()/2-20)))
        self.marchandiseprix= main_font.render(str(port.marchandise.prix_achat), True, "white")
        self.rectprix= self.marchandiseprix.get_rect(center=(self.screen.get_width()/2, (self.screen.get_height()/2-100)))
        self.nom=main_font.render(port.nom, True, "white")
        self.couleur=port.couleur
        self.cancel=Cancel(self.screen.get_width()/2-75, self.screen.get_height()/2+125,self.screen)

        self.port=pygame.Rect(posx,posy,50,50)
        self.ishovered=False
        self.x_pos=posx
        self.y_pos=posy
    
    def display(self):
        pygame.draw.rect(self.screen, self.couleur, self.port)

    def checkforInput(self,position):
        if position[0] in range(self.port.left, self.port.right) and position[1] in range(self.port.top, self.port.bottom):
            self.ishovered=True
        if self.cancel.checkForInput(position)==1 and self.ishovered==True:
            self.ishovered=False
    
    def update(self, position):
        self.cancel.update(position, "red")

    def afficher_interface(self):
            rectangle=pygame.image.load("./images/Rectangle.png").convert_alpha()
            rect=rectangle.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
            self.screen.blit(rectangle,rect)
            
            self.screen.blit(self.marchandisenom, self.rectnom)
            self.screen.blit(self.marchandiseprix, self.rectprix)
            self.cancel.display()

            