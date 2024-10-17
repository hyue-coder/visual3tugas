from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Membuat label
        self.label = QLabel(self)
        self.label.setText("Label1")
        self.label.move(200, 0)  # Posisi label (200, 0)
        
        # Membuat tombol
        self.button = QPushButton(self)
        self.button.setText("Button1")
        
        # Mengatur ukuran dan posisi jendela
        self.setGeometry(0, 0, 400, 400)  # (x, y, width, height)
        
        # Mengatur judul jendela
        self.setWindowTitle("Belajar PyQt5")

app = QApplication([])

window = MyWindow()
window.show()

app.exec_()
