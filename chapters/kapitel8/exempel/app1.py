# -*- coding: utf-8 -*-
"""
QCheckBox Example
Created on Mon Apr 11 09:44:29 2016

@author: Jonas Lindemann
"""

import sys

from math import *

from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    """Main Window class for our application"""

    def __init__(self):
        """Class constructor"""
        super().__init__()

        # Size and position window

        self.resize(400, 200)
        self.move(50, 50)
        self.setWindowTitle("Symbolic calculator")

        # Setup controls

        self.expression_edit = QLineEdit()
        self.result_edit = QLineEdit()

        self.v_box = QVBoxLayout(self)
        self.v_box.addWidget(self.expression_edit)
        self.v_box.addWidget(self.result_edit)
        self.v_box.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.calc_button = QPushButton("Evaluate")
        self.close_button = QPushButton("Close")

        self.h_box = QHBoxLayout(self)
        self.h_box.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))
        self.h_box.addWidget(self.calc_button)
        self.h_box.addWidget(self.close_button)
        self.h_box.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)

        # Connect signals to event methods

        self.calc_button.clicked.connect(self.on_calc_button_clicked)
        self.close_button.clicked.connect(self.on_close_button_clicked)

    def on_calc_button_clicked(self):
        """Calc button event method"""

        expression = self.expression_edit.text()
        result = eval(expression)
        self.result_edit.setText(str(result))

    def on_close_button_clicked(self):
        """Close button event method"""

        self.close()


if __name__ == '__main__':
    """Application main program"""

    # Instantiate application object

    app = QApplication(sys.argv)

    # Create window

    window = MyWindow()
    window.show()

    # Application event loop

    sys.exit(app.exec_())
