import sys
from symtable import Class

from PyQt6.QtWidgets import QApplication, QDialog

from layout import Ui_Dialog

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.small.toggled.connect(self.check)
        self.ui.normal.toggled.connect(self.check)
        self.ui.big.toggled.connect(self.check)

        self.ui.mushroom.toggled.connect(self.check)
        self.ui.salami.toggled.connect(self.check)
        self.ui.double_2.toggled.connect(self.check)
        self.ui.pineapple.toggled.connect(self.check)

        self.ui.orderButton.clicked.connect(self.check)
        self.show()

    def check(self):
        result = self.ui.result
        extras = ""
        size = "Nie wybrano"
        if self.ui.small.isChecked():
            size = "Mała pizza"
        elif self.ui.normal.isChecked():
            size = "Średnia pizza"
        elif self.ui.big.isChecked():
            size = "Duża pizzuszka"
        else:
            return

        if self.ui.mushroom.isChecked():
            extras += "Pieczarka"
        if self.ui.salami.isChecked():
            extras += "Salami"
        if self.ui.double_2.isChecked():
            extras += "Podwójny syr"
        if self.ui.pineapple.isChecked():
            extras += "Ananas"
        self.ui.result.setText(f"Rozmiar pizzy: {size}, dodatki: {extras}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyDialog()
    sys.exit(app.exec())