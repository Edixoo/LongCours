import bateau

class cimetiere:
    def __init__(self) -> None:
        self.cargaisons = [bateau.inventaire]
        
        def ajouter(self, bateau):
            self.cargaisons.append(bateau.inventaire)
        
        def retirer(self, bateau):
            for i in range(len(self.cargaisons)):
                for w in range(len(self.cargaisons.gold)):
                    bateau.cargaisons.gold+=self.cargaisons[i].gold[w]

                for w in range(len(self.cargaisons.textile)):
                    bateau.cargaisons.textile+=self.cargaisons[i].textile[w]

                for w in range(len(self.cargaisons.bois)):
                    bateau.cargaisons.bois+=self.cargaisons[i].bois[w]

                for w in range(len(self.cargaisons.petrole)):
                    bateau.cargaisons.petrole+=self.cargaisons[i].petrole[w]

                for w in range(len(self.cargaisons.cereale)):
                    bateau.cargaisons.cereale+=self.cargaisons[i].cereale[w]

                for w in range(len(self.cargaisons.machine_outils)):
                    bateau.cargaisons.machine_outils+=self.cargaisons[i].machine_outils[w]
            

                