import json
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QComboBox, QFormLayout, QLabel

class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400,400)
        # self.move(50, 50)

        # Création des widgets pour saisir les informations
        self.name_edit = QLineEdit()
        self.couleur_edit= QLineEdit()
        self.choix = QLabel("Choissisez le nombre de joueur")


        # Création du bouton pour enregistrer les informations dans un fichier JSON
        self.save_button = QPushButton("Enregistrer")
        self.save_button1 = QPushButton("Save")


        # Mise en place de la disposition de la fenêtre
        self.layout = QVBoxLayout()
        #selecteur
        self.selecteur = QComboBox()
        self.selecteur.addItems(['2','3','4', '5', '6'])
        
        #addWidget
        self.layout.addWidget(self.choix)
        self.layout.addWidget(self.selecteur)
        self.layout.addWidget(self.save_button)

        self.setLayout(self.layout)
        
        self.records = []
        
        #slots ie back
        self.save_button.clicked.connect(self.getpseudos)


    def getpseudos(self):
        self.selecteur.hide()
        self.save_button.hide()
        self.layout.addWidget(self.save_button1)
        self.layout.addWidget(self.name_edit)
        self.layout.addWidget(self.couleur_edit)
        
        nb = int(self.selecteur.currentText())

        for i in range (0,nb):
            self.midLayout = QFormLayout()
            self.midLayout.addRow("Pseudos :", self.name_edit)
            self.midLayout.addRow("Couleur Bateau :", self.couleur_edit)
            self.layout.addLayout(self.midLayout)
        self.save_button1.clicked.connect(self.save_data)


    def save_data(self):
        name = self.name_edit.text()
        bateau = self.couleur_edit.text()
        data = {"name" : name, "bateau": bateau}
        # Récupération des données saisies par l'utilisateur
            
        self.records.append(data)

        # Ecriture des données dans un fichier JSON
        with open("data.json", "w") as f:
            json.dump(self.records, f)

if __name__ == "__main__":
    app = QApplication([])
    form = Form()
    form.show()
    app.exec()
