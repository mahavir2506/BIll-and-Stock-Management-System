import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton,QCompleter,QWidget,QTabWidget,QVBoxLayout,QLineEdit,QTableWidget,QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont

from PyQt5.QtCore import Qt, QSortFilterProxyModel
#font class
class font_class(QFont):
    def __init__(self):
        super().__init__("Times New Roman",12)
        
        
        
#  billing page class
class Billing(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel('                                                    Raghunandan Jewellers', self)
        self.label.move(0,0)
        self.label.resize(2000,80)
        self.label.setStyleSheet("border: 1px solid black; color:gold; background-color:black")
        self.label.setFont(QFont('Arial', 30))
        self.c_name = QLabel('Customer Name', self)
        self.c_name.setFont(font_class())
        self.c_name.move(25,110) 
        self.c_name_text=QComboBox(self)
        self.c_name_text.setFocusPolicy(Qt.StrongFocus)
        self.c_name_text.setEditable(True)
        self.c_name_text.move(180,110)
        self.c_name_text.setInsertPolicy(QComboBox.NoInsert) 
        self.pFilterModel = QSortFilterProxyModel(self.c_name_text)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.c_name_text.model())
        self.completer = QCompleter(self.pFilterModel, self.c_name_text)
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.c_name_text.setCompleter(self.completer)
        self.c_name_text.lineEdit().textEdited.connect(self.pFilterModel.setFilterFixedString)
        string_list = ['Agrawal Mahavir', 'Agrawal Mahi', 'Agrawal nirmal', 'good bye']#data base load
        self.c_name_text.addItems(string_list)
        self.c_name_text.resize(200,30)
        self.c_mobileno = QLabel('Mobile No.', self)
        self.c_mobileno.setFont(font_class())
        self.c_mobileno.move(420,110) 
        self.c_mobileno_text=QLineEdit(self)
        self.c_mobileno_text.move(554,110)
        self.c_mobileno_text.resize(200,30)
        self.c_address = QLabel('Address.', self)
        self.c_address.setFont(font_class())
        self.c_address.move(794,110) 
        self.c_address_text=QLineEdit(self)
        self.c_address_text.move(900,110)
        self.c_address_text.resize(200,30)
        self.c_billno = QLabel('Billno', self)
        self.c_billno.setFont(font_class())
        self.c_billno.move(1140,110) 
        self.c_address_text=QLineEdit(self)
        self.c_address_text.move(1220,110)
        self.c_address_text.resize(100,30)
        self.i_name = QLabel('Item Name', self)
        self.i_name.setFont(font_class())
        self.i_name.move(25,180) 
        self.i_name_text=QComboBox(self)
        self.i_name_text.setFocusPolicy(Qt.StrongFocus)
        self.i_name_text.setEditable(True)
        self.i_name_text.move(180,180)
        self.i_name_text.setInsertPolicy(QComboBox.NoInsert) 
        self.pFilterModel = QSortFilterProxyModel(self.i_name_text)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.i_name_text.model())
        self.completer = QCompleter(self.pFilterModel, self.i_name_text)
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.i_name_text.setCompleter(self.completer)
        self.i_name_text.lineEdit().textEdited.connect(self.pFilterModel.setFilterFixedString)
        string_list = ['Agrawal Mahavir', 'Agrawal Mahi', 'Agrawal nirmal', 'good bye']#data base load
        self.i_name_text.addItems(string_list)
        self.i_name_text.resize(200,30)
        self.i_weight = QLabel('Item Weight', self)
        self.i_weight.setFont(font_class())
        self.i_weight.move(420,180) 
        self.i_weight_text=QComboBox(self)
        self.i_weight_text.setFocusPolicy(Qt.StrongFocus)
        self.i_weight_text.setEditable(True)
        self.i_weight_text.move(555,180)
        self.i_weight_text.setInsertPolicy(QComboBox.NoInsert) 
        self.pFilterModel = QSortFilterProxyModel(self.i_weight_text)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.i_weight_text.model())
        self.completer = QCompleter(self.pFilterModel, self.i_name_text)
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.i_weight_text.setCompleter(self.completer)
        self.i_weight_text.lineEdit().textEdited.connect(self.pFilterModel.setFilterFixedString)
        string_list = ['Agrawal Mahavir', 'Agrawal Mahi', 'Agrawal nirmal', 'good bye']#data base load
        self.i_weight_text.addItems(string_list)
        self.i_weight_text.resize(200,30)
        self.i_price = QLabel('Price.', self)
        self.i_price.setFont(font_class())
        self.i_price.move(795,180) 
        self.i_price_text=QLineEdit(self)
        self.i_price_text.move(900,180)
        self.i_price_text.resize(200,30)
        self.add=QPushButton("ADD",self)
        self.add.move(1200,180)
        self.add.resize(100,30)
        self.add.setStyleSheet("border :4px solid ")
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.move(25,265)
        self.tableWidget.resize(1000,180)
        self.pending_Ammount=QLabel("Pending Ammount : 8000",self)
        self.pending_Ammount.setFont(font_class())
        self.pending_Ammount.move(850,465)
        self.total_Buying_Ammount=QLabel("Buying Ammount  :  8000",self)
        self.total_Buying_Ammount.setFont(font_class())
        self.total_Buying_Ammount.move(850,505)
        self.i_name1 = QLabel('Item Name', self)
        self.i_name1.setFont(font_class())
        self.i_name1.move(25,550) 
        self.i_name1_text=QComboBox(self)
        self.i_name1_text.setFocusPolicy(Qt.StrongFocus)
        self.i_name1_text.setEditable(True)
        self.i_name1_text.move(180,550)
        self.i_name1_text.setInsertPolicy(QComboBox.NoInsert) 
        self.pFilterModel = QSortFilterProxyModel(self.i_name1_text)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.i_name1_text.model())
        self.completer = QCompleter(self.pFilterModel, self.i_name1_text)
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.i_name1_text.setCompleter(self.completer)
        self.i_name1_text.lineEdit().textEdited.connect(self.pFilterModel.setFilterFixedString)
        string_list = ['Agrawal Mahavir', 'Agrawal Mahi', 'Agrawal nirmal', 'good bye']#data base load
        self.i_name1_text.addItems(string_list)
        self.i_name1_text.resize(200,30)
        self.i_weight1 = QLabel('Item Weight', self)
        self.i_weight1.setFont(font_class())
        self.i_weight1.move(420,550) 
        self.i_weight1_text=QComboBox(self)
        self.i_weight1_text.setFocusPolicy(Qt.StrongFocus)
        self.i_weight1_text.setEditable(True)
        self.i_weight1_text.move(555,550)
        self.i_weight1_text.setInsertPolicy(QComboBox.NoInsert) 
        self.pFilterModel = QSortFilterProxyModel(self.i_weight1_text)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.i_weight1_text.model())
        self.completer = QCompleter(self.pFilterModel, self.i_name_text)
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.i_weight1_text.setCompleter(self.completer)
        self.i_weight1_text.lineEdit().textEdited.connect(self.pFilterModel.setFilterFixedString)
        string_list = ['Agrawal Mahavir', 'Agrawal Mahi', 'Agrawal nirmal', 'good bye']#data base load
        self.i_weight1_text.addItems(string_list)
        self.i_weight1_text.resize(200,30)
        self.i_price1 = QLabel('Price.', self)
        self.i_price1.setFont(font_class())
        self.i_price1.move(795,550) 
        self.i_price1_text=QLineEdit(self)
        self.i_price1_text.move(900,550)
        self.i_price1_text.resize(200,30)
        self.add1=QPushButton("ADD",self)
        self.add1.move(1200,550)
        self.add1.resize(100,30)
        self.add1.setStyleSheet("border :4px solid ")
        self.tableWidget1 = QTableWidget(self)
        self.tableWidget1.setRowCount(10)
        self.tableWidget1.setColumnCount(4)
        self.tableWidget1.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget1.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget1.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget1.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget1.move(25,620)
        self.tableWidget1.resize(1000,200)
        self.pending_Ammount1=QLabel("Pending Ammount : 8000",self)
        self.pending_Ammount1.setFont(font_class())
        self.pending_Ammount1.move(850,830)
        self.total_Buying_Ammount1=QLabel("Buying Ammount  :  8000",self)
        self.total_Buying_Ammount1.setFont(font_class())
        self.total_Buying_Ammount1.move(850,860)
