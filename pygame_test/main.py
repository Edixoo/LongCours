import pygame

pygame.init()

screen = pygame.display.set_mode((0,0))

running=True

image= pygame.image.load("./images/photoshop-2020-logo-37B02055A4-seeklogo.com.png").convert()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                print("Gauche")
            if event.key==pygame.K_RIGHT:
                print("Droite")
            if event.key==pygame.K_UP:
                print("Haut")
            if event.key==pygame.K_DOWN:
                print("Bas")
            

    screen.blit(image,(0,0))

    pygame.display.flip()
pygame.quit