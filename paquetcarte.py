import cartes

class paquetdecarte():
    def __init__(self) -> None:
        self.listecartemouv = []
        self.listecartebdf = []
        self.listecartetemp = []
        #Ajout de 12 cartes mouvement au paquet du jeu (6 de chaque)
        for i in range (12):
            if(i%2==0):
                carte=cartes.carte_mouvement(0,'mouvement direct')   
            else:
                carte=cartes.carte_mouvement(1,'mouvement ordinaire')
            self.listecartemouv.append(carte)        
        #Ajout de 12 cartes bras de fer au paquet du jeu (3 de chaque)
        for i in range(12):
            if(i%4==0):
                carte=cartes.carte_bdf(0,'force 0')
            if(i%4==1):
                carte=cartes.carte_bdf(1,'force 1')
            if(i%4==2):
                carte=cartes.carte_bdf(2,'force 2')
            if(i%4==3):
                carte=cartes.carte_bdf(3,'force 3')
            self.listecartebdf.append(carte)
        #Ajout de 12 cartes tempete au paquet du jeu
        for i in range(12):
            carte=cartes.carte_tempete()
            self.listecartetemp.append(carte)

