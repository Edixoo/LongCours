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
        for i in self.map.zones:
            for w in i.listeport:
                w.marchandise.inflation()  

    def distribuercarte(self) -> None:
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



