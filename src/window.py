from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class MainWindow(QWidget):

    def __init__(self, data : dict) -> None:
        super().__init__()
        self.setWindowTitle("Carga aerea")
        self.setGeometry(0, 0, 480, 480)
        self.box : QGridLayout = QGridLayout(self)
        
        self.table : QTableWidget = QTableWidget(self)
        self.set_table(data)

        self.order : QPushButton = QPushButton("Ordenar", self)
        self.order.clicked.connect(self._on_order_clicked)
        
        self.box.addWidget(self.table)
        self.box.addWidget(self.order)
        self.show()
        pass
    
    def set_table(self, data : dict) -> None:
        self.box.removeWidget(self.table)
        self.table = Table(data, len(data.values()), 5)
        self.box.addWidget(self.table)
        pass
    
    def _on_order_clicked(self) -> None:
        data : dict = self.table.data
        data["Nome"].append("Teste 3")
        self.set_table(data)
        pass

class Table(QTableWidget):
    
    def __init__(self, data : dict, *args) -> None:
        QTableWidget.__init__(self, *args)

        self.data : dict = data
        self.set_data()

        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        pass
    
    def set_data(self) -> None:
        self.clearContents()
        headers : list = []
        for column, key in enumerate(self.data.keys()):
            headers.append(key)
            for row, item in enumerate(self.data[key]):
                new_item : QTableWidgetItem = QTableWidgetItem(item)
                self.setItem(row, column, new_item)
        self.setHorizontalHeaderLabels(headers)
        pass
    