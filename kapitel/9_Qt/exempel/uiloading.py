# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic

class MainWindow:
    """Main window class for the Flow application"""

    def __init__(self, app):
        """Class constructor"""

        # Assign our application instance as a member variable
        
        self.app = app
                
        # Load and show our user interface
        
        self.ui = uic.loadUi('mainwindow.ui')
        
        self.ui.actionFileOpen.triggered.connect(self.onFileOpen)
        self.ui.addButton.clicked.connect(self.onAddButtonClicked)
        self.ui.nodeList.currentRowChanged.connect(self.onCurrentRowChanged)
        self.ui.addTextButton.clicked.connect(self.onAddTextButtonClicked)                
        self.ui.myButton.clicked.connect(self.onMyButtonClicked)
        
        self.ui.show()
        self.ui.raise_()
        
    def onMyButtonClicked(self, event):
        print("onMyButtonClicked")        
        
    def onFileOpen(self, event):
        print("onFileOpen")
        
    def onAddButtonClicked(self, event):
        print("onAddButtonClicked")
        self.ui.nodeList.addItem("Hej hopp!")
        
    def onCurrentRowChanged(self, event):
        print("onCurrentRowChanged")
        self.ui.nodeList.addItem("test")
        
    def onAddTextButtonClicked(self, event):
        print("onAddTextButtonClicked")
        self.ui.nodeList.addItem(self.ui.lineEdit.text())
                                     

if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MainWindow(app)
    
    sys.exit(app.exec_())
