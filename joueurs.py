from paquetcarte import *
from marchandises import *
import random

class joueur:
    def __init__(self,pseudos,monnaie):
        self.pseudos = pseudos
        self.paquet = paquetdecarte()
        self.monnaie : int = monnaie
        self.marchandises : marchandises.marchandises
        self.liste_joueurs : str = []
        
    def getPseudos(self):
        return self.pseudos
        
    def getMonnaie(self):
        return self.monnaie

    def ajout_monnaie(self,n):
        self.monnaie += n
    
    def retirer_monnaie(self, n):
        if(n > self.monnaie):
            print("Le montant est supérieur aux portefeuilles du joueur, reesayé")
        elif n <= 0:
            print("Le montant doit etre strictement supérieur à 0, reesayé")
        else:
         self.monnaie -= n

    def retirerCarte(self):
        return self.carte.retirer()#methode a crée
    
    def declencher_combat(self):
        pass
    
    def declencher_tempete(self):
        pass

    def acheter_marchandises(self,marchandises):
        pass
        
    def deplacer(self,zone):
        pass
    
    def revente(self):
        pass
        
        
