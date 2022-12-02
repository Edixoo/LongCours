class marchandises:
    def __init__(self, ticket: int, nom:str, couleur : str):
        self.ticket_max:  str
        self.nom : str
        self.couleur : str
        
class tresort (marchandises):
    def __init__(self) -> None:
        super().__init__(40, 'textile','jaune')
        
class textiles(marchandises):
    def __init__(self) -> None:
        super().__init__(40, 'textile')
    
class petrole(marchandises):
    def __init__(self)-> None:
        super().__init__(40,'petrole','bleu')
        
class cereales(marchandises):
    def __init__(self)-> None:
        super().__init__(40, 'cereales')
        
class bois(marchandises):
    def __init__(self)-> None:
        super().__init__(40,'bois','marron')
        
class machines_outils(marchandises):
    def __init__(self) -> None :
        super().__init__(40,'machines-outils')
        
def __str__(self):
    pass

          

if __name__ == '__main__':
    pass
 