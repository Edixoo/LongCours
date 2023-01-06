import marchandises
class inventaire:
    
    def __init__(self) -> None:
        """Constructeur de l'inventaire"""
        self.gold=[]
        self.textile=[]
        self.bois=[]
        self.petrole=[]
        self.cereale=[]
        self.machine_outils=[]

    def ajouter(self, march:marchandises.marchandises):
        """Fonction d'ajout d'une marchandise (utile lors de l'achat)"""
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

    def retirer(self, march):
        """Fonction de retrait d'une marchandise (utile lors de l'achat)"""
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

    def echouer(self):
        """Fonction remettant l'inventaire à 0"""
        self.gold=[]
        self.textile=[]
        self.bois=[]
        self.petrole=[]
        self.cereale=[]
        self.machine_outils=[]

    def nettoyer(self):
        self.gold.clear()
        self.bois.clear()
        self.cereale.clear()
        self.machine_outils.clear()
        self.petrole.clear()
        self.textile.clear()

    def __str__(self) -> str:
        print("Contenu de l'inventaire:")
        resultat=""
        if len(self.gold)==0:
            resultat+="- Or: Vide \n"
        else: 
            resultat+="- Or: \n"
            for i in self.gold:
                resultat+="     - "+i
                
        if(len(self.textile)==0):
            resultat+="- Textile: Vide\n"
        else: 
            resultat+="- Textile: \n"
            for i in self.textile:
                resultat+="     - "+i
                
        if(len(self.cereale)==0):
            resultat+="- Cereale: Vide\n"
        else:
            resultat+="- Cereale: \n"
            for i in self.cereale:
                resultat+="     - "+i
                
        if(len(self.bois)==0):
            resultat+="- Bois: Vide\n"
        else:
            resultat+="- Bois: \n"
            for i in self.bois:
                resultat+="     - "+i
            
        if(len(self.machine_outils)==0):
            resultat+="- Machine_outils : Vide\n"
        else:
            resultat+="- Machine_outils \n"
            for i in self.machine_outils:
                resultat+="     - "+i
 
 
        return resultat
    
