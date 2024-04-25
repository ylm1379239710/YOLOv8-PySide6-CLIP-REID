import sys
from functools import partial
from math import ceil

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, \
    QTableWidget, QHBoxLayout, QSpinBox, QLabel, QHeaderView, QAbstractItemView


class TableWithButtons(QTableWidget):
    def __init__(self):
        super().__init__()
        # 设置列头样式，添加底部横线
        self.horizontalHeader().setStyleSheet("""  
            QHeaderView::section {  
                background-color: rgb(245, 249, 254);
                color: #333; /* 字体颜色 */  
                font-weight: bold; /* 字体加粗 */  
                border: 1px solid #d0d0d0; /* 边框 */  
                padding: 4px; /* 内边距 */  
                font-size: 12pt;
            }  
        """)
        self.verticalHeader().setStyleSheet("""  
            QHeaderView::section {  
                background-color: rgb(245, 249, 254);
                border: 1px solid #d0d0d0; /* 边框 */  
            }  
        """)
        self.setStyleSheet("""
            QTableWidget {  
                background-color: rgb(245, 249, 254);
            }  
            QTableWidget::item:selected {  
                background-color: transparent; /* 或者设置为与未选中时相同的颜色 */  
            }  
        """)
        self.setSelectionMode(QAbstractItemView.NoSelection)
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def load_data(self,data,page_spinbox,total_page_num, rows_per_page=15):
        self.data = data  # 假设data是一个二维列表，表示表格数据
        self.rows_per_page = rows_per_page
        self.current_page = 0
        self.total_page = len(self.data) // self.rows_per_page + 1

        self.insertColumn(0)
        self.setColumnCount(len(data[0]) + 1)  # 根据数据确定列数
        self.setHorizontalHeaderLabels([f'Column {i + 1}' for i in range(len(data[0]))])
        last_item = QTableWidgetItem('Action')
        self.setHorizontalHeaderItem(len(data[0]), last_item)
        self.fill_table()

        # 分页组件
        self.page_spinbox = page_spinbox
        self.page_spinbox.setMinimum(1)
        self.page_spinbox.setMaximum(len(self.data) // rows_per_page + (len(self.data) % rows_per_page > 0))
        self.page_spinbox.setValue(self.current_page + 1)
        self.page_spinbox.valueChanged.connect(self.change_page)
        self.page_spinbox.setMaximumSize(100,20)
        self.total_label = total_page_num
        self.total_label.setText(str(self.total_page))

    def fill_table(self):
        self.clearContents()
        self.setRowCount(min(self.rows_per_page, len(self.data) - self.current_page * self.rows_per_page))

        for row, data_row in enumerate(self.data[
                                       self.current_page * self.rows_per_page:self.current_page * self.rows_per_page + self.rowCount()]):
            for col, value in enumerate(data_row):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)  # 设置文本居中
                self.setItem(row, col, item)
            buttons_layout = QHBoxLayout()
            buttons_layout.setContentsMargins(0, 0, 0, 0)
            # 增删改查按钮
            self.delete_button = QPushButton('Delete')
            self.delete_button.clicked.connect(partial(self.delete_selected_rows, row=row))
            self.edit_button = QPushButton('Edit')
            self.edit_button.clicked.connect(partial(self.edit_selected_rows, row=row))
            self.detail_button = QPushButton('Details')
            self.detail_button.clicked.connect(partial(self.edit_selected_rows, row=row))
            buttons_layout.addWidget(self.delete_button)
            buttons_layout.addWidget(self.edit_button)
            buttons_layout.addWidget(self.detail_button)
            custom_widget = QWidget()
            custom_widget.setLayout(buttons_layout)
            self.setCellWidget(row, col + 1, custom_widget)

    def update_page_info(self):
        self.setWindowTitle(f'Table - Page {self.current_page + 1}/{self.page_spinbox.maximum()}')

    def change_page(self, page):
        self.current_page = page - 1
        self.fill_table()
        self.update_page_info()

    def add_row(self,row):
        new_data = [''] * len(self.data[0])  # 新增一行数据，所有字段默认为空字符串
        self.data.append(new_data)
        self.change_page(self.page_spinbox.value())  # 刷新表格以显示新增行

    def delete_selected_rows(self,row):
        del self.data[row + self.current_page * self.rows_per_page]
        self.total_page = ceil(len(self.data) / self.rows_per_page)
        self.total_label.setText(str(self.total_page))
        self.page_spinbox.setMaximum(len(self.data) // self.rows_per_page + (len(self.data) % self.rows_per_page > 0))
        self.change_page(self.page_spinbox.value())  # 刷新表格以删除选中行

    def edit_selected_rows(self,row):
        # 实现编辑选中行的功能，这里仅作占位
        print("Edit selected rows")

    def cell_changed(self, row, col):
        # 实现单元格内容改变时自动更新数据源，这里仅作占位
        print(f"Cell ({row}, {col}) changed")




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 假设有一个初始数据列表
        initial_data = [
            ['Data', 'Row', '1'],
            ['Data2', 'Row', '2'],
            ['Data3', 'Row', '3'],
            ['Data4', 'Row', '4'],
            ['Data5', 'Row', '5'],
            ['Data7', 'Row', '6'],
            ['Data9', 'Row', '7'],['Data', 'Row', '1'],
            ['Data2', 'Row', '2'],
            ['Data3', 'Row', '3'],
            ['Data4', 'Row', '4'],
            ['Data5', 'Row', '5'],
            ['Data7', 'Row', '6'],
            ['Data9', 'Row', '7'],['Data', 'Row', '1'],
            ['Data2', 'Row', '2'],
            ['Data3', 'Row', '3'],
            ['Data4', 'Row', '4'],
            ['Data5', 'Row', '5'],
            ['Data7', 'Row', '6'],
            ['Data9', 'Row', '7'],
        ]

        table_widget = TableWithButtons()
        table_widget.load_data(initial_data)
        # 布局
        layout = QVBoxLayout()
        layout.addWidget(table_widget)
        h_layout = QHBoxLayout()
        h_layout.addWidget(table_widget.page_spinbox)
        h_layout.addWidget(table_widget.total_label)
        layout.addLayout(h_layout)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
