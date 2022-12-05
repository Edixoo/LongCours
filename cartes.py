class carte:
    def __init__(self,type:int,nom:str) -> None:
        """Constructeur de la classe carte
        """
        self.type : int | None = None #0: Mouvement | 1: Tempête | 2: Bras de fer
        self.nom : str 
    
class carte_mouvement(carte):
    def __init__(self,typemouv:int,typenom:str) -> None:
        super().__init__(0,'carte_mouvement')
        self.typemouv: int | None = 0 #0: Mouvement direct | 1: Mouvement ordinaire
        self.typenom: str

class carte_tempete(carte):
    def __init__(self) -> None:
        super().__init__(1,'carte_tempete')
        pass

class carte_bdf(carte):
    def __init__(self,force:int,typenom:str) -> None:
        super().__init__(2,'carte_bdf')
        self.force: int
        self.typenom: str




