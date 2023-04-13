import pygame
import marchandises


main_font = pygame.font.SysFont("Arial", 20)

class Cartes:
    def __init__(self, marchandise: marchandises.marchandises, quantite, posx, posy, screen) -> None:
        self.screen=screen
        self.fond=pygame.image.load("../images/carte.png")
        self.fond= pygame.transform.scale(self.fond, [200,300])
        self.x_pos=posx
        self.y_pos=posy
        self.marchandise=marchandise
        if quantite=="":
            self.quantite=0
        else:
            self.quantite=quantite
        self.rect = self.fond.get_rect(center=(self.x_pos, self.y_pos))
        self.text = main_font.render(marchandise.nom, True, "black")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos-100))
        self.valeur=main_font.render(str(marchandise.prix_achat*int(self.quantite)), True, "black")
        self.valeurect=self.valeur.get_rect(center=(self.x_pos+ 35, self.y_pos+33))
        self.textquantite=main_font.render(str(self.quantite),True,"black")
        self.rect_quantite = self.textquantite.get_rect(center=(self.x_pos+35, self.y_pos+83))

    def display(self):
        self.screen.blit(self.fond, self.rect)
        self.screen.blit(self.text, self.text_rect)
        self.screen.blit(self.textquantite, self.rect_quantite)
        self.screen.blit(self.valeur, self.valeurect)
    
    def update(self, quantite):
        
        if quantite=='':
            self.valeur=main_font.render(str(0), True, "black")
            self.textquantite=main_font.render(str(0),True,"black")
        else:
            self.valeur=main_font.render(str(self.marchandise.prix_achat*int(quantite)), True, "black")
            self.textquantite=main_font.render(str(quantite),True,"black")
    


        