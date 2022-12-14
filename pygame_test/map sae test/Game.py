import pygame
import pytmx
import pyscroll

class Game:
    def __init__(self) -> None:
        self.screen=screen=pygame.display.set_mode((1080,720))
        self.running = True
        self.clock=pygame.time.Clock()

        pygame.display.set_caption("Zizigame")

        tmx_data=pytmx.load_pygame('map_test.tmx')
        map_data=pyscroll.data.TiledMapData(tmx_data)
        map_layer= pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())


        self.group= pyscroll.PyscrollGroup(map_layer, default_layer=1)


    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running= False

    def update(self):
        pass

    def display(self):
        self.group.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)


pygame.init()
game=Game()
game.run()

pygame.quit()