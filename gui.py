# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test-2mfntym.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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
from util import *

# coordinate are used for many times
coordinate_names = []
coordinate_file_name = ''
theory_file_name = ''
class Ui_Qtest(object):
    def setupUi(self, Qtest):
        if not Qtest.objectName():
            Qtest.setObjectName(u"Qtest")
        Qtest.resize(802, 524)
        self.display_pattern = QTableWidget(Qtest)
        self.display_pattern.setObjectName(u"display_pattern")
        self.display_pattern.setGeometry(QRect(20, 20, 541, 192))
        self.display_pattern.verticalHeader().setCascadingSectionResizes(False)
        self.display_pattern.verticalHeader().setDefaultSectionSize(30)
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
        self.coo_box_2.setGeometry(QRect(260, 220, 301, 281))
        self.coo_box_2.setFont(font)
        self.load_th_excel = QPushButton(self.coo_box_2)
        self.load_th_excel.setObjectName(u"load_th_excel")
        self.load_th_excel.setGeometry(QRect(20, 70, 91, 32))
        self.set_column_name = QPushButton(self.coo_box_2)
        self.set_column_name.setObjectName(u"set_column_name")
        self.set_column_name.setGeometry(QRect(20, 160, 101, 32))
        self.save_th = QPushButton(self.coo_box_2)
        self.save_th.setObjectName(u"save_th")
        self.save_th.setGeometry(QRect(20, 210, 101, 32))
        self.add_col_th = QPushButton(self.coo_box_2)
        self.add_col_th.setObjectName(u"add_col_th")
        self.add_col_th.setGeometry(QRect(140, 130, 71, 32))
        self.del_col_th = QPushButton(self.coo_box_2)
        self.del_col_th.setObjectName(u"del_col_th")
        self.del_col_th.setGeometry(QRect(220, 130, 71, 32))
        self.spreadsheet_name = QPlainTextEdit(self.coo_box_2)
        self.spreadsheet_name.setObjectName(u"spreadsheet_name")
        self.spreadsheet_name.setGeometry(QRect(140, 90, 151, 31))
        self.label_2 = QLabel(self.coo_box_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 70, 131, 16))
        self.load_th_csv = QPushButton(self.coo_box_2)
        self.load_th_csv.setObjectName(u"load_th_csv")
        self.load_th_csv.setGeometry(QRect(20, 100, 91, 32))
        self.read_theory = QPushButton(self.coo_box_2)
        self.read_theory.setObjectName(u"read_theory")
        self.read_theory.setGeometry(QRect(20, 130, 101, 32))
        self.clear_th = QPushButton(self.coo_box_2)
        self.clear_th.setObjectName(u"clear_th")
        self.clear_th.setGeometry(QRect(140, 160, 71, 32))
        self.label_3 = QLabel(self.coo_box_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(170, 200, 91, 16))
        self.theory_name = QPlainTextEdit(self.coo_box_2)
        self.theory_name.setObjectName(u"theory_name")
        self.theory_name.setGeometry(QRect(150, 220, 141, 31))
        self.set_vertex = QPushButton(self.coo_box_2)
        self.set_vertex.setObjectName(u"set_vertex")
        self.set_vertex.setGeometry(QRect(20, 30, 241, 32))
        self.check_value = QPushButton(self.coo_box_2)
        self.check_value.setObjectName(u"check_value")
        self.check_value.setGeometry(QRect(220, 160, 71, 32))

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
        self.set_column_name.setText(QCoreApplication.translate("Qtest", u"Refresh", None))
        self.save_th.setText(QCoreApplication.translate("Qtest", u"Save Theory", None))
        self.add_col_th.setText(QCoreApplication.translate("Qtest", u"Add", None))
        self.del_col_th.setText(QCoreApplication.translate("Qtest", u"Delete", None))
        self.label_2.setText(QCoreApplication.translate("Qtest", u"Spreadsheet Name", None))
        self.load_th_csv.setText(QCoreApplication.translate("Qtest", u"CSV", None))
        self.read_theory.setText(QCoreApplication.translate("Qtest", u"Load Theory", None))
        self.clear_th.setText(QCoreApplication.translate("Qtest", u"Clear", None))
        self.label_3.setText(QCoreApplication.translate("Qtest", u"Theory Name", None))
        self.set_vertex.setText(QCoreApplication.translate("Qtest", u"Create Vertex", None))
        self.check_value.setText(QCoreApplication.translate("Qtest", u"Check", None))
    # retranslateUi


    # associate functions with buttons
    def button_connect_function(self):
        self.load_coo.clicked.connect(self.open_coo_file)
        self.display_coo.clicked.connect(self.show_coo)
        self.change_coo.clicked.connect(self.refresh_coo_window)
        self.add_coo.clicked.connect(self.add_coo_row)
        self.del_coo.clicked.connect(self.del_coo_row)
        self.clear_coo.clicked.connect(self.clear_coo_row)
        self.save_coo.clicked.connect(self.save_coo_table)

        self.load_th_csv.clicked.connect(self.open_theory_csv)
        self.load_th_excel.clicked.connect(self.open_theory_excel)
        self.read_theory.clicked.connect(self.show_theory)
        self.add_col_th.clicked.connect(self.add_theory_col)
        self.del_col_th.clicked.connect(self.del_theory_col)
        self.clear_th.clicked.connect(self.clear_theory)
        self.save_th.clicked.connect(self.save_theory)
        self.set_column_name.clicked.connect(self.refresh_th)
        self.check_value.clicked.connect(self.th_value_check)
        self.set_vertex.clicked.connect(self.create_vertex)

    # functions for coordinate part

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
                pop_window_text("Warning", "[Wrong Input] Number of columns exceeds 1, Please check input file")
            
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
        global coordinate_names
        coordinate_names = read_from_window(self.display_pattern,single=True)
        print('update name', coordinate_names)

    def add_coo_row(self):
        if (self.display_pattern.rowCount == 0):
            self.display_pattern.setRowCount(1)
            self.display_pattern.setColumnCount(1)
        else:
            self.display_pattern.setRowCount(self.display_pattern.rowCount+1)
        self.refresh_coo_window()
    
    def del_coo_row(self):
        sel_items = self.display_pattern.selectedItems()
        for item in sel_items:
            self.display_pattern.removeRow(self.display_pattern.indexFromItem(item).row())
        self.refresh_coo_window()

    def clear_coo_row(self):
        self.display_pattern.setRowCount(0)
        self.display_pattern.setColumnCount(0)
        self.display_pattern.clearContents()

    def save_coo_table(self):
        file_name = QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV files(*.csv);;Excel files(*.xlsx , *.xls)')[0]
        # global coordinate_names
        # coordinate_names = []

        file_extension = pathlib.Path(file_name).suffix
        if(file_extension == '.csv'):
            write_to_csv(self.display_pattern, file_name)
        elif(file_extension == '.xls' or file_extension == '.xlsx'):
            write_to_excel(self.display_pattern, file_name, sheetname = 'coordinate')
        
    def open_theory_csv(self):
        file = QFileDialog.getOpenFileName(self,'Select file','','CSV files(*.csv)')
        global theory_file_name
        theory_file_name = file[0]

    def open_theory_excel(self):
        file = QFileDialog.getOpenFileName(self,'Select file','','Excel files(*.xlsx , *.xls)')
        global theory_file_name
        theory_file_name = file[0]
    
    def show_theory(self):
        file_extension = pathlib.Path(theory_file_name).suffix
        file = theory_file_name
        if(file_extension == '.csv'):
            read_from_csv(self.display_pattern, file, coordinate_names)
        elif(file_extension == '.xls' or file_extension == '.xlsx'):
            sheet = self.spreadsheet_name.toPlainText()
            if (len(sheet) == 0):
                pop_window_text('Warning', 'No spreasheet specified')
            read_from_excel(self.display_pattern, file, sheet, coordinate_names)

    def add_theory_col(self):
        if (self.display_pattern.columnCount == 0):
            self.display_pattern.setColumnCount(1)
        else:
            self.display_pattern.setColumnCount(self.display_pattern.columnCount()+1)

    def del_theory_col(self):
        sel_items = self.display_pattern.selectedItems()
        for item in sel_items:
            self.display_pattern.removeColumn(self.display_pattern.indexFromItem(item).column())

    def clear_theory(self):
        self.display_pattern.setRowCount(0)
        self.display_pattern.setColumnCount(0)
        self.display_pattern.clearContents()
        
    def save_theory(self):
        file_name = QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV files(*.csv);;Excel files(*.xlsx , *.xls)')[0]
        file_extension = pathlib.Path(file_name).suffix
        theory_name = self.theory_name.toPlainText()
        if(file_extension == '.csv'):
            write_to_csv(self.display_pattern, file_name)
        elif(file_extension == '.xls' or file_extension == '.xlsx'):
            write_to_excel(self.display_pattern, file_name, theory_name)
    
    def refresh_th(self):
        self.display_pattern.resizeColumnsToContents()
    
    def th_value_check(self):
        data = read_from_window(self.display_pattern, False)
        for i in range(1, len(data)):
            row_data = data[i]
            for j in range(1, len(row_data)):
                value = float(data[i][j])
                if value >1 or value < 0:
                    pop_window_text('Wrong value', 'Value exceeds the range [0,1]')
                    return
    
    def create_vertex(self):
        
        return 0