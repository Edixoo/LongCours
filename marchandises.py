class marchandises:
    def __init__(self):
        self.qtt:int = 0
        self.nom:str
        self.couleur: str 
        self.valeurachat: int = 150

    def cereale(self):
        self.nom = 'cereale'
        self.couleur = 'bleu'
    
    def gold(self):
        self.nom = 'or'
        self.couleur = 'jaune'

    def textile(self):
        self.nom = 'textile'
        self.couleur = 'vert'

    def petrole(self):
        self.nom = 'petrole'
        self.couleur = 'noir'
    
    def bois(self):
        self.nom = 'bois'
        self.couleur = 'marron'

    def machines_outils(self):
        self.nom = 'machine_outils'
        self.couleur = 'gris'




