import inventaire
import cimetiere
import port
import joueurs

class zonedejeu:
    def __init__(self,id:int) -> None:
        self.idzone: int = id
        self.listeport: list[port.port] =[]
        self.cimetiere: cimetiere.cimetiere = cimetiere.cimetiere()
         #Initialisation des ports présents dans la zonedejeu
        if(id%2==0):
            self.listeport.append(port.port(0,"cereale","Port"))
            self.listeport.append(port.port(1,"gold","Port"))
            self.listeport.append(port.port(2,"textile","Port"))
        else:
            self.listeport.append(port.port(0,"petrole","Port"))
            self.listeport.append(port.port(1,"bois","Port"))
            self.listeport.append(port.port(2,"machine_outils","Port"))
            
        