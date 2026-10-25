import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


class Oyna(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("1-masala")
        layout = QVBoxLayout()

        for nom in ["Tugma 1", "Tugma 2", "Tugma 3"]:
            tugma = QPushButton(nom)
            tugma.clicked.connect(lambda checked, n=nom: print(n))
            layout.addWidget(tugma)

        self.setLayout(layout)


app = QApplication(sys.argv)
oyna = Oyna()
oyna.show()
sys.exit(app.exec_())
