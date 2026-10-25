import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton


class Oyna(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("6-masala")
        self.resize(300, 200)

        layout = QVBoxLayout()
        ranglar = [("Qizil", "red"), ("Yashil", "green"), ("Ko'k", "blue")]

        for nom, rang in ranglar:
            rb = QRadioButton(nom)
            rb.toggled.connect(lambda tanlandi, r=rang: self.rang_ber(tanlandi, r))
            layout.addWidget(rb)

        self.setLayout(layout)

    def rang_ber(self, tanlandi, rang):
        if tanlandi:
            self.setStyleSheet(f"QWidget {{ background-color: {rang}; }}")


app = QApplication(sys.argv)
oyna = Oyna()
oyna.show()
sys.exit(app.exec_())
