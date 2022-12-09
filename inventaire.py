class inventaire:
    
    def __init__(self) -> None:
        self.gold=[];
        self.textile=[];
        self.bois=[];
        self.petrole=[];
        self.cereale=[];
        self.machine_outil=[];

    def ajouter(self, march):
        match march.nom:
            case "or":
                self.gold.append(march)
            case "textile":
                self.textile.append(march)
            case "petrole":
                self.petrole.append(march)
            case "bois":
                self.bois.append(march)
            case "cereale":
                self.cereale.append(march)
            case "machine_outils":
                self.machine_outil.append(march)

    def retirer(self, march):
        match march.nom:
            case "or":
                self.gold.remove(march)
            case "textile":
                self.textile.remove(march)
            case "petrole":
                self.petrole.remove(march)
            case "bois":
                self.bois.remove(march)
            case "cereale":
                self.cereale.remove(march)
            case "machine_outils":
                self.machine_outil.remove(march)

    def __str__(self) -> str:
        print("Contenu de l'inventaire:")
        resultat=""
        if len(self.gold)==0:
            resultat+="- Or: Vide \n"
        else: 
            resultat+="- Or: \n"
            for i in self.gold:
                resultat+="     - "+i
        


        # resultat=""
        # resultat+=" - Or: " + str(self.gold) + "\n"
        # resultat+=" - Pétrole: " + str(self.petrole) + "\n"
        # resultat+=" - Céréale: " + str(self.cereale) + "\n"
        # resultat+=" - Bois: " + str(self.bois) + "\n"
        # resultat+=" - F: " + str(sel) + "\n"
        return resultat
if __name__=="__main__":
    r=inventaire()
    r.ajouter