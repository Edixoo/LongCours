import marchandises

class inventaire(marchandises):
    def __init__(self) -> None:
        self.inventaire=[marchandises.marchandises]

    def ajouter(self, march: marchandises.marchandises):
        for i in self.inventaire:
            if i.nom==march.nom:
                i.quantite+=march.quantite
        self.inventaire.append(march)

    def retirer(self, march: marchandises):
        for i in self.inventaire:
            if i.nom==march.nom:
                i.quantite-=march.quantite

