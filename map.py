import pygame
import port
import portgraphique
import CartesGraphique
import marchandises
import cimetiere
from cimetiereGraphique import CimetiereGraphique

class Map:
    def __init__(self) -> None:
        self.screen=pygame.display.set_mode((922,800))
        self.running = True
        self.clock=pygame.time.Clock()

        pygame.display.set_caption("Long Cours")

        porte=port.port(1,"cereale","Le Cap")
        self.lecap=portgraphique.Portgraphique(porte,100,100, self.screen)

        self.carte=CartesGraphique.Cartes(marchandises.cereale(150), 150, self.screen.get_width()/2, self.screen.get_height()/2, self.screen)

        # cimet=cimetiere.cimetiere(inv)
        # self.cimetiere=CimetiereGraphique([150,150],cimet,self.screen)

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running= False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.lecap.checkforInput(pygame.mouse.get_pos())
                self.inventaire.checkforInput(pygame.mouse.get_pos())
                self.cimetiere.checkForInput(pygame.mouse.get_pos())

    def update(self):
        self.lecap.update(pygame.mouse.get_pos())

    def display(self):
        image=pygame.image.load("./MapSAE/Test.png").convert()
        button_surface = pygame.transform.scale(image, (922, 800))
        self.screen.blit(button_surface,(0,0))
        self.lecap.display()
        self.carte.display()
        if self.lecap.ishovered:
            self.lecap.afficher_interface()
        else:
            self.screen.blit(button_surface,(0,0))
            self.lecap.display()
            self.carte.display()
        self.cimetiere.display()
        self.inventaire.display()

        if self.inventaire.isclickedinv:
            self.inventaire.afficher_inv()
        elif self.lecap.isclicked:
            self.lecap.afficher_interface()
        elif self.cimetiere.cimeclicked:
            self.cimetiere.afficher_interface()
        else:
            self.screen.blit(button_surface,(0,0))
            self.lecap.display()
            self.cimetiere.display()
            self.inventaire.display()

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)

pygame.init()
game=Map()


game.run()
pygame.quit()