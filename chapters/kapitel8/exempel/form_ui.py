# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import *

from form_window import *

class MainWindow(QWidget):
    """Main window class for the Flow application"""

    def __init__(self):
        """Class constructor"""

        super().__init__()

        self.setup_ui()

    def setup_ui(self):
        """Initiera gränssnitt"""

        # Instantiera en referens till den av pyuic5 skapade
        # klassen.

        self.ui = Ui_MainWindow()

        # Skapa objektstrukturen.

        self.ui.setupUi(self)

        # Uppdatera gränssnit. Notere att vi måste använda
        # self.ui som prefix.

        self.ui.push_button.setText("Press me!")



if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
