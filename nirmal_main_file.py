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
    
    def received_cellClick(self):
        self.collected_item_amount_value.setHidden(False)
        #print(row, ' ', col)
        row=int(self.received_item_table.currentRow())
        self.received_total_price -= int(self.received_item_table.item(row,2).text())
        self.received_item_table.removeRow(row)
        #print(self.received_total_price)
        self.collected_item_amount_value.setText(str(self.received_total_price))
        
        print(self.received_total_price)
        #print(self.received_item_table.currentRow())
    
    def received_add_item_into_table(self, item_name, item_weight, item_price):
        self.collected_item_amount_value.setHidden(False)
        #print(item_name,' ',item_weight, ' ', item_price)
        row = self.received_item_table.rowCount()
        l=[]
        #l.append("Item Number : "+str(row + 1))
        l.append(item_name)
        l.append(item_weight)
        l.append(item_price)
        l.append(QPushButton("Delete",self))
        #l[3].clicked.connect(lambda: self.delete_item(len(self.item_detail)))
        #l[3].clicked.connect(lambda *args, row=row, column=column: cellClick(row, column))
        #l[3].clicked.connect(lambda *args, row=row, column=col: self.cellClick(row, column))
        
        
        self.received_item_table.setRowCount(row+1)
        col = 0
        for i in l:
            self.received_item_table.setVerticalHeaderLabels("Item Number : " + str(i + 1) for i in range(row+1))
            if col == 3:
                #cell = QTableWidgetItem(str(i))
                #self.received_item_table.setItem(row, col, cell)
                self.received_item_table.setCellWidget(row, 3, l[3])
                l[3].clicked.connect(self.received_cellClick)
            else:
                cell = QTableWidgetItem(str(i))
                self.received_item_table.setItem(row, col, cell)
            col += 1
            
        #print(int(self.received_item_table.item(0,2).text()))
        self.received_total_price = sum([int(self.received_item_table.item(i,2).text()) for i in range(row + 1)])
        print(self.received_total_price)
        self.collected_item_amount_value.setText(str(self.received_total_price))
        #print(self.received_item_table.currentRow(),'     njkbkm')
        #print(self.received_item_table.currentColumn())
     
    def cellClick(self):
        #print(row, ' ', col)
        row=int(self.item_table.currentRow())
        self.total_price -= int(self.item_table.item(row,2).text())
        self.item_table.removeRow(row)
        #print(self.total_price)
        self.total_Buying_Ammount_value.setText(str(self.total_price))
        #print(self.item_table.currentRow())
    
    def add_item_into_table(self, item_name, item_weight, item_price):
        #print(item_name,' ',item_weight, ' ', item_price)
        row = self.item_table.rowCount()
        l=[]
        #l.append("Item Number : "+str(row + 1))
        l.append(item_name)
        l.append(item_weight)
        l.append(item_price)
        l.append(QPushButton("Delete",self))
        #l[3].clicked.connect(lambda: self.delete_item(len(self.item_detail)))
        #l[3].clicked.connect(lambda *args, row=row, column=column: cellClick(row, column))
        #l[3].clicked.connect(lambda *args, row=row, column=col: self.cellClick(row, column))
        
        
        self.item_table.setRowCount(row+1)
        col = 0
        for i in l:
            self.item_table.setVerticalHeaderLabels("Item Number : " + str(i + 1) for i in range(row+1))
            if col == 3:
                #cell = QTableWidgetItem(str(i))
                #self.item_table.setItem(row, col, cell)
                self.item_table.setCellWidget(row, 3, l[3])
                l[3].clicked.connect(self.cellClick)
            else:
                cell = QTableWidgetItem(str(i))
                self.item_table.setItem(row, col, cell)
            col += 1
            
        #print(int(self.item_table.item(0,2).text()))
        self.total_price = sum([int(self.item_table.item(i,2).text()) for i in range(row + 1)])
        self.total_Buying_Ammount_value.setText(str(self.total_price))
        #print(self.item_table.currentRow(),'     njkbkm')
        #print(self.item_table.currentColumn())
        
        
            
        
    def __init__(self):
        super().__init__()
        self.item_detail=[]
        #label for shop name
        
        self.label = QLabel('Customer Detail', self)
        self.label.move(20,0)
        self.label.resize(2000,80)
        #self.label.setStyleSheet("border: 1px solid black; color:gold; background-color:black")
        self.label.setFont(QFont('Arial', 30))
        
        #starting labels for cutomer detail.....
        
        #c_name label
        
        self.c_name = QLabel('Customer Name', self)
        self.c_name.setFont(font_class())
        self.c_name.move(25,110)
        
        #c_name text in which we use combo box
         
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
        string_list = ['Agrawal Mahavir', 'Agrawal Mahi', 'Agrawal nirmal', 'good bye']  #this data will be load from database
        self.c_name_text.addItems(string_list)
        self.c_name_text.resize(200,30)
        self.c_name_text.setFont(font_class())
        self.c_name_text.setCurrentText('')
        
        #label for cusomer mobile number
        
        self.c_mobileno = QLabel('Mobile No.', self)
        self.c_mobileno.setFont(font_class())
        self.c_mobileno.move(420,110) 
        
        #line edit for mobile number
        
        self.c_mobileno_text=QLineEdit(self)
        self.c_mobileno_text.move(554,110)
        self.c_mobileno_text.resize(200,30)
        self.c_mobileno_text.setFont(font_class())
        
        #label for cusomer address
        
        self.c_address = QLabel('Address.', self)
        self.c_address.setFont(font_class())
        self.c_address.move(794,110) 
        
        #edit line for c_address
        
        self.c_address_text=QLineEdit(self)
        self.c_address_text.move(900,110)
        self.c_address_text.resize(200,30)
        self.c_address_text.setFont(font_class())
        
        #lebel for c_billno
        
        self.c_billno = QLabel('Billno', self)
        self.c_billno.setFont(font_class())
        self.c_billno.move(1140,110)
        
        #edit line for c_billno
        
        self.c_billno_text=QLineEdit(self)
        self.c_billno_text.move(1220,110)
        self.c_billno_text.resize(100,30)
        self.c_billno_text.setFont(font_class())
        
        
        #items detail started
        self.item_detail_label = QLabel('Item Detail', self)
        self.item_detail_label.move(20,170)
        self.item_detail_label.resize(2000,80)
        #self.label.setStyleSheet("border: 1px solid black; color:gold; background-color:black")
        self.item_detail_label.setFont(QFont('Arial', 30))
        
    
        #label for an item name
        
        self.i_name = QLabel('Item Name', self)
        self.i_name.setFont(font_class())
        self.i_name.move(25,282) 
        
        #combo box for item name
        
        self.i_name_text=QComboBox(self)
        self.i_name_text.setFocusPolicy(Qt.StrongFocus)
        self.i_name_text.setEditable(True)
        self.i_name_text.move(180,282)
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
        self.i_name_text.setFont(font_class())
        self.i_name_text.setCurrentText('')
        
        #weight label for an item
        
        self.i_weight = QLabel('Item Weight', self)
        self.i_weight.setFont(font_class())
        self.i_weight.move(420,282)
        
        #weight combo box for an item
        
        self.i_weight_text=QComboBox(self)
        self.i_weight_text.setFocusPolicy(Qt.StrongFocus)
        self.i_weight_text.setEditable(True)
        self.i_weight_text.move(555,282)
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
        self.i_weight_text.setFont(font_class())
        self.i_weight_text.setCurrentText('')
        
        #label for an item price
        
        self.i_price = QLabel('Price.', self)
        self.i_price.setFont(font_class())
        self.i_price.move(795,282)
        
        #edit line for an item price
        
        self.i_price_text=QLineEdit(self)
        self.i_price_text.move(900,282)
        self.i_price_text.resize(200,30)
        self.i_price_text.setFont(font_class())
        
        self.add=QPushButton("Add Item",self)
        self.add.move(1200,282)
        self.add.resize(100,30)
        #self.add.setStyleSheet("border :4px solid ")
        self.add.clicked.connect(lambda:self.add_item_into_table(self.i_name_text.currentText(), self.i_weight_text.currentText(), self.i_price_text.text()))
        #table for item
        self.item_table = QTableWidget(self)
        #self.tableWidget.setRowCount(10)
        self.item_table.setColumnCount(4)
        self.item_table.setColumnWidth(0,300)
        self.item_table.setFont(font_class())
        self.item_table.setHorizontalHeaderLabels(["Item Name", "Item Weight", "Item Price",''])
        self.item_table.move(25,340)
        self.item_table.resize(850,195)
        self.item_table.setEnabled(True)
        self.item_table.setShowGrid(False)
        

        #pending amount label        
        self.pending_Ammount=QLabel("Pending Amount : ",self)
        self.pending_Ammount.setFont(font_class())
        self.pending_Ammount.move(950,370)
        
        #pending amount label        
        self.pending_amount = 0
        self.pending_Ammount_value=QLabel(str(self.pending_amount),self)
        self.pending_Ammount_value.setFont(font_class())
        self.pending_Ammount_value.move(1100,370)
        
        
        #buying amount label
        self.total_Buying_Ammount=QLabel("Buying Amount  : ",self)
        self.total_Buying_Ammount.setFont(font_class())
        self.total_Buying_Ammount.move(950,410)
        
        #buying amount label
        #self.buying_amount=0
        self.total_Buying_Ammount_value=QLabel(str(0),self)
        self.total_Buying_Ammount_value.setFont(font_class())
        self.total_Buying_Ammount_value.move(1100,410)
        
        
        #customer received item
   
        #items detail started
        self.received_item_detail_label = QLabel('Received Item Detail', self)
        self.received_item_detail_label.move(20,560)
        self.received_item_detail_label.resize(2000,80)
        #self.label.setStyleSheet("border: 1px solid black; color:gold; background-color:black")
        self.received_item_detail_label.setFont(QFont('Arial', 30))
        
    
        #label for an item name
        
        self.received_i_name = QLabel('Item Name', self)
        self.received_i_name.setFont(font_class())
        self.received_i_name.move(25,672) 
        
        #combo box for item name
        
        self.received_i_name_text=QComboBox(self)
        self.received_i_name_text.setFocusPolicy(Qt.StrongFocus)
        self.received_i_name_text.setEditable(True)
        self.received_i_name_text.move(180,672)
        self.received_i_name_text.setInsertPolicy(QComboBox.NoInsert) 
        self.pFilterModel = QSortFilterProxyModel(self.received_i_name_text)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.received_i_name_text.model())
        self.completer = QCompleter(self.pFilterModel, self.received_i_name_text)
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.received_i_name_text.setCompleter(self.completer)
        self.received_i_name_text.lineEdit().textEdited.connect(self.pFilterModel.setFilterFixedString)
        string_list = ['Agrawal Mahavir', 'Agrawal Mahi', 'Agrawal nirmal', 'good bye']#data base load
        self.received_i_name_text.addItems(string_list)
        self.received_i_name_text.resize(200,30)
        self.received_i_name_text.setFont(font_class())
        self.received_i_name_text.setCurrentText('')
        
        #weight label for an item
        
        self.received_i_weight = QLabel('Item Weight', self)
        self.received_i_weight.setFont(font_class())
        self.received_i_weight.move(420,672)
        
        #weight combo box for an item
        
        self.received_i_weight_text=QComboBox(self)
        self.received_i_weight_text.setFocusPolicy(Qt.StrongFocus)
        self.received_i_weight_text.setEditable(True)
        self.received_i_weight_text.move(555,672)
        self.received_i_weight_text.setInsertPolicy(QComboBox.NoInsert) 
        self.pFilterModel = QSortFilterProxyModel(self.received_i_weight_text)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.received_i_weight_text.model())
        self.completer = QCompleter(self.pFilterModel, self.received_i_name_text)
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.received_i_weight_text.setCompleter(self.completer)
        self.received_i_weight_text.lineEdit().textEdited.connect(self.pFilterModel.setFilterFixedString)
        string_list = ['Agrawal Mahavir', 'Agrawal Mahi', 'Agrawal nirmal', 'good bye']#data base load
        self.received_i_weight_text.addItems(string_list)
        self.received_i_weight_text.resize(200,30)
        self.received_i_weight_text.setFont(font_class())
        self.received_i_weight_text.setCurrentText('')
        
        #label for an item price
        
        self.received_i_price = QLabel('Price.', self)
        self.received_i_price.setFont(font_class())
        self.received_i_price.move(795,672)
        
        #edit line for an item price
        
        self.received_i_price_text=QLineEdit(self)
        self.received_i_price_text.move(900,672)
        self.received_i_price_text.resize(200,30)
        self.received_i_price_text.setFont(font_class())
        
        self.received_add=QPushButton("Add Item",self)
        self.received_add.move(1200,672)
        self.received_add.resize(100,30)
        #self.add.setStyleSheet("border :4px solid ")
        self.received_add.clicked.connect(lambda:self.received_add_item_into_table(self.received_i_name_text.currentText(), self.received_i_weight_text.currentText(), self.received_i_price_text.text()))
        #table for item
        self.received_item_table = QTableWidget(self)
        #self.tableWidget.setRowCount(10)
        self.received_item_table.setColumnCount(4)
        self.received_item_table.setColumnWidth(0,300)
        self.received_item_table.setFont(font_class())
        self.received_item_table.setHorizontalHeaderLabels(["Item Name", "Item Weight", "Item Price",''])
        self.received_item_table.move(25,730)
        self.received_item_table.resize(850,195)
        self.received_item_table.setEnabled(True)
        self.received_item_table.setShowGrid(False)
        

        #Collected Item Amount label        
        
        self.collected_item_amount=QLabel("Collected Item Amount : ",self)
        self.collected_item_amount.setFont(font_class())
        self.collected_item_amount.move(950,760)
        
        #collected item value label
        self.received_total_price = 0
        self.collected_item_amount_value=QLabel('00000000000000000000',self)
        self.collected_item_amount_value.setHidden(True)
        self.collected_item_amount_value.setFont(font_class())
        self.collected_item_amount_value.move(1160,760)
        self.collected_item_amount_value.setHidden(True)
        
        #total amount
        self.total_amount=QLabel("Total Amount  : ",self)
        self.total_amount.setFont(font_class())
        self.total_amount.move(950,810)
        
        #total amount value
        self.overall_total = 0
        self.total_amount_value=QLabel(str(self.overall_total),self)
        self.total_amount_value.setFont(font_class())
        self.total_amount_value.move(1080,810)
        
        
        
        
        
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
        self.label = QLabel('Raghunandan Jewellers', self)
        self.label.move(0,0)
        self.label.resize(2000,100)
        #self.label.setStyleSheet("border: 1px solid black; color:gold; background-color:black")
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