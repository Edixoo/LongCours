class inventaire:
    
    def __init__(self) -> None:
        self.inventaire={}
        self.inventaire["gold"]=0
        self.inventaire["textile"]=0
        self.inventaire["petrole"]=0
        self.inventaire["cereale"]=0
        self.inventaire["bois"]=0
        self.inventaire["machine-outil"]=0

    def ajouter(self, march):
        self.inventaire[march.nom]+=march.quantite

    def retirer(self, march):
        self.inventaire[march.nom]-=march.quantite

    def __str__(self):
        print("Contenu de l'inventaire:")
        resultat=""
        for i in self.inventaire.keys():
            resultat+=" - " + i +": " + str(self.inventaire[i]) + "\n"
        return resultat

    def getOr(self):
        return self.inventaire["gold"]

    def getTextile(self):
        return self.inventaire["textile"]
    
    def getPetrole(self):
        return self.inventaire["petrole"]
    
    def getCereale(self):
        return self.inventaire["cereale"]
    
    def getBois(self):
        return self.inventaire["bois"]
    
    def getMachine_Outil(self):
        return self.inventaire["machine-outil"]