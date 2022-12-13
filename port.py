import joueurs
import marchandises

class port:
    def __init__(self,id:int,type:str) -> None:
        
        self.id:int =id
        self.marchandise : marchandises.marchandises
        self.couleur:marchandises.marchandises.couleur
        self.presence: list[joueurs.joueur] #liste des joueurs présent dans le port

        match type:
            case "cereale":

            case "machine_outils":
                ...