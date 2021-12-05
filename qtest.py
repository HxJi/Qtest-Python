from typing import NewType
from PyQt5 import QtCore, QtGui
from PySide2 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
import sys
from main_window import Ui_main_window


class MainWindow(QtWidgets.QMainWindow, Ui_main_window):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    qtest = MainWindow()
    qtest.show()
    app.exec_()

if __name__ == '__main__':
    main()
