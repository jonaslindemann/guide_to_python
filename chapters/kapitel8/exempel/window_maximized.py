# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 09:44:29 2016

@author: lindemann
"""

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QMainWindow):
    """Main Window class for our application"""

    def __init__(self):
        """Class constructor"""
        super().__init__()
        
        self.resize(200,100)
        self.move(50,50)
        self.setWindowTitle("MyWindow")
        self.setWindowState(Qt.WindowMaximized)
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    window = MyWindow()
    window.show()
    
    sys.exit(app.exec_())
