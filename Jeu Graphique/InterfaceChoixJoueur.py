import pygame
from joueurs import joueur as j
from buttons import Button, Cancel

class ChoixJoueur:
    def __init__(self, screen, listej, joueur) -> None:
        self.screen=screen
        self.listejoueur=listej

        self.font=pygame.font.SysFont("Arial", 20)
        self.joueurUn=joueur
        self.fond=pygame.image.load("../images/Rectangle.png")
        self.joueurDeux: j | None
        self.font=pygame.font.SysFont("Arial", 20)

        self.fond= pygame.transform.scale(self.fond, [900,700])
        self.fondrect=self.fond.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
        self.cancel=Cancel(451,697, self.screen)

        self.placement=[[self.screen.get_width()/2-150,self.screen.get_width()/2+150],[self.screen.get_width()/2-200,self.screen.get_width()/2,self.screen.get_width()/2+200],[self.screen.get_height()/2-100,self.screen.get_height()/2+100]] #liste des placements sous forme [[placement double], [placement triple], [etage]]
        self.afficher=False

        self.bouton1=Button([0,0], [0,0], "tt", self.screen, 0)
        self.bouton2=Button([0,0], [0,0], "tt", self.screen, 0)
        self.bouton3=Button([0,0], [0,0], "tt", self.screen, 0)
        self.bouton4=Button([0,0], [0,0], "tt", self.screen, 0)
        self.bouton5=Button([0,0], [0,0], "tt", self.screen, 0)


    def display(self):
        placement=0

        self.screen.blit(self.fond,self.fondrect)
        if len(self.listejoueur)==2:
            for i in self.listejoueur:
                if i!=self.joueurUn:
                    self.joueur1=i
                    nomadverse=self.font.render(i.pseudo, True, "white")
                    rect=nomadverse.get_rect(center=(self.screen.get_width()/2, self.screen.get_height()/2))
                    self.screen.blit(nomadverse, rect)
                    self.bouton1= Button([self.screen.get_width()/2, self.screen.get_height()/2+55], [100,50], "Attaquer", self.screen, 20)
                    self.bouton1.display()
        elif len(self.listejoueur)==3:
            for i in self.listejoueur:
                if i!=self.joueurUn:
                    placement+=1

                    if placement==1:
                        self.joueur1=i
                        nomadverse=self.font.render(i.pseudo, True, "white")
                        rect=nomadverse.get_rect(center=(self.placement[0][0], self.screen.get_height()/2))
                        self.screen.blit(nomadverse, rect)
                        self.bouton1=Button([self.placement[0][0], self.screen.get_height()/2+55], [100,50], "Attaquer", self.screen, 20)
                        self.bouton1.display()
                    
                    if placement==2:
                        self.joueur2=i
                        nomadverse=self.font.render(i.pseudo, True, "white")
                        rect=nomadverse.get_rect(center=(self.placement[0][1], self.screen.get_height()/2))
                        self.screen.blit(nomadverse, rect)
                        self.bouton2=Button([self.placement[0][1], self.screen.get_height()/2+55], [100,50], "Attaquer", self.screen, 20)
                        self.bouton2.display()

        elif len(self.listejoueur)==4:
            for i in self.listejoueur:
                if i!=self.joueurUn:
                    placement+=1

                    if placement==1:
                        self.joueur1=i
                        nomadverse=self.font.render(i.pseudo, True, "white")
                        rect=nomadverse.get_rect(center=(self.placement[0][0], self.placement[2][0]))
                        self.screen.blit(nomadverse, rect)
                        self.bouton1=Button([self.placement[0][0], self.placement[2][0]+55], [100,50], "Attaquer", self.screen, 20)
                        self.bouton1.display()
                    
                    if placement==2:
                        self.joueur2=i
                        nomadverse=self.font.render(i.pseudo, True, "white")
                        rect=nomadverse.get_rect(center=(self.placement[0][1], self.placement[2][0]))
                        self.screen.blit(nomadverse, rect)
                        self.bouton2=Button([self.placement[0][1], self.placement[2][0]+55], [100,50], "Attaquer", self.screen, 20)
                        self.bouton2.display()
                    
                    if placement==3:
                        self.joueur3=i
                        nomadverse=self.font.render(i.pseudo, True, "white")
                        rect=nomadverse.get_rect(center=(self.screen.get_width()/2, self.placement[2][1]))
                        self.screen.blit(nomadverse, rect)
                        self.bouton2=Button([self.screen.get_width()/2, self.placement[2][1]+55], [100,50], "Attaquer", self.screen, 20)
                        self.bouton2.display()

        elif len(self.listejoueur)==5:
            for i in self.listejoueur:
                if i!=self.joueurUn:
                    placement+=1

                    if placement==1:
                        self.joueur1=i
                        nomadverse=self.font.render(i.pseudo, True, "white")
                        rect=nomadverse.get_rect(center=(self.placement[0][0], self.placement[2][0]))
                        self.screen.blit(nomadverse, rect)
                        self.bouton1=Button([self.placement[0][0], self.placement[2][0]+55], [100,50], "Attaquer", self.screen, 20)
                        self.bouton1.display()
                    
                    if placement==2:
                        self.joueur2=i
                        nomadverse=self.font.render(i.pseudo, True, "white")
                        rect=nomadverse.get_rect(center=(self.placement[0][1], self.placement[2][0]))
                        self.screen.blit(nomadverse, rect)
                        self.bouton2=Button([self.placement[0][1], self.placement[2][0]+55], [100,50], "Attaquer", self.screen, 20)
                        self.bouton2.display()
                    
                    if placement==3:
                        self.joueur3=i
                        nomadverse=self.font.render(i.pseudo, True, "white")
                        rect=nomadverse.get_rect(center=(self.placement[0][0], self.placement[2][1]))
                        self.screen.blit(nomadverse, rect)
                        self.bouton3=Button([self.placement[0][0], self.placement[2][1]+55], [100,50], "Attaquer", self.screen, 20)
                        self.bouton3.display()
                    
                    if placement==4:
                        self.joueur4=i
                        nomadverse=self.font.render(i.pseudo, True, "white")
                        rect=nomadverse.get_rect(center=(self.placement[0][1], self.placement[2][1]))
                        self.screen.blit(nomadverse, rect)
                        self.bouton4=Button([self.placement[0][1], self.placement[2][1]+55], [100,50], "Attaquer", self.screen, 20)
                        self.bouton4.display()
                        
        elif len(self.listejoueur)==6:
            for i in self.listejoueur:
                if i!=self.joueurUn:
                    placement+=1

                    if placement==1:
                        self.joueur1=i
                        nomadverse=self.font.render(i.pseudo, True, "white")
                        rect=nomadverse.get_rect(center=(self.placement[1][0], self.placement[2][0]))
                        self.screen.blit(nomadverse, rect)
                        self.bouton1=Button([self.placement[1][0], self.placement[2][0]+55], [100,50], "Attaquer", self.screen, 20)
                        self.bouton1.display()
                    
                    if placement==2:
                        self.joueur2=i
                        nomadverse=self.font.render(i.pseudo, True, "white")
                        rect=nomadverse.get_rect(center=(self.placement[1][1], self.placement[2][0]))
                        self.screen.blit(nomadverse, rect)
                        self.bouton2=Button([self.placement[1][1], self.placement[2][0]+55], [100,50], "Attaquer", self.screen, 20)
                        self.bouton2.display()
                    
                    if placement==3:
                        self.joueur3=i
                        nomadverse=self.font.render(i.pseudo, True, "white")
                        rect=nomadverse.get_rect(center=(self.placement[1][2], self.placement[2][0]))
                        self.screen.blit(nomadverse, rect)
                        self.bouton3=Button([self.placement[1][2], self.placement[2][0]+55], [100,50], "Attaquer", self.screen, 20)
                        self.bouton3.display()
                    
                    if placement==4:
                        self.joueur4=i
                        nomadverse=self.font.render(i.pseudo, True, "white")
                        rect=nomadverse.get_rect(center=(self.placement[0][0], self.placement[2][1]))
                        self.screen.blit(nomadverse, rect)
                        self.bouton4=Button([self.placement[0][0], self.placement[2][1]+55], [100,50], "Attaquer", self.screen, 20)
                        self.bouton4.display()
                    
                    if placement==5:
                        self.joueur5=i
                        nomadverse=self.font.render(i.pseudo, True, "white")
                        rect=nomadverse.get_rect(center=(self.placement[0][1], self.placement[2][1]))
                        self.screen.blit(nomadverse, rect)
                        self.bouton5=Button([self.placement[0][1], self.placement[2][1]+55], [100,50], "Attaquer", self.screen, 20)
                        self.bouton5.display()
        
        self.cancel.display()
                    
    def checkForInput(self, position):
        if self.bouton1.checkForInput(position):
            return self.joueur1
        elif self.bouton2.checkForInput(position):
            return self.joueur2
        elif self.bouton3.checkForInput(position):
            return self.joueur3
        elif self.bouton4.checkForInput(position):
            return self.joueur4
        elif self.bouton5.checkForInput(position):
            return self.joueur5
        elif self.cancel.checkForInput(position):
            return 1
        else:
            return 0
    
    def update(self, position):
        self.bouton1.update(position, "grey")
        self.bouton2.update(position, "grey")
        self.bouton3.update(position, "grey")
        self.bouton4.update(position, "grey")
        self.bouton5.update(position, "grey")
        self.cancel.update(position, "red")