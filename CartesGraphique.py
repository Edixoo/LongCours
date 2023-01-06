import pygame
import zone


main_font = pygame.font.SysFont("cambria", 20)

class Cartes:
    def __init__(self, marchandise, quantite, posx, posy, screen) -> None:
        self.screen=screen
        self.fond=pygame.image.load("./images/carte.jpg")
        self.x_pos=posx
        self.y_pos=posy
        self.rect = self.fond.get_rect(center=(self.x_pos, self.y_pos))
        self.marchandise=marchandise
        self.text = main_font.render(self.marchandise, True, "black")
        self.text_rect = self.text.get_rect(center=(self.x_pos, 100))
        self.quantite=quantite
        self.textquantite=main_font.render(self.quantite,True,"black")
        self.rect_quantite = self.textquantite.get_rect(center=(self.x_pos, 200))

    def update(self):
        self.screen.blit(self.fond, self.rect)
        self.screen.blit(self.text, self.text_rect)
        self.screen.blit(self.textquantite, self.rect_quantite)
    
    


        