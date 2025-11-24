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

        self.resize(200, 200)
        self.move(50, 50)
        self.setWindowTitle("MyWindow")

        # Define action

        self.action_dialog = QAction("Open dialog", self)
        self.action_dialog.setShortcut("Ctrl-T")
        self.action_dialog.triggered.connect(self.on_dialog)

        # Connect action to menu

        self.file_menu = self.menuBar().addMenu("File")
        self.file_menu.addAction(self.action_dialog)

    def on_dialog(self):
        """Method for handling MyAction"""
        QMessageBox.critical(self, "Meddelande", "Ouch!")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
