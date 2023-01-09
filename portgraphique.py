import pygame
import port

pygame.init()
main_font = pygame.font.SysFont("cambria", 20)

class Portgraphique:
    def __init__(self, port, posx, posy, screen) -> None:
        self.marchandisenom=main_font.render(port.marchandise.nom, True, "white")
        self.rectnom=self.marchandisenom.get_rect(center=(posx, posy))
        self.marchandiseprix= main_font.render(str(port.marchandise.prix_achat), True, "white")
        self.rectprix= self.marchandiseprix.get_rect(center=(posx, posy))
        self.nom=main_font.render(port.nom, True, "white")
        self.couleur=port.couleur
        self.screen: pygame.Surface =screen
        print(self.screen.get_width())
        self.port=pygame.Rect(posx,posy,20,20)
        self.ishovered=False
        self.x_pos=posx
        self.y_pos=posy
    
    def display(self):
        pygame.draw.rect(self.screen, self.couleur, self.port)

    def hovered(self,position):
        if position[0] in range(self.port.left, self.port.right) and position[1] in range(self.port.top, self.port.bottom):
            self.screen.blit(self.marchandiseprix, self.rectprix)
            self.screen.blit(self.marchandisenom, self.rectnom)
            self.ishovered=True
        else:
            self.ishovered=False