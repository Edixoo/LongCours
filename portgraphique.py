import pygame
import port

main_font = pygame.font.SysFont("cambria", 20)

class Portgraphique:
    def __init__(self, port, posx, posy, screen) -> None:
        self.marchandisenom=main_font.render(port.marchandise.nom, True, "white")
        self.marchandiseprix= main_font.render(port.marchandise.prix, True, "white")
        self.nom=main_font.render(port.nom, True, "white")
        self.couleur=port.couleur
        self.screen: pygame.Surface =screen
        print(self.screen.get_width())
        self.port=pygame.Rect(posx,posy,10,10)
        self.ishovered=False
        self.x_pos=posx
        self.y_pos=posy
    
    def display(self):
        pygame.draw.rect(self.screen, self.couleur, self.port)
        self.screen.blit(self.nom, center=(self.x_pos, self.y_pos))
        self.screen.blit(self.marchandisenom, center=(self.x_pos+200, self.y_pos-100))

    def hovered(self,position):
        if position[0] in range(self.port.left, self.port.right) and position[1] in range(self.port.top, self.port.bottom):
            affichage=pygame.Rect(self.screen.get_width()/2, int(self.screen.get_height()/2))