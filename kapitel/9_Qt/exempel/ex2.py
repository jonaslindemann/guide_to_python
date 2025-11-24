# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication, QWidget

class MyWindow(QWidget):
    def __init__(self):
        """MyWindow constructor"""

        super().__init__()

        # Skapa gränssnittskontroller

        self.init_gui()

    def init_gui(self):
        """Initiera gränssnitt"""

        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle("MyWindow")

        # Visa fönster

        self.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)

    # Skapa vårt MyWindow objekt

    window = MyWindow()

    # Starta händelseloop

    sys.exit(app.exec_())
