from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel, QDesktopWidget
from PyQt5 import QtCore

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.label.setText("Label1")
        self.label.move(200, 0)
        
        self.button = QPushButton(self)
        self.button.setText("Button1")
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Belajar PyQt5")
        
        # Cek ukuran main window dan center window di tengah layar
        cwa = self.frameGeometry()  
        cwc = QDesktopWidget().availableGeometry().center()  
        cwa.moveCenter(cwc)
        self.move(cwa.topLeft())
        
        # Nonaktifkan resize, tapi pertahankan minimize dan close button
        self.setFixedSize(300, 300)
        
        # Mengatur flag: menonaktifkan maximize tetapi mempertahankan minimize dan close
        self.setWindowFlags(QtCore.Qt.Window |
                            QtCore.Qt.WindowMinimizeButtonHint |
                            QtCore.Qt.WindowCloseButtonHint |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowTitleHint)

# Program Utama
app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
