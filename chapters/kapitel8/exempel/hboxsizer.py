# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 09:44:29 2016

@author: lindemann
"""

import sys

from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    """Main Window class for our application"""

    def __init__(self):
        """Class constructor"""
        super().__init__()

        self.init_gui()

    def init_gui(self):
        """Inititera gränssnitt"""

        self.resize(200,200)
        self.move(50,50)
        self.setWindowTitle('MyWindow')
        
        self.button1 = QPushButton('Button1', self)
        self.button2 = QPushButton('Button2', self)
        self.button3 = QPushButton('Button3', self)
        self.button4 = QPushButton('Button4', self)
        
        self.hbox = QHBoxLayout(self)
        self.hbox.addWidget(self.button1)
        self.hbox.addWidget(self.button2)
        self.hbox.addWidget(self.button3)
        self.hbox.addWidget(self.button4)
        
        self.setLayout(self.hbox)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    window = MyWindow()
    window.show()
    
    sys.exit(app.exec_())
