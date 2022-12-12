import inventaire

class bateau:
    def __init__(self, couleur : str):
   
        self.couleur: str = couleur
        self.inventaire: inventaire.inventaire
        
        
    def ajoutermarchandises(self, marchandise):
        self.inventaire.ajouter(marchandise)

    def retirermarchandises(self, marchandise):
        self.inventaire.retirer(marchandise)

    