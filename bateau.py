import inventaire

class bateau:
    def __init__(self, couleur : str):
   
        self.couleur: str = couleur
        self.inventaire: inventaire.inventaire
        
    def ajouter(self, marchandise):
        self.inventaire.ajouter(marchandise)

    def retirer(self, marchandise):
        self.inventaire.retirer(marchandise)

    