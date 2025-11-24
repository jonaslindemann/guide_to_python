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
        """MyWidget constructor"""
        super().__init__()

        self.init_gui()

    def init_gui(self):
        """Initiera gränssnitt"""

        self.resize(200,200)
        self.move(50,50)
        self.setWindowTitle("MyWindow")
        
        self.button1 = QPushButton("Button1")
        self.button2 = QPushButton("Button2")
        self.button3 = QPushButton("Button3")
        self.button4 = QPushButton("Button4")
        self.button5 = QPushButton("Button5")
        self.button6 = QPushButton("Button6")
        self.button7 = QPushButton("Button7")
        self.button8 = QPushButton("Button8")
        self.button9 = QPushButton("Button9")

        self.button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.grid = QGridLayout(self)
        self.grid.addWidget(self.button1, 0, 0)
        self.grid.addWidget(self.button2, 0, 1)
        self.grid.addWidget(self.button3, 0, 2)
        self.grid.addWidget(self.button4, 1, 0)
        self.grid.addWidget(self.button5, 1, 1)
        self.grid.addWidget(self.button6, 1, 2)
        self.grid.addWidget(self.button7, 2, 0)
        self.grid.addWidget(self.button8, 2, 1)
        self.grid.addWidget(self.button9, 2, 2)

        self.grid.setContentsMargins(20, 40, 20, 40)

        self.grid.setHorizontalSpacing(20)
        self.grid.setVerticalSpacing(20)

        self.grid.setColumnStretch(0, 1)
        self.grid.setColumnStretch(1, 4)
        self.grid.setColumnStretch(2, 1)

        self.grid.setRowStretch(0, 1)
        self.grid.setRowStretch(1, 4)
        self.grid.setRowStretch(2, 1)

        self.setLayout(self.grid)
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    window = MyWindow()
    window.show()
    
    sys.exit(app.exec_())
