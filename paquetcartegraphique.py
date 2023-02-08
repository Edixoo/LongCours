import pygame
from buttons import Button, Cancel


class PaquetdeCartes:
    def __init__(self, screen, joueur) -> None:
        self.screen=screen
        fond= pygame.image.load("./images/Rectangle.png").convert_alpha()
        self.fond=pygame.transform.scale(fond,[900,700])

        self.fondrect=self.fond.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
        self.joueur=joueur

        self.bouton=Button([65, self.screen.get_height()-40], [100, 50], "Cartes", self.screen, 20)
        self.isclicked=False
        fonttitre=pygame.font.SysFont("Arial", 40, True)
        self.titre=fonttitre.render("Menu Cartes", True, "White")
        self.font=pygame.font.SysFont("Arial", 20)

        self.tempete=self.joueur.getTempete()
        self.cartetempete=pygame.image.load("./images/carte_tempete.png").convert_alpha()
        self.cartetempete=pygame.transform.scale(self.cartetempete,[200,300])
        self.recttempete=self.cartetempete.get_rect(center=(self.screen.get_width()/2+230, self.screen.get_height()/2))
        self.restanttemp=self.font.render("Restant:    " + str(len(self.tempete)), True, "white")
        self.tempeteclicked=False
        
        self.depldirect=self.joueur.getMouvement()
        self.cartedepldirect=pygame.image.load("./images/carte_depldirect.png").convert_alpha()
        self.cartedepldirect=pygame.transform.scale(self.cartedepldirect, [200,300])
        self.rectdepldirect=self.cartedepldirect.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
        self.restantdepldirect=self.font.render("Restant:   " + str(len(self.depldirect)), True, "white")
        self.depldirectclicked=False
        
        self.baston=self.joueur.getBaston()
        self.cartebaston=pygame.image.load("./images/carte_baston.png").convert_alpha()
        self.cartebaston=pygame.transform.scale(self.cartebaston,[200,300])
        self.rectbaston=self.cartebaston.get_rect(center=(self.screen.get_width()/2-230, self.screen.get_height()/2))
        self.restant=self.font.render("Restant:", True, "white")
        self.forceun=self.font.render("Force I:     " + str(len(self.joueur.getForceUn())), True, "White")
        self.forcedeux=self.font.render("Force II:     " + str(len(self.joueur.getForceDeux())), True, "White")
        self.forcetrois=self.font.render("Force III:     " + str(len(self.joueur.getForceTrois())), True, "White")
        self.forcequatre=self.font.render("Force IV:     " + str(len(self.joueur.getForceQuatre())), True, "White")
        self.bastonclicked=False

        self.cancel=Cancel(450,700, self.screen)

    
    def display(self):
        self.bouton.display()

        if self.isclicked:
            self.screen.blit(self.fond, self.fondrect)
            self.screen.blit(self.titre, self.titre.get_rect(center=[self.screen.get_width()/2, 90]))
            self.screen.blit(self.cartetempete, self.recttempete)
            rect=self.restanttemp.get_rect(center=(self.screen.get_width()/2+230,575))
            self.screen.blit(self.restanttemp, rect)
            
            self.screen.blit(self.cartedepldirect, self.rectdepldirect)
            rect=self.restantdepldirect.get_rect(center=(self.screen.get_width()/2, 575))
            self.screen.blit(self.restantdepldirect, rect)

            self.screen.blit(self.cartebaston, self.rectbaston)
            rect=self.restant.get_rect(center=(self.screen.get_width()/2-245, 575))
            self.screen.blit(self.restant, rect)
            self.screen.blit(self.forceun, [self.screen.get_width()/2-245, 600])
            self.screen.blit(self.forcedeux, [self.screen.get_width()/2-245, 620])
            self.screen.blit(self.forcetrois, [self.screen.get_width()/2-245, 640])
            self.screen.blit(self.forcequatre, [self.screen.get_width()/2-245, 660])
            self.cancel.display()
        
    def update(self, position):
        self.cancel.update(position, "red")
        self.bouton.update(position, "grey")
        if position[0] in range(self.recttempete.left, self.recttempete.right) and position[1] in range(self.recttempete.top, self.recttempete.bottom):
            self.cartetempete=pygame.image.load("./images/carte_tempete.png").convert_alpha()
            self.cartetempete=pygame.transform.scale(self.cartetempete, [220,320])
            self.recttempete=self.cartetempete.get_rect(center=(self.screen.get_width()/2+230, self.screen.get_height()/2))
        else:
            self.cartetempete=pygame.image.load("./images/carte_tempete.png").convert_alpha()
            self.cartetempete=pygame.transform.scale(self.cartetempete,[200,300])
            self.recttempete=self.cartetempete.get_rect(center=(self.screen.get_width()/2+230, self.screen.get_height()/2))
        if position[0] in range(self.rectdepldirect.left, self.rectdepldirect.right) and position[1] in range(self.rectdepldirect.top, self.rectdepldirect.bottom):
            self.cartedepldirect=pygame.image.load("./images/carte_depldirect.png").convert_alpha()
            self.cartedepldirect=pygame.transform.scale(self.cartedepldirect, [220,320])
            self.rectdepldirect=self.cartedepldirect.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
        else:
            self.cartedepldirect=pygame.image.load("./images/carte_depldirect.png").convert_alpha()
            self.cartedepldirect=pygame.transform.scale(self.cartedepldirect,[200,300])
            self.rectdepldirect=self.cartedepldirect.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
        if position[0] in range(self.rectbaston.left, self.rectbaston.right) and position[1] in range(self.rectbaston.top, self.rectbaston.bottom):
            self.cartebaston=pygame.image.load("./images/carte_baston.png").convert_alpha()
            self.cartebaston=pygame.transform.scale(self.cartebaston, [220,320])
            self.rectbaston=self.cartebaston.get_rect(center=(self.screen.get_width()/2-230, self.screen.get_height()/2))
        else:
            self.cartebaston=pygame.image.load("./images/carte_baston.png").convert_alpha()
            self.cartebaston=pygame.transform.scale(self.cartebaston,[200,300])
            self.rectbaston=self.cartebaston.get_rect(center=(self.screen.get_width()/2-230, self.screen.get_height()/2))

    def checkforInput(self, position):
        if self.bouton.checkForInput(position):
            self.isclicked=True
            print("hello")
        if self.isclicked:
            if self.cancel.checkForInput(position):
                self.isclicked=False
            elif position[0] in range(self.recttempete.left, self.recttempete.right) and position[1] in range(self.recttempete.top, self.recttempete.bottom) and len(self.tempete)>0:
                self.isclicked=False
                #Placer le lancement de la tempête ici
            elif position[0] in range(self.rectdepldirect.left, self.rectdepldirect.right) and position[1] in range(self.rectdepldirect.top, self.rectdepldirect.bottom) and len(self.depldirect)>0:
                self.isclicked=False
                #Placer le déplacement direct ici
            elif position[0] in range(self.rectbaston.left, self.rectbaston.right) and position[1] in range(self.rectbaston.top, self.rectbaston.bottom) and (len(self.joueur.getForceUn())>0 or len(self.joueur.getForceDeux())>0 or len(self.joueur.getForceTrois())>0 or len(self.joueur.getForceQuatre())>0):
                self.isclicked=False
                #placer le lancement de la baston ici



        

