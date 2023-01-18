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
    def __init__(self,listejoueurs: list[joueurs.joueur], listezones: list[zone.zonedejeu], position=position) -> None:
        self.screen=pygame.display.set_mode((922,800))
        self.running = True
        self.clock=pygame.time.Clock()

        pygame.display.set_caption("Long Cours")

        porte=port.port(1,"cereale","Le Cap")
        self.lecap=portgraphique.Portgraphique(porte,100,100, self.screen)

        self.carte=CartesGraphique.Cartes(marchandises.cereale(150), 150, self.screen.get_width()/2, self.screen.get_height()/2, self.screen)
        
        self.joueur= joueur
        inv= inventaire.inventaire()
        march= marchandises.cereale(150)
        inv.ajouter(march)
        self.inventaire=InventaireGraphique.InventaireGraphique(self.screen, inv)
        cimet=cimetiere.cimetiere()
        self.cimetiere=CimetiereGraphique([150,150],cimet,self.screen)
        self.marchandise= marchandises.cereale(150)
        self.text=""
        self.joueuractuel=joueurGraphique.joueurGraphique(self.screen, self.joueur)
        
        self.positionport=position
        self.listejoueurs=listejoueurs
        self.listezones=listezones
        self.portgraphique=[]
        
        for i in range (len(self.listezones)-1):
            print(len(self.listezones[i].listeport)-1)
            for j in range(3):
                self.portgraphique.append(portgraphique.Portgraphique(self.listezones[i].listeport[j],self.positionport[i][j][0],self.positionport[i][j][1],self.screen))
                
            self.portgraphique.append(CimetiereGraphique(self.positionport[i][3],self.listezones[i].cimetiere, self.screen))
        

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running= False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                self.lecap.checkforInput(pygame.mouse.get_pos())
                self.inventaire.checkforInput(pygame.mouse.get_pos())
                self.cimetiere.checkforInput(pygame.mouse.get_pos())
    
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
        self.lecap.update(pygame.mouse.get_pos(), self.text)
        self.inventaire.update(pygame.mouse.get_pos())
        self.cimetiere.update(pygame.mouse.get_pos())
        for i in self.portgraphique:
            if type(i)==CimetiereGraphique:
                i.update(pygame.mouse.get_pos())
            else:
                i.update(pygame.mouse.get_pos(), self.text)

    def display(self):
        image=pygame.image.load("./MapSAE/Test.png").convert()
        map= pygame.transform.scale(image, (922, 800))
        self.screen.blit(map,(0,0))
        self.lecap.display()
        self.carte.display()
        self.cimetiere.display()
        self.inventaire.display()
        self.joueuractuel.display(self.lecap)
        for i in self.portgraphique:
            i.display()
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
        elif self.cimetiere.cimeclicked:
            self.cimetiere.afficher_interface()
            if self.cimetiere.invclick:
                self.cimetiere.inventaire.afficher_inv()
        else:
            self.screen.blit(map,(0,0))
            self.lecap.display()
            self.cimetiere.display()
            self.inventaire.display()
            self.joueuractuel.display(self.lecap)
            for i in self.portgraphique:
                i.display()

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)


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