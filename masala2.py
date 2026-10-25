import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QLabel)
from PyQt5.QtCore import Qt


class Oyna(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("2-masala")

        self.label = QLabel("Tugmani bosing")
        self.label.setAlignment(Qt.AlignCenter)

        chap = QPushButton("Chapga")
        orta = QPushButton("O'rtaga")
        ong = QPushButton("O'ngga")

        chap.clicked.connect(lambda: self.label.setText("Chapga"))
        orta.clicked.connect(lambda: self.label.setText("O'rtaga"))
        ong.clicked.connect(lambda: self.label.setText("O'ngga"))

        h = QHBoxLayout()
        h.addWidget(chap)
        h.addWidget(orta)
        h.addWidget(ong)

        v = QVBoxLayout()
        v.addWidget(self.label)
        v.addLayout(h)
        self.setLayout(v)


app = QApplication(sys.argv)
oyna = Oyna()
oyna.show()
sys.exit(app.exec_())
