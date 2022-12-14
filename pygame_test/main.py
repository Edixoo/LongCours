import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

running=True

image= pygame.image.load("./images/photoshop-2020-logo-37B02055A4-seeklogo.com.png").convert()


clock=pygame.time.Clock()

x=0

y=0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_q]:
        x-=1
    if pressed[pygame.K_d]:
        x+=1
    if pressed[pygame.K_z]:
        y-=1
    if pressed[pygame.K_s]:
        y+=1
    screen.fill((0,0,0))
    screen.blit(image,(x,y))

    pygame.display.flip()
    clock.tick(60)

    
pygame.quit