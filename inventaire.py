class inventaire:
    
    def __init__(self) -> None:
        self.inventaire=[]

    def ajouter(self, march):
        self.inventaire.append(march)

    def retirer(self, march):
        self.inventaire.pop(march)

    def consulter(self):
        print("Contenu de l'inventaire: \n")
        for i in self.inventaire:
            print(" - " + i + "\n")