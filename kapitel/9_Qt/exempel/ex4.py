# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        """MyWidget constructor"""
        super().__init__()

        self.init_gui()

    def init_gui(self):
        """Initialise UI"""

        self.button = QPushButton("Press me", self)
        self.button.setToolTip("I am a button. Please press me")
        self.button.resize(self.button.sizeHint())
        self.button.move(50,50)

        self.button.clicked.connect(self.on_button_clicked)

        self.line_edit = QLineEdit(self)
        self.line_edit.move(50,20)
        self.line_edit.setText("Text")

        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle("MyWidget")

        self.show()

    def on_button_clicked(self):
        """Event method for button clicked"""
        QMessageBox.information(self, "Text", self.line_edit.text())

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
