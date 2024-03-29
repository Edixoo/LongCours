import paquetcarte
import joueurs
import cartedujeu
import random as rd
import marchandises as march
import random as r

class world:
    def __init__(self) -> None:
        """Constructeur de base du monde"""
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
    
    def acheter(self,jou:joueurs.joueur):
        """Fonction permettan au joueur d'acheter des ressources dans la case où il se trouve

        Args:
            jou (joueurs.joueur)

        Returns:
            qtt (int) quantite achetée
        """
        if(jou.posidport==3):
            print("Achat impossible, vous êtes sur un port")
        else:
            marchandise=self.map.zones[jou.posidzone].listeport[jou.posidport].marchandise
            print("Type de marchandise:",marchandise.nom)
            print("Prix unitaire de la marchandise",marchandise.prix_achat)
            print("Combien de marchandise souhaitez vous acheter ?")
            qtt=int(input())
            while(jou.monnaie<(qtt*marchandise.prix_achat)):
                print("Vous n'avez pas les moyens d'en acheter autant ! ")
                print("Combien de marchandise souhaitez vous acheter ?")
                qtt=int(input())
            marchandise.qttachete=qtt
            if(qtt!=0):
                jou.retirer_monnaie(qtt*marchandise.prix_achat)
                match marchandise.nom:
                    case "cereale":
                        jou.bateau.inventaire.cereale.append(marchandise)
                    case "gold":
                        jou.bateau.inventaire.gold.append(marchandise)
                    case "machine_outils":
                        jou.bateau.inventaire.machine_outils.append(marchandise)
                    case "textile":
                        jou.bateau.inventaire.textile.append(marchandise)
                    case "petrole":
                        jou.bateau.inventaire.petrole.append(marchandise)
                    case "bois":
                        jou.bateau.inventaire.bois.append(marchandise)
            return qtt

    def obtind(self,ind):
        """Fonction permettant d'obtenir les indices des port et zone
        Cette fonction est utile lors de l'utilisation d'une carte tempête.

        Args:
            ind (int): Indice du joueur

        Returns:
            zone (int): Indice de la zone
            port (int): Indice du port
        """
        port=self.listejoueur[ind].posidport
        zone=self.listejoueur[ind].posidzone
        return zone,port
    
    def echouer(self,zone,port):
        """Fonction faisant échouer tous les bateaux se trouvant dans une zone & case précise

        Args:
            zone (int): indice de la zone
            port (int): indice du port
        """
        for i in self.listejoueur:
            if(i.posidport==port and i.posidzone==zone):
                a=i.echouer()
                self.map.zones[zone].cimetiere.inventaire.bois+=a.bois
                self.map.zones[zone].cimetiere.inventaire.gold+=a.gold
                self.map.zones[zone].cimetiere.inventaire.cereale+=a.cereale
                self.map.zones[zone].cimetiere.inventaire.machine_outils+=a.machine_outils
                self.map.zones[zone].cimetiere.inventaire.petrole+=a.petrole
                self.map.zones[zone].cimetiere.inventaire.textile+=a.textile
    
    def afficherinv(self,jou:joueurs.joueur):
        """Fonction permettant l'affichage des informations d'un joueurs

        Args:
            jou (joueurs.joueur): composant joueur
        """
        print("_________________________")
        print("Pseudo:",jou.pseudo)
        print("Couleur:",jou.couleur)
        print("Argent:",jou.monnaie,"$")
        print("Zone:",jou.posidzone)
        if(jou.posidport==3):
            print("Cimetière:",jou.posidport)
        else:
            print("Port:",jou.posidport)
        print(jou.bateau.inventaire)

    def tourdejeu(self,jou:joueurs.joueur):
        """Fonction permettant au joueur de jouer son tour

        Args:
            jou (joueurs.joueur): Il s'agit du joueur, cet argument possède 
            toutes les composantes de la classe joueur
        """
        print("_________________________")
        print("Souhaitez vous voir vos informations ? (Non:0 | Oui:1)")
        qinv=int(input())
        if(qinv==1):
            self.afficherinv(jou)
        print("_________________________")
        roll=r.randint(0,5)
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
                print("Vous vous trouvez au port",jou.posidport,"de la zone",jou.posidzone)
            case 1:
                a=jou.vendre(roll)
            case 2:
                a=self.acheter(jou)
                if(a==0):
                    print("Vous n'avez rien acheté, votre tour est terminé")
                else:
                    print("Tour terminé, votre achat a été effectué !")
            case 3:
                cartechoix=jou.choixcarte(0)
                cartechoix=jou.SelectEtRetraitCarte(cartechoix)
                if(cartechoix.type==0): #Carte deplacement instantannée choisie
                    print("_________________________")
                    a,b=cartechoix.use()
                    jou.mouvement(a,b)
                    print("Vous avez été déplacé dans la zone",a,"et dans le port",b)
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
                    
                    print("Qui est votre cible ?")
                    listecibleindex=[int]
                    for i in listecible:
                        print("Le joueur", i.id+1,"?")
                        listecibleindex.append(i.id)
                    if(len(listecible)==0):
                        print("Pas de cible valide ! Bras de fer impossible. Fin de tour")
                        combat=1     
                    else:
                        cible=int(input())-1  
                        while(cible not in listecibleindex):
                            print("Cible invalide")
                            for i in listecible:
                                print("Le joueur", i.id+1,"?")
                            cible+=int(input()) 
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
                                print("Defenseur joueur",cible+1,"Souhaitez-vous vous défendre (Non: 0 | Oui:1)")
                                print("_________________________")
                                choixdef=int(input())
                                while(choixdef!=0 and choixdef!=1):
                                        print("_________________________")
                                        print("Erreur de saisie")
                                        print("La force de l'attaquant est :",forceattaq,"et celle du défenseur:",forcedef)
                                        print("Défenseur joueur",cible+1,"souhaitez vous jouer une nouvelle carte ?")
                                        print("_________________________")
                                        choixdef=int(input())
                                if(choixdef==0):
                                    self.listejoueur[jou.id].bateau.inventaire.bois+=self.listejoueur[cible].bateau.inventaire.bois
                                    self.listejoueur[jou.id].bateau.inventaire.gold+=self.listejoueur[cible].bateau.inventaire.gold
                                    self.listejoueur[jou.id].bateau.inventaire.cereale+=self.listejoueur[cible].bateau.inventaire.cereale
                                    self.listejoueur[jou.id].bateau.inventaire.machine_outils+=self.listejoueur[cible].bateau.inventaire.machine_outils
                                    self.listejoueur[jou.id].bateau.inventaire.petrole+=self.listejoueur[cible].bateau.inventaire.petrole
                                    self.listejoueur[jou.id].bateau.inventaire.textile+=self.listejoueur[cible].bateau.inventaire.textile
                                    self.listejoueur[cible].bateau.inventaire.nettoyer()
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
                                    forcedef+=cartedef.force
                                    firstturn=1
                                    print("_________________________")
                            else:
                                if(forceattaq>=forcedef):
                                    print("_________________________")
                                    print("La force de l'attaquant est :",forceattaq,"et celle du défenseur:",forcedef)
                                    print("Défenseur ( joueur",cible+1,")souhaitez vous jouer une nouvelle carte ?")
                                    choixdef=int(input())
                                    while(choixdef!=0 and choixdef!=1):
                                        print("_________________________")
                                        print("Erreur de saisie")
                                        print("Défenseur joueur",cible+1,"souhaitez vous jouer une nouvelle carte ? (Non:0 | Oui:1)")
                                        print("_________________________")
                                        choixdef=int(input())
                                    if(choixdef==0):
                                        self.listejoueur[jou.id].bateau.inventaire.bois+=self.listejoueur[cible].bateau.inventaire.bois
                                        self.listejoueur[jou.id].bateau.inventaire.gold+=self.listejoueur[cible].bateau.inventaire.gold
                                        self.listejoueur[jou.id].bateau.inventaire.cereale+=self.listejoueur[cible].bateau.inventaire.cereale
                                        self.listejoueur[jou.id].bateau.inventaire.machine_outils+=self.listejoueur[cible].bateau.inventaire.machine_outils
                                        self.listejoueur[jou.id].bateau.inventaire.petrole+=self.listejoueur[cible].bateau.inventaire.petrole
                                        self.listejoueur[jou.id].bateau.inventaire.textile+=self.listejoueur[cible].bateau.inventaire.textile
                                        self.listejoueur[cible].bateau.inventaire.nettoyer()
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
                                    print("Attaquant joueur",jou.id+1,"souhaitez vous jouer une nouvelle carte ? (Non:0 | Oui:1)")
                                    choixattaquant=int(input())
                                    while(choixattaquant!=0 and choixattaquant!=1):
                                        print("_________________________")
                                        print("Erreur de saisie")
                                        print("Attaquant joueur",jou.id+1,"souhaitez vous jouer une nouvelle carte ? (Non:0 | Oui:1)")
                                        print("_________________________")
                                        choixattaquant=int(input())
                                    if(choixattaquant==0):
                                        self.listejoueur[cible].bateau.inventaire.bois+=self.listejoueur[jou.id].bateau.inventaire.bois
                                        self.listejoueur[cible].bateau.inventaire.gold+=self.listejoueur[jou.id].bateau.inventaire.gold
                                        self.listejoueur[cible].bateau.inventaire.cereale+=self.listejoueur[jou.id].bateau.inventaire.cereale
                                        self.listejoueur[cible].bateau.inventaire.machine_outils+=self.listejoueur[jou.id].bateau.inventaire.machine_outils
                                        self.listejoueur[cible].bateau.inventaire.petrole+=self.listejoueur[jou.id].bateau.inventaire.petrole
                                        self.listejoueur[cible].bateau.inventaire.textile+=self.listejoueur[jou.id].bateau.inventaire.textile
                                        self.listejoueur[jou.id].bateau.inventaire.nettoyer()
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
        """Fonction permettant au monde de s'actualiser et d'appeler 
        les fonctions dont il a besoin
        """
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

                            
                                




                    
                    
                        




    
        



    
    

            



