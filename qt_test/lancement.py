
from PyQt6.QtWidgets import  QWidget, QLineEdit, QPushButton,QVBoxLayout, QLabel, QMessageBox
from PyQt6 import QtCore, QtGui, QtWidgets
import ressources as r
import json
import random
import sys

class Player(QWidget):
    def __init__(self):
        super().__init__()
        self.mainLayout : QVBoxLayout = QVBoxLayout() ; self.setLayout(self.mainLayout)
        self.name_edit = QLineEdit() ; self.mainLayout.addWidget(self.name_edit)
        self.name_edit.setPlaceholderText("Entrez le pseudo du joueur ")
        self.name_edit.setStyleSheet("QLineEdit{\n"
"color: rgb(255, 255, 255);\n"
"}")

       
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setStyleSheet("#centralwidget\n"
"{\n"
"    background-image: url(:/img/background_map.png);\n"


"}")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.ItemRole.FieldRole, spacerItem)
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        self.formFrame = QtWidgets.QFrame(self.centralwidget)
        self.formFrame.setMaximumSize(QtCore.QSize(1677721, 1677721))
        self.formFrame.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.formFrame.setStyleSheet("#formFrame{\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(246, 211, 101, 255), stop:1 rgba(251, 171, 126, 255));\n"
"padding:50px;\n"
"margin-top : 30px;\n"
"border : 2px solid;\n"
"}\n"
"#label{\n"
"color : \"white\";\n"
"font-size : 18px;\n"
"margin-top : 30px;\n"
"}")
        self.formFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.formFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.formFrame.setObjectName("formFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.formFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.save_button = QtWidgets.QPushButton(self.formFrame)
        
        self.save_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ClosedHandCursor))
        self.save_button.setMouseTracking(True)
        self.save_button.setStyleSheet("#save_button{\n"
"margin-top : 15px;\n"
"height : 50px;\n"
"width: 100px;\n"
"color : white;\n"
"background-color: green;\n"
"font-size : 18px;\n"
"border-radius : 15px;\n"
"}\n"
"\n"
"#save_button:hover{\n"
"border:2px solid green;\n"
"color:green;\n"
"background-color : white;\n"
"}")
        self.save_button.setObjectName("save_button")
        self.gridLayout_2.addWidget(self.save_button, 2, 0, 1, 1)

        self.selecteur = QtWidgets.QComboBox(self.formFrame)
        self.selecteur.setStyleSheet("#selecteur{\n"
"background-color: rgb(255, 255, 255);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.selecteur.setObjectName("selecteur")
        self.selecteur.addItem("")
        self.selecteur.addItem("")
        self.selecteur.addItem("")
        self.selecteur.addItem("")
        self.selecteur.addItem("")
        self.gridLayout_2.addWidget(self.selecteur, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.formFrame)
        self.label.setStyleSheet("QLabel{\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.mainLayout.addWidget(self.formFrame)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.mainLayout)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.ItemRole.LabelRole, spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.ItemRole.FieldRole, spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.ItemRole.FieldRole, spacerItem3)
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(450, 248))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-image: url(:/logo/logo.png);\n"
"background-repeat : no-repeat;"
"border:none;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        # self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.save_button.setText(_translate("MainWindow", "Enregistrer"))
        self.selecteur.setItemText(0, _translate("MainWindow", "2"))
        self.selecteur.setItemText(1, _translate("MainWindow", "3"))
        self.selecteur.setItemText(2, _translate("MainWindow", "4"))
        self.selecteur.setItemText(3, _translate("MainWindow", "5"))
        self.selecteur.setItemText(4, _translate("MainWindow", "6"))
        self.label.setText(_translate("MainWindow", "Choissisez le nombre de joueurs"))
        #slots
        self.save_button.clicked.connect(self.updatescreen)

    def updatescreen(self):
        self.save_button.hide()
        self.selecteur.hide()
        self.label.hide()
        self.get_pseudos()
      

    def get_pseudos(self):
        self.save_button1 = QPushButton("Commencez")
        self.save_button1.setStyleSheet("QPushButton{\n"
"margin-top : 15px;\n"
"height : 50px;\n"
"width: 100px;\n"
"color : white;\n"
"background-color: green;\n"
"font-size : 18px;\n"
"border-radius : 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:2px solid green;\n"
"color:green;\n"
"background-color : white;\n"
"}")
        self.save_button1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ClosedHandCursor))
        self.save_button1.setMouseTracking(True)
        self.gridLayout_2.addWidget(self.save_button1, 2, 0, 1, 1)

        nb_players = int(self.selecteur.currentText())
        choice = QLabel("Veuillez entrez le pseudo des joueurs")
        choice.setStyleSheet("QLabel{\n"
"color : \"white\";\n"
"font-size : 18px;\n"
"margin-top : 30px;\n"
"}")
        self.gridLayout_2.addWidget(choice, 1, 0, 1, 1)
        self.playersLayout : QVBoxLayout = QVBoxLayout() ; self.mainLayout.addLayout(self.playersLayout)
        self.playersList : list[Player] = []
        
        self.nb_players = int(self.selecteur.currentText())
        self.choix_couleurs = ["Bleu", "Vert", "Jaune", "Noir","Gris", "Rose", "Marron","Orange","Rouge"]
        self.couleurs = random.sample(self.choix_couleurs,self.nb_players)
        self.players_label =  []
        self.playersList : list[Player] = []
        #pour chaque joueur selectionné, le nom est demandé et la couleur attribuée avec un random
        for i in range (0, self.nb_players):
            p = Player() ; self.playersLayout.addWidget(p)
            self.label_2 = QLabel(self.couleurs[i])
            self.playersLayout.addWidget(self.label_2)
            self.players_label.append(self.label_2)
            self.playersList.append(p)
            self.label_2.setStyleSheet("QLabel{\n"
"color : \"white\";\n"
"font-size : 18px;\n"
"}")
        self.save_button1.clicked.connect(self.save_data)
        
    def save_data(self):
        players = {}
        for i in range(0,len(self.playersList)):
            names =  self.playersList[i].name_edit.text()
            if not names:
                QMessageBox.warning(MainWindow, "Erreur", "Veuillez saisir le nom de chaque joueur.")
                return
            player_id = f"player{i+1}"            
            for color in range(0,len(self.couleurs)):
                color = self.couleurs[i]
                players[player_id] = {"name": names, "color" : color }
            
        self.records = []
        self.records.append(players)
        # Ecriture des données dans un fichier JSON
        with open('data.json', 'w') as f:
            json.dump(self.records,f)
        f.close()

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        try:
                sys.exit(app.exec())
        except:
                print("Exiting")
