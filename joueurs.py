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
        self.id:int=id
        
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

    def choixcarte(self,carte:int): #Carte = type de carte à appeler ici : 0 = toutes les cartes, 1 = déplacement direct , 2 = baston , 3 = tempête
        """Fonction permettant de définir quelle carte jouer"""
        choix=-1
        if(len(self.listecartes)==0):
            return False
        """ listchoixcarte=[c.carte] """
        if(carte==0):
            while(int(choix)>=len(self.listecartes) or int(choix)<0):
                numcarte=1
                for i in self.listecartes:
                    
                    print('Carte N°',numcarte)
                    """ listchoixcarte.append(i) """
                    i.affichercarte()
                    numcarte+=1
                print('Quelle carte souhaitez vous jouer ?')
                choix=input()
            choix=int(choix)-1
            return choix
        if(carte==1):
            listechoix:list[int]=[]
            while(int(choix) not in listechoix):
                numcarte=1
                for i in self.listecartes:
                    if(i.type==0):
                        print('Carte N°',numcarte)
                        i.affichercarte()
                        listechoix.append(numcarte)
                    numcarte+=1
                    if(len(listechoix)==0):
                        return False
                print('Quelle carte souhaitez vous jouer ?')
                choix=input()
            choix=int(choix)-1
            return choix
        if(carte==2):
            listechoix:list[int]=[]
            while(int(choix) not in listechoix):
                numcarte=1
                for i in self.listecartes:
                    if(i.type==2):
                        print('Carte N°',numcarte)
                        i.affichercarte()
                        listechoix.append(numcarte)
                    numcarte+=1
                    if(len(listechoix)==0):
                        return False
                print('Quelle carte souhaitez vous jouer ?')
                choix=input()
            choix=int(choix)-1
            return choix
        if(carte==3):
            listechoix:list[int]=[]
            while(int(choix) not in listechoix):
                numcarte=1
                for i in self.listecartes:
                    numcarte+=1
                    if(i.type==1):
                        print('Carte N°',numcarte)
                        i.affichercarte()
                        listechoix.append(numcarte)
                    
                    if(len(listechoix)==0):
                        return False
                print('Quelle carte souhaitez vous jouer ?')
                choix=input()
            choix=int(choix)-1
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
        """Fonction permettant de faire échouer le joueur

        Returns:
            inventaire: inventaire du bateau du joueur ayant échoué
        """
        a=self.bateau.echouer()
        self.posidport=0
        self.posidzone=0
        return a

    def marchandisevendable(self):
        """Fonction permettant de lancer un dé allant de 0 à 5 pour déterminer la marchandise qui sera vendable

        Returns:
            int: indice du type de marchandise vendable
        """
        roll=r.randint(0,5)
        return roll
 
    def deplacementnormal(self):
        """Fonction permettant au joueur de se déplacer sur les cases adjacentes
        """
        print("Souhaitez vous vous déplacer au port le plus proche (port) ou changer de zone ? (zone)")
        choix = input()
        while(choix!="port" and choix!="zone"):
            print("erreur de saisie")
            print("Souhaitez vous vous déplacer au port le plus proche (port) ou changer de zone ? (zone)")
            choix = input()
        if(choix=="port"):
            choixport=[0,1,2,3]
            print("Dans quel port souhaitez vous aller ?")
            i=0
            while(i<len(choixport)):
                if(choixport[i]==self.posidport):
                    i=i
                else:
                    if(i==3):
                        print("Le cimetière ?(",i+1,")")
                    else:
                        print("Le port ? (",i+1,")")
                i+=1
            choixportuser=input()
            self.posidport=int(choixportuser)
        else:
            if(self.posidzone==0):
                print("Zone disponibles : 1 / 5")
                choixzoneuser=input()
                while(int(choixzoneuser)!=1 and int(choixzoneuser)!=5):
                    print("Erreur de saisie")
                    print("Zone disponibles : 1 / 5")
                    choixzoneuser=input() 
                print("Déplacement vers la zone",choixzoneuser,"(le port sera le 0)")
                self.posidzone=int(choixzoneuser)
                self.posidport=0
            else:
                if(self.posidzone==5):
                    print("Zone disponibles : 0 / 4")
                    choixzoneuser=input()
                    while(int(choixzoneuser)!=0 and int(choixzoneuser)!=4):
                        print("Erreur de saisie")
                        print("Zone disponibles : 0 / 4")
                        choixzoneuser=input() 
                    print("Déplacement vers la zone",choixzoneuser,"(le port sera le 0)")
                    self.posidzone=int(choixzoneuser)
                    self.posidport=0
                else:
                    print("Zones disponibles:",self.posidzone-1,"/",self.posidzone+1)
                    choixzoneuser=input()
                    while(int(choixzoneuser)!=self.posidzone-1 and int(choixzoneuser)!=self.posidzone+1):
                        print("Erreur de saisie")
                        print("Zones disponibles:",self.posidzone-1,"/",self.posidzone+1)
                        choixzoneuser=input() 
                    print("Déplacement vers la zone",choixzoneuser,"(le port sera le 0)")
                    self.posidzone=int(choixzoneuser)
                    self.posidport=0

    def vendre(self,typemarch:int):
        """Fonction permettant au joueur de vendre une ressource sur le port où il se trouve"""
        match typemarch:
            case 0:
                qtt = self.bateau.inventaire.getGold()
                qtt=int(qtt)
                print("Vous pouvez vendre:",qtt,"or, combien voulez-vous en vendre ?")
                choix=input()
                while(choix<0 or choix>qtt):
                    print("Erreur dans le nombre choisis")
                    print("Vous pouvez vendre:",qtt,"or, combien voulez-vous en vendre ?")
                    choix=input()
                print("Vous avez décidé d'en vendre:",choix)
                prixacq=self.bateau.inventaire.retirer(qtt,typemarch)
                prixacq=3*prixacq
                self.ajout_monnaie(prixacq)
                print("Cette vente vous a rapporté",prixacq,"$")

            case 1:
                print("Après lancé du dè, vous pouvez vendre du textile")
                qtt = int(self.bateau.inventaire.getTextile())
                if(qtt=="vide"):
                    print("Vous n'avez pas de textile à vendre")
                    return 0
                qtt=int(qtt)
                print("Vous pouvez vendre:",qtt,"textile, combien voulez-vous en vendre ?")
                choix=input()
                while(choix<0 or choix>qtt):
                    print("Erreur dans le nombre choisis")
                    print("Vous pouvez vendre:",qtt,"textile, combien voulez-vous en vendre ?")
                    choix=input()
                print("Vous avez décidé d'en vendre:",choix)
                prixacq=self.bateau.inventaire.retirer(qtt,typemarch)
                prixacq=3*prixacq
                self.ajout_monnaie(prixacq)
                print("Cette vente vous a rapporté",prixacq,"$")
            case 2:
                print("Après lancé du dè, vous pouvez vendre du bois")
                qtt = int(self.bateau.inventaire.getBois())
                if(qtt=="vide"):
                    print("Vous n'avez pas de bois à vendre")
                    return 0
                qtt=int(qtt)
                print("Vous pouvez vendre:",qtt,"bois, combien voulez-vous en vendre ?")
                choix=input()
                while(choix<0 or choix>qtt):
                    print("Erreur dans le nombre choisis")
                    print("Vous pouvez vendre:",qtt,"bois, combien voulez-vous en vendre ?")
                    choix=input()
                print("Vous avez décidé d'en vendre:",choix)
                prixacq=self.bateau.inventaire.retirer(qtt,typemarch)
                prixacq=3*prixacq
                self.ajout_monnaie(prixacq)
                print("Cette vente vous a rapporté",prixacq,"$")
            case 3:
                print("Après lancé du dè, vous pouvez vendre du pétrole")
                qtt = int(self.bateau.inventaire.getPetrole())
                if(qtt=="vide"):
                    print("Vous n'avez pas de pétrole à vendre")
                    return 0
                qtt=int(qtt)
                print("Vous pouvez vendre:",qtt,"pétrole, combien voulez-vous en vendre ?")
                choix=input()
                while(choix<0 or choix>qtt):
                    print("Erreur dans le nombre choisis")
                    print("Vous pouvez vendre:",qtt,"pétrole, combien voulez-vous en vendre ?")
                    choix=input()
                print("Vous avez décidé d'en vendre:",choix)
                prixacq=self.bateau.inventaire.retirer(qtt,typemarch)
                prixacq=3*prixacq
                self.ajout_monnaie(prixacq)
                print("Cette vente vous a rapporté",prixacq,"$")
            case 4:
                print("Après lancé du dè, vous pouvez vendre des céréales")
                qtt = int(self.bateau.inventaire.getCereale())
                if(qtt=="vide"):
                    print("Vous n'avez pas de céréales à vendre")
                    return 0
                qtt=int(qtt)
                print("Vous pouvez vendre:",qtt,"céréales, combien voulez-vous en vendre ?")
                choix=input()
                while(int(choix)<0 or int(choix)>qtt):
                    print("Erreur dans le nombre choisis")
                    print("Vous pouvez vendre:",qtt,"céréales, combien voulez-vous en vendre ?")
                    choix=input()
                print("Vous avez décidé d'en vendre:",choix)
                prixacq=self.bateau.inventaire.retirer(qtt,typemarch)
                prixacq=3*prixacq
                self.ajout_monnaie(prixacq)
                print("Cette vente vous a rapporté",prixacq,"$")
            case 5:
                print("Après lancé du dè, vous pouvez vendre des machines à outils")
                qtt = int(self.bateau.inventaire.getMachineOutils())
                if(qtt=="vide"):
                    print("Vous n'avez pas de machine à outils à vendre")
                    return 0
                qtt=int(qtt)
                print("Vous pouvez vendre:",qtt,"machine à outils, combien voulez-vous en vendre ?")
                choix=input()
                while(choix<0 or choix>qtt):
                    print("Erreur dans le nombre choisis")
                    print("Vous pouvez vendre:",qtt,"machine à outils, combien voulez-vous en vendre ?")
                    choix=input()
                print("Vous avez décidé d'en vendre:",choix)
                prixacq=self.bateau.inventaire.retirer(qtt,typemarch)
                prixacq=3*prixacq
                self.ajout_monnaie(prixacq)
                print("Cette vente vous a rapporté",prixacq,"$")
            
            
            
            
        
    


    




"""  

    
    
    

    def acheter_marchandises(self,port):
        pass
        
    def deplacer(self,zone):
        pass
    
    def revente(self,port):
        pass
        
        
"""