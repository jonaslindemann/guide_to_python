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

        self.button1 = QPushButton("Information", self)
        self.button1.resize(100,30)
        self.button1.move(20,20)

        self.button2 = QPushButton("Varning", self)
        self.button2.resize(100,30)
        self.button2.move(20+120,20)

        self.button3 = QPushButton("Fel", self)
        self.button3.resize(100,30)
        self.button3.move(20+120*2,20)

        # Koppla metod till signalen clicked

        self.button1.clicked.connect(self.on_button1_clicked)
        self.button2.clicked.connect(self.on_button2_clicked)
        self.button3.clicked.connect(self.on_button3_clicked)

        # Visa fönster

        self.show()

    def on_button1_clicked(self):
        """Händelsemetod för signalen clicked"""
        QMessageBox.information(self, "Information", "Detta är ett informellt meddelande")

    def on_button2_clicked(self):
        """Händelsemetod för signalen clicked"""
        QMessageBox.warning(self, "Varning", "Detta är en varning!")

    def on_button3_clicked(self):
        """Händelsemetod för signalen clicked"""
        QMessageBox.critical(self, "Fel", "Detta är allvarligt!")


if __name__ == "__main__":

    app = QApplication(sys.argv)

    # Skapa vårt MyWindow objekt

    window = MyWindow()

    # Starta händelseloop

    sys.exit(app.exec_())
