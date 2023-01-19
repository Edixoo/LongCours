import marchandises
class inventaire:
    
    def __init__(self) -> None:
        """Constructeur de l'inventaire"""
        self.gold: list[marchandises.marchandises] =[]
        self.textile: list[marchandises.marchandises] =[]
        self.bois: list[marchandises.marchandises] =[]
        self.petrole: list[marchandises.marchandises] =[]
        self.cereale: list[marchandises.marchandises] =[]
        self.machine_outils: list[marchandises.marchandises] =[]

    def ajouter(self, march:marchandises.marchandises):
        """Fonction d'ajout d'une marchandise (utile lors de l'achat)

        Args:
            march (marchandises.marchandises): objet de type marchandise
        """
        match march.nom:
            case "gold":
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
                self.machine_outils.append(march)
    
    def retirergraph(self, march:marchandises.marchandises):
        """Fonction d'ajout d'une marchandise (utile lors de l'achat)

        Args:
            march (marchandises.marchandises): objet de type marchandise
        """
        match march.nom:
            case "gold":
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
                self.machine_outils.remove(march)

    def retirer(self, qtt:int,typemarch:int):
        """Fonction de retrait d'une marchandise (utile lors de la vente)

        Args:
            qtt (int): quantite à retirer
            typemarch (int): le type de la marchandise à retirer

        Returns:
            int: retourne le prix
        """
        qttvendue=0
        prixacq=0
        match typemarch:
            case 0:
                while(qttvendue!=qtt):
                    for i in range (len(self.gold)):
                        if(self.gold[i].qttachete<(qtt-qttvendue)):
                            qttvendue+=self.gold[i].qttachete
                            prixacq+=(self.gold[i].prix_achat*self.gold[i].qttachete)
                            self.gold.remove(i)
                        else:
                            dif=qtt-qttvendue
                            self.gold[i].qttachete-=dif
                            qttvendue+=dif
                            prixacq+=(self.gold[i].prix_achat*dif)
                return prixacq
            case 1:
                while(qttvendue!=qtt):
                    for i in range (len(self.textile)):
                        if(self.textile[i].qttachete<(qtt-qttvendue)):
                            qttvendue+=self.textile[i].qttachete
                            prixacq+=(self.textile[i].prix_achat*self.textile[i].qttachete)
                            self.textile.remove(i)
                        else:
                            dif=qtt-qttvendue
                            self.textile[i].qttachete-=dif
                            qttvendue+=dif
                            prixacq+=(self.textile[i].prix_achat*dif)
                return prixacq
            case 2:
                while(qttvendue!=qtt):
                    for i in range (len(self.bois)):
                        if(self.bois[i].qttachete<(qtt-qttvendue)):
                            qttvendue+=self.bois[i].qttachete
                            prixacq+=(self.bois[i].prix_achat*self.bois[i].qttachete)
                            self.bois.remove(i)
                        else:
                            dif=qtt-qttvendue
                            self.bois[i].qttachete-=dif
                            qttvendue+=dif
                            prixacq+=(self.bois[i].prix_achat*dif)
                return prixacq
            case 3:
                while(qttvendue!=qtt):
                    for i in range (len(self.petrole)):
                        if(self.petrole[i].qttachete<(qtt-qttvendue)):
                            qttvendue+=self.petrole[i].qttachete
                            prixacq+=(self.petrole[i].prix_achat*self.petrole[i].qttachete)
                            self.petrole.remove(i)
                        else:
                            dif=qtt-qttvendue
                            self.petrole[i].qttachete-=dif
                            qttvendue+=dif
                            prixacq+=(self.petrole[i].prix_achat*dif)
                return prixacq
            case 4:
                while(qttvendue!=qtt):
                    for i in range (len(self.cereale)):
                        if(self.cereale[i].qttachete<(qtt-qttvendue)):
                            qttvendue+=self.cereale[i].qttachete
                            prixacq+=(self.cereale[i].prix_achat*self.cereale[i].qttachete)
                            self.cereale.remove(i)
                        else:
                            dif=qtt-qttvendue
                            self.cereale[i].qttachete-=dif
                            qttvendue+=dif
                            prixacq+=(self.cereale[i].prix_achat*dif)
                return prixacq
            case 5:
                while(qttvendue!=qtt):
                    for i in range (len(self.machine_outils)):
                        if(self.machine_outils[i].qttachete<(qtt-qttvendue)):
                            qttvendue+=self.machine_outils[i].qttachete
                            prixacq+=(self.machine_outils[i].prix_achat*self.machine_outils[i].qttachete)
                            self.machine_outils.remove(i)
                        else:
                            dif=qtt-qttvendue
                            self.machine_outils[i].qttachete-=dif
                            qttvendue+=dif
                            prixacq+=(self.machine_outils[i].prix_achat*dif)
                return prixacq

    def nettoyer(self):
        """Fonction permettant de vider l'inventaire
        """
        self.gold.clear()
        self.bois.clear()
        self.cereale.clear()
        self.machine_outils.clear()
        self.petrole.clear()
        self.textile.clear()

    
    def getGold(self):
        """Fonction permettant d'obtenir le nombre de d'or

        Returns:
            str: nombre de d'or
        """
        resultat=0
        if len(self.gold)==0:
            return "Vide"
        for i in self.gold:
            resultat+=i.qttachete
        return str(resultat)
    
    def getTextile(self):
        """Fonction permettant d'obtenir le nombre de textile

        Returns:
            str: nombre de textile
        """
        resultat=0
        if len(self.textile)==0:
            return "Vide"
        for i in self.textile:
            resultat+=i.qttachete
        return str(resultat)
    
    def getBois(self):
        """Fonction permettant d'obtenir le nombre de bois

        Returns:
            str: nombre de bois
        """
        resultat=0
        if len(self.bois)==0:
            return "Vide"
        for i in self.bois:
            resultat+=i.qttachete
        return str(resultat)

    def getPetrole(self):
        """Fonction permettant d'obtenir le nombre de pétrole

        Returns:
            str: nombre de pétrole
        """
        resultat=0
        if len(self.petrole)==0:
            return "Vide"
        for i in self.petrole:
            resultat+=i.qttachete
        return str(resultat)

    def getCereale(self):
        """Fonction permettant d'obtenir le nombre de céréales

        Returns:
            str: nombre de céréales
        """
        resultat=0
        if len(self.cereale)==0:
            return "Vide"
        for i in self.cereale:
            resultat+=i.qttachete
        return str(resultat)

    def getMachineOutils(self):
        """Fonction permettant d'obtenir le nombre de machine à outils

        Returns:
            str: nombre de machine à outils
        """
        resultat=0
        if len(self.machine_outils)==0:
            return "Vide"
        for i in self.machine_outils:
            resultat+=i.qttachete
        return str(resultat)

    def getMarchandiseByName(self, marchandise: marchandises.marchandises):
        match marchandise.nom:
            case "cereale":
                return self.getCereale()
            case "bois":
                return self.getBois()
            case "petrole":
                return self.getPetrole()
            case "machine_outils":
                return self.getMachineOutils()
            case "gold":
                return self.getGold()
            case "textile":
                return self.getTextile()
        
    def __str__(self) -> str:
        """Redéfinition du print pour l'objet inventaire

        Returns:
            str: format d'affichage reformaté
        """
        resultat=""
        if len(self.gold)==0:
            resultat+="- Or: Vide \n"
        else: 
            resultat+="- Or: \n"
            for i in self.gold:
                resultat+="     - "+ str(i.qttachete)
                
        if(len(self.textile)==0):
            resultat+="- Textile: Vide\n"
        else: 
            resultat+="- Textile: "
            for i in self.textile:
                resultat+=str(i.qttachete)+"\n"
                
        if(len(self.cereale)==0):
            resultat+="- Cereale: Vide\n"
        else:
            resultat+="- Cereale: "
            for i in self.cereale:
                resultat+=str(i.qttachete)+"\n"
                
        if(len(self.bois)==0):
            resultat+="- Bois: Vide\n"
        else:
            resultat+="- Bois: "
            for i in self.bois:
                resultat+=str(i.qttachete)+"\n"
            
        if(len(self.machine_outils)==0):
            resultat+="- Machine_outils : Vide\n"
        else:
            resultat+="- Machine_outils "
            for i in self.machine_outils:
                resultat+=str(i.qttachete)+"\n"

        if(len(self.petrole)==0):
            resultat+="- Petrole: Vide\n"
        else:
            resultat+="- Petrole:"
            for i in self.petrole:
                resultat+=str(i.qttachete)+"\n"
 
        return resultat
    
