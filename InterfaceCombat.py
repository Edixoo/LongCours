import pygame
import joueurs as j
from buttons import Button

class Combat:
    def __init__(self, joueur1, joueur2, screen) -> None:
        self.screen=screen
        self.joueur1: j.joueur =joueur1
        self.choixj1=False
        self.joueur2: j.joueur =joueur2
        self.choixj2=False
        fond= pygame.image.load("./images/Rectangle.png").convert_alpha()
        self.fond=pygame.transform.scale(fond,[900,700])
        self.fondrect=self.fond.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
        fonttitre=pygame.font.SysFont("Arial", 40, True)
        self.titre=fonttitre.render(self.joueur1.pseudo + " vs " + self.joueur2.pseudo, True, "White")

        self.font=pygame.font.SysFont("Arial", 20, True)


        cartebaston=pygame.image.load("./images/carte_baston.png").convert_alpha()

        #Joueur 1
        self.j1cartebastonforce1=pygame.transform.scale(cartebaston,[130,210])
        self.j1rectbastonforce1=self.j1cartebastonforce1.get_rect(center=(self.screen.get_width()/4-100, self.screen.get_height()/2-125))
        self.j1forceun=self.font.render("Force I", True, "black")
        self.j1restantun=self.font.render("Restant: "+ str(len(self.joueur1.getForceUn())), True, "white")

        self.j1cartebastonforce2=pygame.transform.scale(cartebaston,[130,210])
        self.j1rectbastonforce2=self.j1cartebastonforce2.get_rect(center=(self.screen.get_width()/4+75, self.screen.get_height()/2-125))
        self.j1forcedeux=self.font.render("Force II", True, "black")
        self.j1restantdeux=self.font.render("Restant: "+ str(len(self.joueur1.getForceDeux())), True, "white")
        
        self.j1cartebastonforce3=pygame.transform.scale(cartebaston,[130,210])
        self.j1rectbastonforce3=self.j1cartebastonforce3.get_rect(center=(self.screen.get_width()/4-100, self.screen.get_height()/2+150))
        self.j1forcetrois=self.font.render("Force III", True, "black")
        self.j1restanttrois=self.font.render("Restant: "+ str(len(self.joueur1.getForceTrois())), True, "white")

        self.j1cartebastonforce4=pygame.transform.scale(cartebaston,[130,210])
        self.j1rectbastonforce4=self.j1cartebastonforce4.get_rect(center=(self.screen.get_width()/4+75, self.screen.get_height()/2+150))
        self.j1forcequatre=self.font.render("Force IV", True, "black")
        self.j1restantquatre=self.font.render("Restant:"+ str(len(self.joueur1.getForceQuatre())), True, "white")

        #Joueur 2
        self.j2cartebastonforce1=pygame.transform.scale(cartebaston,[130,210])
        self.j2rectbastonforce1=self.j2cartebastonforce1.get_rect(center=(self.screen.get_width()/4*3-75, self.screen.get_height()/2-125))
        self.j2forceun=self.font.render("Force I", True, "black")
        self.j2restantun=self.font.render("Restant:"+ str(len(self.joueur2.getForceUn())), True, "white")

        self.j2cartebastonforce2=pygame.transform.scale(cartebaston,[130,210])
        self.j2rectbastonforce2=self.j2cartebastonforce2.get_rect(center=(self.screen.get_width()/4*3+100, self.screen.get_height()/2-125))
        self.j2forcedeux=self.font.render("Force II", True, "black")
        self.j2restantdeux=self.font.render("Restant:"+ str(len(self.joueur2.getForceDeux())), True, "white")
        
        self.j2cartebastonforce3=pygame.transform.scale(cartebaston,[130,210])
        self.j2rectbastonforce3=self.j2cartebastonforce3.get_rect(center=(self.screen.get_width()/4*3-75, self.screen.get_height()/2+150))
        self.j2forcetrois=self.font.render("Force III", True, "black")
        self.j2restanttrois=self.font.render("Restant:"+ str(len(self.joueur2.getForceTrois())), True, "white")

        self.j2cartebastonforce4=pygame.transform.scale(cartebaston,[130,210])
        self.j2rectbastonforce4=self.j2cartebastonforce4.get_rect(center=(self.screen.get_width()/4*3+100, self.screen.get_height()/2+150))
        self.j2forcequatre=self.font.render("Force IV", True, "black")
        self.j2restantquatre=self.font.render("Restant:"+ str(len(self.joueur2.getForceQuatre())), True, "white")

        self.button=Button([self.screen.get_width()/2, 700], [125,65], "Recommencer", self.screen, 20)
        self.egalite=False
        self.close=Button([self.screen.get_width()/2, 700], [100,50], "Fermer", self.screen, 20)

    def display(self):
        self.screen.blit(self.fond, self.fondrect)
        self.screen.blit(self.titre, self.titre.get_rect(center=[self.screen.get_width()/2, 90]))


        #Joueur 1
        if self.choixj1==False:
            self.screen.blit(self.j1cartebastonforce1, self.j1rectbastonforce1)
            self.screen.blit(self.j1forceun, self.j1forceun.get_rect(center=(self.screen.get_width()/4-100, 290)))
            self.screen.blit(self.j1restantun, self.j1restantun.get_rect(center=(self.screen.get_width()/4-100, 410)))
            
            self.screen.blit(self.j1cartebastonforce2, self.j1rectbastonforce2)
            self.screen.blit(self.j1forcedeux, self.j1forcedeux.get_rect(center=(self.screen.get_width()/4+75, 290)))
            self.screen.blit(self.j1restantdeux, self.j1restantdeux.get_rect(center=(self.screen.get_width()/4+75, 410)))


            self.screen.blit(self.j1cartebastonforce3, self.j1rectbastonforce3)
            self.screen.blit(self.j1forcetrois, self.j1forcetrois.get_rect(center=(self.screen.get_width()/4-100, 566)))
            self.screen.blit(self.j1restanttrois, self.j1restanttrois.get_rect(center=(self.screen.get_width()/4-100, 700)))

            self.screen.blit(self.j1cartebastonforce4, self.j1rectbastonforce4)
            self.screen.blit(self.j1forcequatre, self.j1forcequatre.get_rect(center=(self.screen.get_width()/4+75, 566)))
            self.screen.blit(self.j1restantquatre, self.j1restantquatre.get_rect(center=(self.screen.get_width()/4+75, 700)))
        elif self.choixj2==False and self.choixj1:
            selection=self.font.render( self.joueur1.pseudo + " a sélectionné sa carte", True, "white")
            self.screen.blit(selection, selection.get_rect(center=[self.screen.get_width()/4, self.screen.get_height()/2]))
        #Joueur 2

        if self.choixj2==False:
            self.screen.blit(self.j2cartebastonforce1, self.j2rectbastonforce1)
            self.screen.blit(self.j2forceun, self.j2forceun.get_rect(center=(self.screen.get_width()/4*3-75, 290)))
            self.screen.blit(self.j2restantun, self.j2restantun.get_rect(center=(self.screen.get_width()/4*3-75, 410)))
            
            self.screen.blit(self.j2cartebastonforce2, self.j2rectbastonforce2)
            self.screen.blit(self.j2forcedeux, self.j2forcedeux.get_rect(center=(self.screen.get_width()/4*3+100, 290)))
            self.screen.blit(self.j2restantdeux, self.j2restantdeux.get_rect(center=(self.screen.get_width()/4*3+100, 410)))


            self.screen.blit(self.j2cartebastonforce3, self.j2rectbastonforce3)
            self.screen.blit(self.j2forcetrois, self.j2forcetrois.get_rect(center=(self.screen.get_width()/4*3-75, 566)))
            self.screen.blit(self.j2restanttrois, self.j2restanttrois.get_rect(center=(self.screen.get_width()/4*3-75, 700)))

            self.screen.blit(self.j2cartebastonforce4, self.j2rectbastonforce4)
            self.screen.blit(self.j2forcequatre, self.j2forcequatre.get_rect(center=(self.screen.get_width()/4*3+100, 566)))
            self.screen.blit(self.j2restantquatre, self.j2restantquatre.get_rect(center=(self.screen.get_width()/4*3+100, 700)))
        elif self.choixj1==False and self.choixj2:
            selection=self.font.render( self.joueur2.pseudo + " a sélectionné sa carte", True, "white")
            self.screen.blit(selection, selection.get_rect(center=[self.screen.get_width()/4*3, self.screen.get_height()/2]))
        
        if self.choixj1 and self.choixj2:
            resultat=self.joueur1.testcartebaston(self.cartejoueurun, self.cartejoueurdeux)
            if resultat=="AWin":
                res=self.font.render(self.joueur1.pseudo + " a gagné cette bataille", True, "white")
                self.screen.blit(res, res.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2)))
                self.close.display()
            elif resultat=="BWin":
                res=self.font.render(self.joueur2.pseudo + " a gagné cette bataille", True, "white")
                self.screen.blit(res, res.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2)))
                self.close.display()
            elif resultat=="Equal":
                res=self.font.render("Jeu égal, recommencez", True, "white")
                self.screen.blit(res, res.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2)))
                self.egalite=True
                self.button.display()
                



    def update(self, position):

        if position[0] in range(self.j1rectbastonforce1.left, self.j1rectbastonforce1.right) and position[1] in range(self.j1rectbastonforce1.top, self.j1rectbastonforce1.bottom):
            self.j1cartebastonforce1=pygame.image.load("./images/carte_baston.png").convert_alpha()
            self.j1cartebastonforce1=pygame.transform.scale(self.j1cartebastonforce1, [150,230])
            self.j1rectbastonforce1=self.j1cartebastonforce1.get_rect(center=(self.screen.get_width()/4-100, self.screen.get_height()/2-125))
        else:
            self.j1cartebastonforce1=pygame.image.load("./images/carte_baston.png").convert_alpha()
            self.j1cartebastonforce1=pygame.transform.scale(self.j1cartebastonforce1, [130,210])
            self.j1rectbastonforce1=self.j1cartebastonforce1.get_rect(center=(self.screen.get_width()/4-100, self.screen.get_height()/2-125))
        
        if position[0] in range(self.j1rectbastonforce2.left, self.j1rectbastonforce2.right) and position[1] in range(self.j1rectbastonforce2.top, self.j1rectbastonforce2.bottom):
            self.j1cartebastonforce2=pygame.image.load("./images/carte_baston.png").convert_alpha()
            self.j1cartebastonforce2=pygame.transform.scale(self.j1cartebastonforce2, [150,230])
            self.j1rectbastonforce2=self.j1cartebastonforce2.get_rect(center=(self.screen.get_width()/4+75, self.screen.get_height()/2-125))
        else:
            self.j1cartebastonforce2=pygame.image.load("./images/carte_baston.png").convert_alpha()
            self.j1cartebastonforce2=pygame.transform.scale(self.j1cartebastonforce2, [130,210])
            self.j1rectbastonforce2=self.j1cartebastonforce2.get_rect(center=(self.screen.get_width()/4+75, self.screen.get_height()/2-125))

        if position[0] in range(self.j1rectbastonforce3.left, self.j1rectbastonforce3.right) and position[1] in range(self.j1rectbastonforce3.top, self.j1rectbastonforce3.bottom):
            self.j1cartebastonforce3=pygame.image.load("./images/carte_baston.png").convert_alpha()
            self.j1cartebastonforce3=pygame.transform.scale(self.j1cartebastonforce3, [150,230])
            self.j1rectbastonforce3=self.j1cartebastonforce3.get_rect(center=(self.screen.get_width()/4-100, self.screen.get_height()/2+150))
        else:
            self.j1cartebastonforce3=pygame.image.load("./images/carte_baston.png").convert_alpha()
            self.j1cartebastonforce3=pygame.transform.scale(self.j1cartebastonforce3, [130,210])
            self.j1rectbastonforce3=self.j1cartebastonforce3.get_rect(center=(self.screen.get_width()/4-100, self.screen.get_height()/2+150))

        if position[0] in range(self.j1rectbastonforce4.left, self.j1rectbastonforce4.right) and position[1] in range(self.j1rectbastonforce4.top, self.j1rectbastonforce4.bottom):
            self.j1cartebastonforce4=pygame.image.load("./images/carte_baston.png").convert_alpha()
            self.j1cartebastonforce4=pygame.transform.scale(self.j1cartebastonforce4, [150,230])
            self.j1rectbastonforce4=self.j1cartebastonforce4.get_rect(center=(self.screen.get_width()/4+75, self.screen.get_height()/2+150))
        else:
            self.j1cartebastonforce4=pygame.image.load("./images/carte_baston.png").convert_alpha()
            self.j1cartebastonforce4=pygame.transform.scale(self.j1cartebastonforce4, [130,210])
            self.j1rectbastonforce4=self.j1cartebastonforce4.get_rect(center=(self.screen.get_width()/4+75, self.screen.get_height()/2+150))

        if self.choixj1 and self.choixj2:
            if self.egalite:
                self.button.update(position, "grey")
            else:
                self.close.update(position, "grey")



        #Joueur 2

        if position[0] in range(self.j2rectbastonforce1.left, self.j2rectbastonforce1.right) and position[1] in range(self.j2rectbastonforce1.top, self.j2rectbastonforce1.bottom):
            self.j2cartebastonforce1=pygame.image.load("./images/carte_baston.png").convert_alpha()
            self.j2cartebastonforce1=pygame.transform.scale(self.j2cartebastonforce1, [150,230])
            self.j2rectbastonforce1=self.j2cartebastonforce1.get_rect(center=(self.screen.get_width()/4*3-75, self.screen.get_height()/2-125))
        else:
            self.j2cartebastonforce1=pygame.image.load("./images/carte_baston.png").convert_alpha()
            self.j2cartebastonforce1=pygame.transform.scale(self.j2cartebastonforce1, [130,210])
            self.j2rectbastonforce1=self.j2cartebastonforce1.get_rect(center=(self.screen.get_width()/4*3-75, self.screen.get_height()/2-125))
        
        if position[0] in range(self.j2rectbastonforce2.left, self.j2rectbastonforce2.right) and position[1] in range(self.j2rectbastonforce2.top, self.j2rectbastonforce2.bottom):
            self.j2cartebastonforce2=pygame.image.load("./images/carte_baston.png").convert_alpha()
            self.j2cartebastonforce2=pygame.transform.scale(self.j2cartebastonforce2, [150,230])
            self.j2rectbastonforce2=self.j2cartebastonforce2.get_rect(center=(self.screen.get_width()/4*3+100, self.screen.get_height()/2-125))
        else:
            self.j2cartebastonforce2=pygame.image.load("./images/carte_baston.png").convert_alpha()
            self.j2cartebastonforce2=pygame.transform.scale(self.j2cartebastonforce2, [130,210])
            self.j2rectbastonforce2=self.j2cartebastonforce2.get_rect(center=(self.screen.get_width()/4*3+100, self.screen.get_height()/2-125))

        if position[0] in range(self.j2rectbastonforce3.left, self.j2rectbastonforce3.right) and position[1] in range(self.j2rectbastonforce3.top, self.j2rectbastonforce3.bottom):
            self.j2cartebastonforce3=pygame.image.load("./images/carte_baston.png").convert_alpha()
            self.j2cartebastonforce3=pygame.transform.scale(self.j2cartebastonforce3, [150,230])
            self.j2rectbastonforce3=self.j2cartebastonforce3.get_rect(center=(self.screen.get_width()/4*3-75, self.screen.get_height()/2+150))
        else:
            self.j2cartebastonforce3=pygame.image.load("./images/carte_baston.png").convert_alpha()
            self.j2cartebastonforce3=pygame.transform.scale(self.j2cartebastonforce3, [130,210])
            self.j2rectbastonforce3=self.j2cartebastonforce3.get_rect(center=(self.screen.get_width()/4*3-75, self.screen.get_height()/2+150))

        if position[0] in range(self.j2rectbastonforce4.left, self.j2rectbastonforce4.right) and position[1] in range(self.j2rectbastonforce4.top, self.j2rectbastonforce4.bottom):
            self.j2cartebastonforce4=pygame.image.load("./images/carte_baston.png").convert_alpha()
            self.j2cartebastonforce4=pygame.transform.scale(self.j2cartebastonforce4, [150,230])
            self.j2rectbastonforce4=self.j2cartebastonforce4.get_rect(center=(self.screen.get_width()/4*3+100, self.screen.get_height()/2+150))
        else:
            self.j2cartebastonforce4=pygame.image.load("./images/carte_baston.png").convert_alpha()
            self.j2cartebastonforce4=pygame.transform.scale(self.j2cartebastonforce4, [130,210])
            self.j2rectbastonforce4=self.j2cartebastonforce4.get_rect(center=(self.screen.get_width()/4*3+100, self.screen.get_height()/2+150))

    def checkForInput(self, position):

        #Joueur 1
        if position[0] in range(self.j1rectbastonforce1.left, self.j1rectbastonforce1.right) and position[1] in range(self.j1rectbastonforce1.top, self.j1rectbastonforce1.bottom):
            self.cartejoueurun=self.joueur1.retraitCarteBaston(1)
            if self.cartejoueurun!=False:
                self.choixj1=True
        elif position[0] in range(self.j1rectbastonforce2.left, self.j1rectbastonforce2.right) and position[1] in range(self.j1rectbastonforce2.top, self.j1rectbastonforce2.bottom):
            self.cartejoueurun=self.joueur1.retraitCarteBaston(2)
            if self.cartejoueurun!=False:
                self.choixj1=True
        elif position[0] in range(self.j1rectbastonforce3.left, self.j1rectbastonforce3.right) and position[1] in range(self.j1rectbastonforce3.top, self.j1rectbastonforce3.bottom):
            self.cartejoueurun=self.joueur1.retraitCarteBaston(3)
            if self.cartejoueurun!=False:
                self.choixj1=True
        elif position[0] in range(self.j1rectbastonforce4.left, self.j1rectbastonforce4.right) and position[1] in range(self.j1rectbastonforce4.top, self.j1rectbastonforce4.bottom):
            self.cartejoueurun=self.joueur1.retraitCarteBaston(4)
            if self.cartejoueurun!=False:
                self.choixj1=True
        
        #Joueur 2

        elif position[0] in range(self.j2rectbastonforce1.left, self.j2rectbastonforce1.right) and position[1] in range(self.j2rectbastonforce1.top, self.j2rectbastonforce1.bottom):
            self.cartejoueurdeux=self.joueur2.retraitCarteBaston(1)
            if self.cartejoueurdeux!=False:
                self.choixj2=True
        elif position[0] in range(self.j2rectbastonforce2.left, self.j2rectbastonforce2.right) and position[1] in range(self.j2rectbastonforce2.top, self.j2rectbastonforce2.bottom):
            self.cartejoueurdeux=self.joueur2.retraitCarteBaston(2)
            if self.cartejoueurdeux!=False:
                self.choixj2=True
        elif position[0] in range(self.j2rectbastonforce3.left, self.j2rectbastonforce3.right) and position[1] in range(self.j2rectbastonforce3.top, self.j2rectbastonforce3.bottom):
            self.cartejoueurdeux=self.joueur2.retraitCarteBaston(3)
            if self.cartejoueurdeux!=False:
                self.choixj2=True
        elif position[0] in range(self.j2rectbastonforce4.left, self.j2rectbastonforce4.right) and position[1] in range(self.j2rectbastonforce4.top, self.j2rectbastonforce4.bottom):
            self.cartejoueurdeux=self.joueur2.retraitCarteBaston(4)
            if self.cartejoueurdeux!=False:
                self.choixj2=True
        
        if self.choixj1 and self.choixj2:
            if self.egalite:
                if self.button.checkForInput(position):
                    self.choixj1=False
                    self.choixj2=False
                    self.reset()
            else:
                if self.close.checkForInput(position):
                    return self.joueur1, self.joueur2
        return 0

    def reset(self):
                #Joueur 1
        self.j1restantun=self.font.render("Restant: "+ str(len(self.joueur1.getForceUn())), True, "white")
        self.j1restantdeux=self.font.render("Restant: "+ str(len(self.joueur1.getForceDeux())), True, "white")
        self.j1restanttrois=self.font.render("Restant: "+ str(len(self.joueur1.getForceTrois())), True, "white")
        self.j1restantquatre=self.font.render("Restant:"+ str(len(self.joueur1.getForceQuatre())), True, "white")

        #Joueur 2
        self.j2restantun=self.font.render("Restant:"+ str(len(self.joueur2.getForceUn())), True, "white")
        self.j2restantdeux=self.font.render("Restant:"+ str(len(self.joueur2.getForceDeux())), True, "white")
        self.j2restanttrois=self.font.render("Restant:"+ str(len(self.joueur2.getForceTrois())), True, "white")
        self.j2restantquatre=self.font.render("Restant:"+ str(len(self.joueur2.getForceQuatre())), True, "white")