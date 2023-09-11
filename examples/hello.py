from PyQt6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])

window = QWidget()
window.setWindowTitle("PyQt App")
window.resize(300, 100)
msg = QLabel("<h1>Hello, World!</h1>", parent=window)

window.show()
app.exec()
