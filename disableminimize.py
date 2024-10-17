from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel, QDesktopWidget
from PyQt5 import QtCore

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Membuat Label
        self.label = QLabel(self)
        self.label.setText("Label1")
        self.label.move(200, 0)
        
        # Membuat Button
        self.button = QPushButton(self)
        self.button.setText("Button1")
        
        # Atur ukuran dan posisi jendela
        self.setGeometry(0, 0, 300, 300)
        
        # Menambahkan judul ke jendela
        self.setWindowTitle("Belajar PyQt5")
        
        # Pusatkan jendela di layar
        cwa = self.frameGeometry()  
        cwc = QDesktopWidget().availableGeometry().center()  
        cwa.moveCenter(cwc)
        self.move(cwa.topLeft())
        
        # Nonaktifkan resize, tetapi tetap tampilkan tombol minimize dan close
        self.setFixedSize(500, 500)
        
        # Hanya nonaktifkan tombol maximize
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)

# Program Utama
app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
