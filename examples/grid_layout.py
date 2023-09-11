from PyQt6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout")
        layout = QGridLayout()
        layout.addWidget(QPushButton("Button (0, 0)"), 0, 0)
        layout.addWidget(QPushButton("Button (0, 1)"), 0, 1)
        layout.addWidget(QPushButton("Button (1, 0)"), 1, 0)
        layout.addWidget(QPushButton("Button (1, 1)"), 1, 1)
        self.setLayout(layout)


app = QApplication([])
window = Window()
window.show()
app.exec()
