import pygame
import port, portgraphique, CartesGraphique
import marchandises
import cimetiere
import inventaire
import InventaireGraphique
import joueurs
from cimetiereGraphique import CimetiereGraphique
import joueurGraphique
import zone
import cartedujeu, world

position=[[(285,195),(216,267),(124,214),(222,131)],[(289,84),(506,124),(669,42),(435,184)],[(753,206),(719,332),(592,194),(682,243)],[(549,390),(647,462),(604,543),(524,446)],[(605,622),(528,756),(307,638),(455,588)],[(193,558),(102,526),(258,366),(249,594)]]

class Map:
    def __init__(self,listejoueurs: list[joueurs.joueur], listezones: list[zone.zonedejeu], marchandise, position=position) -> None:
        self.screen=pygame.display.set_mode((922,800))
        self.running = True
        self.clock=pygame.time.Clock()
        pygame.display.set_caption("Long Cours")
        
        self.text=""
        self.positionport=position
        self.listezones=listezones
        self.portgraphique=[]
        self.marchandise=
        for i in range (len(self.listezones)):
            for j in range(len(self.listezones[i].listeport)):
                    self.portgraphique.append(portgraphique.Portgraphique(self.listezones[i].listeport[j],self.positionport[i][j][0],self.positionport[i][j][1],self.screen))
                
            self.portgraphique.append(CimetiereGraphique(self.positionport[i][3], self.listezones[i].cimetiere, self.screen))

        self.listejoueurs=[]
        for i in listejoueurs:
            self.listejoueurs.append(joueurGraphique.joueurGraphique(self.screen,i, self.portgraphique[0]))
        
        self.joueuractuel=listejoueurs[0]
        self.inventaire=InventaireGraphique.InventaireGraphique(self.screen, self.joueuractuel.bateau.inventaire)
        

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running= False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                for i in self.portgraphique:
                    i.checkforInput(pygame.mouse.get_pos())

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
        for i in self.portgraphique:
            if type(i)==portgraphique.Portgraphique:
                i.update(pygame.mouse.get_pos(), self.text)
            else:
                i.update(pygame.mouse.get_pos())

    def display(self):
        image=pygame.image.load("./MapSAE/Test.png").convert()
        map= pygame.transform.scale(image, (922, 800))
        self.screen.blit(map,(0,0))
        self.inventaire.display()
        for i in self.portgraphique:
            i.display()
        self.joueuractuel.display()
        for i in self.portgraphique:
            if type(i)==portgraphique.Portgraphique:
                if i.isclicked:
                    i.afficher_interface()
                    if i.clickachat:
                        i.acheter.display(self.joueur)
                    elif i.clickvente:
                        i.vendre.display(self.joueur, self.marchandise)
                    else:
                        self.text=""
            else:
                if i.cimeclicked:
                    i.afficher_interface()
                    if i.invclick:
                        i.inventaire.afficher_inv()

        if self.inventaire.isclickedinv:
            self.inventaire.afficher_inv()

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)
    
    def changementdetour(self, marchandise, joueur):
        self.joueuractuel=joueur
        self.


listejoueur=world.world()
listejoueur.definirjoueurs()
listejoueur=listejoueur.listejoueur
listezone=cartedujeu.cartejeu().zones
pygame.init()
joueur= joueurs.joueur(1, "Salut", "yellow")
game=Map(listejoueur, listezone)


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