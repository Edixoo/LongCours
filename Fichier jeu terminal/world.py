import paquetcarte
import joueurs
import cartedujeu
import random as rd
import marchandises as march
import random as r
import psycopg2

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

    def actuclass(self,pseudo:str):
        try:
            connection = psycopg2.connect(
                host="postgresql-saejv.alwaysdata.net",
                database="saejv_longcours",
                user="saejv",
                password="jeuvideo123.."
            )

            cursor = connection.cursor()
            insert_query = f"SELECT classementjou('{pseudo}')"
            cursor.execute(insert_query)
            connection.commit()
            print("Victoires enregistrées au classement !")
        except (Exception, psycopg2.Error) as error:
            print("Erreur insertion dans la table des scores :", error)
        finally:
            if(connection):
                cursor.close()
                connection.close()

    def afficher_table_classement(self):
        try:
            connection = psycopg2.connect(
                host="postgresql-saejv.alwaysdata.net",
                database="saejv_longcours",
                user="saejv",
                password="jeuvideo123.."
            )
            cursor = connection.cursor()
            query = "SELECT * FROM public.classement"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except (Exception, psycopg2.Error) as error:
            print("Erreur lors de la connexion à la base de données :", error)
        finally:
            if(connection):
                cursor.close()
                connection.close()

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

    def deplacementnormalIA(self,jou:joueurs.joueur):
        a=r.randint(0,1) #0 changement de zone, 1 changement de port.
        positionzone=0
        if(a==0):
            b=r.randint(0,1)#Zone précédent ou Zone suivante
            if(b==0):#Zone précédente
                positionzone=(jou.posidzone-1)%6
            else:
                positionzone=(jou.posidzone+1)%6
            jou.mouvement(positionzone,0)
            return jou
        else:
            deplacementpossible=[0,1,2,3]
            del deplacementpossible[jou.posidport]
            b=r.randint(0,len(deplacementpossible)-1)
            jou.mouvement(jou.posidzone,b)
            return jou

    def depinstpossIA(jou:joueurs.joueur):
        isinstantpossible = False
        cartejouable = 0
        for i in jou.listecartes:
            if(i.type==0):
                cartejouable=i
                isinstantpossible=True
        return cartejouable,isinstantpossible

    def venteposs(self, jou: joueurs.joueur, marchvendable: int):
        ventepossible = False
        if jou.posidport == 3:
            return ventepossible
        qttpos = 0
        marchandise = self.map.zones[jou.posidzone].listeport[jou.posidport].marchandise
        if marchvendable == 0 and marchandise.nom == 'gold':
            ventepossible = True
            qttpos = jou.bateau.inventaire.getGold()
            if qttpos == 0:
                ventepossible = False
        elif marchvendable == 1 and marchandise.nom == 'textile':
            ventepossible = True
            qttpos = jou.bateau.inventaire.getTextile()
            if qttpos == 0:
                ventepossible = False
        elif marchvendable == 2 and marchandise.nom == 'bois':
            ventepossible = True
            qttpos = jou.bateau.inventaire.getBois()
            if qttpos == 0:
                ventepossible = False
        elif marchvendable == 3 and marchandise.nom == 'petrole':
            ventepossible = True
            qttpos = jou.bateau.inventaire.getPetrole()
            if qttpos == 0:
                ventepossible = False
        elif marchvendable == 4 and marchandise.nom == 'cereale':
            ventepossible = True
            qttpos = jou.bateau.inventaire.getCereale()
            if qttpos == 0:
                ventepossible = False
        elif marchvendable == 5 and marchandise.nom == 'machine_outils':
            ventepossible = True
            qttpos = jou.bateau.inventaire.getMachineOutils()
            if qttpos == 0:
                ventepossible = False
        return ventepossible, qttpos, marchvendable


    def acheterIA(self, jou: joueurs.joueur):
        if jou.posidport==3:
            return jou
        marchandise = self.map.zones[jou.posidzone].listeport[jou.posidport].marchandise
        qtt = jou.monnaie // marchandise.prix_achat  
        if qtt != 0:  
            marchandise.qttachete = qtt
            jou.retirer_monnaie(qtt * marchandise.prix_achat)
            if marchandise.nom == "cereale":
                jou.bateau.inventaire.cereale.append(marchandise)
            elif marchandise.nom == "gold":
                jou.bateau.inventaire.gold.append(marchandise)
            elif marchandise.nom == "machine_outils":
                jou.bateau.inventaire.machine_outils.append(marchandise)
            elif marchandise.nom == "textile":
                jou.bateau.inventaire.textile.append(marchandise)
            elif marchandise.nom == "petrole":
                jou.bateau.inventaire.petrole.append(marchandise)
            elif marchandise.nom == "bois":
                jou.bateau.inventaire.bois.append(marchandise)
        return jou

    def getprixdevente(self,jou:joueurs.joueur):
        prixdevente = self.map.zones[jou.posidzone].listeport[jou.posidport].marchandise.prix_achat
        return prixdevente
    
    def vendreIA(self,jou:joueurs.joueur,marchvendable:int):
        ventepossible,qttpos,marchvendable = self.venteposs(jou,marchvendable)
        if(ventepossible):
            pv=self.getprixdevente(jou)
            pv=pv*qttpos
            jou.ajout_monnaie(pv)
            match marchvendable:
                case 0:
                    jou.bateau.inventaire.gold=[]
                case 1:
                    jou.bateau.inventaire.textile=[]
                case 2:
                    jou.bateau.inventaire.bois=[]
                case 3:
                    jou.bateau.inventaire.petrole=[]
                case 4:
                    jou.bateau.inventaire.cereale=[]
                case 5:
                    jou.bateau.inventaire.machine_outils=[]
        return jou

    def tourdejeu(self,jou:joueurs.joueur):
        """Fonction permettant au joueur de jouer son tour s'il s'agit d'un bot, l'effectue automatiquement

            Args:
            jou (joueurs.joueur): Il s'agit du joueur, cet argument possède 
            toutes les composantes de la classe joueur
        """

        if "BOT" not in jou.pseudo:
            
            premierchoix=True
            jouercarte=True
            print("_________________________")
            print(f'Joueur {jou.id+1} souhaitez vous voir vos informations ? (Non:0 | Oui:1)')
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
            print('Que souhaitez vous faire ? Joueur',jou.id+1,'\n Vous déplacer (mouvement normal) ? [0] \n Vendre ? [1] \n Acheter ? [2] \n Jouer une carte ? [3]\n Passer votre tour ? [4]')
            choix=int(input())
            print("_________________________")
            possibilite=["vendre","acheter","deplacnorm","carte","passtour"]
            choixpos=[0,1,2,3,4]
            while choix!=4:
                if premierchoix!=True:
                    while choix not in choixpos:
                        print("_________________________")
                        print('Que souhaitez vous faire ? Joueur',jou.id+1,'\n Vous déplacer (mouvement normal) ? [0] \n Vendre ? [1] \n Acheter ? [2] \n Jouer une carte ? [3]\n Passer votre tour ? [4]')
                        choix=int(input())
                        print("_________________________")
                match choix:
                    case 0:
                        if "deplacnorm" in possibilite:
                            jou.deplacementnormal()
                            print("Vous vous trouvez au port",jou.posidport,"de la zone",jou.posidzone)
                            premierchoix = False
                            choix=20
                            possibilite.remove("deplacnorm")
                        else:
                            print("Vous ne pouvez plus utiliser le déplacement normal")
                            premierchoix = False
                            choix=20
                    case 1:
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
                            print("Vous ne possédez pas la ressource ! ") 
                            try:
                                del possibilite[possibilite.index("vendre")]
                                premierchoix=False
                                choix=20

                            except:
                                premierchoix=False
                                choix=20
                            
                        else:
                            if "vendre" in possibilite:
                                a=jou.vendre(roll)
                                print("Ressource vendue !")
                                del possibilite[possibilite.index("vendre")] 
                                choix=20
                            else:
                                print("Vous ne pouvez plus vendre ce tour-ci")  
                            premierchoix = False 
                            choix=20
                    case 2:
                        if "acheter" in possibilite:
                            achat = self.acheter(jou)
                            if achat == 0:
                                print("Vous n'avez rien acheté")
                            else:
                                print("Achat effectué !")
                            del possibilite[possibilite.index("acheter")]
                            premierchoix = False 
                            choix=20
                        else:
                            print("Vous ne pouvez plus acheter ce tour-ci !")
                            premierchoix = False
                            choix=20
                    case 3:
                        jouercarte = True
                        while jouercarte:
                            cartechoix = jou.choixcarte(4)
                            cartechoix = jou.SelectEtRetraitCarte(cartechoix)
                            if cartechoix.type == 0: #Carte deplacement instantanée choisie
                                print("_________________________")
                                a, b = cartechoix.use()
                                jou.mouvement(a, b)
                                print("Vous avez été déplacé dans la zone", a+1, "et dans le port", b+1)
                                print("_________________________")
                                if len(jou.listecartes) == 0:
                                    jouercarte = False
                                else:
                                    print("Souhaitez-vous jouer une autre carte ? [0]: NON | [1]: OUI")
                                    othercard = -1
                                    while othercard not in [0, 1]:
                                        try:
                                            othercard = int(input())
                                        except ValueError:
                                            print("Erreur de saisie : Souhaitez-vous jouer une autre carte ? [0]: NON | [1]: OUI")
                                    if othercard == 0:
                                        jouercarte = False

                            elif cartechoix.type == 1: #Carte tempête choisie
                                indcible = -1
                                while indcible >= len(self.listejoueur) or indcible < 0:
                                    try:
                                        indcible = cartechoix.use()
                                    except ValueError:
                                        print("Erreur de saisie. Entrez un nombre entier pour choisir la cible.")
                                zone, port = self.obtind(indcible)
                                self.echouer(zone, port)
                                print("_________________________")
                                print("Tous les bateaux dans la zone", zone+1, "port", port+1, "se sont échoués")
                                print("_________________________")
                                if len(jou.listecartes) == 0:
                                    jouercarte = False
                                else:
                                    print("Souhaitez-vous jouer une autre carte ? [0]: NON | [1]: OUI")
                                    othercard = -1
                                    while othercard not in [0, 1]:
                                        try:
                                            othercard = int(input())
                                        except ValueError:
                                            print("Erreur de saisie : Souhaitez-vous jouer une autre carte ? [0]: NON | [1]: OUI")
                                    if othercard == 0:
                                        jouercarte = False

                            elif cartechoix.type == 2: #Carte bras de fer
                                listecible = []
                                for j in self.listejoueur:
                                    if jou.posidport == j.posidport and jou.posidzone == j.posidzone and jou.id != j.id:
                                        listecible.append(j)
                                if not listecible:
                                    print("Pas de cible valide ! Bras de fer impossible. Fin de tour")
                                    jouercarte = False
                                else:
                                    print("Qui est votre cible ?")
                                    listecibleindex = []
                                    for i in listecible:
                                        print("Le joueur", i.id+1,"?")
                                        listecibleindex.append(i.id)
                                    cible = -1
                                    while cible not in listecibleindex:
                                        try:
                                            cible = int(input())-1
                                        except ValueError:
                                            print("Cible invalide. Entrez un nombre entier correspondant à un joueur cible.")
                                    print("_________________________")
                                    print("Début du BRAS DE FER !")
                                    if "BOT" in self.listejoueur[cible].pseudo:
                                        bot=True
                                    else:
                                        bot=False
                                    combat = 0
                                    forceattaq = 0
                                    forcedef = 0
                                    firstturn = 0
                                    gagnant = 0
                                    while combat == 0:
                                        if firstturn == 0:
                                            forceattaq = cartechoix.force
                                            print("_________________________")
                                            print("La force de l'attaquant est :", forceattaq, "et celle du défenseur :", forcedef)
                                            print("Défenseur joueur", cible+1, "Souhaitez-vous vous défendre (Non: 0 | Oui:1)")
                                            print("_________________________")
                                            
                                            if(bot):
                                                choixdef=0
                                            else:
                                                choixdef = int(input())
                                            
                                            while choixdef != 0 and choixdef != 1:
                                                print("_________________________")
                                                print("Erreur de saisie")
                                                print("La force de l'attaquant est :", forceattaq, "et celle du défenseur :", forcedef)
                                                print("Défenseur joueur", cible+1, "souhaitez vous vous défendre ? (Non: 0 | Oui:1)")
                                                print("_________________________")
                                                
                                                if(bot):
                                                    choixdef=0
                                                else:
                                                    choixdef = int(input())
                                            
                                            if choixdef == 0:
                                                self.listejoueur[jou.id].bateau.inventaire.bois += self.listejoueur[cible].bateau.inventaire.bois
                                                self.listejoueur[jou.id].bateau.inventaire.gold += self.listejoueur[cible].bateau.inventaire.gold
                                                self.listejoueur[jou.id].bateau.inventaire.cereale += self.listejoueur[cible].bateau.inventaire.cereale
                                                self.listejoueur[jou.id].bateau.inventaire.machine_outils += self.listejoueur[cible].bateau.inventaire.machine_outils
                                                self.listejoueur[jou.id].bateau.inventaire.petrole += self.listejoueur[cible].bateau.inventaire.petrole
                                                self.listejoueur[jou.id].bateau.inventaire.textile += self.listejoueur[cible].bateau.inventaire.textile
                                                self.listejoueur[cible].bateau.inventaire.nettoyer()
                                                print("Comme vous avez refusé de vous défendre, le joueur", jou.id+1, "repart avec votre inventaire !")
                                                print("_________________________")
                                                gagnant = 1
                                                combat = 1
                                                
                                            else:
                                                print("_________________________")
                                                print("La force de l'attaquant est :", forceattaq, "et celle du défenseur :", forcedef)
                                                print("Choix du défenseur (Joueur", cible+1, ")")
                                                
                                                cartedef = self.listejoueur[cible].choixcarte(2)
                                                cartedef = self.listejoueur[cible].SelectEtRetraitCarte(cartedef)
                                                forcedef += cartedef.force
                                                firstturn = 1
                                                print("_________________________")
                                        else:
                                            if forceattaq >= forcedef:
                                                print("_________________________")
                                                print("La force de l'attaquant est :", forceattaq, "et celle du défenseur:", forcedef)
                                                print("Défenseur ( joueur", cible+1, ") souhaitez vous jouer une nouvelle carte ?")
                                                choixdef = int(input())
                                                while choixdef not in [0, 1]:
                                                    print("_________________________")
                                                    print("Erreur de saisie")
                                                    print("Défenseur joueur", cible+1, "souhaitez vous jouer une nouvelle carte ? (Non:0 | Oui:1)")
                                                    print("_________________________")
                                                    choixdef = int(input())
                                                if choixdef == 0:
                                                    self.listejoueur[jou.id].bateau.inventaire.bois += self.listejoueur[cible].bateau.inventaire.bois
                                                    self.listejoueur[jou.id].bateau.inventaire.gold += self.listejoueur[cible].bateau.inventaire.gold
                                                    self.listejoueur[jou.id].bateau.inventaire.cereale += self.listejoueur[cible].bateau.inventaire.cereale
                                                    self.listejoueur[jou.id].bateau.inventaire.machine_outils += self.listejoueur[cible].bateau.inventaire.machine_outils
                                                    self.listejoueur[jou.id].bateau.inventaire.petrole += self.listejoueur[cible].bateau.inventaire.petrole
                                                    self.listejoueur[jou.id].bateau.inventaire.textile += self.listejoueur[cible].bateau.inventaire.textile
                                                    self.listejoueur[cible].bateau.inventaire.nettoyer()
                                                    print("Comme vous avez refusé de vous défendre, le joueur", jou.id+1, "repart avec votre inventaire !")
                                                    print("_________________________")
                                                    gagnant = 1
                                                    combat = 1
                                                else:
                                                    print("La force de l'attaquant est :", forceattaq, "et celle du défenseur:", forcedef)
                                                    print("Choix du défenseur ( Joueur", cible+1, ")")
                                                    cartedef = self.listejoueur[cible].choixcarte(2)
                                                    cartedef = self.listejoueur[cible].SelectEtRetraitCarte(cartedef)
                                                    forcedef += cartedef.force
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
                                    if gagnant == 1:
                                        print("_________________________")
                                        print("Bras de fer terminé, Bravo joueur", jou.id+1, "!") 
                                        print("_________________________") 
                                    else:
                                        print("_________________________")
                                        print("Bras de fer terminé, Bravo joueur", cible+1, "!") 
                                        print("_________________________")
                                    print("Souhaitez-vous jouer une autre carte ? [0]: NON | [1]: OUI")
                                    othercard = int(input())
                                    while othercard not in [0, 1]:
                                        print("Erreur de saisie : Souhaitez-vous jouer une autre carte ? [0]: NON | [1]: OUI")
                                        othercard = int(input())
                                    if othercard == 0 or len(jou.listecartes) == 0:
                                        jouercarte = False
                                    del possibilite[possibilite.index("carte")]
                                    premierchoix=False
                            choix=20
        else: #S'il s'agit d'un bot
            possibilite=["deplacnorm","vendre","acheter","carte","passtour"]
            jouercarte=True
            print("_________________________")
            self.afficherinv(jou)
            print("_________________________")
            roll=r.randint(0,5)
            choixpos=[0,1,2,3,4]
            choix=r.choice(choixpos)
            while choix!=4:
                if choix == 0:
                    if "deplacnorm" in possibilite:
                        self.deplacementnormalIA(jou)
                        print("Le bot s'est déplacé au port",jou.posidport,"de la zone",jou.posidzone)
                        premierchoix=False
                        del choixpos[0]
                        choix=r.choice(choixpos)
                elif choix == 1:
                    qttpos=0
                    if roll == 0:
                        for ressource in jou.bateau.inventaire.gold:
                            qttpos+=ressource.qttachete
                    elif roll == 1:
                        for ressource in jou.bateau.inventaire.textile:
                            qttpos+=ressource.qttachete
                    elif roll == 2:
                        for ressource in jou.bateau.inventaire.bois:
                            qttpos+=ressource.qttachete
                    elif roll == 3:
                        for ressource in jou.bateau.inventaire.petrole:
                            qttpos+=ressource.qttachete
                    elif roll == 4:
                        for ressource in jou.bateau.inventaire.cereale:
                            qttpos+=ressource.qttachete
                    elif roll == 5:
                        for ressource in jou.bateau.inventaire.machine_outils:
                            qttpos+=ressource.qttachete
                    if(qttpos==0):
                        print("Le bot ne possède pas la ressource ! ") 
                        if "vendre" in possibilite:
                            del possibilite[possibilite.index("vendre")]
                    else:
                        if "vendre" in possibilite:
                            a=self.vendreIA(jou,roll)
                            print("Ressource vendue !")
                            del possibilite[possibilite.index("vendre")]
                        else:
                            print("Le bot ne peut plus vendre")  
                    premierchoix=False
                    choix=r.choice(choixpos)
                elif choix == 2:
                    if "acheter" in possibilite:
                        a=self.acheterIA(jou)
                        if(a==0):
                            print("Le bot n'a rien acheté")
                        else:
                            print("Achat effectué !")
                        del possibilite[possibilite.index("acheter")] 
                    else:
                        print("Le bot ne peut plus acheter ce tour-ci !")
                    choix=r.choice(choixpos)
                elif choix == 3:
                    while jouercarte == True:
                        cartechoix=jou.choixcarte(0)
                        cartechoix=jou.SelectEtRetraitCarte(cartechoix)
                        if cartechoix.type == 0: # Carte deplacement instantannée choisie
                            print("_________________________")
                            a=r.randint(0,5)
                            b=r.randint(0,3)
                            jou.mouvement(a,b)
                            print("Le bot a été déplacé dans la zone",a+1,"et dans le port",b+1) # Correction here
                            print("_________________________")
                            othercard = r.randint(0,1)
                            while othercard not in [0,1]:
                                print("Erreur de saisie : Souhaitez vous jouer une autre carte ? [0]: NON | [1]: OUI")
                                othercard = r.randint(0,1)
                            if othercard == 0 or len(jou.listecartes) == 0:
                                jouercarte = False
                        elif cartechoix.type == 1: # Carte tempête choisie
                            indcible = -1
                            while indcible >= len(self.listejoueur) or indcible < 0:
                                indcible = r.randint(0, len(self.listejoueur)-1)
                            zone,port = self.obtind(indcible)
                            self.echouer(zone, port)
                            print("_________________________")
                            print("Tous les bateaux dans la zone",zone+1,"port",port+1,"se sont échoués")
                            print("_________________________")
                            othercard = r.randint(0,1)
                            while othercard not in [0,1]:
                                print("Erreur de saisie : Souhaitez vous jouer une autre carte ? [0]: NON | [1]: OUI")
                                othercard = r.randint(0,1)
                            if othercard == 0 or len(jou.listecartes) == 0:
                                jouercarte = False
                        elif cartechoix.type == 2: #Carte bras de fer
                            listecible = []
                            for j in self.listejoueur:
                                if(jou.posidport == j.posidport and jou.posidzone == j.posidzone and jou.id != j.id):
                                    listecible.append(j)
                            print("Qui va être ciblé ?")
                            listecibleindex = []
                            for i in listecible:
                                print("Le joueur", i.id+1,"?")
                                listecibleindex.append(i.id)
                            if len(listecible) == 0:
                                print("Pas de cible valide ! Bras de fer impossible. Fin de tour")
                                combat = 1     
                            else:
                                cible = r.choice(listecibleindex)
                                print("_________________________")
                                print("Début du BRAS DE FER !")
                                if("BOT" in self.listejoueur[cible].pseudo):
                                    bot=True
                                else:
                                    bot=False
                                combat=0
                                forceattaq=0
                                forcedef=0
                                firstturn=0
                                gagnant=0
                                while combat == 0:
                                    if firstturn == 0:
                                        forceattaq = cartechoix.force
                                        print("_________________________")
                                        print("La force de l'attaquant est :", forceattaq, "et celle du défenseur:", forcedef)
                                        print("Défenseur joueur", cible+1, "Souhaitez-vous vous défendre (Non: 0 | Oui:1)")
                                        print("_________________________")
                                        if(bot):
                                            choixdef=0
                                        else:
                                            choixdef = int(input())
                                        while choixdef != 0 and choixdef != 1:
                                            print("_________________________")
                                            print("Erreur de saisie")
                                            print("La force de l'attaquant est :", forceattaq, "et celle du défenseur:", forcedef)
                                            print("Défenseur joueur", cible+1, "souhaitez vous jouer une nouvelle carte ?")
                                            print("_________________________")
                                            if(bot):
                                                choixdef=0
                                            else:
                                                choixdef = int(input())
                                        if choixdef == 0:
                                            self.listejoueur[jou.id].bateau.inventaire.bois += self.listejoueur[cible].bateau.inventaire.bois
                                            self.listejoueur[jou.id].bateau.inventaire.gold += self.listejoueur[cible].bateau.inventaire.gold
                                            self.listejoueur[jou.id].bateau.inventaire.cereale += self.listejoueur[cible].bateau.inventaire.cereale
                                            self.listejoueur[jou.id].bateau.inventaire.machine_outils += self.listejoueur[cible].bateau.inventaire.machine_outils
                                            self.listejoueur[jou.id].bateau.inventaire.petrole += self.listejoueur[cible].bateau.inventaire.petrole
                                            self.listejoueur[jou.id].bateau.inventaire.textile += self.listejoueur[cible].bateau.inventaire.textile
                                            self.listejoueur[cible].bateau.inventaire.nettoyer()
                                            print("Comme vous avez refusé de vous défendre, le joueur", jou.id+1, "repart avec votre inventaire !")
                                            print("_________________________")
                                            gagnant = 1
                                            combat = 1
                                        else:
                                            print("_________________________")
                                            print("La force de l'attaquant est :", forceattaq, "et celle du défenseur:", forcedef)
                                            print("Choix du défenseur ( Joueur", cible+1, ")")
                                            cartedef = self.listejoueur[cible].choixcarte(2)
                                            cartedef = self.listejoueur[cible].SelectEtRetraitCarte(cartedef)
                                            forcedef += cartedef.force
                                            firstturn = 1
                                            print("_________________________")
                                    else:
                                        if forceattaq >= forcedef:
                                            print("_________________________")
                                            print("La force de l'attaquant est :", forceattaq, "et celle du défenseur:", forcedef)
                                            print("Défenseur ( joueur", cible + 1, ") souhaitez-vous jouer une nouvelle carte ?")
                                            choixdef = int(input())
                                            while choixdef not in [0, 1]:
                                                print("_________________________")
                                                print("Erreur de saisie")
                                                print("Défenseur joueur", cible+1, "souhaitez-vous jouer une nouvelle carte ? (Non: 0 | Oui: 1)")
                                                print("_________________________")
                                                choixdef = int(input())
                                            if choixdef == 0:
                                                self.listejoueur[jou.id].bateau.inventaire.bois += self.listejoueur[cible].bateau.inventaire.bois
                                                self.listejoueur[jou.id].bateau.inventaire.gold += self.listejoueur[cible].bateau.inventaire.gold
                                                self.listejoueur[jou.id].bateau.inventaire.cereale += self.listejoueur[cible].bateau.inventaire.cereale
                                                self.listejoueur[jou.id].bateau.inventaire.machine_outils += self.listejoueur[cible].bateau.inventaire.machine_outils
                                                self.listejoueur[jou.id].bateau.inventaire.petrole += self.listejoueur[cible].bateau.inventaire.petrole
                                                self.listejoueur[jou.id].bateau.inventaire.textile += self.listejoueur[cible].bateau.inventaire.textile
                                                self.listejoueur[cible].bateau.inventaire.nettoyer()
                                                print("Comme vous avez refusé de vous défendre, le joueur", jou.id+1, "repart avec votre inventaire !")
                                                print("_________________________")
                                                gagnant = 1
                                                combat = 1
                                            else:
                                                print("La force de l'attaquant est :", forceattaq, "et celle du défenseur:", forcedef)
                                                print("Choix du défenseur ( Joueur", cible+1, ")")
                                                cartedef = self.listejoueur[cible].choixcarte(2)
                                                cartedef = self.listejoueur[cible].SelectEtRetraitCarte(cartedef)
                                                forcedef += cartedef.force
                                        else:
                                            print("_________________________")
                                            print("Le bot va décider s'il attaque ou non")
                                            choixattaquant=r.randint(0,1)
                                            while(choixattaquant not in [0,1]):
                                                print("Le bot réfléchis")
                                                choixattaquant=r.randint(0,1)
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
                                                listecartebataille: list[int] = []
                                                while carteattaquant not in listecartebataille:
                                                    cpt = 0
                                                    for i in jou.listecartes:
                                                        if i.type == 2:
                                                            listecartebataille.append(cpt)
                                                        cpt += 1
                                                    if not listecartebataille:
                                                        carteattaquant = False
                                                        break
                                                    else:
                                                        carteattaquant = r.choice(listecartebataille)
                                                        carteattaquant -= 1
                                                #
                                                if(carteattaquant!=False):
                                                    carteattaquant=self.listejoueur[jou.id].SelectEtRetraitCarte(carteattaquant)
                                                    forceattaq+=carteattaquant.force
                                    if(gagnant==1):
                                        print("_________________________")
                                        print("Bras de fer terminé, Bravo joueur",jou.id+1,"! ") 
                                        print("_________________________") 
                                    else:
                                        print("_________________________")
                                        print("Bras de fer terminé, Bravo joueur",cible+1,"! ") 
                                        print("_________________________")
                                    othercard = r.randint(0,1)
                                    while othercard not in [0,1]:
                                        print("Le bot réfléchis")
                                        othercard = r.randint(0,1)
                                    if othercard == 0:
                                        jouercarte=False
                    try:
                        del possibilite[possibilite.index("carte")]
                    except:
                        pass
                    premierchoix=False                
                    choix=r.choice(choixpos)
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
                self.actuclass(self.listejoueur[0].pseudo)
                self.jeuon=False
                self.afficher_table_classement()
            self.inflation

                            
                                




                    
                    
                        




    
        



    
    

            



