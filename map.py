import pygame
import buttons
import port
import portgraphique

class Map:
    def __init__(self) -> None:
        self.screen=pygame.display.set_mode((922,800))
        self.running = True
        self.clock=pygame.time.Clock()

        pygame.display.set_caption("Long Cours")
        self.button=buttons.Acheter(100,700, self.screen)

        porte=port.port(1,"cereale","Le Cap")
        self.lecap=portgraphique.Portgraphique(porte,100,100, self.screen)

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running= False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.button.checkForInput(pygame.mouse.get_pos())

    def update(self):
        self.button.changeColor(pygame.mouse.get_pos(), "red")
        self.lecap.hovered(pygame.mouse.get_pos())

    def display(self):
        image=pygame.image.load("./MapSAE/Test.png").convert()
        button_surface = pygame.transform.scale(image, (922, 800))
        self.screen.blit(button_surface,(0,0))
        self.lecap.display()
        self.button.update()
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