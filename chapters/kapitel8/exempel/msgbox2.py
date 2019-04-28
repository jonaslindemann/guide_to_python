# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        """MyWindow konstruktor"""
        super().__init__()

        # Skapa gränssnittskontroller

        self.init_gui()

    def init_gui(self):
        """Initiera gränssnitt"""

        # Sätt fönsteregenskaper

        self.setGeometry(300, 300, 400, 100)
        self.setWindowTitle("MyWidget")

        # Skapa en knappkontroll

        self.button1 = QPushButton("Radera", self)
        self.button1.resize(100,30)
        self.button1.move(20,20)

        # Koppla metod till signalen clicked

        self.button1.clicked.connect(self.on_button1_clicked)

        # Visa fönster

        self.show()

    def on_button1_clicked(self):
        """Händelsemetod för signalen clicked"""

        result = QMessageBox.question(
            self, "Bekräftelse", "Är du säker på att du vill ta bort filen?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if result == QMessageBox.Yes:
            QMessageBox.information(self, "Val", "Du valde Yes")
        else:
            QMessageBox.information(self, "Val", "Du valde No")



if __name__ == "__main__":

    app = QApplication(sys.argv)

    # Skapa vårt MyWindow objekt

    window = MyWindow()

    # Starta händelseloop

    sys.exit(app.exec_())
