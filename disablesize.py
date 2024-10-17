# =========== Window Management ==============
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel, QDesktopWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Membuat label
        self.label = QLabel(self)
        self.label.setText("Label1")
        self.label.move(200, 0)
        
        # Membuat tombol
        self.button = QPushButton(self)
        self.button.setText("Button1")
        
        # Mengatur ukuran jendela
        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Belajar PyQt5")
        
        # Memindahkan jendela ke tengah layar
        cwa = self.frameGeometry()  # Mendapatkan geometri (ukuran dan posisi) frame jendela
        cwc = QDesktopWidget().availableGeometry().center()  # Mendapatkan posisi tengah dari layar yang tersedia
        cwa.moveCenter(cwc)  # Memindahkan jendela ke tengah layar
        self.move(cwa.topLeft())  # Memindahkan jendela ke koordinat kiri atas dari posisi tengah layar
        self.setFixedSize(500,500)

# Mengecek apakah script dijalankan langsung
if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
