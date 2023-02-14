import pygame
import portgraphique
import marchandises
import InventaireGraphique
import joueurs
from cimetiereGraphique import CimetiereGraphique
import joueurGraphique
import zone
import cartedujeu, world
from buttons import Button, Cancel
import random as rd
import paquetcartegraphique

position=[[(285,195),(216,267),(124,214),(222,131)],[(289,84),(506,124),(669,42),(435,184)],[(753,206),(719,332),(592,194),(682,243)],[(549,390),(647,462),(604,543),(524,446)],[(605,622),(528,756),(307,638),(455,588)],[(193,558),(102,526),(258,366),(249,594)]]
marchandise= [marchandises.cereale(1),marchandises.bois(1),marchandises.gold(1),marchandises.machine_outils(1), marchandises.petrole(1), marchandises.textile(1)]
class Map:
    def __init__(self,listejoueurs: list[joueurs.joueur], listezones: list[zone.zonedejeu], position=position, listemarchandises=marchandise) -> None:
        self.screen=pygame.display.set_mode((922,800))
        self.running = True
        self.clock=pygame.time.Clock()
        pygame.display.set_caption("Long Cours")
        self.mouvcheck=False
        self.deplacement=True
        self.text=""
        self.positionport=position
        self.listezones=listezones
        self.listegraphiques=[]
        self.listeportgraphiques=[]
        self.marchandise: marchandises.marchandises
        for i in range (len(self.listezones)):
            for j in range(len(self.listezones[i].listeport)):
                    self.listeportgraphiques.append(portgraphique.Portgraphique(self.listezones[i].listeport[j],self.positionport[i][j][0],self.positionport[i][j][1],self.screen))
                
            self.listeportgraphiques.append(CimetiereGraphique(self.positionport[i][3], self.listezones[i].cimetiere, self.screen))
            self.listegraphiques.append(self.listeportgraphiques)
            self.listeportgraphiques=[]
        self.listemarchandises=listemarchandises
        self.listejoueursgraphiques=[]
        for i in listejoueurs:
            self.listejoueursgraphiques.append(joueurGraphique.joueurGraphique(self.screen,i, self.listegraphiques[0][0]))
        self.font=pygame.font.SysFont("Arial", 20, True)
        self.listejoueurs=listejoueurs
        self.joueuractuel=listejoueurs[0]
        self.inventaire=InventaireGraphique.InventaireGraphique(self.screen, self.joueuractuel.bateau.inventaire, self.joueuractuel.monnaie)
        self.sedeplacer=Button((self.screen.get_width()-60, self.screen.get_height()-40),[100,50],"Se déplacer",self.screen,20)
        self.changertour=Button((self.screen.get_width()-60,30), [100,50],"Changer Tour", self.screen, 15)
        self.canceldeplacer=Cancel(self.screen.get_width()-180, self.screen.get_height()-40, self.screen)
        
        self.paquetjoueur=paquetcartegraphique.PaquetdeCartes(self.screen, self.joueuractuel)

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running= False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.paquetjoueur.checkforInput(pygame.mouse.get_pos())
                print(pygame.mouse.get_pos())
                for i in range(len(self.listegraphiques)):
                    for j in range(len(self.listegraphiques[i])):
                        if self.joueuractuel.posidport==j and self.joueuractuel.posidzone==i:
                            self.listegraphiques[i][j].checkforInput(pygame.mouse.get_pos())
                self.inventaire.checkforInput(pygame.mouse.get_pos())
                if self.sedeplacer.checkForInput(pygame.mouse.get_pos()):
                    self.mouvcheck=True
                    i=self.mouvement()
                elif self.mouvcheck==True and self.canceldeplacer.checkForInput(pygame.mouse.get_pos()):
                    self.mouvcheck=False
                if self.changertour.checkForInput(pygame.mouse.get_pos()):
                    self.changementdetour()
            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_BACKSPACE:
                    self.text=self.text[:-1]
                if len(self.text)<4:
                    if event.key== pygame.K_0 or event.key==pygame.K_KP0:
                        self.text+="0"
                    elif event.key== pygame.K_1 or event.key==pygame.K_KP1:
                        self.text+="1"
                    elif event.key== pygame.K_2 or event.key==pygame.K_KP2:
                        self.text+="2"
                    elif event.key== pygame.K_3 or event.key==pygame.K_KP3:
                        self.text+="3"
                    elif event.key== pygame.K_4 or event.key==pygame.K_KP4:
                        self.text+="4"
                    elif event.key== pygame.K_5 or event.key==pygame.K_KP5:
                        self.text+="5"
                    elif event.key== pygame.K_6 or event.key==pygame.K_KP6:
                        self.text+="6"
                    elif event.key== pygame.K_7 or event.key==pygame.K_KP7:
                        self.text+="7"
                    elif event.key== pygame.K_8 or event.key==pygame.K_KP8:
                        self.text+="8"
                    elif event.key== pygame.K_9 or event.key==pygame.K_KP9:
                        self.text+="9"

    def update(self):
        self.inventaire.update(pygame.mouse.get_pos())
        for i in self.listegraphiques:
            for j in i:
                if type(j)==portgraphique.Portgraphique:
                    j.update(pygame.mouse.get_pos(), self.text)
                else:
                    j.update(pygame.mouse.get_pos())
        self.changertour.update(pygame.mouse.get_pos(),"grey")
        self.canceldeplacer.update(pygame.mouse.get_pos(),"red")
        self.sedeplacer.update(pygame.mouse.get_pos(), "grey")
        self.paquetjoueur.update(pygame.mouse.get_pos())

    def display(self):
        image=pygame.image.load("./MapSAE/Test.png").convert()
        map= pygame.transform.scale(image, (922, 800))
        self.screen.blit(map,(0,0))
        self.nomjoueuractu=self.font.render("Tour de:" + self.joueuractuel.pseudo, True, "black")
        self.nommarchandise=self.font.render("Marchandise: "+self.marchandise.nom, True, "black")
        self.screen.blit(self.nomjoueuractu, (0,0))
        self.screen.blit(self.nommarchandise, (100,0))
        if self.deplacement:
            self.sedeplacer.display()
        self.changertour.display()
        self.inventaire.display()
        for i in self.listejoueursgraphiques:
            i.display()
        for i in self.listegraphiques:
            for j in i:
                j.display(self.joueuractuel)
        for i in self.listegraphiques:
            for j in i:
                if type(j)==portgraphique.Portgraphique:
                    if j.isclicked:
                        j.afficher_interface(self.joueuractuel)
                        if j.clickachat:
                            j.acheter.display(self.joueuractuel)
                            self.joueuractuel=j.joueur
                            self.inventaire=InventaireGraphique.InventaireGraphique(self.screen, self.joueuractuel.bateau.inventaire, self.joueuractuel.monnaie)
                        elif j.clickvente:
                            j.vendre.display(self.joueuractuel, self.marchandise)
                            self.joueuractuel=j.joueur
                            self.inventaire=InventaireGraphique.InventaireGraphique(self.screen, self.joueuractuel.bateau.inventaire, self.joueuractuel.monnaie)
                        else:
                            self.text=""
                else:
                    if j.cimeclicked:
                        j.afficher_interface()
                        if j.invclick:
                            j.inventaire.afficher_inv()
        self.paquetjoueur.display()
        if self.inventaire.isclickedinv:
            self.inventaire.afficher_inv()
        if self.mouvcheck:
                liste=self.mouvement()
                self.canceldeplacer.display()
                for i in liste:
                    if self.checkforInput(pygame.mouse.get_pos(),i[0])!=False:
                        for j in self.listejoueursgraphiques:
                            if j.joueur==self.joueuractuel:
                                j.move(i[1])
                                for k in range(len(self.listegraphiques)):
                                    if i[1] in self.listegraphiques[k]:
                                        self.joueuractuel.posidport=self.listegraphiques[k].index(i[1])
                                        self.joueuractuel.posidzone=k
                                self.mouvcheck=False
                                self.deplacement=False
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)
    
    def changementdetour(self):
        index=self.listejoueurs.index(self.joueuractuel)
        if index+1<len(self.listejoueurs):
            self.joueuractuel=self.listejoueurs[index+1]
        else:
            self.joueuractuel=self.listejoueurs[0]
        self.marchandise=rd.choice(self.listemarchandises)
        self.paquetjoueur=paquetcartegraphique.PaquetdeCartes(self.screen, self.joueuractuel)
        self.deplacement=True
    
    def mouvement(self):
        self.listemouvement=[]
        rectlist=[]
        liste=self.listegraphiques[self.joueuractuel.posidzone]
        for i in self.listegraphiques[self.joueuractuel.posidzone]:
            if liste.index(i)!=self.joueuractuel.posidport:
                self.listemouvement.append(i)
        if self.joueuractuel.posidzone>0 and self.joueuractuel.posidzone<5:
            self.listemouvement.append(self.listegraphiques[self.joueuractuel.posidzone-1][0])
            self.listemouvement.append(self.listegraphiques[self.joueuractuel.posidzone+1][0])
        elif self.joueuractuel.posidzone==0:
            self.listemouvement.append(self.listegraphiques[self.joueuractuel.posidzone+1][0])
            self.listemouvement.append(self.listegraphiques[-1][0])
        else:
            self.listemouvement.append(self.listegraphiques[0][0])
            self.listemouvement.append(self.listegraphiques[self.joueuractuel.posidzone-1][0])

        for i in self.listemouvement:
            rect=pygame.Rect(i.rect.x+10,i.rect.y+20, 10,10)
            pygame.draw.rect(self.screen, "white", rect)
            rectlist.append((rect,i))
        return rectlist
    
    def checkforInput(self, position, rect):
        if position[0] in range(rect.left, rect.right) and position[1] in range(rect.top, rect.bottom):
            return True
        else:
            return False

listejoueur=world.world()
listejoueur.definirjoueurs()
listejoueur=listejoueur.listejoueur
listezone=cartedujeu.cartejeu().zones
pygame.init()
game=Map(listejoueur, listezone)
game.changementdetour()
game.run()
pygame.quit()


"""
Dans appel de Map:
    - liste de joueurs (bouclé pour les mettre en joueurGraphique) 
    - liste de zones (bouclé pour récupérer la liste de ports puis transformé les ports en portgraphique et le cimetiere en cimetiere graphique)
    - Liste position Listepos[posZone][PosPort] = (Tuple possédant position de la case sur l'interface) --> 0,1,2 --> Port | 3 --> Cimetiere
    fonction changementdetour
    - change le joueur actuel
    
"""