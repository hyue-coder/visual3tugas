from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QHBoxLayout

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")  
        self.setGeometry(100, 100, 300, 200)
        layout = QHBoxLayout()

        btn1 = QPushButton("button 1")
        btn2 = QPushButton("button 2")
        btn3 = QPushButton("button 3")
        btn4 = QPushButton("button 4")

        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication([])
Window = MyWindow()
Window.show()
app.exec()