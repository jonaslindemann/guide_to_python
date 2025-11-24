# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 09:44:29 2016

@author: lindemann
"""

import sys

from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    """Huvudklass för vårt fönster"""

    def __init__(self):
        """Klass constructor"""
        super().__init__()

        self.init_gui()

    def init_gui(self):

        # Konfigurera fönster

        self.resize(400, 200)
        self.move(50, 50)
        self.setWindowTitle("MyWindow")

        # Skapa combobox-kontroll

        self.combo_box = QComboBox(self)
        self.combo_box.move(20, 20)

        # Lägg till alternativ

        self.combo_box.addItem("Alternativ 1")
        self.combo_box.addItem("Alternativ 2")
        self.combo_box.addItem("Alternativ 3")
        self.combo_box.addItem("Alternativ 4")

        # Ange standardval

        self.combo_box.setCurrentIndex(3)

        # Koppla händelsemetod till signal

        self.combo_box.currentIndexChanged.connect(self.on_current_index_changed)

    def on_current_index_changed(self, index):
        """Hantera signalen currentIndexChanged"""

        QMessageBox.information(self, "Meddelande", "Du valde: " + str(index))
        QMessageBox.information(self, "Meddelande", "Texten var: " + self.combo_box.currentText())
        

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    window = MyWindow()
    window.show()
    
    sys.exit(app.exec_())