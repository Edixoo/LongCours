import bateau
import inventaire
import joueurs

class cimetiere:
    def __init__(self):
        self.inventaire : inventaire.inventaire
        self.presence : list[joueurs.joueur] = []
        
    def recupechouage(self, bateau:bateau.bateau):
        """Fonction permettant au bateau entré en paramètre de déposer son inventaire(le bateau à subis un tempête)"""
        self.inventaire.append(bateau.inventaire)
        bateau.inventaire.echouer()

    def ramassercargaison(self, bateau:bateau.bateau):
        """Fonction permettant au bateau entré en paramètre de récupérer le contenu du cimetiere"""
        for i in range(len(self.inventaire)):
            bateau.inventaire.gold+=self.inventaire.gold
            bateau.inventaire.textile+=self.inventaire.textile
            bateau.inventaire.bois+=self.inventaire.bois
            bateau.inventaire.petrole+=self.inventaire.petrole
            bateau.inventaire.cereale+=self.inventaire.cereale
            bateau.inventaire.machine_outils+=self.inventaire.machine_outils
            
            

                