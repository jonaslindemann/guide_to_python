#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 17:10:06 2017

@author: lindemann
"""

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from random import *

class MainWindow(QMainWindow):
    """Main window class for the Flow application"""

    def __init__(self):
        """Class constructor"""
        super().__init__()

        # Load and show our user interface
        
        uic.loadUi("graphicsview1.ui", self)
        
        self.scene = QGraphicsScene(self.graphicsView)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setInteractive(True)
        self.graphicsView.setRenderHint(QPainter.Antialiasing)  
                
        for i in range(100):
            line = self.scene.addLine(
                    uniform(-1000.0, 1000.0),
                    uniform(-1000.0, 1000.0),
                    uniform(-1000.0, 1000.0),
                    uniform(-1000.0, 1000.0),
                    QPen(Qt.red)
                    )

        self.graphicsView.show()

        self.resize(800, 800)

    def showEvent(self, event):
        self.graphicsView.fitInView(self.scene.sceneRect())
        self.graphicsView.centerOn(0,0)

    def resizeEvent(self, event):
        print("resize")
        self.graphicsView.fitInView(self.scene.sceneRect())
        self.graphicsView.centerOn(0,0)


                    


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())
