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
        """Initiera gränssnitt"""

        # Konfigurera fönster
        
        self.resize(400,200)
        self.move(50,50)
        self.setWindowTitle("MyWindow")

        # Skapa knapp
        
        self.button = QPushButton("Tryck", self)
        self.button.move(50,50)
        self.button.resize(100,50)
        self.button.clicked.connect(self.on_button_clicked)

        # Skapa textkontroll

        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(20,20)
        self.lineEdit.setText("Text")
        
    def on_button_clicked(self):
        """Händelsemetod för signalen clicked"""
        QMessageBox.information(self, "Text", self.lineEdit.text())
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    window = MyWindow()
    window.show()
    
    sys.exit(app.exec_())
