import paquetcarte
import joueurs
import cartedujeu

class world:
    """Constructeur de base du monde"""
    def __init__(self) -> None:
        self.map: cartedujeu.cartejeu #Class à créer
        self.jeudecarte: paquetcarte.paquetdecarte
        self.listejoueur: joueurs.listejoueurs
        self.nbtour : int
        self.jeuon: bool

    def inflation(self) -> None:
        for i in self.map.zones:
            for w in i.listeport:
                w.marchandise.inflation()        

