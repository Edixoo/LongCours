import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QPushButton, QLineEdit, QVBoxLayout, QComboBox

class combo(QWidget):
   def __init__(self, parent = None):
      super(combo, self).__init__(parent)
      self.resize(700,700)
      self.move(50, 50)
      self.choix = QLabel("Choissisez le nombre de joueur")
      

      self.layout = QHBoxLayout()
      self.cb = QComboBox()
      self.cb.addItems(['2','3','4', '5', '6'])
    
     
      self.setLayout(self.layout)
      self.setWindowTitle("Commencez le jeu")
      
      self.layout.addWidget(self.choix)
      self.layout.addWidget(self.cb)
      
    # slots ie callback
      self.cb.currentIndexChanged.connect(self.selectionchange)

   def selectionchange(self,i):
      print ("Current index",i,"selection changed ",self.cb.currentText())
      self.getpseudos()
      
   def getpseudos(self):
       pseudos = int(self.cb.currentText())
       
       self.joueurs_nom = []
       for i in range(0,pseudos):
            self.joueurs_nom = QLineEdit()
            self.layout.addWidget(self.joueurs_nom)
       return self.joueurs_nom
      
    
    
def main():
   app = QApplication(sys.argv)
   ex = combo()
   ex.show()
   sys.exit(app.exec())

if __name__ == '__main__':
   main()
        
