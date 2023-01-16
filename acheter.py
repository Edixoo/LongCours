import pygame
import pygame_gui
import inputtextbox
import joueurs

class Acheter:
    def __init__(self, marchandise, joueur: joueurs.joueur, screen) -> None:
        self.screen=screen
        self.marchandise= marchandise
        self.argentjoueur=joueur.monnaie
        self.textbox=pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 275), (900, 50)),self.screen)