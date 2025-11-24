# -*- coding: utf-8 -*-
"""
QCheckBox Example
Created on Mon Apr 11 09:44:29 2016

@author: Jonas Lindemann
"""

import sys

from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    """Main Window class for our application"""

    def __init__(self):
        """Class constructor"""
        super().__init__()

        self.resize(400,100)
        self.move(50,50)
        self.setWindowTitle("MyWindow")

        self.check_box = QCheckBox("Extra allt", self)
        self.check_box.move(20,20)
        self.check_box.setChecked(True)
        self.check_box.stateChanged.connect(self.on_state_change)


    def on_state_change(self):
        """Respond to button click"""
        if self.check_box.checkState():
            QMessageBox.information(self, "Meddelande", "Extra allt")
        else:
            QMessageBox.information(self, "Meddelande", "Inget")

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    window = MyWindow()
    window.show()
    
    sys.exit(app.exec_())