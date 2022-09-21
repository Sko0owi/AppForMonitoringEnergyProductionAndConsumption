import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from src.UIHandler import Ui_Class
from src.csvFilesHandler import csvInit
from os.path import exists as file_exists
from os import system

def window():
    app = QApplication(sys.argv)
    
    win = QtWidgets.QMainWindow()
    win.ui = Ui_Class().Ui_MainWindow()
    win.ui.setupUi(win)
    win.show()

    sys.exit(app.exec_())

def startApp():
    system('mode con: cols=150 lines=30')
    
    csvInit(file_exists("csvFiles/readingsFromRegister.csv"))

    window()


startApp()