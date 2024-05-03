from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
from PySide6.QtCore import Qt, QFileInfo
import os
from dao import file_dao
from entity.file_model import FileData
from datetime import datetime

class VideoUploader(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Video Uploader')
        self.setGeometry(300, 300, 300, 200)

        layout = QVBoxLayout()

        self.upload_button = QPushButton('Upload Video')
        self.upload_button.clicked.connect(self.upload_video)
        layout.addWidget(self.upload_button)

        self.label = QLabel('No video uploaded yet.')
        layout.addWidget(self.label)

        self.setLayout(layout)

    def upload_video(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Videos (*.mp4 *.avi)", options=options)
        if fileName:
            file_info = QFileInfo(fileName)
            print(file_info.fileName())
            print(file_info.filePath())
            print(file_info.size())
            # 提取文件扩展名
            base_name, extension = os.path.splitext(file_info.filePath())
            extension = extension[1:]  # 移除点号
            print(extension)
            file_data = FileData(file_info.fileName(),datetime.now(),file_info.filePath(),file_info.fileName(),file_info.fileName(),file_info.size(),extension)
            # self.add_video_to_db(file_data)
            self.label.setText(f'Video uploaded: {fileName}')
            self.get_all_data()

    def add_video_to_db(self, file_data):
        print(file_dao.add_file_data(file_data))

    def get_all_data(self):
        file_dao.get_all_file_data()
        # 获取类实例的属性名
        attr_names = [attr for attr in dir(FileData) if
                      not attr.startswith('__') and not callable(getattr(FileData, attr))]
        print(attr_names)

if __name__ == '__main__':
    app = QApplication([])
    ex = VideoUploader()
    ex.show()
    app.exec()