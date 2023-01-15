class marchandises:
    def __init__(self,qttach:int,type:str,couleur:str):
        self.qttachete:int =qttach
        self.nom:str = type
        self.couleur: str = couleur
        self.prix_achat: float = 150
            
    def inflation(self):
        """Fonction inflation de la valeur de la marchandise"""
        self.prix_achat*=1.05
                

class cereale(marchandises):
    """Constructeur de cereale(marchandise)"""
    def __init__(self,qttach:int) -> None:
        super().__init__(qttach,'cereale','blue')
        
class gold(marchandises):
    """Constructeur de gold(marchandise)"""
    def __init__(self,qttach:int) -> None:
        super().__init__(qttach,'gold','yellow')
        pass
class textile(marchandises):
    """Constructeur de textile(marchandise)"""
    def __init__(self,qttach:int) -> None:
        super().__init__(qttach,'textile','green')
        pass
class petrole(marchandises):
    """Constructeur de petrole(marchandise)"""
    def __init__(self,qttach:int) -> None:
        super().__init__(qttach,'petrole','black')
        pass
class bois(marchandises):
    """Constructeur de bois(marchandise)"""
    def __init__(self,qttach:int) -> None:
        super().__init__(qttach,'bois','brown')
        pass
class machine_outils(marchandises):
    """Constructeur de machine_outils(marchandise)"""
    def __init__(self,qttach:int) -> None:
        super().__init__(qttach,'machine_outils','grey')
        pass

