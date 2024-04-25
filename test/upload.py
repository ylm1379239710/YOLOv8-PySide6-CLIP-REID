from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
from PySide6.QtCore import Qt
import os
import sqlite3


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
            self.add_video_to_db(fileName)
            self.label.setText(f'Video uploaded: {fileName}')

    def add_video_to_db(self, path):
        conn = sqlite3.connect('test.db')
        c = conn.cursor()
        c.execute("INSERT INTO videos (path) VALUES (?)", (path,))
        conn.commit()
        conn.close()


if __name__ == '__main__':
    app = QApplication([])
    ex = VideoUploader()
    ex.show()
    app.exec()