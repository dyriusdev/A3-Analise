from PyQt5.QtWidgets import *

class MainWindow(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Problema da mochila")
        self.setGeometry(0, 0, 480, 480)
        
        self.create_table()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

        self.show()
        pass

    def create_table(self) -> None:
        self.table = QTableWidget()
        self.table.setRowCount(4)
        self.table.setColumnCount(5)

        self.table.setItem(0, 0, QTableWidgetItem("Nome"))
        self.table.setItem(0, 1, QTableWidgetItem("Valor"))
        self.table.setItem(0, 2, QTableWidgetItem("Peso"))
        self.table.setItem(0, 3, QTableWidgetItem("Prioridade"))
        self.table.setItem(0, 4, QTableWidgetItem("Capacidade"))

        self.table.setItem(1, 0, QTableWidgetItem("1-1"))
        self.table.setItem(1, 1, QTableWidgetItem("10$"))
        self.table.setItem(1, 2, QTableWidgetItem("32kg"))
        self.table.setItem(1, 3, QTableWidgetItem("1"))
        self.table.setItem(1, 4, QTableWidgetItem("50"))

        self.table.setItem(2, 0, QTableWidgetItem("1-2"))
        self.table.setItem(2, 1, QTableWidgetItem("2-2"))
        
        self.table.setItem(3, 0, QTableWidgetItem("1-3"))
        self.table.setItem(3, 1, QTableWidgetItem("2-3"))

        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        pass