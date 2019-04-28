# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 09:44:29 2016

@author: lindemann
"""

import sys

from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    """Main Window class for our application"""

    def __init__(self):
        """Class constructor"""
        super().__init__()

        self.init_gui()

    def init_gui(self):
        """Initiera gränssnitt"""

        # Sätt fönsteregenskaper

        self.setGeometry(300, 300, 400, 100)
        self.setWindowTitle("MyWidget")

        # Skapa en knappkontroll

        self.button1 = QPushButton("Öppna fil", self)
        self.button1.resize(100,30)
        self.button1.move(20,20)

        self.button2 = QPushButton("Spara fil", self)
        self.button2.resize(100,30)
        self.button2.move(20+120,20)

        # Koppla metod till signalen clicked

        self.button1.clicked.connect(self.on_button1_clicked)
        self.button2.clicked.connect(self.on_button2_clicked)

        # Visa fönster

        self.show()

    def on_button1_clicked(self):
        """Händelsemetod för signalen clicked"""
        filename, _ = QFileDialog.getOpenFileName(
            self, 'Open file', '', 'Input files (*.*)')

        if filename != "":
            QMessageBox.information(self, "Val", filename)

    def on_button2_clicked(self):
        """Händelsemetod för signalen clicked"""
        filename, _ = QFileDialog.getSaveFileName(
            self, 'Save file', '', 'Input files (*.inp)')

        if filename != "":
            QMessageBox.information(self, "Val", filename)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
