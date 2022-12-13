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
        return self.pseudo
        
    def getMonnaie(self):
        return self.monnaie

    def ajout_monnaie(self,n:int):
        self.monnaie += n
    
    def retirer_monnaie(self, n:int):
        if(n > self.monnaie):
            print("Le montant est supérieur au portefeuille du joueur, reesayez")
        elif n <= 0:
            print("Le montant doit etre strictement supérieur à 0, reesayez")
        else:
         self.monnaie -= n

    def jouercarte(self, indcarte):
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