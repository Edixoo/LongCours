class carte:
    def __init__(self,type:int,nom:str) -> None:
        """Constructeur de base de la classe carte

        Args:
            type (int): permet de définir de quel carte il s'agit
            nom (str): nom de la carte
        """
        
        self.type : int | None = None #0: Mouvement | 1: Tempête | 2: Bras de fer
        self.nom : str 

    
class carte_mouvdirect(carte):
    """Constructeur de la classe carte de mouvement direct"""
    def __init__(self) -> None:
        super().__init__(type=0,nom="carte_mouvdirect")
        self.type=0
        self.nom="carte_mouvdirect"
    
    def use(self) -> int:
        """Fonction permettant de donner les coordonnées pour le déplacement du joueur

        Returns:
            a,b (int): les coordonnées
        """
        a=-1;b=-1
        while((a<0 or a>5) and (b<0 or b>3)):
            print('Où souhaitez vous aller ? (Zone: 0->5)')
            a=int(input())
            print('Port: 0->3 [3 = cimetiere]')
            b=int(input())
        return a,b
    
    def affichercarte(self)->None:
        print(self.nom)
        
class carte_tempete(carte):
    """Constructeur de la classe carte tempête"""
    def __init__(self) -> None:
        super().__init__(type=1,nom="carte_tempete")
        self.type=1
        self.nom="carte_tempete"
    
    def use(self)-> None:
        """Fonction permettant d'utiliser la carte

        Returns:
            int: indice de la cible
        """
        indcible=-1
        print('Sur quel joueur souhaitez vous déclencher la tempête ?')
        indcible=int(input())
        indcible-=1
        return indcible
    
    def affichercarte(self)->None:
        print(self.nom)

class carte_bdf(carte):
    """Constructeur de la classe carte bras de fer"""
    def __init__(self,force:int,typenom:str) -> None:
        super().__init__(type=2,nom="carte_bdf")
        self.type=2
        self.nom="carte_bdf"
        self.force: int = force
        self.typenom: str = typenom
    def use(self)-> None:
        """Fonction permettant d'obtenir la force de la carte

        Returns:
            int: force
        """
        print("Vous jouez la carte bras de fer de force",self.force)
        return self.force
    
    def affichercarte(self)->None:
        print("Carte bras de fer de",self.typenom)
        




