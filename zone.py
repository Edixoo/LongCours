import inventaire
import cimetiere
import port
import joueurs

class zonedejeu:
    def __init__(self,id:int) -> None:
        self.idzone: int = id
        self.listeport: list[port.port]
        self.cimetiere: cimetiere.cimetiere = cimetiere.cimetiere()
        for i in range (3):
            self.listeport.append(port.port(i))
            
        