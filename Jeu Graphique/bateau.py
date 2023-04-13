import inventaire

class bateau:
    
    def __init__(self,couleur:str):
        """Constructeur de la classe bateau """
        self.couleur: str 
        self.inventaire: inventaire.inventaire = inventaire.inventaire()
        
        
    def ajoutermarchandises(self, marchandise):
        """ Fonction permettant l'ajout d'une marchandise au bateau (appel de la fonction ajouter d'inventaire) """
        self.inventaire.ajouter(marchandise)

    def retirermarchandises(self, marchandise):
        """ Fonction permettant le retrait d'une marchandise au bateau (appel de la fonction retirer d'inventaire) """
        self.inventaire.retirer(marchandise)

    def echouer(self):
        """Fonction permettant de nettoyer l'inventaire du bateau et de le renvoyer

        Returns:
            a inventaire: inventaire du bateau pour récupérer et mettre dans le cimetiere
        """
        a = self.inventaire
        self.inventaire.nettoyer()
        return a
