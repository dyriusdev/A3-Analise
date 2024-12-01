"""
Codigo principal do projeto onde o programa será executado
"""
from PyQt5.QtWidgets import QApplication
from window import MainWindow

data = {
    "Nome" : ["Teste 1", "Teste 2"],
    "Valor" : ["50", "25"],
    "Peso" : ["10", "5"],
    "Prioridade" : ["1", "0"],
    "Capacidade" : ["25", "40"],
}

#Execução
app = QApplication([])
window = MainWindow(data)
app.exec_()