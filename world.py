import paquetcarte
import joueurs
import cartedujeu
import random as rd

class world:
    """Constructeur de base du monde"""
    def __init__(self) -> None:
        self.map: cartedujeu.cartejeu #Class à créer
        self.jeudecarte: paquetcarte.paquetdecarte
        self.listejoueur: list[joueurs.joueur]
        self.nbtour : int
        self.jeuon: bool

    




    def inflation(self) -> None:
        """Fonction d'appel de l'inflation, permettant d'augmenter les prix des marchandises dans les ports de 5% """
        for i in self.map.zones:
            for w in i.listeport:
                w.marchandise.inflation()  

    def definirjoueurs(self):
        """Fonction de création des joueurs"""
        nbjoueur = 0
        while (nbjoueur<1 or nbjoueur>6):
            print('Combien de joueurs désirez vous ?')
            nbjoueur=input()
        for i in range (nbjoueur):
            print('Joueur',i+1,'Quel pseudo désirez vous ?')
            pseudo=input()
            couleur=0
            print('Quelle couleur désirez vous ?')
            couleur=input()
            self.listejoueur.append(joueurs.joueur(i,pseudo,couleur))

    def distribuercarte(self) -> None:
            """Fonction de distribution des cartes (utile au début de la partie)"""
            nbcarte = len(self.jeudecarte.listecartemouv)+len(self.jeudecarte.listecartebdf)+len(self.jeudecarte.listecartetemp)
            nbjoueur = len(self.listejoueur)
            cartesbdf = self.jeudecarte.listecartebdf
            cartesmouv = self.jeudecarte.listecartemouv
            cartestemp = self.jeudecarte.listecartetemp
            rd.shuffle(cartesbdf)
            rd.shuffle(cartesmouv)
            rd.shuffle(cartestemp)
            if(nbcarte%nbjoueur!=0):
                del cartesbdf[rd.randint(0,len(cartesbdf)-1)]
            paquet=cartesbdf+cartesmouv+cartestemp
            for i in range(0,len(paquet)):
                numjou=0
                self.listejoueur[numjou].listecartes.append(paquet[0])
                del paquet[0]
                numjou+=1
                if (numjou==nbjoueur):
                    numjou=0
    def obtind(self,ind):
        port=self.listejoueur[ind].posidport
        zone=self.listejoueur[ind].posidzone
        return zone,port
    def echouer(self,zone,port):
        for i in self.listejoueur:
            if(i.posidport==port and i.posidzone==zone):
                a=i.echouer()
                self.map.zones[zone].cimetiere.inventaire+=a


            
    def tourdejeu(self,jou:joueurs.joueur):
        """Fonction permettant au joueur de jouer son tour"""
        print('Que souhaitez vous faire ? \n Vous déplacer (mouvement normal) ? [0] \n Vendre ? [1] \n Acheter ? [2] \n Jouer une carte ? [3]\n')
        choix=input()
        match choix:
            case 0:
                jou.deplacementnormal()
            case 1:
                jou.vendre()
            case 2:
                jou.acheter()
            case 3:
                cartechoix=jou.choixcarte()
                cartechoix=jou.SelectEtRetraitCarte(cartechoix)
                if(cartechoix.type==0): #Carte deplacement instantannée choisie
                    a,b=cartechoix.use()
                if(cartechoix.type==1): #Carte tempête choisie
                    indcible=-1
                    while(indcible>=len(self.listejoueur) or indcible<0):
                        indcible=cartechoix.use()
                    zone,port=self.obtind(indcible)
                    self.echouer(zone,port)
                if(cartechoix.type==2): #Carte bras de fer
                    listecible=[joueurs]
                    for j in self.listejoueur:
                        if(jou.posidport == j.posidport and jou.posidzone == j.posidzone and jou.id!=j.id):
                            listecible.append(jou)
                    cible=-1
                    print("Qui est votre cible ?")
                    for i in listecible:
                        print("Le joueur", i.id+1,"?")
                    cible+=input()
                    print("Début du BRAS DE FER !")

                    combat=0
                    while(combat==0):
                        print("Joueur",jou.id+1)
                        forceattaq=cartechoix.use()
                        print("Joueur",cible+1,"Souhaitez-vous vous défendre ? (Oui: 0 | Non: 1)")
                        choixattq=input()
                        if(choixattq==1):
                            self.listejoueur[jou.id].bateau.inventaire+=self.listejoueur[cible].bateau.inventaire
                            self.listejoueur[cible].bateau.inventaire.nettoyer()
                            combat=1
                        else:
                            carteattaque=self.listejoueur[cible].choixcarte()
                            carteattaque=self.listejoueur[cible].SelectEtRetraitCarte(carteattaque)
                            forcedef=carteattaque.use()
                            while(forcedef>forceattaq):
                                print("Joueur",jou.id+1,"Voulez vous jouer une autre carte bras de fer ? (Oui: 0 | Non: 1)")
                                choixattaquant=input()
                                if(choixattaquant==1):
                                    self.listejoueur[cible].bateau.inventaire+=self.listejoueur[jou.id].bateau.inventaire
                                    self.listejoueur[jou.id].bateau.inventaire.nettoyer()
                                    combat=1
                                else:
                                    carteattaquant=self.listejoueur[jou.id].choixcarte()
                                    if(carteattaquant!=False):
                                        carteattaquant=self.listejoueur[jou.id].SelectEtRetraitCarte(carteattaquant)
                                        if(carteattaquant.type!=2):
                                            print("Vous n'avez pas sélectionné une carte bras de fer, vous perdez ce bras de fer et la carte sélectionnée")
                                            self.listejoueur[cible].bateau.inventaire+=self.listejoueur[jou.id].bateau.inventaire
                                            self.listejoueur[jou.id].bateau.inventaire.nettoyer()
                                            combat=1                                        
                                        forceattaq=carteattaquant.use()
                                    else:
                                        print("Vous n'avez plus de carte à jouer, vous perdez")
                                        self.listejoueur[cible].bateau.inventaire+=self.listejoueur[jou.id].bateau.inventaire
                                        self.listejoueur[jou.id].bateau.inventaire.nettoyer()
                                        combat=1
                            while(forceattaq>forcedef):
                                print("Joueur",cible+1,"Voulez vous jouer une autre carte bras de fer ? (Oui: 0 | Non: 1)")
                                choixattq=input()
                                if(choixattq==1):
                                    self.listejoueur[jou.id].bateau.inventaire+=self.listejoueur[cible].bateau.inventaire
                                    self.listejoueur[cible].bateau.inventaire.nettoyer()
                                    combat=1
                                else:
                                    cartedef=self.listejoueur[jou.id].choixcarte())
                                    if(cartedef!=False):
                                        cartedef=self.listejoueur[jou.id].SelectEtRetraitCarte(cartedef)
                                        if(cartedef.type!=2):
                                            print("Vous n'avez pas sélectionné une carte bras de fer, vous perdez ce bras de fer et la carte sélectionnée")
                                            self.listejoueur[jou.id].bateau.inventaire+=self.listejoueur[cible].bateau.inventaire
                                            self.listejoueur[cible].bateau.inventaire.nettoyer()
                                            combat=1
                                        forceattaq=cartedef.use()
                                    else:
                                        print("Vous n'avez plus de carte à jouer, vous perdez")
                                        self.listejoueur[jou.id].bateau.inventaire+=self.listejoueur[cible].bateau.inventaire
                                        self.listejoueur[cible].bateau.inventaire.nettoyer()
                                        combat=1
                    print("Bras de fer terminé, Bravo !")
    
    def jouerpartie(self):
        termine=0
        self.definirjoueurs()
        self.distribuercarte()
        while(termine==0):
            for jou in self.listejoueur:
                self.tourdejeu(jou)
                if(len(jou.listecartes)==0):
                    print("Joueur",jou.id+1,"vous n'avez plus de carte à jouer, vous avez donc perdu")
                    del self.listejoueur[jou.id]
            self.inflation

                            
                                




                    
                    
                        




    
        



    
    

            



