import paquetcarte
import joueurs
import cartedujeu
import random as rd
import marchandises as march

class world:
    """Constructeur de base du monde"""
    def __init__(self) -> None:
        self.map: cartedujeu.cartejeu = cartedujeu.cartejeu()
        self.jeudecarte: paquetcarte.paquetdecarte = paquetcarte.paquetdecarte() 
        self.listejoueur: list[joueurs.joueur] 
        self.nbtour : int =0
        self.jeuon: bool = True
        self.listejoueur=[]
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
            nbjoueur=int(input())
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
            if(nbcarte%nbjoueur!=0): #Le jeu de carte contient 36 cartes, si 5 joueurs, retrait d'une carte
                del cartesbdf[rd.randint(0,len(cartesbdf)-1)]
            paquet=cartesbdf+cartesmouv+cartestemp
            numjou=0
            for i in range(0,len(paquet)):
                
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
                self.map.zones[zone].cimetiere.inventaire.bois+=a.bois
                self.map.zones[zone].cimetiere.inventaire.gold+=a.gold
                self.map.zones[zone].cimetiere.inventaire.cereale+=a.cereale
                self.map.zones[zone].cimetiere.inventaire.machine_outils+=a.machine_outils
                self.map.zones[zone].cimetiere.inventaire.petrole+=a.petrole
                self.map.zones[zone].cimetiere.inventaire.textile+=a.textile
    
    def tourdejeu(self,jou:joueurs.joueur):
        """Fonction permettant au joueur de jouer son tour"""
        print('Que souhaitez vous faire ? Joueur',jou.id+1,'\n Vous déplacer (mouvement normal) ? [0] \n Vendre ? [1] \n Acheter ? [2] \n Jouer une carte ? [3]\n')
        choix=int(input())
        match choix:
            case 0:
                jou.deplacementnormal()
            case 1:
                a=jou.vendre()
            case 2:
                a=jou.acheter()
            case 3:
                cartechoix=jou.choixcarte(0)
                cartechoix=jou.SelectEtRetraitCarte(cartechoix)
                if(cartechoix.type==0): #Carte deplacement instantannée choisie
                    a,b=cartechoix.use()
                    jou.mouvement(a,b)
                if(cartechoix.type==1): #Carte tempête choisie
                    indcible=-1
                    while(indcible>=len(self.listejoueur) or indcible<0):
                        indcible=cartechoix.use()
                    zone,port=self.obtind(indcible)
                    self.echouer(zone,port)
                if(cartechoix.type==2): #Carte bras de fer
                    listecible:list[joueurs.joueur]=[]
                    for j in self.listejoueur:
                        if(jou.posidport == j.posidport and jou.posidzone == j.posidzone and jou.id!=j.id):
                            listecible.append(j)
                    cible=-1
                    print("Qui est votre cible ?")
                    for i in listecible:
                        print("Le joueur", i.id+1,"?")
                    cible+=int(input())
                    print("Début du BRAS DE FER !")

                    combat=0
                    forceattaq=0
                    forcedef=0
                    while(combat==0):
                        print("Joueur",jou.id+1)
                        forceattaq=cartechoix.use()
                        print("Joueur",cible+1,"Souhaitez-vous vous défendre ? (Oui: 0 | Non: 1)")
                        choixattq=int(input())
                        if(choixattq==1):
                            self.listejoueur[jou.id].bateau.inventaire.bois+=self.listejoueur[cible].bateau.inventaire.bois
                            self.listejoueur[jou.id].bateau.inventaire.gold+=self.listejoueur[cible].bateau.inventaire.gold
                            self.listejoueur[jou.id].bateau.inventaire.cereale+=self.listejoueur[cible].bateau.inventaire.cereale
                            self.listejoueur[jou.id].bateau.inventaire.machine_outils+=self.listejoueur[cible].bateau.inventaire.machine_outils
                            self.listejoueur[jou.id].bateau.inventaire.petrole+=self.listejoueur[cible].bateau.inventaire.petrole
                            self.listejoueur[jou.id].bateau.inventaire.textile+=self.listejoueur[cible].bateau.inventaire.textile
                            self.listejoueur[cible].bateau.inventaire.nettoyer()
                            combat=1
                        else:
                            carteattaque=self.listejoueur[cible].choixcarte(2)
                            carteattaque=self.listejoueur[cible].SelectEtRetraitCarte(carteattaque)
                            forcedef=carteattaque.use()
                            print("Joueur",cible+1)
                            print("Votre puissance est de :",forcedef)
                            print("Celle de votre adversaire:",forceattaq)
                            while(1):
                                while(forcedef>forceattaq):
                                    print("Joueur",jou.id+1,"Voulez vous jouer une autre carte bras de fer ? (Oui: 0 | Non: 1)")
                                    choixattaquant=input()
                                    choixattaquant=int(choixattaquant)
                                    if(choixattaquant==1):
                                        self.listejoueur[cible].bateau.inventaire.bois+=self.listejoueur[jou.id].bateau.inventaire.bois
                                        self.listejoueur[cible].bateau.inventaire.gold+=self.listejoueur[jou.id].bateau.inventaire.gold
                                        self.listejoueur[cible].bateau.inventaire.cereale+=self.listejoueur[jou.id].bateau.inventaire.cereale
                                        self.listejoueur[cible].bateau.inventaire.machine_outils+=self.listejoueur[jou.id].bateau.inventaire.machine_outils
                                        self.listejoueur[cible].bateau.inventaire.petrole+=self.listejoueur[jou.id].bateau.inventaire.petrole
                                        self.listejoueur[cible].bateau.inventaire.textile+=self.listejoueur[jou.id].bateau.inventaire.textile
                                        self.listejoueur[jou.id].bateau.inventaire.nettoyer()
                                        combat=1
                                    else:
                                        carteattaquant=self.listejoueur[jou.id].choixcarte(2)
                                        if(carteattaquant!=False):
                                            carteattaquant=self.listejoueur[jou.id].SelectEtRetraitCarte(carteattaquant)
                                            if(carteattaquant.type!=2):
                                                print("Vous n'avez pas sélectionné une carte bras de fer, vous perdez ce bras de fer et la carte sélectionnée")
                                                self.listejoueur[cible].bateau.inventaire.bois+=self.listejoueur[jou.id].bateau.inventaire.bois
                                                self.listejoueur[cible].bateau.inventaire.gold+=self.listejoueur[jou.id].bateau.inventaire.gold
                                                self.listejoueur[cible].bateau.inventaire.cereale+=self.listejoueur[jou.id].bateau.inventaire.cereale
                                                self.listejoueur[cible].bateau.inventaire.machine_outils+=self.listejoueur[jou.id].bateau.inventaire.machine_outils
                                                self.listejoueur[cible].bateau.inventaire.petrole+=self.listejoueur[jou.id].bateau.inventaire.petrole
                                                self.listejoueur[cible].bateau.inventaire.textile+=self.listejoueur[jou.id].bateau.inventaire.textile
                                                self.listejoueur[jou.id].bateau.inventaire.nettoyer()
                                                combat=1                                        
                                            forceattaq+=carteattaquant.use()
                                            print("Joueur",jou.id+1)
                                            print("Votre puissance est de :",forceattaq)
                                            print("Celle de votre adversaire:",forcedef)
                                        else:
                                            print("Vous n'avez plus de carte baston à jouer, vous perdez le combat")
                                            self.listejoueur[cible].bateau.inventaire.bois+=self.listejoueur[jou.id].bateau.inventaire.bois
                                            self.listejoueur[cible].bateau.inventaire.gold+=self.listejoueur[jou.id].bateau.inventaire.gold
                                            self.listejoueur[cible].bateau.inventaire.cereale+=self.listejoueur[jou.id].bateau.inventaire.cereale
                                            self.listejoueur[cible].bateau.inventaire.machine_outils+=self.listejoueur[jou.id].bateau.inventaire.machine_outils
                                            self.listejoueur[cible].bateau.inventaire.petrole+=self.listejoueur[jou.id].bateau.inventaire.petrole
                                            self.listejoueur[cible].bateau.inventaire.textile+=self.listejoueur[jou.id].bateau.inventaire.textile
                                            self.listejoueur[jou.id].bateau.inventaire.nettoyer()
                                            combat=1
                                while(forceattaq>forcedef):
                                    print("Joueur",cible+1,"Voulez vous jouer une autre carte bras de fer ? (Oui: 0 | Non: 1)")
                                    choixattq=int(input())
                                    if(choixattq==1):
                                        self.listejoueur[jou.id].bateau.inventaire.bois+=self.listejoueur[cible].bateau.inventaire.bois
                                        self.listejoueur[jou.id].bateau.inventaire.gold+=self.listejoueur[cible].bateau.inventaire.gold
                                        self.listejoueur[jou.id].bateau.inventaire.cereale+=self.listejoueur[cible].bateau.inventaire.cereale
                                        self.listejoueur[jou.id].bateau.inventaire.machine_outils+=self.listejoueur[cible].bateau.inventaire.machine_outils
                                        self.listejoueur[jou.id].bateau.inventaire.petrole+=self.listejoueur[cible].bateau.inventaire.petrole
                                        self.listejoueur[jou.id].bateau.inventaire.textile+=self.listejoueur[cible].bateau.inventaire.textile
                                        self.listejoueur[cible].bateau.inventaire.nettoyer()
                                        combat=1
                                    else:
                                        cartedef=self.listejoueur[jou.id].choixcarte(2)
                                        if(cartedef!=False):
                                            cartedef=self.listejoueur[jou.id].SelectEtRetraitCarte(cartedef)
                                            if(cartedef.type!=2):
                                                print("Vous n'avez pas sélectionné une carte bras de fer, vous perdez ce bras de fer et la carte sélectionnée")
                                                self.listejoueur[jou.id].bateau.inventaire.bois+=self.listejoueur[cible].bateau.inventaire.bois
                                                self.listejoueur[jou.id].bateau.inventaire.gold+=self.listejoueur[cible].bateau.inventaire.gold
                                                self.listejoueur[jou.id].bateau.inventaire.cereale+=self.listejoueur[cible].bateau.inventaire.cereale
                                                self.listejoueur[jou.id].bateau.inventaire.machine_outils+=self.listejoueur[cible].bateau.inventaire.machine_outils
                                                self.listejoueur[jou.id].bateau.inventaire.petrole+=self.listejoueur[cible].bateau.inventaire.petrole
                                                self.listejoueur[jou.id].bateau.inventaire.textile+=self.listejoueur[cible].bateau.inventaire.textile
                                                self.listejoueur[cible].bateau.inventaire.nettoyer()
                                                combat=1
                                            forcedef+=cartedef.use()
                                            print("Joueur",cible+1)
                                            print("Votre puissance est de :",forcedef)
                                            print("Celle de votre adversaire:",forceattaq)
                                        else:
                                            print("Joueur",cible+1,"Vous n'avez plus de carte baston à jouer, vous perdez")
                                            self.listejoueur[jou.id].bateau.inventaire.bois+=self.listejoueur[cible].bateau.inventaire.bois
                                            self.listejoueur[jou.id].bateau.inventaire.gold+=self.listejoueur[cible].bateau.inventaire.gold
                                            self.listejoueur[jou.id].bateau.inventaire.cereale+=self.listejoueur[cible].bateau.inventaire.cereale
                                            self.listejoueur[jou.id].bateau.inventaire.machine_outils+=self.listejoueur[cible].bateau.inventaire.machine_outils
                                            self.listejoueur[jou.id].bateau.inventaire.petrole+=self.listejoueur[cible].bateau.inventaire.petrole
                                            self.listejoueur[jou.id].bateau.inventaire.textile+=self.listejoueur[cible].bateau.inventaire.textile
                                            self.listejoueur[cible].bateau.inventaire.nettoyer()
                                            combat=1
                    if(forceattaq>forcedef):
                        gagnant=jou.id+1
                    else:
                        gagnant=cible+1
                    print("Bras de fer terminé, Bravo",gagnant,"! ")
    
    def jouerpartie(self):
        self.definirjoueurs()
        self.distribuercarte()
        while(self.jeuon==True):
            for jou in self.listejoueur:
                self.tourdejeu(jou)
                if(len(jou.listecartes)==0):
                    print("Joueur",jou.id+1,"vous n'avez plus de carte à jouer, vous avez donc perdu")
                    del self.listejoueur[jou.id]
            if(len(self.listejoueur)==1):
                print("Joueur",self.listejoueur[0].id+1,"BRAVO ! Vous avez gagné avec",self.listejoueur[0].monnaie,"$")
                self.jeuon=False
            self.inflation

                            
                                




                    
                    
                        




    
        



    
    

            



