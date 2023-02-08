import pygame
from buttons import Button, Cancel


class PaquetdeCartes:
    def __init__(self, screen, joueur) -> None:
        self.screen=screen
        fond= pygame.image.load("./images/Rectangle.png").convert_alpha()
        self.fond=pygame.transform.scale(fond,[900,700])

        self.fondrect=fond.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
        self.joueur=joueur
        self.screen.blit(self.fond, self.fondrect)

        self.font=pygame.font.SysFont("Arial", 20)

        self.tempete=self.joueur.getTempete()
        self.cartetempete=pygame.image.load("./images/carte_tempete.png").convert_alpha()
        self.cartetempete=pygame.transform.scale(self.cartetempete,[200,300])
        self.recttempete=self.cartetempete.get_rect(center=(300, self.screen.get_height()/2))
        self.restanttemp=self.font.render("Restant:    " + str(len(self.tempete)), True, "white")
        
        self.depldirect=self.joueur.getMouvement()
        self.cartedepldirect=pygame.image.load("./images/carte_depldirect.png").convert_alpha()
        self.cartedepldirect=pygame.transform.scale(self.cartedepldirect, [200,300])
        self.rectdepldirect=self.cartedepldirect.get_rect(center=(500, self.screen.get_height()/2))
        self.restantdepldirect=self.font.render("Restant:   " + str(len(self.depldirect)), True, "white")
        
        self.baston=self.joueur.getBaston()
        self.cartebaston=pygame.image.load("./images/carte_baston.png").convert_alpha()
        self.cartebaston=pygame.transform.scale(self.cartebaston,[200,300])
        self.rectbaston=self.cartebaston.get_rect(center=(100, self.screen.get_height()/2))
        self.restant=self.font.render("Restant:", True, "white")
        self.forceun=self.font.render("Force I:     " + str(len(self.joueur.getForceUn())), True, "White")
        self.forcedeux=self.font.render("Force II:     " + str(len(self.joueur.getForceDeux())), True, "White")
        self.forcetrois=self.font.render("Force III:     " + str(len(self.joueur.getForceTrois())), True, "White")
        self.forcequatre=self.font.render("Force IV:     " + str(len(self.joueur.getForceQuatre())), True, "White")

        self.cancel=Cancel(450,700, self.screen)

    def display(self):
        self.screen.blit(self.fond, self.fondrect)

        # self.screen.blit(self.cartetempete, self.recttempete)
        # self.screen.blit(self.restanttemp, [300, 500])
        # self.screen.blit(self.cartedepldirect, self.rectdepldirect)
        # self.screen.blit(self.restantdepldirect, [500, 500])
        # self.screen.blit(self.cartebaston, self.rectbaston)
        # self.cancel.display()







        