# add stock
class AddStock(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel('                                                    Raghunandan Jewellers', self)
        self.label.move(0,0)
        self.label.resize(2000,100)
        self.label.setStyleSheet("border: 1px solid black; color:gold; background-color:black")
        self.label.setFont(QFont('Arial', 30))


#stock detail
class StockDetail(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel('                                                    Raghunandan Jewellers', self)
        self.label.move(0,0)
        self.label.resize(2000,100)
        self.label.setStyleSheet("border: 1px solid black; color:gold; background-color:black")
        self.label.setFont(QFont('Arial', 30))



# customer detail
class CustomerDetail(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel('                                                    Raghunandan Jewellers', self)
        self.label.move(0,0)
        self.label.resize(2000,100)
        self.label.setStyleSheet("border: 1px solid black; color:gold; background-color:black")
        self.label.setFont(QFont('Arial', 30))

#main class
class Soni(QMainWindow):
    def __init__(self):
        super().__init__()
        x=0
        y=0
        width=2000
        height=1000
        self.setGeometry(x,y,width,height)#position_X,position_Y,Width,Height
        self.tabs = QTabWidget(self)
        self.billing = Billing()
        self.add_stock = AddStock()
        self.stock_detail = StockDetail()
        self.customer_detail = CustomerDetail()
        self.tabs.resize(2000,1000)
        
        # Add tabs
        self.tabs.addTab(self.billing,"Billing")
        self.tabs.addTab(self.add_stock,"Add Stock")
        self.tabs.addTab(self.stock_detail,"Stock Detail")
        self.tabs.addTab(self.customer_detail,"Customer Detail")
        self.setWindowTitle("Jwallery")
        self.show()
app = QApplication(sys.argv)
ex=Soni()
sys.exit(app.exec_())