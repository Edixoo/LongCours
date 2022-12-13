import bateau
import inventaire
import joueurs

class cimetiere:
    def __init__(self):
        self.inventaire : list[inventaire.inventaire] = []
        self.presence : list[joueurs.joueur] = []
        
    def recupechouage(self, bateau:bateau.bateau):
        self.inventaire.append(bateau.inventaire)
        bateau.inventaire.echouer()

    def ramassercargaison(self, bateau:bateau.bateau):
        for i in range(len(self.inventaire)):
            bateau.inventaire.gold+=self.inventaire[0].gold
            bateau.inventaire.textile+=self.inventaire[0].textile
            bateau.inventaire.bois+=self.inventaire[0].bois
            bateau.inventaire.petrole+=self.inventaire[0].petrole
            bateau.inventaire.cereale+=self.inventaire[0].cereale
            bateau.inventaire.machine_outils+=self.inventaire[0].machine_outils
            del self.inventaire[0]
            

                