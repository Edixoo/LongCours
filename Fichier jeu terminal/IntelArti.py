import world
import random as r


def venteposs(jou:world.joueurs.joueur,world:world.world,marchvendable:int):
    ventepossible=False
    if(jou.posidport==3):
        return ventepossible
    qttpos=0
    match marchvendable:
                        case 0:
                            if(world.map.zones[jou.posidzone].listeport[jou.posidport].marchandise.nom=='gold'):
                                ventepossible=True
                                qttpos=int(jou.bateau.inventaire.getGold)
                                if(qttpos==0):
                                    ventepossible=False
                        case 1:
                            if(world.map.zones[jou.posidzone].listeport[jou.posidport].marchandise.nom=='textile'):
                                ventepossible=True
                                qttpos=int(jou.bateau.inventaire.getTextile)
                                if(qttpos==0):
                                    ventepossible=False
                        case 2:
                            if(world.map.zones[jou.posidzone].listeport[jou.posidport].marchandise.nom=='bois'):
                                ventepossible=True
                                qttpos=int(jou.bateau.inventaire.getBois)
                                if(qttpos==0):
                                    ventepossible=False
                        case 3:
                            if(world.map.zones[jou.posidzone].listeport[jou.posidport].marchandise.nom=='petrole'):
                                ventepossible=True
                                qttpos=int(jou.bateau.inventaire.getPetrole)
                                if(qttpos==0):
                                    ventepossible=False
                        case 4:
                            if(world.map.zones[jou.posidzone].listeport[jou.posidport].marchandise.nom=='cereale'):
                                ventepossible=True
                                qttpos=int(jou.bateau.inventaire.getCereale)
                                if(qttpos==0):
                                    ventepossible=False
                        case 5:
                            if(world.map.zones[jou.posidzone].listeport[jou.posidport].marchandise.nom=='machine_outils'):
                                ventepossible=True
                                qttpos=int(jou.bateau.inventaire.getMachineOutils)
                                if(qttpos==0):
                                    ventepossible=False
    return ventepossible,qttpos,marchvendable
def depinstposs(jou:world.joueurs.joueur):
    isinstantpossible = False
    cartejouable = 0
    for i in jou.listecartes:
        if(i.type==0):
            cartejouable=i
            isinstantpossible=True
    return cartejouable,isinstantpossible
def getprixdevente(jou:world.joueurs.joueur,world:world.world):
    prixdevente = world.map.zones[jou.posidzone].listeport[jou.posidport].marchandise.prix_achat
    return prixdevente
def vendre(jou:world.joueurs.joueur,world:world.world,marchvendable:int):
    ventepossible,qttpos,marchvendable=venteposs(jou,world)
    if(ventepossible):
        pv=getprixdevente(jou,world)
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
def acheter(jou:world.joueurs.joueur,world:world.world):
    marchandise=world.map.zones[jou.posidzone].listeport[jou.posidport].marchandise
    qtt=jou.monnaie%marchandise.prix_achat
    if(qtt!=0):
        marchandise.qttachete=qtt
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
    return jou
def deplacementnormal(jou:world.joueurs.joueur):
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



def Iaalea(jou:world.joueurs.joueur,world:world.world):
    a=r.randint(0,1)
    match a:
        case 0: #Cas déplacement avant action
            b=0
            marchvendable=r.randint(0,5)
            cartejouable,isinstantpossible=depinstposs(jou)
            if(isinstantpossible==True):
                b=r.randint(0,1)
            if(b==0):#Cas déplacement normal
                jou=deplacementnormal(jou)
            else: #Cas déplacement instantané
                c=r.randint(0,5)
                d=r.randint(0,3)
                cartejouable=jou.SelectEtRetraitCarte(cartejouable)
                jou.mouvement(c,d)
                ventepossible,qttavendre,marchvendable=venteposs(jou,world)
                if(ventepossible): #Si une vente est possible
                    e=r.randint(0,1)
                    if(e==0): #Cas de la vente
                        jou=vendre(jou,world,marchvendable)
                    else: #Cas de l'achat
                        jou=acheter(jou,world)




            
            
        case 1: #Cas action avant déplacement
            print('Test')
    


