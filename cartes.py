class carte:
    def __init__(self,type:int,nom:str) -> None:
        
        
        self.type : int | None = None #0: Mouvement | 1: Tempête | 2: Bras de fer
        self.nom : str 
    # def use(self)-> int,int:
    #     pass

    def affichercarte(self)->None:
        for i in self:
            print(i)
class carte_mouvdirect(carte):
    """Constructeur de la classe carte de mouvement direct"""
    def __init__(self) -> None:
        super().__init__(0,'carte_mouvdirect')
        pass
    def use(self) -> int:
        a=-1;b=-1
        while((a<0 or a>5) and (b<0 or b>4)):
            print('Où souhaitez vous aller ? (Zone: 0->5)')
            a=int(input())
            print('Port: 0->4 [4 = cimetiere]')
            b=int(input())
        return a,b
class carte_tempete(carte):
    """Constructeur de la classe carte tempête"""
    def __init__(self) -> None:
        super().__init__(1,'carte_tempete')
        pass
    def use(self)-> None:
        indcible=-1
        print('Sur quel joueur souhaitez vous déclencher la tempête ?')
        indcible=input()
        indcible-=1
        return indcible

class carte_bdf(carte):
    """Constructeur de la classe carte bras de fer"""
    def __init__(self,force:int,typenom:str) -> None:
        super().__init__(2,'carte_bdf')
        self.force: int = force
        self.typenom: str = typenom
    def use(self)-> None:
        print("Vous jouez la carte bras de fer de force",self.force)
        return self.force




