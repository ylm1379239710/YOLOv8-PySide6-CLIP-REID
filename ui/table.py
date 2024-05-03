import math
import os
import sys
from datetime import datetime
from functools import partial
from math import ceil

from entity.file_model import FileData
from ui.confirm_message_box import ConfirmMessageBox
from ui.details_box import DetailsBox
from ui.edit_dialog import EditDialogBox
from ui.message_box import MessageBox
from dao import file_dao, record_dao
from PySide6.QtCore import Qt, QFileInfo, QSize
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, \
    QTableWidget, QHBoxLayout, QSpinBox, QLabel, QHeaderView, QAbstractItemView, QFileDialog


class TableWithButtons(QTableWidget):
    def __init__(self):
        super().__init__()
        # 设置列头样式，添加底部横线
        self.mode = None
        self.details_box = None
        self.edit_box = None
        self.title_edit = None
        self.type_box = None
        self.search_button = None
        self.confirm_message_box = None
        self.add_button = None
        self.detail_button = None
        self.edit_button = None
        self.delete_button = None
        self.total_label = None
        self.page_spinbox = None
        self.total_page = None
        self.rows_per_page = None
        self.data = None
        self.current_page = None
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
        # self.verticalHeader().setStyleSheet("""
        #     QHeaderView::section {
        #         background-color: rgb(245, 249, 254);
        #         border: 1px solid #d0d0d0; /* 边框 */
        #     }
        # """)
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
        self.verticalHeader().setVisible(False)

    def load_data(self, mode, page_spinbox, total_page_num, label, add_button, search_button, type_box, line_edit,
                  rows_per_page=15):
        self.mode = mode
        if self.mode == 1:
            self.data = file_dao.get_all_file_data()
        else:
            self.data = record_dao.get_all_record()
        self.rows_per_page = rows_per_page
        self.current_page = 0
        self.total_page = len(self.data) // self.rows_per_page + 1

        if len(self.data) > 0:
            self.insertColumn(0)
            self.setColumnCount(len(self.data[0]) + 1)  # 根据数据确定列数
            self.setHorizontalHeaderLabels(label)
            last_item = QTableWidgetItem('Action')
            self.setHorizontalHeaderItem(len(self.data[0]), last_item)
            self.fill_table()
        else:
            self.insertColumn(0)
            if self.mode == 1:
                self.setColumnCount(5 + 1)  # 根据数据确定列数
                self.setHorizontalHeaderLabels(label)
                last_item = QTableWidgetItem('Action')
                self.setHorizontalHeaderItem(5, last_item)
            else:
                self.setColumnCount(4 + 1)  # 根据数据确定列数
                self.setHorizontalHeaderLabels(label)
                last_item = QTableWidgetItem('Action')
                self.setHorizontalHeaderItem(4, last_item)

        # 分页组件
        self.page_spinbox = page_spinbox
        self.page_spinbox.setMinimum(1)
        self.page_spinbox.setMaximum(len(self.data) // rows_per_page + (len(self.data) % rows_per_page > 0))
        self.page_spinbox.setValue(self.current_page + 1)
        self.page_spinbox.valueChanged.connect(self.change_page)
        self.page_spinbox.setMaximumSize(100, 20)
        self.total_label = total_page_num
        self.total_label.setText(str(self.total_page))

        # 新增按钮
        self.add_button = add_button
        self.add_button.clicked.connect(self.add_data)

        # 搜索按钮
        self.search_button = search_button
        self.search_button.clicked.connect(self.search_data)

        # 数据类型选择
        self.type_box = type_box

        # 标题输入框
        self.title_edit = line_edit

    def load_data_again(self):
        if self.mode == 1:
            self.data = file_dao.get_all_file_data()
        else:
            self.data = record_dao.get_all_record()

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
            self.delete_button.clicked.connect(partial(self.delete_confirm, row=row))
            if self.mode == 1:
                self.edit_button = QPushButton('Edit')
                self.edit_button.clicked.connect(partial(self.edit_confirm, row=row))
            self.detail_button = QPushButton('Details')
            self.detail_button.clicked.connect(partial(self.get_details, row=row))
            buttons_layout.addWidget(self.delete_button)
            if self.mode == 1:
                buttons_layout.addWidget(self.edit_button)
            buttons_layout.addWidget(self.detail_button)
            custom_widget = QWidget()
            custom_widget.setLayout(buttons_layout)
            self.setCellWidget(row, col + 1, custom_widget)

    # def update_page_info(self):
    #     self.setWindowTitle(f'Table - Page {self.current_page + 1}/{self.page_spinbox.maximum()}')

    def change_page(self):
        self.total_page = ceil(len(self.data) / self.rows_per_page)
        self.total_label.setText(str(self.total_page))
        self.page_spinbox.setMaximum(len(self.data) // self.rows_per_page + (len(self.data) % self.rows_per_page > 0))
        if self.page_spinbox.value() == 0:
            self.current_page = 1
            self.page_spinbox.setValue(1)
        else:
            self.current_page = self.page_spinbox.value() - 1
        self.fill_table()
        # self.update_page_info()

    def add_data(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        # 文件过滤器，允许选择图片和视频
        file_filter = "Images or Videos(*.jpg *.jpeg *.png *.bmp *.mp4 *.avi *.mov *.mkv)"
        fileNames, _ = QFileDialog.getOpenFileNames(self, "选择图片或视频文件", "",
                                                    file_filter, options=options)
        if fileNames:
            for file in fileNames:
                file_info = QFileInfo(file)
                # 提取文件扩展名
                base_name, extension = os.path.splitext(file_info.filePath())
                extension = extension[1:]  # 移除点号
                file_data = FileData(file_info.fileName(), datetime.now(), file_info.filePath(), file_info.fileName(),
                                     file_info.fileName(), file_info.size(), extension)
                file_dao.add_file_data(file_data)
            # self.load_data_again()
            self.search_data()  # 刷新表格以删除选中行

    def delete_confirm(self, row):
        self.confirm_message_box = ConfirmMessageBox()
        data_id = self.data[row + self.current_page * self.rows_per_page][0]
        self.confirm_message_box.text.setText("确认进行删除id为" + str(data_id) + "数据的操作吗?")
        self.confirm_message_box.confirmed.connect(lambda: self.delete_file_data(data_id))
        self.confirm_message_box.exec()

    def delete_file_data(self, data_id):
        if self.mode == 1:
            file_dao.delete_file_data_by_id(data_id)
        else:
            record_dao.delete_record_by_id(data_id)
        self.search_data()  # 刷新表格以删除选中行

    def search_data(self):
        # 获取data的type和title的搜索值
        title = self.title_edit.text()
        type = self.type_box.currentText()
        if self.mode == 1:
            self.data = file_dao.search_data_by_condition(title, type)
        else:
            self.data = record_dao.search_record_by_condition(title, type)
        self.change_page()

    def edit_confirm(self, row):
        self.edit_box = EditDialogBox()
        data_id = self.data[row + self.current_page * self.rows_per_page][0]
        title = self.data[row + self.current_page * self.rows_per_page][1]
        description = self.data[row + self.current_page * self.rows_per_page][4]
        self.edit_box.title_edit.setText(title)
        self.edit_box.description_edit.setText(description)
        self.edit_box.confirmed.connect(lambda: self.edit_data(data_id, self.edit_box.title_edit.text(),
                                                               self.edit_box.description_edit.toPlainText()))
        self.edit_box.exec()

    def edit_data(self, data_id, title, description):
        if self.mode == 1:
            file_dao.edit_by_id(data_id, title, description)
        self.search_data()  # 刷新表格以删除选中行

    def get_details(self, row):
        data_id = self.data[row + self.current_page * self.rows_per_page][0]
        if self.mode == 1:
            data = file_dao.get_data_by_id(data_id)
            self.details_box = DetailsBox(data[4])
            self.details_box.id_text.setText(str(data[0]))
            self.details_box.title_text.setText(str(data[1]))
            self.details_box.description_text.setText(str(data[2]))
            self.details_box.upload_date_text.setText(str(data[3]))
            self.details_box.file_path_text.setText(str(data[4]))
            self.details_box.file_name_text.setText(str(data[5]))
            self.details_box.file_size_text.setText(str(self.format_file_size(data[6])))
            self.details_box.file_type_text.setText(str(data[7]))
        else:
            data = record_dao.get_record_by_id(data_id)
            self.details_box = DetailsBox(data[5])
            self.details_box.id_text.setText(str(data[0]))
            self.details_box.title_text.setText(str(data[1]))
            self.details_box.description_label.setFixedSize(QSize(0, 0))
            self.details_box.description_text.setFixedSize(QSize(0, 0))
            self.details_box.upload_date_text.setText(str(data[2]))
            self.details_box.file_path_text.setText(str(data[5]))
            self.details_box.file_name_label.setFixedSize(QSize(0, 0))
            self.details_box.file_name_text.setFixedSize(QSize(0, 0))
            self.details_box.file_size_label.setText('Result：')
            self.details_box.file_size_text.setText(str(data[4]))
            self.details_box.file_type_text.setText(data[3])
            self.details_box.file_type_label.setText('TaskType：')
        self.details_box.show()

    def format_file_size(self, size_bytes):
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "{} {}".format(s, size_name[i])


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
            ['Data9', 'Row', '7'], ['Data', 'Row', '1'],
            ['Data2', 'Row', '2'],
            ['Data3', 'Row', '3'],
            ['Data4', 'Row', '4'],
            ['Data5', 'Row', '5'],
            ['Data7', 'Row', '6'],
            ['Data9', 'Row', '7'], ['Data', 'Row', '1'],
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
