import pygame
import port, portgraphique, CartesGraphique
import marchandises
import cimetiere
import inventaire
import InventaireGraphique
import acheter, joueurs
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
        
        inv= inventaire.inventaire()
        march= marchandises.cereale(150)
        inv.ajouter(march)
        self.inventaire=InventaireGraphique.InventaireGraphique(self.screen, inv)
        cimet=cimetiere.cimetiere(inv)
        self.cimetiere=CimetiereGraphique([150,150],cimet,self.screen)

        self.text=""

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running= False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                self.lecap.checkforInput(pygame.mouse.get_pos())
                self.inventaire.checkforInput(pygame.mouse.get_pos())
                self.cimetiere.checkForInput(pygame.mouse.get_pos())
            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_BACKSPACE:
                    self.text=self.text[:-1]
                else:
                    self.text+= event.unicode



    def update(self):
        self.lecap.update(pygame.mouse.get_pos(), self.text)
        self.inventaire.update(pygame.mouse.get_pos())
        self.cimetiere.update(pygame.mouse.get_pos())

    def display(self):
        image=pygame.image.load("./MapSAE/Test.png").convert()
        map= pygame.transform.scale(image, (922, 800))
        self.screen.blit(map,(0,0))
        self.lecap.display()
        self.carte.display()
        self.cimetiere.display()
        self.inventaire.display()
        if self.lecap.isclicked:
            self.lecap.afficher_interface()
            if self.lecap.clickachat:
                self.lecap.acheter.display()
            else:
                self.text=""
        elif self.inventaire.isclickedinv:
            self.inventaire.afficher_inv()
        elif self.lecap.isclicked:
            self.lecap.afficher_interface()
        elif self.cimetiere.cimeclicked:
            self.cimetiere.afficher_interface()
            if self.cimetiere.invclick:
                self.cimetiere.inventaire.afficher_inv()
        else:
            self.screen.blit(map,(0,0))
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