class port:
    def __init__(self, nom, marchandise) -> None:
        
        self.nom= nom
        self.marchandise=marchandise
        self.couleur=marchandise.couleur
        self.presence=[] #liste des joueurs présent dans le port