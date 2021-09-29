from typing import NewType
from PyQt5 import QtCore, QtGui
from PySide2 import QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from gui import Ui_Qtest

class ExampleApp(QtWidgets.QMainWindow, Ui_Qtest):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()