import paquetcarte
import joueurs
import cartedujeu
import random as rd

class world:
    """Constructeur de base du monde"""
    def __init__(self) -> None:
        self.map: cartedujeu.cartejeu #Class à créer
        self.jeudecarte: paquetcarte.paquetdecarte
        self.listejoueur: list[joueurs.joueur]
        self.nbtour : int
        self.jeuon: bool

    




    def inflation(self) -> None:
        """Fonction d'appel de l'inflation, permettant d'augmenter les prix des marchandises dans les ports de 5% """
        for i in self.map.zones:
            for w in i.listeport:
                w.marchandise.inflation()  

    def definirjoueurs(self):
        """Fonction de création des joueurs"""
        nbjoueur = 0
        while (nbjoueur<1 or nbjoueur>6):
            print('Combien de joueurs désirez vous ?')
            nbjoueur=input()
        for i in range (nbjoueur):
            print('Joueur',i+1,'Quel pseudo désirez vous ?')
            pseudo=input()
            couleur=0
            print('Quelle couleur désirez vous ?')
            couleur=input()
            self.listejoueur.append(joueurs.joueur(pseudo,couleur))

    def distribuercarte(self) -> None:
            """Fonction de distribution des cartes (utile au début de la partie)"""
            nbcarte = len(self.jeudecarte.listecartemouv)+len(self.jeudecarte.listecartebdf)+len(self.jeudecarte.listecartetemp)
            nbjoueur = len(self.listejoueur)
            cartesbdf = self.jeudecarte.listecartebdf
            cartesmouv = self.jeudecarte.listecartemouv
            cartestemp = self.jeudecarte.listecartetemp
            rd.shuffle(cartesbdf)
            rd.shuffle(cartesmouv)
            rd.shuffle(cartestemp)
            if(nbcarte%nbjoueur!=0):
                del cartesbdf[rd.randint(0,len(cartesbdf)-1)]
            paquet=cartesbdf+cartesmouv+cartestemp
            for i in range(0,len(paquet)):
                numjou=0
                self.listejoueur[numjou].listecartes.append(paquet[0])
                del paquet[0]
                numjou+=1
                if (numjou==nbjoueur):
                    numjou=0
    def obtind(self,ind):
        port=self.listejoueur[ind].posidport
        zone=self.listejoueur[ind].posidzone
        return zone,port
    def echouer(self,zone,port):
        for i in self.listejoueur:
            if(i.posidport==port and i.posidzone==zone):
                a=i.echouer()
                self.map.zones[zone].cimetière.inventaire+=a


            
    def tourdejeu(self,jou:joueurs.joueur):
        """Fonction permettant au joueur de jouer son tour"""
        print('Que souhaitez vous faire ? \n Vous déplacer (mouvement normal) ? [0] \n Vendre ? [1] \n Acheter ? [2] \n Jouer une carte ? [3]\n')
        choix=input()
        match choix:
            case 0:
                jou.deplacementnormal()
            case 1:
                jou.vendre()
            case 2:
                jou.acheter()
            case 3:
                cartechoix=jou.choixcarte()
                cartechoix=jou.SelectEtRetraitCarte(cartechoix)
                if(cartechoix.type==0):
                    a,b=cartechoix.use()
                if(cartechoix.type==1):
                    indcible=-1
                    while(indcible>=len(self.listejoueur) or indcible<0):
                        indcible=cartechoix.use()
                    zone,port=self.obtind(indcible)
                    self.echouer(zone,port)
                    
                if(cartechoix.type==2):
    
        



    
    

            



