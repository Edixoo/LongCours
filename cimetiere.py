import bateau

class cimetiere:
    def __init__(self) -> None:
        self.cargaisons = [bateau.inventaire]
        
        def echouer(self, bateau):
            self.cargaisons.append(bateau.inventaire)
        
        def ramassercargaison(self, bateau):
            for i in range(len(self.cargaisons)):
                bateau.cargaisons.gold+=self.cargaisons[0].gold
                bateau.cargaisons.textile+=self.cargaisons[0].textile
                bateau.cargaisons.bois+=self.cargaisons[0].bois
                bateau.cargaisons.petrole+=self.cargaisons[0].petrole
                bateau.cargaisons.cereale+=self.cargaisons[0].cereale
                bateau.cargaisons.machine_outils+=self.cargaisons[0].machine_outils
                del self.cargaison[0]
            

                