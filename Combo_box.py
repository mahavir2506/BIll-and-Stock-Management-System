import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton,QCompleter, QComboBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSortFilterProxyModel
app = QApplication(sys.argv)
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,400,600)#position_X,position_Y,Width,Height
        self.setWindowTitle("QLineEdit Example")
        self.combo=QComboBox(self)
        self.combo.setFocusPolicy(Qt.StrongFocus)
        self.combo.setEditable(False)
        #self.combo.lineEdit().textEdited.connect(self.pFilterModel.setFilterFixedString)
        #self.completer.activated.connect(self.on_completer_activated)
        self.submit=QPushButton("Click",self) 
        self.show_combo_text=QLabel(self)
        self.show_combo_text.setText("hello")
        self.show_combo_text.move(100,250)
        self.submit.move(100,200) 
        string_list = ['Agrawal Mahavir', 'Agrawal Mahi', 'Agrawal nirmal', 'good bye']#data base load
        self.combo.addItems(string_list)
        self.combo.move(100,100)#x ,y
        self.submit.clicked.connect(lambda:self.clickme(5))
        self.combo.resize(300, 40)
        self.show()
    def clickme(self,n):
       print("hello",n) 
    
ex=Example()
sys.exit(app.exec_()) 