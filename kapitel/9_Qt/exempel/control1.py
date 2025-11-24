# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication

class MyWindow(QWidget):
    def __init__(self):
        """MyWindow konstruktor"""
        super().__init__()

        # Skapa gränssnittskontroller

        self.init_gui()

    def init_gui(self):
        """Initiera gränssnitt"""

        # Skapa en knappkontroll

        self.button1 = QPushButton("Press me", self)
        self.button1.resize(100,30)
        self.button1.move(20,20)

        self.button2 = QPushButton("Press me", self)
        self.button2.resize(100,30)
        self.button2.move(20+120,20)

        self.button3 = QPushButton("Press me", self)
        self.button3.resize(100,30)
        self.button3.move(20+120*2,20)

        # Koppla metod till signalen clicked

        self.button1.clicked.connect(self.on_button1_clicked)
        self.button2.clicked.connect(self.on_button2_clicked)

        # Sätt fönsteregenskaper

        self.setGeometry(300, 300, 400, 100)
        self.setWindowTitle("MyWidget")

        # Visa fönster

        self.show()

    def on_button1_clicked(self):
        """Händelsemetod för signalen clicked"""
        if self.button2.isVisible():
            self.button2.setVisible(False)
        else:
            self.button2.setVisible(True)


    def on_button2_clicked(self):
        """Händelsemetod för signalen clicked"""
        if self.button3.isEnabled():
            self.button3.setEnabled(False)
        else:
            self.button3.setEnabled(True)



if __name__ == "__main__":

    app = QApplication(sys.argv)

    # Skapa vårt MyWindow objekt

    window = MyWindow()

    # Starta händelseloop

    sys.exit(app.exec_())
