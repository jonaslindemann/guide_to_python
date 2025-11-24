# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QWidget):
    """Huvudklass för fönstret"""

    def __init__(self):
        """Klass constructor"""
        super().__init__()

        self.init_gui()

    def init_gui(self):
        """Initiera gränssnitt"""

        # Konfigurera fönster

        self.resize(400, 200)
        self.move(50, 50)
        self.setWindowTitle("MyWindow")

        # Skapa knapp

        self.button = QPushButton("Tryck", self)
        self.button.move(230, 18)
        self.button.clicked.connect(self.on_button_clicked)

        # Skapa textetikett

        self.label = QLabel("Textruta", self)
        self.label.move(20, 22)

        # Skapa textkontroll

        self.line_edit = QLineEdit(self)
        self.line_edit.move(80, 20)
        self.line_edit.setText("Text")

        # Skapa label-kontroll med bild.

        self.image_label = QLabel("Bild", self)
        self.image_label.move(20, 60)
        self.image_label.setScaledContents(True)
        self.image_label.resize(300, 100)
        self.image_label.setPixmap(QPixmap("python_logo.png"))

        self.show()

    def on_button_clicked(self):
        """Händelsemetod för signalen clicked"""
        QMessageBox.information(self, "Text", self.line_edit.text())


if __name__ == "__main__":

    app = QApplication(sys.argv)

    # Skapa vårt MyWindow objekt

    window = MyWindow()

    # Starta händelseloop

    sys.exit(app.exec_())
