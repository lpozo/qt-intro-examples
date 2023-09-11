from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Signals and slots")
        self.resize(300, 70)
        centralWidget = QWidget()
        button = QPushButton("Greet!")

        # Connect the clicked signal to the greet() slot
        button.clicked.connect(self.greet)

        self.msgLabel = QLabel("")
        layout = QVBoxLayout()
        layout.addWidget(self.msgLabel)
        layout.addWidget(button)
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)

    def greet(self):
        if self.msgLabel.text():
            self.msgLabel.setText("")
        else:
            self.msgLabel.setText("Hello, World!")


app = QApplication([])
window = Window()
window.show()
app.exec()
