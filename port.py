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
                march=marchandises.cereale(0)
                self.marchandise=march
            case "gold":
                march=marchandises.cereale(0)
                self.marchandise=march
            case "textile":
                march=marchandises.cereale(0)
                self.marchandise=march
            case "petrole":
                march=marchandises.cereale(0)
                self.marchandise=march
            case "bois":
                march=marchandises.cereale(0)
                self.marchandise=march
            case "machine_outils":
                march=marchandises.cereale(0)
                self.marchandise=march
            case _:
                march=marchandises.marchandises(0,"Marchandise invalide","Pas de couleur")
                print("Erreur de saisie")