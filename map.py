import pygame
import port, portgraphique, CartesGraphique
import marchandises
import cimetiere
import inventaire
import InventaireGraphique
import acheter, joueurs
from cimetiereGraphique import CimetiereGraphique

class Map:
    def __init__(self,joueur) -> None:
        self.screen=pygame.display.set_mode((922,800))
        self.running = True
        self.clock=pygame.time.Clock()

        pygame.display.set_caption("Long Cours")

        porte=port.port(1,"cereale","Le Cap")
        self.lecap=portgraphique.Portgraphique(porte,100,100, self.screen)

        self.carte=CartesGraphique.Cartes(marchandises.cereale(150), 150, self.screen.get_width()/2, self.screen.get_height()/2, self.screen)
        
        self.joueur= joueur
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
                if len(self.text)<4:
                    if event.key== pygame.K_0 or event.key==pygame.K_KP0:
                        self.text+="0"
                    elif event.key== pygame.K_1 or event.key==pygame.K_KP1:
                        self.text+="1"
                    elif event.key== pygame.K_2 or event.key==pygame.K_KP2:
                        self.text+="2"
                    elif event.key== pygame.K_3 or event.key==pygame.K_KP3:
                        self.text+="3"
                    elif event.key== pygame.K_4 or event.key==pygame.K_KP4:
                        self.text+="4"
                    elif event.key== pygame.K_5 or event.key==pygame.K_KP5:
                        self.text+="5"
                    elif event.key== pygame.K_6 or event.key==pygame.K_KP6:
                        self.text+="6"
                    elif event.key== pygame.K_7 or event.key==pygame.K_KP7:
                        self.text+="7"
                    elif event.key== pygame.K_8 or event.key==pygame.K_KP8:
                        self.text+="8"
                    elif event.key== pygame.K_9 or event.key==pygame.K_KP9:
                        self.text+="9"



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
                self.lecap.acheter.display(self.joueur)
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
joueur= joueurs.joueur(1, "Salut", "yellow")
game=Map(joueur)


game.run()
pygame.quit()