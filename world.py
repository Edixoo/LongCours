import paquetcarte
import joueurs
import cartedujeu
import random as rd
import marchandises as march
import random as r

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
        print("_________________________")
        roll=roll=r.randint(0,5)
        match roll:
            case 0:
                print("La marchandise vendable ce tour est : l'or")
            case 1:
                print("La marchandise vendable ce tour est : le textile ")
            case 2:
                print("La marchandise vendable ce tour est : le bois ")
            case 3:
                print("La marchandise vendable ce tour est : le pétrole ")
            case 4:
                print("La marchandise vendable ce tour est : les céréales")
            case 5:
                print("La marchandise vendable ce tour est : les machines à outils ")
        print('Que souhaitez vous faire ? Joueur',jou.id+1,'\n Vous déplacer (mouvement normal) ? [0] \n Vendre ? [1] \n Acheter ? [2] \n Jouer une carte ? [3]\n')
        choix=int(input())
        print("_________________________")
        if(choix==1):
            qttpos=0
            match roll:
                case 0:
                    for ressource in jou.bateau.inventaire.gold:
                        qttpos+=ressource.qttachete
                case 1:
                    for ressource in jou.bateau.inventaire.textile:
                        qttpos+=ressource.qttachete
                case 2:
                    for ressource in jou.bateau.inventaire.bois:
                        qttpos+=ressource.qttachete
                case 3:
                    for ressource in jou.bateau.inventaire.petrole:
                        qttpos+=ressource.qttachete
                case 4:
                    for ressource in jou.bateau.inventaire.cereale:
                        qttpos+=ressource.qttachete
                case 5:
                    for ressource in jou.bateau.inventaire.machine_outils:
                        qttpos+=ressource.qttachete
            if(qttpos==0):
                print("Vous ne pouvez vendre cette ressource ! ")
                while(choix!=0 and choix!=2 and choix!=3):
                    print('Que souhaitez vous faire ? Joueur',jou.id+1,'\n Vous déplacer (mouvement normal) ? [0] \n Acheter ? [2] \n Jouer une carte ? [3]\n')
                    choix=int(input())            
        match choix:
            case 0:
                jou.deplacementnormal()
                print("Vous vous trouver au port",jou.posidport+1,"de la zone",jou.posidzone)
            case 1:
                a=jou.vendre()
            case 2:
                a=jou.acheter()
            case 3:
                cartechoix=jou.choixcarte(0)
                cartechoix=jou.SelectEtRetraitCarte(cartechoix)
                if(cartechoix.type==0): #Carte deplacement instantannée choisie
                    print("_________________________")
                    a,b=cartechoix.use()
                    jou.mouvement(a,b)
                    print("_________________________")
                if(cartechoix.type==1): #Carte tempête choisie
                    indcible=-1
                    while(indcible>=len(self.listejoueur) or indcible<0):
                        indcible=cartechoix.use()
                    zone,port=self.obtind(indcible)
                    self.echouer(zone,port)
                    print("_________________________")
                    print("Tous les bateau dans la zone",zone+1,"port",port+1,"se sont échoués")
                    print("_________________________")
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
                    if(cible<0 or cible>5):
                        print("Pas de cible valide ! Bras de fer impossible. Fin de tour")
                        combat=1
                    else:
                        print("_________________________")
                        print("Début du BRAS DE FER !")
                        combat=0
                        forceattaq=0
                        forcedef=0
                        firstturn=0
                        while(combat==0):
                            if(firstturn==0):
                                forceattaq=cartechoix.force
                                print("_________________________")
                                print("La force de l'attaquant est :",forceattaq,"et celle du défenseur:",forcedef)
                                print("Joueur",cible+1,"Souhaitez-vous vous défendre (Non: 0 | Oui:1)")
                                print("_________________________")
                                choixdef=int(input())
                                while(choixdef!=0 and choixdef!=1):
                                        print("_________________________")
                                        print("Erreur de saisie")
                                        print("La force de l'attaquant est :",forceattaq,"et celle du défenseur:",forcedef)
                                        print("Défenseur joueur",cible+1,"souhaitez vous jouer une nouvelle carte ?")
                                        print("_________________________")
                                        choixdef=int(input)
                                if(choixdef==0):
                                    self.listejoueur[jou.id].bateau.inventaire.bois+=self.listejoueur[cible].bateau.inventaire.bois
                                    self.listejoueur[jou.id].bateau.inventaire.gold+=self.listejoueur[cible].bateau.inventaire.gold
                                    self.listejoueur[jou.id].bateau.inventaire.cereale+=self.listejoueur[cible].bateau.inventaire.cereale
                                    self.listejoueur[jou.id].bateau.inventaire.machine_outils+=self.listejoueur[cible].bateau.inventaire.machine_outils
                                    self.listejoueur[jou.id].bateau.inventaire.petrole+=self.listejoueur[cible].bateau.inventaire.petrole
                                    self.listejoueur[jou.id].bateau.inventaire.textile+=self.listejoueur[cible].bateau.inventaire.textile
                                    print("Comme vous avez refusé de vous défendre, le joueur",jou.id+1,"reparts avec votre inventaire !")
                                    print("_________________________")
                                    gagnant=1
                                    combat=1
                                else:
                                    print("_________________________")
                                    print("La force de l'attaquant est :",forceattaq,"et celle du défenseur:",forcedef)
                                    print("Choix du défenseur ( Joueur",cible+1,")")
                                    cartedef=self.listejoueur[cible].choixcarte(2)
                                    cartedef=self.listejoueur[cible].SelectEtRetraitCarte(cartedef)
                                    forcedef=cartedef.force
                                    print("_________________________")
                            else:
                                if(forceattaq>=forcedef):
                                    print("_________________________")
                                    print("La force de l'attaquant est :",forceattaq,"et celle du défenseur:",forcedef)
                                    print("Défenseur ( joueur",cible+1,")souhaitez vous jouer une nouvelle carte ?")
                                    choixdef=int(input)
                                    while(choixdef!=0 and choixdef!=1):
                                        print("_________________________")
                                        print("Erreur de saisie")
                                        print("Défenseur joueur",cible+1,"souhaitez vous jouer une nouvelle carte ? (Non:0 | Oui:1)")
                                        print("_________________________")
                                        choixdef=int(input)
                                    if(choixdef==0):
                                        self.listejoueur[jou.id].bateau.inventaire.bois+=self.listejoueur[cible].bateau.inventaire.bois
                                        self.listejoueur[jou.id].bateau.inventaire.gold+=self.listejoueur[cible].bateau.inventaire.gold
                                        self.listejoueur[jou.id].bateau.inventaire.cereale+=self.listejoueur[cible].bateau.inventaire.cereale
                                        self.listejoueur[jou.id].bateau.inventaire.machine_outils+=self.listejoueur[cible].bateau.inventaire.machine_outils
                                        self.listejoueur[jou.id].bateau.inventaire.petrole+=self.listejoueur[cible].bateau.inventaire.petrole
                                        self.listejoueur[jou.id].bateau.inventaire.textile+=self.listejoueur[cible].bateau.inventaire.textile
                                        print("Comme vous avez refusé de vous défendre, le joueur",jou.id+1,"reparts avec votre inventaire !")
                                        print("_________________________")
                                        gagnant=1
                                        combat=1
                                    else:
                                        print("La force de l'attaquant est :",forceattaq,"et celle du défenseur:",forcedef)
                                        print("Choix du défenseur ( Joueur",cible+1,")")
                                        cartedef=self.listejoueur[cible].choixcarte(2)
                                        cartedef=self.listejoueur[cible].SelectEtRetraitCarte(cartedef)
                                        forcedef+=cartedef.force
                                else:
                                    print("_________________________")
                                    print("Attaquant joueur",cible+1,"souhaitez vous jouer une nouvelle carte ? (Non:0 | Oui:1)")
                                    choixattaquant=int(input)
                                    while(choixattaquant!=0 and choixattaquant!=1):
                                        print("_________________________")
                                        print("Erreur de saisie")
                                        print("Attaquant joueur",cible+1,"souhaitez vous jouer une nouvelle carte ? (Non:0 | Oui:1)")
                                        print("_________________________")
                                        choixattaquant=int(input)
                                    if(choixattaquant==0):
                                        self.listejoueur[cible].bateau.inventaire.bois+=self.listejoueur[jou.id].bateau.inventaire.bois
                                        self.listejoueur[cible].bateau.inventaire.gold+=self.listejoueur[jou.id].bateau.inventaire.gold
                                        self.listejoueur[cible].bateau.inventaire.cereale+=self.listejoueur[jou.id].bateau.inventaire.cereale
                                        self.listejoueur[cible].bateau.inventaire.machine_outils+=self.listejoueur[jou.id].bateau.inventaire.machine_outils
                                        self.listejoueur[cible].bateau.inventaire.petrole+=self.listejoueur[jou.id].bateau.inventaire.petrole
                                        self.listejoueur[cible].bateau.inventaire.textile+=self.listejoueur[jou.id].bateau.inventaire.textile
                                        print("Comme vous avez refusé de vous défendre, le joueur",cible+1,"reparts avec votre inventaire !")
                                        print("_________________________")
                                        gagnant=2
                                        combat=1
                                    else:
                                        print("_________________________")
                                        print("La force de l'attaquant est :",forceattaq,"et celle du défenseur:",forcedef)
                                        print("Choix de l'attaquant ( Joueur",jou.id+1,")")
                                        carteattaquant=self.listejoueur[jou.id].choixcarte(2)
                                        carteattaquant=self.listejoueur[jou.id].SelectEtRetraitCarte(carteattaquant)
                                        forceattaq+=carteattaquant.force
                                        print("_________________________")
                        if(gagnant==1):
                            print("_________________________")
                            print("Bras de fer terminé, Bravo joueur",jou.id+1,"! ") 
                            print("_________________________") 
                        else:
                            print("_________________________")
                            print("Bras de fer terminé, Bravo joueur",cible+1,"! ") 
                            print("_________________________")
                        
    
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

                            
                                




                    
                    
                        




    
        



    
    

            



