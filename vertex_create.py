from os import path
import PySide2
import numpy as np
from numpy import core
import pandas as pd
import csv
import os
import string
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import pathlib
import xlsxwriter
from utility import *

class vertex_window(QDialog):
    def __init__(self, coordinate_names):
        super().__init__()
        self.setWindowTitle("Create Vertex")
        print(coordinate_names)
        self.set_button = QPushButton('OK')
        self.set_button.clicked.connect(self.read_box)
        self.cancel_button = QPushButton('Cancel')
        self.cancel_button.clicked.connect(self.clear_box)

        layout = QGridLayout()
        self.checkboxs = []
        self.result=[]
        row = 0
        for coordinate in coordinate_names:
            self.checkboxs.append(QCheckBox('1'))
            self.checkboxs.append(QCheckBox('0'))

            layout.addWidget(QLabel(coordinate), row, 0)
            layout.addWidget(self.checkboxs[2*row], row, 1)
            layout.addWidget(self.checkboxs[2*row+1], row, 2)
            row = row + 1
        layout.addWidget(self.set_button, row, 0)
        layout.addWidget(self.cancel_button, row, 1)
        self.setLayout(layout)

    def read_box(self):
        for i in range(0, len(self.checkboxs),2):
            value = int(self.checkboxs[i].isChecked())
            self.result.append(value)
        self.close()

    def clear_box(self):
        for checkbox in self.checkboxs:
            checkbox.setChecked(False)