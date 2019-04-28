# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic

class MainWindow(QWidget):
    """Main window class for the Flow application"""

    def __init__(self):
        """Class constructor"""

        super().__init__()

        # Load and show our user interface

        self.init_gui()

    def init_gui(self):
        """Initialisera gränssnitt"""

        uic.loadUi("form.ui", self)

        self.push_button.setText("Press me!")


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
