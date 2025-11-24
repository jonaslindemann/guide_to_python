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

        self.init_gui()

    def init_gui(self):
        """Initiera gränssnitt"""
        
        self.resize(200,200)
        self.move(50,50)
        self.setWindowTitle("MyWindow")
        
        # Define action
        
        self.my_action = QAction("MyAction", self.ui)
        self.my_action.setShortcut("Ctrl-T")
        self.my_action.triggered.connect(self.on_my_action)
        
        # Connect action to menu

        self.file_menu = self.ui.menuBar().addMenu("File")
        self.file_menu.addAction(self.my_action)
        
        # Create a toolbar
        
        self.toolbar = self.ui.addToolBar("MyToolbar")
        self.toolbar.addAction(self.my_action)
        
    def on_my_action(self):
        """Method for handling MyAction"""
        QMessageBox.information(self, "Meddelande", "Ouch!")
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    window = MyWindow()
    window.show()
    
    sys.exit(app.exec_())
