import inventaire
import cimetiere
import port
import joueurs

class zonedejeu:
    def __init__(self,id:int) -> None:
        self.idzone: int = id
        self.listeport: list[port.port]
        self.cimetiere: cimetiere.cimetiere = cimetiere.cimetiere()
        
        for i in range(3): #Initialisation des ports présents dans la zonedejeu
            if(id%2==0):
                self.listeport.append(port.port(i,"cereale","Port"))
                self.listeport.append(port.port(i,"gold","Port"))
                self.listeport.append(port.port(i,"textile","Port"))
            else:
                self.listeport.append(port.port(i,"petrole","Port"))
                self.listeport.append(port.port(i,"bois","Port"))
                self.listeport.append(port.port(i,"machine_outils","Port"))
            
        