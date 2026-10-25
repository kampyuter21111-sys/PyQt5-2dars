import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel


class Oyna(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3-masala")

        self.combo = QComboBox()
        self.combo.addItems(["Python", "C++", "Java"])
        self.label = QLabel("Tanlangan til: Python")

        self.combo.currentTextChanged.connect(
            lambda matn: self.label.setText("Tanlangan til: " + matn)
        )

        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(self.label)
        self.setLayout(layout)


app = QApplication(sys.argv)
oyna = Oyna()
oyna.show()
sys.exit(app.exec_())
