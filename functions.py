def show_popup_1(self):
        msg = QMessageBox()
        msg.setWindowTitle("Wrong Input")
        msg.setText("Coordinate Name only has one column!")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry|QMessageBox.Ignore)
        msg.setDefaultButton(QMessageBox.Cancel)
        x = msg.exec_() 


    def openexcel(self):
        openfile_name = QFileDialog.getOpenFileName(self,'Select file','','Excel files(*.xlsx , *.xls)')
        global coordinate_file_name
        coordinate_file_name = openfile_name[0]

    def create_table_show(self):
        if len(coordinate_file_name) > 0:
            input_table = pd.read_excel(coordinate_file_name)
            input_table_rows = input_table.shape[0]
            input_table_colunms = input_table.shape[1]
            input_table_header = input_table.columns.values.tolist()

            if input_table_colunms > 1:
                self.show_popup_1()
                return 

            global coordinate_names
            coordinate_names = []
            self.show_coo.setColumnCount(input_table_colunms)
            self.show_coo.setRowCount(input_table_rows)
            self.show_coo.setHorizontalHeaderLabels(input_table_header)

            for i in range(input_table_rows):
                input_table_rows_values = input_table.iloc[[i]]
                input_table_rows_values_array = np.array(input_table_rows_values)
                input_table_rows_values_list = input_table_rows_values_array.tolist()[0]
                coordinate_names.append(input_table_rows_values_list[0])
                for j in range(input_table_colunms):
                    input_table_items_list = input_table_rows_values_list[j]
                    input_table_items = str(input_table_items_list)
                    newItem = QTableWidgetItem(input_table_items) 
                    newItem.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                    self.show_coor.setItem(i, j, newItem)
        else:
            self.simpletable.show()

    def opencsv(self):
        openfile_name = QFileDialog.getOpenFileName(self,'Select file','','CSV files(*.csv)')
        global coordinate_file_name
        coordinate_file_name = openfile_name[0]

    def create_table_show_csv(self):
        if len(coordinate_file_name) > 0:
            input_table = pd.read_csv(coordinate_file_name, header=None)
            input_table_rows = input_table.shape[0]
            input_table_colunms = input_table.shape[1]
            input_table_header = input_table.columns.values.tolist()

            if input_table_colunms > 1:
                self.show_popup_1()
                return 

            global coordinate_names
            coordinate_names = []

            self.show_coo.setColumnCount(input_table_colunms)
            self.show_coo.setRowCount(input_table_rows)
            self.show_coo.setHorizontalHeaderLabels(input_table_header)

            for i in range(input_table_rows):
                input_table_rows_values = input_table.iloc[[i]]
                
                input_table_rows_values_array = np.array(input_table_rows_values)
                input_table_rows_values_list = input_table_rows_values_array.tolist()[0]
                coordinate_names.append(input_table_rows_values_list[0])
                for j in range(input_table_colunms):
                    input_table_items_list = input_table_rows_values_list[j]
                    input_table_items = str(input_table_items_list)
                    newItem = QTableWidgetItem(input_table_items) 
                    newItem.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                    self.show_coo.setItem(i, j, newItem)
        else:
            self.simpletable.show()

    def clear_table_show(self):
        self.show_coo.setRowCount(0)
        self.show_coo.setColumnCount(0)
        self.show_coo.clearContents()

    def add_coo_row(self):
        row_count = self.show_coo.rowCount()
        if(row_count == 0):
            self.show_coo.setRowCount(1)
            self.show_coo.setColumnCount(1)
        else:
            self.show_coo.setRowCount(row_count+1)
        
    def del_coo_row(self):
        sel_range = self.show_coo.selectedItems()
        for item in sel_range:
            self.show_coo.removeRow(self.show_coo.indexFromItem(item).row())

    def save_coo_table(self):
        path = QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV(*.csv)')[0]
        global coordinate_names
        coordinate_names = []
        with open(path, 'w') as stream:
            writer = csv.writer(stream)
            for row in range(self.show_coo.rowCount()):
                rowdata = []
                for column in range(self.show_coo.columnCount()):
                    item = self.show_coo.item(row, column)
                    if item is not None:
                        rowdata.append(item.text())
                        coordinate_names.append(item.text())
                    else:
                        rowdata.append('')
                writer.writerow(rowdata)

    def open_theory(self):
        openfile_name = QFileDialog.getOpenFileName(self,'Select file','','Excel files(*.xlsx , *.xls)')
        global theory_file_name
        theory_file_name = openfile_name[0]

    def show_popup_2(self):
        msg = QMessageBox()
        msg.setWindowTitle("Wrong Input")
        msg.setText("Coordinate number mismatch the number of rows!")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry|QMessageBox.Ignore)
        msg.setDefaultButton(QMessageBox.Cancel)
        x = msg.exec_() 

    def show_theory_table(self):
        theory_sheet_name = self.spreadsheet_name.toPlainText()
        global coordinate_names
        
        print(theory_sheet_name)
        
        if len(theory_file_name) > 0:
            input_table = pd.read_excel(theory_file_name, theory_sheet_name, header=0)
            input_table_rows = input_table.shape[0]
            input_table_colunms = input_table.shape[1]
            input_table_header = input_table.columns.values.tolist()

            if(input_table_rows != len(coordinate_names)):
                self.show_popup_2()
                return

            print(coordinate_names)
            print(input_table_header)
            
            self.show_coo_2.setColumnCount(input_table_colunms)
            self.show_coo_2.setRowCount(len(coordinate_names))
            self.show_coo_2.setHorizontalHeaderLabels(input_table_header)

            for i in range(input_table_rows):
                input_table_rows_values = input_table.iloc[[i]]
                input_table_rows_values_array = np.array(input_table_rows_values)
                input_table_rows_values_list = input_table_rows_values_array.tolist()[0]
                for j in range(input_table_colunms):
                    input_table_items_list = input_table_rows_values_list[j]
                    input_table_items = str(input_table_items_list)
                    newItem = QTableWidgetItem(input_table_items) 
                    newItem.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
                    self.show_coo_2.setItem(i, j, newItem)
            self.show_coo_2.setVerticalHeaderLabels(coordinate_names)
        else:
            self.simpletable.show()

    def reset_column_name(self):
        column_name = self.column_name.toPlainText().split(",")
        self.show_coo_2.setColumnCount(len(column_name))
        self.show_coo_2.setHorizontalHeaderLabels(column_name)

    def clear_table_show_2(self):
        self.show_coo_2.setRowCount(0)
        self.show_coo_2.setColumnCount(0)
        self.show_coo_2.clearContents()

    def save_coo_table_2(self):
        path = QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV(*.csv)')[0]
        header = []
        for i in range(self.show_coo_2.columnCount()):
            header.append(self.show_coo_2.horizontalHeaderItem(i).text())
        with open(path, 'w') as stream:
            writer = csv.writer(stream)
            writer.writerow(header)
            for row in range(self.show_coo_2.rowCount()):
                rowdata = []
                for column in range(self.show_coo_2.columnCount()):
                    item = self.show_coo_2.item(row, column)
                    if item is not None:
                        rowdata.append(item.text())
                    else:
                        rowdata.append('')
                writer.writerow(rowdata)