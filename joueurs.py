import cartes as c
import bateau as b


class joueur:
    def __init__(self,pseudo: str, couleur:str):
        self.pseudo:str =pseudo
        self.couleur:str =couleur 
        self.bateau:b.bateau = b.bateau(couleur)
        self.monnaie:int= 2000
        self.listecartes: list[c.carte] =[]
        self.posidzone:int =0
        self.posidport:int =0
        
    def getPseudo(self):
        """Fonction d'obtention du pseudo du joueur"""
        return self.pseudo
        
    def getMonnaie(self):
        """Fonction d'obtention de l'argent du joueur"""
        return self.monnaie

    def ajout_monnaie(self,n:int):
        """Fonction d'ajout d'un montant N d'argent au joueur"""
        self.monnaie += n
    
    def retirer_monnaie(self, n:int):
        """Fonction de retrait d'un montant N d'argent au joueur"""
        if(n > self.monnaie):
            print("Le montant est supérieur au portefeuille du joueur, reesayez")
        elif n <= 0:
            print("Le montant doit etre strictement supérieur à 0, reesayez")
        else:
         self.monnaie -= n

    def jouercarte(self, indcarte):
        """Fonction permettant au joueur de jouer une carte"""
        if(indcarte>=len(self.listecartes) or indcarte<0):
            return 0
        cartejoue=self.listecartes[indcarte]
        del self.listecartes[indcarte]
        return cartejoue

"""  

    
    
    

    def acheter_marchandises(self,port):
        pass
        
    def deplacer(self,zone):
        pass
    
    def revente(self,port):
        pass
        
        
"""