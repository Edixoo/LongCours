class bateaux:
    def __init__(self, type : str, couleur : str):
   
        self.type: str = type
        self.couleur: str = couleur
        self.nb_bateaux : int = 7
        
class corsaire(bateaux):
    def __init__(self)-> None:
        super().__init__("corsaire", "noir")
        
    