import inventaire

class bateau:
    """Constructeur de la classe bateau """
    def __init__(self,couleur:str):
   
        self.couleur: str 
        self.inventaire: inventaire.inventaire = inventaire.inventaire()
        
        
    def ajoutermarchandises(self, marchandise):
        """ Fonction permettant l'ajout d'une marchandise au bateau (appel de la fonction ajouter d'inventaire) """
        self.inventaire.ajouter(marchandise)

    def retirermarchandises(self, marchandise):
        """ Fonction permettant le retrait d'une marchandise au bateau (appel de la fonction retirer d'inventaire) """
        self.inventaire.retirer(marchandise)

    