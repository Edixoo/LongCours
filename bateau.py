import inventaire

class bateau:
    def __init__(self, couleur : str):
   
        self.couleur: str = couleur
        self.inventaire: inventaire.inventaire = inventaire.inventaire()
        
    