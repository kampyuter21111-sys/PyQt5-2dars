import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLineEdit, QPushButton, QComboBox)


class Oyna(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("4-masala")

        self.edit = QLineEdit()
        self.edit.setPlaceholderText("So'z kiriting...")
        self.tugma = QPushButton("Qo'shish")
        self.combo = QComboBox()

        self.tugma.clicked.connect(self.qosh)
        self.edit.returnPressed.connect(self.qosh)

        h = QHBoxLayout()
        h.addWidget(self.edit)
        h.addWidget(self.tugma)

        v = QVBoxLayout()
        v.addLayout(h)
        v.addWidget(self.combo)
        self.setLayout(v)

    def qosh(self):
        soz = self.edit.text().strip()
        if soz:
            self.combo.addItem(soz)
            self.edit.clear()


app = QApplication(sys.argv)
oyna = Oyna()
oyna.show()
sys.exit(app.exec_())
