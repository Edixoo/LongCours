import inventaire
import cimetiere
import port

class zonedejeu:
    def __init__(self) -> None:
        self.idzone: int 
        self.listeport: [port.port]
        self.cimetière: cimetiere.cimetiere