import cartes as c
import bateau as b
import random as r

class joueur:
    def __init__(self, id:int ,pseudo: str, couleur:str):
        self.pseudo:str =pseudo
        self.couleur:str =couleur 
        self.bateau:b.bateau = b.bateau(couleur)
        self.monnaie:int= 2000
        self.listecartes: list[c.carte] =[]
        self.posidzone:int =0
        self.posidport:int =0
        self.id:int
        
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

    def choixcarte(self):
        """Fonction permettant de définir quelle carte jouer"""
        choix=-1
        if(len(self.listecartes)==0):
            return False
        
        while(choix>=len(self.listecartes) or choix<0):
            for i in self.listecartes:
                numcarte=1
                print('Carte N°',numcarte)
                i.affichercarte()
                numcarte+=1
            print('Quelle carte souhaitez vous jouer ?')
            choix=input()
        choix=choix-1
        return choix
        
    def SelectEtRetraitCarte(self, choix):
        """Fonction permettant au joueur de jouer une carte"""
        cartejoue=self.listecartes[choix]
        del self.listecartes[choix]
        return cartejoue

    def mouvement(self,idzone,idport):
        """Fonction permettant au joueur de se déplacer"""
        self.posidzone=idzone
        self.posidport=idport

    def echouer(self):
        a=self.bateau.echouer()
        self.posidport=0
        self.posidzone=0
        return a
    
    def acheter(self):
        # A faire
        return 0

    def vendre(self):
        typemarch = r.randint(0,5)
        match typemarch:
            case 0:
                print("Après lancé du dè, vous pouvez vendre de l'or")
                qtt = int(self.bateau.inventaire.getGold())
                if(qtt=="vide"):
                    print("Vous n'avez pas d'or à vendre")
                    return 0
                print("Vous pouvez vendre:",qtt,"or, combien voulez-vous en vendre ?")
                choix=input()
                while(choix<0 or choix>qtt):
                    print("Erreur dans le nombre choisis")
                    print("Vous pouvez vendre:",qtt,"or, combien voulez-vous en vendre ?")
                    choix=input()
                print("Vous avez décidé d'en vendre:",choix)

            case 1:
                print("Après lancé du dè, vous pouvez vendre du textile")
                qtt = int(self.bateau.inventaire.getTextile())
            case 2:
                print("Après lancé du dè, vous pouvez vendre du bois")
                qtt = int(self.bateau.inventaire.getBois())
            case 3:
                print("Après lancé du dè, vous pouvez vendre du pétrole")
                qtt = int(self.bateau.inventaire.getPetrole())
            case 4:
                print("Après lancé du dè, vous pouvez vendre des céréales")
                qtt = int(self.bateau.inventaire.getCereale())
            case 5:
                print("Après lancé du dè, vous pouvez vendre des machines à outils")
                qtt = int(self.bateau.inventaire.getMachineOutils())
            
            
            
            
        
    def deplacementnormal(self):
        # A faire
        return 0


    




"""  

    
    
    

    def acheter_marchandises(self,port):
        pass
        
    def deplacer(self,zone):
        pass
    
    def revente(self,port):
        pass
        
        
"""