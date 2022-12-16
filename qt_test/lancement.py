import json
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QComboBox, QFormLayout, QLabel


class Player(QWidget):
    def __init__(self):
        super().__init__()
        
        self.mainLayout : QVBoxLayout = QVBoxLayout() ; self.setLayout(self.mainLayout)
        
        self.name_edit = QLineEdit() ; self.mainLayout.addWidget(self.name_edit)
        self.name_edit.setPlaceholderText("Entrez le pseudos du joueur ")
        
        self.selecteur_couleurs = QComboBox() ; self.mainLayout.addWidget(self.selecteur_couleurs)
        self.selecteur_couleurs.addItems(['Noir','Bleu','Jaune', 'Vert', 'Rouge'])#juste pour test


class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400,400)
        # self.move(50, 50)

        # Création des widgets pour saisir les informations
        self.choix = QLabel("Choissisez le nombre de joueur")
        self.choix1 = QLabel("Choissisez la couleur du bateau")


        # Création du bouton pour enregistrer les informations dans un fichier JSON
        self.save_button = QPushButton("Enregistrer")
        self.save_button1 = QPushButton("Save")


        # Mise en place de la disposition de la fenêtre
        self.mainLayout = QHBoxLayout()
        #selecteur
        
        self.selecteur = QComboBox()
        self.selecteur.addItems(['2','3','4', '5', '6'])
        
        #addWidget
        
        self.mainLayout.addWidget(self.choix)
        self.mainLayout.addWidget(self.selecteur)
        self.mainLayout.addWidget(self.save_button)
        
        self.setLayout(self.mainLayout)
        
        self.records = []
        
        #slots ie back
        self.save_button.clicked.connect(self.getpseudos)


    def getpseudos(self):
        self.selecteur.hide()
        self.save_button.hide()
        self.choix.hide()
        self.mainLayout.addWidget(self.save_button1)
        self.mainLayout.addWidget(self.choix1)
        nb = int(self.selecteur.currentText())

        self.playersLayout : QVBoxLayout = QVBoxLayout() ; self.mainLayout.addLayout(self.playersLayout)
        self.playersList : list[Player] = []
        for i in range (0, nb):
            # self.midLayout = QFormLayout()
            p = Player() ; self.playersLayout.addWidget(p)
            self.playersList.append(p)

            
        self.save_button1.clicked.connect(self.save_data)


    def save_data(self):
        
        #TODO faire ca        
        # self.playersList[i].name_edit.text()
        # A chaque tour de boucle tu ajoutes un nv joueur (comme dans l'annuaire avec des personnes)
        
        
        
        
        
        # name = self.name_edit.text()
        # bateau = self.selecteur_couleurs.currentText()
        # data = {"name" : name, "coulduf bateau": bateau}
        # # Récupération des données saisies par l'utilisateur
            
        # self.records.append(data)

        # # Ecriture des données dans un fichier JSON
        # with open("data.json", "w") as f:
        #     json.dump(self.records, f)
        pass




if __name__ == "__main__":
    app = QApplication([])
    form = Form()
    form.show()
    app.exec()
