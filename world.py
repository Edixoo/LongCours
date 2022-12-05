import paquetcarte
import joueurs
import cartedujeu

class world:
    """Constructeur de base du monde"""
    def __init__(self) -> None:
        self.map: cartedujeu.carte #Class à créer
        self.jeudecarte: paquetcarte.paquetdecarte
        self.listejoueur: joueurs.listejoueurs


