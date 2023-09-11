from PyQt6.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QHBoxLayout")
        layout = QHBoxLayout()
        layout.addWidget(QPushButton("Left"))
        layout.addWidget(QPushButton("Center"))
        layout.addWidget(QPushButton("Right"))
        self.setLayout(layout)


app = QApplication([])
window = Window()
window.show()
app.exec()
