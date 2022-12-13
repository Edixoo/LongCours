class marchandises:
    def __init__(self,qttach:int,type:str,couleur:str):
        self.qttachete:int =qttach
        self.nom:str = type
        self.couleur: str = couleur
        self.valeurachat: int = 150


class cereale(marchandises):
    def __init__(self,qttach:int) -> None:
        super().__init__(qttach,'cereale','bleu')
        pass
class gold(marchandises):
    def __init__(self,qttach:int) -> None:
        super().__init__(qttach,'gold','jaune')
        pass
class textile(marchandises):
    def __init__(self,qttach:int) -> None:
        super().__init__(qttach,'textile','vert')
        pass
class petrole(marchandises):
    def __init__(self,qttach:int) -> None:
        super().__init__(qttach,'petrole','noir')
        pass
class bois(marchandises):
    def __init__(self,qttach:int) -> None:
        super().__init__(qttach,'bois','marron')
        pass
class machine_outils(marchandises):
    def __init__(self,qttach:int) -> None:
        super().__init__(qttach,'machine_outils','gris')
        pass





