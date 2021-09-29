# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test-2mfntym.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from os import path
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

# coordinate are used for many times
coordinate_names = []
coordinate_file_name = ''

class Ui_Qtest(object):
    def setupUi(self, Qtest):
        if not Qtest.objectName():
            Qtest.setObjectName(u"Qtest")
        Qtest.resize(565, 524)
        self.display_pattern = QTableWidget(Qtest)
        self.display_pattern.setObjectName(u"display_pattern")
        self.display_pattern.setGeometry(QRect(20, 20, 521, 192))
        self.coo_box = QGroupBox(Qtest)
        self.coo_box.setObjectName(u"coo_box")
        self.coo_box.setGeometry(QRect(20, 220, 221, 201))
        font = QFont()
        font.setPointSize(14)
        self.coo_box.setFont(font)
        self.label_5 = QLabel(self.coo_box)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 30, 131, 21))
        self.gamble_num = QSpinBox(self.coo_box)
        self.gamble_num.setObjectName(u"gamble_num")
        self.gamble_num.setGeometry(QRect(150, 30, 61, 21))
        self.load_coo = QPushButton(self.coo_box)
        self.load_coo.setObjectName(u"load_coo")
        self.load_coo.setGeometry(QRect(10, 60, 201, 32))
        self.add_coo = QPushButton(self.coo_box)
        self.add_coo.setObjectName(u"add_coo")
        self.add_coo.setGeometry(QRect(10, 100, 91, 32))
        self.del_coo = QPushButton(self.coo_box)
        self.del_coo.setObjectName(u"del_coo")
        self.del_coo.setGeometry(QRect(120, 100, 91, 32))
        self.clear_coo = QPushButton(self.coo_box)
        self.clear_coo.setObjectName(u"clear_coo")
        self.clear_coo.setGeometry(QRect(10, 130, 91, 32))
        self.save_coo = QPushButton(self.coo_box)
        self.save_coo.setObjectName(u"save_coo")
        self.save_coo.setGeometry(QRect(120, 130, 91, 32))
        self.display_coo = QPushButton(self.coo_box)
        self.display_coo.setObjectName(u"display_coo")
        self.display_coo.setGeometry(QRect(120, 160, 91, 32))
        self.change_coo = QPushButton(self.coo_box)
        self.change_coo.setObjectName(u"change_coo")
        self.change_coo.setGeometry(QRect(10, 160, 91, 32))
        self.coo_box_2 = QGroupBox(Qtest)
        self.coo_box_2.setObjectName(u"coo_box_2")
        self.coo_box_2.setGeometry(QRect(250, 220, 291, 281))
        self.coo_box_2.setFont(font)
        self.load_th_excel = QPushButton(self.coo_box_2)
        self.load_th_excel.setObjectName(u"load_th_excel")
        self.load_th_excel.setGeometry(QRect(20, 70, 91, 32))
        self.set_column_name = QPushButton(self.coo_box_2)
        self.set_column_name.setObjectName(u"set_column_name")
        self.set_column_name.setGeometry(QRect(20, 210, 101, 32))
        self.save_th = QPushButton(self.coo_box_2)
        self.save_th.setObjectName(u"save_th")
        self.save_th.setGeometry(QRect(20, 240, 101, 32))
        self.add_col_th = QPushButton(self.coo_box_2)
        self.add_col_th.setObjectName(u"add_col_th")
        self.add_col_th.setGeometry(QRect(20, 170, 71, 32))
        self.del_col_th = QPushButton(self.coo_box_2)
        self.del_col_th.setObjectName(u"del_col_th")
        self.del_col_th.setGeometry(QRect(110, 170, 71, 32))
        self.spreadsheet_name = QPlainTextEdit(self.coo_box_2)
        self.spreadsheet_name.setObjectName(u"spreadsheet_name")
        self.spreadsheet_name.setGeometry(QRect(150, 90, 121, 31))
        self.label_2 = QLabel(self.coo_box_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 70, 131, 16))
        self.load_th_csv = QPushButton(self.coo_box_2)
        self.load_th_csv.setObjectName(u"load_th_csv")
        self.load_th_csv.setGeometry(QRect(20, 100, 91, 32))
        self.read_theory = QPushButton(self.coo_box_2)
        self.read_theory.setObjectName(u"read_theory")
        self.read_theory.setGeometry(QRect(20, 130, 251, 32))
        self.clear_th = QPushButton(self.coo_box_2)
        self.clear_th.setObjectName(u"clear_th")
        self.clear_th.setGeometry(QRect(200, 170, 70, 32))
        self.label_3 = QLabel(self.coo_box_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 210, 91, 16))
        self.theory_name = QPlainTextEdit(self.coo_box_2)
        self.theory_name.setObjectName(u"theory_name")
        self.theory_name.setGeometry(QRect(150, 230, 121, 31))
        self.set_vertex = QPushButton(self.coo_box_2)
        self.set_vertex.setObjectName(u"set_vertex")
        self.set_vertex.setGeometry(QRect(20, 30, 251, 32))

        self.retranslateUi(Qtest)
        self.button_connect_function()
        QMetaObject.connectSlotsByName(Qtest)
    # setupUi

    def retranslateUi(self, Qtest):
        Qtest.setWindowTitle(QCoreApplication.translate("Qtest", u"Qtest-Py", None))
        self.coo_box.setTitle(QCoreApplication.translate("Qtest", u"Coordinate", None))
        self.label_5.setText(QCoreApplication.translate("Qtest", u"Number of Gambles", None))
        self.load_coo.setText(QCoreApplication.translate("Qtest", u"Load from File", None))
        self.add_coo.setText(QCoreApplication.translate("Qtest", u"Add", None))
        self.del_coo.setText(QCoreApplication.translate("Qtest", u"Delete", None))
        self.clear_coo.setText(QCoreApplication.translate("Qtest", u"Clear", None))
        self.save_coo.setText(QCoreApplication.translate("Qtest", u"Save", None))
        self.display_coo.setText(QCoreApplication.translate("Qtest", u"Display", None))
        self.change_coo.setText(QCoreApplication.translate("Qtest", u"Refresh", None))
        self.coo_box_2.setTitle(QCoreApplication.translate("Qtest", u"Patter/Vertex Entry", None))
        self.load_th_excel.setText(QCoreApplication.translate("Qtest", u"Excel", None))
        self.set_column_name.setText(QCoreApplication.translate("Qtest", u"Set Col Name", None))
        self.save_th.setText(QCoreApplication.translate("Qtest", u"Save Theory", None))
        self.add_col_th.setText(QCoreApplication.translate("Qtest", u"Add", None))
        self.del_col_th.setText(QCoreApplication.translate("Qtest", u"Delete", None))
        self.label_2.setText(QCoreApplication.translate("Qtest", u"Spreadsheet Name", None))
        self.load_th_csv.setText(QCoreApplication.translate("Qtest", u"CSV", None))
        self.read_theory.setText(QCoreApplication.translate("Qtest", u"Load Theory", None))
        self.clear_th.setText(QCoreApplication.translate("Qtest", u"Clear", None))
        self.label_3.setText(QCoreApplication.translate("Qtest", u"Theory Name", None))
        self.set_vertex.setText(QCoreApplication.translate("Qtest", u"Set Vertex", None))
    # retranslateUi

    # associate functions with buttons
    def button_connect_function(self):
        self.load_coo.clicked.connect(self.open_coo_file)
        self.display_coo.clicked.connect(self.show_coo)
        self.change_coo.clicked.connect(self.refresh_coo_window)
        # self.add_coo.clicked.connect(self.add_coo_row)
        # self.del_coo.clicked.connect(self.del_coo_row)
        # self.clear_coo.clicked.connect(self.clear_coo_row)
        # self.save_coo.clicked.connect(self.save_coo_table)


        # self.load_th_csv.clicked.connect(self.open_theory_csv)
        # self.load_th_excel.clicked.connect(self.open_theory_excel)
        # self.set_column_name
        # self.add_col_th
        # self.del_col_th
        # self.read_theory
        # self.clear_th
        # self.set_vertex

    # functions for coordinate part
    def pop_window_text(self, title, text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry|QMessageBox.Ignore)
        msg.setDefaultButton(QMessageBox.Cancel)
        x = msg.exec_()

    def open_coo_file(self):
        openfile_name = QFileDialog.getOpenFileName(self,'Select file','','CSV files(*.csv);;Excel files(*.xlsx , *.xls)')
        global coordinate_file_name
        coordinate_file_name = openfile_name[0]
        print(coordinate_file_name)
    
    def show_coo(self):
        print('show coo')
        gamble_number = self.gamble_num.value()
        global coordinate_names
        coordinate_names = []
        # generate by gambles
        if (gamble_number > 0):
            alphabet_list = list(string.ascii_uppercase)
            elem_list = alphabet_list[:gamble_number]
            for i in range(len(elem_list)):
                for j in range(i+1,len(elem_list)):
                    coordinate_names.append(elem_list[i]+elem_list[j])
            num_rows = len(coordinate_names)
            num_columns = 1
        # load from files
        else:
            file_name = coordinate_file_name
            assert len(file_name) != 0, "Not a valid file path"
            file_extension = pathlib.Path(file_name).suffix
            print(file_name, file_extension)
            if(file_extension == '.csv'):
                input_table = pd.read_csv(file_name, header=None)
            elif(file_extension == '.xls' or file_extension == '.xlsx'):
                input_table = pd.read_excel(file_name)
            else:
                return -1

            num_rows, num_columns = input_table.shape[0], input_table.shape[1]
            if (num_columns > 1):
                self.pop_window_text("Warning", "[Wrong Input] Number of columns exceeds 1, Please check input file")
            
            table_header = input_table.columns.values.tolist()
            
            for i in range(num_rows):
                row_value = input_table.iloc[i][0]
                coordinate_names.append(row_value)

        print(coordinate_names)
        self.display_pattern.setColumnCount(num_columns)
        self.display_pattern.setRowCount(num_rows)
        self.display_pattern.resizeColumnsToContents()
        

        for i in range(num_rows):
            newItem = QTableWidgetItem(coordinate_names[i])
            newItem.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            self.display_pattern.setItem(0, i, newItem)
        # self.display_pattern.setVerticalHeaderLabels(coordinate_names)
        self.display_pattern.setHorizontalHeaderLabels(['Coordinate'])
        self.display_pattern.resizeColumnsToContents()
        
    

    def refresh_coo_window(self):
        self.display_pattern.resizeColumnsToContents()




            