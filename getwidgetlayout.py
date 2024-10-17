from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")  # Set title for the window
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout()

        btn1 = QPushButton("button 1")
        btn2 = QPushButton("button 2")
        btn3 = QPushButton("button 3")
        btn4 = QPushButton("button 4")

        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        
        self.setLayout(layout)

app = QApplication([])
Window = MyWindow()
Window.show()
app.exec()