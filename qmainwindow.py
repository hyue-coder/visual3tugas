from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow

app = QApplication([])

window = QMainWindow()

# Membuat label di dalam jendela
label = QLabel(window)  # Label di dalam window
label.setText("Label1")  # Mengatur teks label menjadi "Label1"
label.move(200, 0)  

button = QPushButton(window)  
button.setText("Button1")  
window.show()


app.exec_()

