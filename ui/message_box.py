from PySide6.QtCore import QTimer, Qt, QSize
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QPixmap, QIcon


# Single-button dialog box, which disappears automatically after appearing for a specified period of time
class MessageBox(QMessageBox):
    def __init__(self, *args, title='提示', count=1, time=1000, auto=False, **kwargs):
        super(MessageBox, self).__init__(*args, **kwargs)
        self._count = count
        self._time = time
        self._auto = auto  # Whether to close automatically
        assert count > 0  # must be greater than 0
        assert time >= 500  # Must be >=500 milliseconds
        self.setStyleSheet('''
                            QWidget{color:black;
                                    background-color: qlineargradient(x0:0, y0:1, x1:1, y1:1,stop:0.4  rgb(255, 150, 150), stop:1 rgb(100,10,130 ));
                                    font: 13pt "Microsoft YaHei UI";
                                    padding-right: 5px;
                                    padding-top: 14px;
                                    font-weight: light;}
                            QLabel{
                                color:white;
                                background-color: rgba(107, 128, 210, 0);}''')

        self.setWindowTitle(title)
        icon = QIcon()
        icon.addFile(u":/all/img/logo.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        # self.setIconPixmap(QPixmap(":/all/img/logo.jpg"))
        self.setStandardButtons(QMessageBox.StandardButton.Close)  # close button
        self.closeBtn = self.button(QMessageBox.StandardButton.Close)  # get close button
        self.closeBtn.setText('Close')
        self.closeBtn.setVisible(False)
        self._timer = QTimer(self, timeout=self.doCountDown)
        self._timer.start(self._time)

    def doCountDown(self):
        self._count -= 1
        if self._count <= 0:
            self._timer.stop()
            if self._auto:  # auto close
                self.accept()
                self.close()

if __name__ == '__main__':
    MessageBox(QWidget=None, text='123', auto=True).exec()
