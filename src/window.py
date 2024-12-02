from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from knapsack import *

class MainWindow(QWidget):

    def __init__(self, data : list[Object]) -> None:
        super().__init__()
        self.setWindowTitle("Carga aerea")
        self.setGeometry(0, 0, 480, 480)
        self.objects : list[Object] = data
        self.sack : Knapsack = Knapsack()

        self.box : QGridLayout = QGridLayout(self)
        self.table : QTableWidget = QTableWidget(self)
        self.set_table(data)

        self.choose : QPushButton = QPushButton("Escolher melhores itens", self)
        self.choose.clicked.connect(self._on_choose_clicked)
        
        self.max_weight_label : QLabel = QLabel(self)
        self.max_weight_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.max_weight_label.setText("Aperte 'Escolher melhores itens'")

        self.box.addWidget(self.choose)
        self.box.addWidget(self.max_weight_label)
        self.box.addWidget(self.table)
        self.show()
        pass
    
    def set_table(self, data : list[Object]) -> None:
        self.box.removeWidget(self.table)
        self.table = Table(data, len(data), 4)
        self.box.addWidget(self.table)
        pass
    
    def _on_choose_clicked(self) -> None:
        space = 3
        size = len(self.objects)
        maximum_value, choosen_objects = self.sack.sack(size, self.objects, space)
        self.max_weight_label.setText(f"Valor máximo que pode ser obtido na mochila é : {maximum_value}")
        self.set_table(choosen_objects)

        a, b = self.sack.calculate_weight(choosen_objects, space)
        print(a)
        print()
        for i in b:
            print(i)
        pass

class Table(QTableWidget):
    
    def __init__(self, data : list[Object], *args) -> None:
        QTableWidget.__init__(self, *args)

        self.objects : list[Object] = data
        self.set_data()

        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        pass
    
    def set_data(self) -> None:
        self.clearContents()
        self.setHorizontalHeaderLabels(["Nome", "Valor", "Peso", "Prioridade"])
        for row in range(len(self.objects)):
            self.setItem(row, 0, QTableWidgetItem(str(self.objects[row].name)))
            self.setItem(row, 1, QTableWidgetItem(str(self.objects[row].value)))
            self.setItem(row, 2, QTableWidgetItem(str(self.objects[row].weight)))
            self.setItem(row, 3, QTableWidgetItem(str(self.objects[row].priority)))
        pass
    