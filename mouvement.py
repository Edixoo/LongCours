import pygame

class Mouvement:
    def __init__(self, screen, joueur, listeports) -> None:
        self.screen=screen
        self.joueur=joueur
        self.listeports=listeports

        self.coordonnees=