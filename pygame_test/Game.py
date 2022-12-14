import pygame
from Player import Player
class Game:
    def __init__(self,screen) -> None:
        self.screen=screen
        self.running = True
        self.clock=pygame.time.Clock()
        self.player=Player(0,0)
        self.area=pygame.Rect(300, 150, 300, 300)
        self.area_color = "red"
    
    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running= False
        
        keys=pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.player.velocity[0]= -1
        elif keys[pygame.K_d]:
            self.player.velocity[0]= 1
        else:
            self.player.velocity[0]= 0
        if keys[pygame.K_z]:
            self.player.velocity[1]= -1
        elif keys[pygame.K_s]:
            self.player.velocity[1]= 1
        else:
            self.player.velocity[1]= 0

    def update(self):
        self.player.move()
        if self.area.colliderect(self.player.rect):
            self.area_color= "blue"
        else:
            self.area_color= "red"

    def display(self):
        self.screen.fill("white")
        pygame.draw.rect(self.screen, self.area_color, self.area)
        self.player.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)


pygame.init()
screen=pygame.display.set_mode((1080,720))
pygame.display.set_caption("Zizigame")
game=Game(screen)
game.run()

pygame.quit()