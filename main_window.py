# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowmiUDWB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from numpy import left_shift

from utility import *
from scipy.special import comb
from vertex_create import *
class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(800, 600)
        self.centralwidget = QWidget(main_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 350, 161, 16))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.coo_spin_box = QSpinBox(self.centralwidget)
        self.coo_spin_box.setObjectName(u"coo_spin_box")
        self.coo_spin_box.setGeometry(QRect(190, 350, 91, 22))
        self.add_coo = QPushButton(self.centralwidget)
        self.add_coo.setObjectName(u"add_coo")
        self.add_coo.setGeometry(QRect(20, 380, 71, 31))
        self.del_coo = QPushButton(self.centralwidget)
        self.del_coo.setObjectName(u"del_coo")
        self.del_coo.setGeometry(QRect(110, 380, 71, 32))
        self.clear_coo = QPushButton(self.centralwidget)
        self.clear_coo.setObjectName(u"clear_coo")
        self.clear_coo.setGeometry(QRect(200, 380, 71, 31))
        self.save_coo = QPushButton(self.centralwidget)
        self.save_coo.setObjectName(u"save_coo")
        self.save_coo.setGeometry(QRect(20, 410, 71, 32))
        self.load_coo = QPushButton(self.centralwidget)
        self.load_coo.setObjectName(u"load_coo")
        self.load_coo.setGeometry(QRect(110, 410, 71, 32))
        self.auto_coo = QPushButton(self.centralwidget)
        self.auto_coo.setObjectName(u"auto_coo")
        self.auto_coo.setGeometry(QRect(200, 410, 71, 32))
        self.set_coo_num = QCheckBox(self.centralwidget)
        self.set_coo_num.setObjectName(u"set_coo_num")
        self.set_coo_num.setGeometry(QRect(290, 350, 61, 20))
        self.monitor = QTableWidget(self.centralwidget)
        self.monitor.setObjectName(u"monitor")
        self.monitor.setGeometry(QRect(20, 10, 331, 331))
        self.lock_coo = QCheckBox(self.centralwidget)
        self.lock_coo.setObjectName(u"lock_coo")
        self.lock_coo.setGeometry(QRect(290, 370, 51, 20))
        self.th_vetex = QCheckBox(self.centralwidget)
        self.th_vetex.setObjectName(u"th_vetex")
        self.th_vetex.setGeometry(QRect(380, 20, 86, 20))
        self.th_ins = QCheckBox(self.centralwidget)
        self.th_ins.setObjectName(u"th_ins")
        self.th_ins.setGeometry(QRect(460, 20, 86, 20))
        self.th_alt = QCheckBox(self.centralwidget)
        self.th_alt.setObjectName(u"th_alt")
        self.th_alt.setGeometry(QRect(540, 20, 101, 21))
        self.save_th = QPushButton(self.centralwidget)
        self.save_th.setObjectName(u"save_th")
        self.save_th.setGeometry(QRect(380, 80, 71, 32))
        self.del_vertex = QPushButton(self.centralwidget)
        self.del_vertex.setObjectName(u"del_vertex")
        self.del_vertex.setGeometry(QRect(470, 50, 71, 32))
        self.load_th = QPushButton(self.centralwidget)
        self.load_th.setObjectName(u"load_th")
        self.load_th.setGeometry(QRect(470, 80, 71, 32))
        self.add_vertex = QPushButton(self.centralwidget)
        self.add_vertex.setObjectName(u"add_vertex")
        self.add_vertex.setGeometry(QRect(380, 50, 71, 31))
        self.clear_vertex = QPushButton(self.centralwidget)
        self.clear_vertex.setObjectName(u"clear_vertex")
        self.clear_vertex.setGeometry(QRect(560, 50, 71, 31))
        self.th_list = QListWidget(self.centralwidget)
        self.th_list.setObjectName(u"th_list")
        self.th_list.setGeometry(QRect(380, 120, 331, 192))
        self.vertex_chcek = QPushButton(self.centralwidget)
        self.vertex_chcek.setObjectName(u"vertex_chcek")
        self.vertex_chcek.setGeometry(QRect(640, 50, 71, 31))
        self.lock_th = QCheckBox(self.centralwidget)
        self.lock_th.setObjectName(u"lock_th")
        self.lock_th.setGeometry(QRect(650, 90, 51, 20))
        self.calculate_ins_order = QPushButton(self.centralwidget)
        self.calculate_ins_order.setObjectName(u"calculate_ins_order")
        self.calculate_ins_order.setGeometry(QRect(380, 320, 331, 32))
        self.vertex_auto = QPushButton(self.centralwidget)
        self.vertex_auto.setObjectName(u"vertex_auto")
        self.vertex_auto.setGeometry(QRect(560, 80, 71, 32))
        self.append_left_op = QPushButton(self.centralwidget)
        self.append_left_op.setObjectName(u"append_left_op")
        self.append_left_op.setGeometry(QRect(380, 380, 111, 32))
        self.append_right_op = QPushButton(self.centralwidget)
        self.append_right_op.setObjectName(u"append_right_op")
        self.append_right_op.setGeometry(QRect(510, 380, 101, 32))
        self.begin_ineq = QPushButton(self.centralwidget)
        self.begin_ineq.setObjectName(u"begin_ineq")
        self.begin_ineq.setGeometry(QRect(380, 350, 71, 32))
        self.end_ineq = QPushButton(self.centralwidget)
        self.end_ineq.setObjectName(u"end_ineq")
        self.end_ineq.setGeometry(QRect(470, 350, 71, 32))
        self.cal_ineq_matrix = QPushButton(self.centralwidget)
        self.cal_ineq_matrix.setObjectName(u"cal_ineq_matrix")
        self.cal_ineq_matrix.setGeometry(QRect(560, 350, 141, 32))
        self.load_data = QPushButton(self.centralwidget)
        self.load_data.setObjectName(u"load_data")
        self.load_data.setGeometry(QRect(380, 430, 101, 32))
        self.save_data = QPushButton(self.centralwidget)
        self.save_data.setObjectName(u"save_data")
        self.save_data.setGeometry(QRect(490, 430, 101, 32))
        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(main_window)
        self.statusbar.setObjectName(u"statusbar")
        main_window.setStatusBar(self.statusbar)

        self.button_connect_function()
        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("main_window", u"Number of Coordinates", None))
        self.add_coo.setText(QCoreApplication.translate("main_window", u"Add", None))
        self.del_coo.setText(QCoreApplication.translate("main_window", u"Delete", None))
        self.clear_coo.setText(QCoreApplication.translate("main_window", u"Clear", None))
        self.save_coo.setText(QCoreApplication.translate("main_window", u"Save", None))
        self.load_coo.setText(QCoreApplication.translate("main_window", u"Load", None))
        self.auto_coo.setText(QCoreApplication.translate("main_window", u"Auto", None))
        self.set_coo_num.setText(QCoreApplication.translate("main_window", u"Set", None))
        self.lock_coo.setText(QCoreApplication.translate("main_window", u"Lock", None))
        self.th_vetex.setText(QCoreApplication.translate("main_window", u"Vertex", None))
        self.th_ins.setText(QCoreApplication.translate("main_window", u"Intensity", None))
        self.th_alt.setText(QCoreApplication.translate("main_window", u"Alternatives", None))
        self.save_th.setText(QCoreApplication.translate("main_window", u"Save", None))
        self.del_vertex.setText(QCoreApplication.translate("main_window", u"Delete", None))
        self.load_th.setText(QCoreApplication.translate("main_window", u"Load", None))
        self.add_vertex.setText(QCoreApplication.translate("main_window", u"Add", None))
        self.clear_vertex.setText(QCoreApplication.translate("main_window", u"Clear", None))
        self.vertex_chcek.setText(QCoreApplication.translate("main_window", u"Check", None))
        self.lock_th.setText(QCoreApplication.translate("main_window", u"Lock", None))
        self.calculate_ins_order.setText(QCoreApplication.translate("main_window", u"Calculate Intensity Order", None))
        self.vertex_auto.setText(QCoreApplication.translate("main_window", u"Auto", None))
        self.append_left_op.setText(QCoreApplication.translate("main_window", u"Add to Left", None))
        self.append_right_op.setText(QCoreApplication.translate("main_window", u"Add to Right", None))
        self.begin_ineq.setText(QCoreApplication.translate("main_window", u"Begin", None))
        self.end_ineq.setText(QCoreApplication.translate("main_window", u"End", None))
        self.cal_ineq_matrix.setText(QCoreApplication.translate("main_window", u"Calculate Matrix", None))
        self.load_data.setText(QCoreApplication.translate("main_window", u"Load Data", None))
        self.save_data.setText(QCoreApplication.translate("main_window", u"Save Data", None))

        
    # retranslateUi

    def button_connect_function(self):
        self.th_mode = 0
        self.theory_count = 0
        self.A_matrix = []
        self.B_matrix = []
        
        self.load_coo.clicked.connect(self.load_coo_file)
        self.add_coo.clicked.connect(self.add_coo_row)
        self.del_coo.clicked.connect(self.del_coo_row)
        self.clear_coo.clicked.connect(self.clear_coo_row)
        self.save_coo.clicked.connect(self.save_coo_table)
        self.set_coo_num.clicked.connect(self.manual_coo_gene)
        self.auto_coo.clicked.connect(self.auto_coo_gene)
        self.lock_coo.clicked.connect(self.move_coo_header)

        self.th_vetex.clicked.connect(self.set_th_mode)
        self.th_alt.clicked.connect(self.set_th_mode)
        self.th_ins.clicked.connect(self.set_th_mode)
        
        self.del_vertex.clicked.connect(self.del_vertex_node)
        self.add_vertex.clicked.connect(self.add_vertex_node)
        self.clear_vertex.clicked.connect(self.clear_vertex_node)
        self.load_th.clicked.connect(self.load_theory)
        self.save_th.clicked.connect(self.save_theory)

        self.vertex_chcek.clicked.connect(self.check_vertex_range)
        self.lock_th.clicked.connect(self.move_vertex_name_header)

        self.calculate_ins_order.clicked.connect(self.intensity_order_cal)
        self.vertex_auto.clicked.connect(self.create_vertex_auto)

        self.append_left_op.clicked.connect(self.append_left_ineq)
        self.append_right_op.clicked.connect(self.append_right_ineq)

        self.begin_ineq.clicked.connect(self.start_ineq_one)
        self.end_ineq.clicked.connect(self.end_ineq_one)
        self.cal_ineq_matrix.clicked.connect(self.final_ieq_matrix)

        self.load_data.clicked.connect(self.load_data_func)
        self.save_data.clicked.connect(self.save_data_func)

    ### Coordinate Part
    def move_coo_header(self):
        if(not self.lock_coo.isChecked()):
            return
        window = self.monitor
        coordinate_names = []
        for row in range(window.rowCount()):
            for column in range(window.columnCount()):
                item = window.item(row, column)
                if item is not None:
                    coordinate_names.append(item.text())
                else:
                    coordinate_names.append('')
        self.coo = coordinate_names
        self.monitor.setVerticalHeaderLabels(coordinate_names)
        self.monitor.setHorizontalHeaderLabels([''])
        self.monitor.clearContents()


    def save_coo_table(self):
        file_name = QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV files(*.csv);;Excel files(*.xlsx , *.xls)')[0]
        file_extension = pathlib.Path(file_name).suffix
        if(file_extension == '.csv'):
            write_to_csv(self.monitor, file_name, None)
        elif(file_extension == '.xls' or file_extension == '.xlsx'):
            write_to_excel(self.monitor, file_name, sheetname = 'coordinate')

    def clear_coo_row(self):
        clear_window(self.monitor)

    def load_coo_file(self):
        self.clear_coo_row()
        filename = QFileDialog.getOpenFileName(self,'Select file:','','CSV files(*.csv);;Excel files(*.xlsx , *.xls)')[0]
        file_extension = pathlib.Path(filename).suffix
        if(file_extension == '.csv'):
            input_table = pd.read_csv(filename, header=None)
        elif(file_extension == '.xls' or file_extension == '.xlsx'):
            input_table = pd.read_excel(filename)
        else:
            return -1

        num_coo, _ = input_table.shape[0], input_table.shape[1]
        coordinates = []
        for i in range(num_coo):
            row_value = input_table.iloc[i][0]
            coordinates.append(row_value)
        self.monitor.setColumnCount(1)
        self.monitor.setRowCount(num_coo)
        self.coo_spin_box.setValue(num_coo)
        display_coordinate(self.monitor, coordinates, num_coo)


    def add_coo_row(self):
        add_row_in_window(self.monitor, 1)
    
    # only delete after content exists
    def del_coo_row(self):
        sel_items = self.monitor.selectedItems()
        sel_rows = []
        for item in sel_items:
            sel_rows.append(self.monitor.indexFromItem(item).row())
        remove_row_in_window(self.monitor, sel_rows)

    def manual_coo_gene(self):
        if(self.set_coo_num.isChecked()):
            num_coo = self.coo_spin_box.value()
            self.monitor.setColumnCount(1)
            self.monitor.setRowCount(num_coo)
        else:
            return

    def auto_coo_gene(self):
        self.clear_coo_row()
        num, ok = QInputDialog.getInt(self, 'Generate Coordinates', 'Number of Gamble:')
        num_gamble = num
        num_coo = int(comb(num, 2))
        self.coo_spin_box.setValue(num_coo)
        coordinates = list(generate_coordinate(num_gamble))
        self.monitor.setColumnCount(1)
        self.monitor.setRowCount(num_coo)
        display_coordinate(self.monitor, coordinates, num_coo)
        
    ### Theory Part

    def set_th_mode(self):
        vertex = self.th_vetex.isChecked()
        ins = self.th_ins.isChecked()
        alt = self.th_alt.isChecked()

        # check conflict
        if (vertex and ins) or (vertex and alt) or (ins and alt):
            pop_window_text('Theory', 'Only one method required')
        else:
            print(self.coo)
            print(self.th_mode)
            if self.th_mode == 0:
                self.monitor.setRowCount(self.monitor.rowCount()+1)
            if vertex:
                self.th_mode = 1
                self.monitor.setVerticalHeaderLabels(['Coordinates']+self.coo)
            elif ins:
                self.th_mode = 2
                self.monitor.setVerticalHeaderLabels(['instance']+self.coo)
            else:
                self.th_mode = 3
                self.monitor.setVerticalHeaderLabels(['alternative']+self.coo)

    def del_vertex_node(self):
        sel_items = self.monitor.selectedItems()
        for item in sel_items:
            self.monitor.removeColumn(self.monitor.indexFromItem(item).column())
        
    def add_vertex_node(self):
        if (self.monitor.rowCount == 0):
            self.monitor.setColumnCount(1)
        else:
            self.monitor.setColumnCount(self.monitor.columnCount()+1)
        
    def clear_vertex_node(self):
        self.th_mode = 0
        self.monitor.setColumnCount(0)
        self.monitor.clearContents()

    def load_theory(self):
        file = QFileDialog.getOpenFileName(self,'Select file:','','CSV files(*.csv);;Excel files(*.xlsx , *.xls)')
        theory_file_name = file[0]
        file_extension = pathlib.Path(theory_file_name).suffix

        if(file_extension == '.csv'):
            input_table = pd.read_csv(theory_file_name, skiprows=1)       
        elif(file_extension == '.xls' or file_extension == '.xlsx'):
            input_table = pd.read_excel(theory_file_name)

        display_theory(self.monitor, input_table, len(self.coo))


    def save_theory(self):
        file_name = QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV files(*.csv);;Excel files(*.xlsx , *.xls)')[0]
        file_extension = pathlib.Path(file_name).suffix

        theory_name, ok = QInputDialog.getText(self, 'Enter', 'Theory Name:')
        
        if(file_extension == '.csv'):
            write_to_csv(self.monitor, file_name, theory_name)
        elif(file_extension == '.xls' or file_extension == '.xlsx'):
            write_to_excel(self.monitor, file_name, theory_name)
        
        self.th_list.insertItem(self.th_list.count()+1, theory_name)
        
    def check_vertex_range(self):
        theory_lock_status = self.lock_th.isChecked()

        if self.th_mode != 1:
            pop_window_text('warning', 'No need to check')
        else:
            check_col_values(self.monitor, theory_lock_status)
    
    def move_vertex_name_header(self):
        if(not self.lock_th.isChecked()):
            return
        window = self.monitor
        vertex_names = []
        for column in range(window.columnCount()):
            item = window.item(0, column)
            if item is not None:
                vertex_names.append(item.text())
            else:
                vertex_names.append('')
        self.monitor.removeRow(0)
        self.monitor.setHorizontalHeaderLabels(vertex_names)

    def intensity_order_cal(self):
        if(self.th_mode != 2):
            pop_window_text('Warning', 'Wrong Mode')
            return
        lock_status = self.lock_th.isChecked()
        total_order = order_intensity_cal(self.monitor, lock_status)

        self.th_list.clear()
        for one_col_order in total_order:
            item = generate_p_string(one_col_order, self.coo)
            self.th_list.insertItem(self.th_list.count()+1, item)
        
    
    def create_vertex_auto(self):
        window = vertex_window(self.coo)
        x = window.exec()
        # list of 0/1 on the current dimension
        if(not self.lock_th.isChecked()):
            values = window.result
        self.monitor.setColumnCount(self.monitor.columnCount() + 1)

        for i in range(self.monitor.rowCount()):
            newItem = QTableWidgetItem(str(values[i]))
            newItem.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
            self.monitor.setItem(i+2, -1, newItem)
    
    def start_ineq_one(self):
        self.left_p = []
        self.left_m = []

        self.right_p = []
        self.right_m = []
        self.A_col = np.zeros(len(self.coo))
        self.B_col = np.zeros(len(self.coo))
        self.ineq_str = '<='

    def end_ineq_one(self):
        if(self.left_p == []):
            self.ineq_str = '0' + self.ineq_str
        elif(self.right_p == []):
            self.ineq_str =  self.ineq_str + '0'
        self.th_list.insertItem(self.th_list.count()+1, self.ineq_str)
        
        self.A_matrix.append(self.A_col)
        self.B_matrix.append(self.B_col)
        

    def append_left_ineq(self):
        if(not self.th_mode == 3):
            pop_window_text('Warning', 'Wrong Mode')
            return
        p = getInt(self, 'Get Prob', 'P')
        m = getDouble(self, 'Get Multiplier', 'Mult')
        self.left_p.append(p)
        self.left_m.append(m)
        if(m > 0):
            self.ineq_str = '+' + str(m) + 'P_%d:%s'%(p, self.coo[p]) + self.ineq_str
        else:
            self.ineq_str = str(m) + 'P_%d:%s'%(p, self.coo[p]) + self.ineq_str
        self.A_col[p] = m


    def append_right_ineq(self):
        if(not self.th_mode == 3):
            pop_window_text('Warning', 'Wrong Mode')
            return
        p = getInt(self, 'Get Prob', 'P')
        m = getDouble(self, 'Get Multiplier', 'Mult')
        self.right_p.append(p)
        self.right_m.append(m)
        if(m > 0):
            self.ineq_str = self.ineq_str + '+' + str(m) + 'P_%d:%s'%(p, self.coo[p])
        else:
            self.ineq_str = self.ineq_str + str(m) + 'P_%d:%s'%(p, self.coo[p])

        self.B_col[p] = m

    def final_ieq_matrix(self):
        print('A matrix', np.array(self.A_matrix))
        print(np.array(self.A_matrix).shape)
        print('B matrix', np.array(self.B_matrix))
        print(np.array(self.B_matrix).shape)
        self.A_matrix = []
        self.B_matrix = []
    
    # Add mapping between coordinate name and P_number when last two modes are checked

    # Add constant button to the inequalitity
    # Allow simplification and  edit on the inequality 
    # unlock and lock, reset all button
    # mark the monitor window with theory or data
    # load inequalities 
    # support equalities like we support inequalities
    # dataset, automatic update when people trigger it

    # data part: read and write data

    def load_data_func(self):
        file = QFileDialog.getOpenFileName(self,'Select file:','','CSV files(*.csv);;Excel files(*.xlsx , *.xls)')
        theory_file_name = file[0]
        file_extension = pathlib.Path(theory_file_name).suffix

        if(file_extension == '.csv'):
            input_table = pd.read_csv(theory_file_name)       
        elif(file_extension == '.xls' or file_extension == '.xlsx'):
            input_table = pd.read_excel(theory_file_name)

        display_theory(self.monitor, input_table, len(self.coo))

    def save_data_func(self):
        file_name = QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV files(*.csv);;Excel files(*.xlsx , *.xls)')[0]
        file_extension = pathlib.Path(file_name).suffix

        dataset_name, ok = QInputDialog.getText(self, 'Enter', 'Dataset Name:')
        
        if(file_extension == '.csv'):
            write_to_csv(self.monitor, file_name, None)
        elif(file_extension == '.xls' or file_extension == '.xlsx'):
            write_to_excel(self.monitor, file_name, dataset_name)