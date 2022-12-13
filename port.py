import joueurs
import marchandises

class port:
    def __init__(self, nom, marchandise) -> None:
        
        self.nom= nom
        self.marchandise : marchandises.marchandises
        self.couleur=marchandise.couleur
        self.presence=[joueurs.joueur] #liste des joueurs présent dans le port
