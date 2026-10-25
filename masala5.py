import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QLabel

MAHSULOTLAR = [("Olma", 5000), ("Banan", 7000), ("Uzum", 8000)]


class Oyna(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("5-masala")
        layout = QVBoxLayout()

        self.checkboxlar = []
        for nom, narx in MAHSULOTLAR:
            cb = QCheckBox(f"{nom} - {narx} so'm")
            cb.stateChanged.connect(self.hisobla)
            layout.addWidget(cb)
            self.checkboxlar.append((cb, narx))

        self.label = QLabel("Umumiy narx: 0 so'm")
        layout.addWidget(self.label)
        self.setLayout(layout)

    def hisobla(self):
        jami = sum(narx for cb, narx in self.checkboxlar if cb.isChecked())
        self.label.setText(f"Umumiy narx: {jami} so'm")


app = QApplication(sys.argv)
oyna = Oyna()
oyna.show()
sys.exit(app.exec_())
