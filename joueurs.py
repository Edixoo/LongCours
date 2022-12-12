import cartes
import bateau


class joueur:
    def __init__(self,pseudo: str, cartes):
        self.pseudo=pseudo
        self.bateau=bateau.bateau
        self.monnaie=2000
        self.listecartes= cartes
        self.positionzone=0
        self.position=0
        
    def getPseudo(self):
        return self.pseudo
        
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

    def retirerCarte(self, carte):
        return self.cartes.pop(carte)

"""  

    
    
    

    def acheter_marchandises(self,port):
        pass
        
    def deplacer(self,zone):
        pass
    
    def revente(self,port):
        pass
        
        
"""