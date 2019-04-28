# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 09:44:29 2016

@author: lindemann
"""

import sys

from PyQt5.QtWidgets import QWidget, QListWidget, QMessageBox, QApplication

class MyWindow(QWidget):
    """Main Window class for our application"""

    def __init__(self):
        """Class konstruktor"""
        super().__init__()

        self.init_gui()

    def init_gui(self):
        """Skapa gränssnitt"""

        # Sätt fönsteregenskaper

        self.resize(400,200)
        self.move(50,50)
        self.setWindowTitle("MyWindow")

        # Skapa listkontroll

        self.list_box = QListWidget(self)
        self.list_box.move(20,20)
        self.list_box.resize(100,100)

        # Lägg till alternativ i listan

        for i in range(100):
            self.list_box.addItem("Alternativ %d" % i)

        # Sätt standardalternativet till rad 2

        self.list_box.setCurrentRow(2)

        # Koppla en händelsemetod till signal

        self.list_box.currentRowChanged.connect(self.on_current_row_changed)

    def on_current_row_changed(self, curr):
        """Hantera signalen currentRowChanged"""
        QMessageBox.information(self, "Meddelande", "Du valde: " + str(curr))
        QMessageBox.information(self, "Meddelande", "Raden innehöll: " + self.list_box.currentItem().text())


if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
