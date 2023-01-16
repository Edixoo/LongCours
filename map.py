import pygame
import port
import portgraphique
import InventaireGraphique
import inventaire
import marchandises

class Map:
    def __init__(self) -> None:
        self.screen=pygame.display.set_mode((922,800))
        self.running = True
        self.clock=pygame.time.Clock()

        pygame.display.set_caption("Long Cours")

        porte=port.port(1,"cereale","Le Cap")
        self.lecap=portgraphique.Portgraphique(porte,100,100, self.screen)

        inv=inventaire.inventaire()
        march=marchandises.gold(1550)
        marchan=marchandises.machine_outils(5415)
        inv.ajouter(marchan)
        self.inventaire=InventaireGraphique.InventaireGraphique(self.screen, inv)

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running= False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                self.lecap.checkforInput(pygame.mouse.get_pos())
                self.inventaire.checkforInput(pygame.mouse.get_pos())

    def update(self):
        self.lecap.update(pygame.mouse.get_pos())
        self.inventaire.update(pygame.mouse.get_pos())

    def display(self):
        image=pygame.image.load("./MapSAE/Test.png").convert()
        button_surface = pygame.transform.scale(image, (922, 800))
        self.screen.blit(button_surface,(0,0))
        self.lecap.display()
        self.inventaire.display()

        if self.lecap.isclicked:
            self.lecap.afficher_interface()
        else:
            self.screen.blit(button_surface,(0,0))
            self.lecap.display()
            self.inventaire.display()

        
        if self.inventaire.isclickedinv:
            self.inventaire.afficher_inv()
        else:
            self.screen.blit(button_surface,(0,0))
            self.lecap.display()
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