"""
Codigo principal do projeto onde o programa será executado
"""
from PyQt5.QtWidgets import QApplication
from window import MainWindow
from knapsack import Object

objects = [
    Object("Objeto 1", 100, 3, 3),
    Object("Objeto 2", 250, 2, 1),
    Object("Objeto 3", 300, 5, 2),
    Object("Objeto 4", 500, 4, 2),
]

#Execução
app = QApplication([])
window = MainWindow(objects)
app.exec_()