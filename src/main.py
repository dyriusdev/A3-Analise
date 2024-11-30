"""
Codigo principal do projeto onde o programa será executado
"""
from PyQt5.QtWidgets import QApplication
from window import MainWindow

#Execução
app = QApplication([])
app.setApplicationName("Problema da mochila")
window = MainWindow()
app.exec_()