import pygame
import marchandises


main_font = pygame.font.SysFont("cambria", 20)

class Cartes:
    def __init__(self, marchandise: marchandises.marchandises, quantite, posx, posy, screen) -> None:
        self.screen=screen
        self.fond=pygame.image.load("./images/carte.png")
        self.fond= pygame.transform.scale(self.fond, [200,300])
        self.x_pos=posx
        self.y_pos=posy
        self.rect = self.fond.get_rect(center=(self.x_pos, self.y_pos))
        self.marchandise=marchandise
        self.text = main_font.render(self.marchandise.nom, True, "black")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos-100))
        self.valeur=main_font.render(str(self.marchandise.prix_achat), True, "black")
        self.valeurect=self.valeur.get_rect(center=(self.x_pos+ 35, self.y_pos+33))
        self.quantite=quantite
        self.textquantite=main_font.render(str(self.quantite),True,"black")
        self.rect_quantite = self.textquantite.get_rect(center=(self.x_pos+35, self.y_pos+83))

    def display(self):
        self.screen.blit(self.fond, self.rect)
        self.screen.blit(self.text, self.text_rect)
        self.screen.blit(self.textquantite, self.rect_quantite)
        self.screen.blit(self.valeur, self.valeurect)
    
    


        