# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 09:44:29 2016

@author: lindemann
"""

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyWindow(QWidget):
    """Huvudklass för vårt fönster"""

    def __init__(self):
        """Klass konstructor"""
        super().__init__()

        self.init_gui()

    def init_gui(self):
        """Skapa gränssnitt"""

        # Konfigurera fönster

        self.resize(300, 150)
        self.move(50, 50)
        self.setWindowTitle("MyWindow")

        # Skapa kontroller

        self.vert_slider = QSlider(Qt.Vertical, self)
        self.vert_slider.move(20, 20)
        self.vert_slider.setMaximum(100)
        self.vert_slider.setMinimum(0)
        self.vert_slider.setValue(50)

        self.horiz_slider = QSlider(Qt.Horizontal, self)
        self.horiz_slider.move(50, 20)
        self.horiz_slider.setMaximum(100)
        self.horiz_slider.setMinimum(0)
        self.horiz_slider.setValue(50)

        # Koppla signaler

        self.vert_slider.valueChanged.connect(self.on_value_changed)
        self.horiz_slider.valueChanged.connect(self.on_value_changed)

    def on_value_changed(self, value):
        """Hantera signalen valueChanged"""
        print("vertical value   =", self.vert_slider.value())
        print("horizontal value =", self.horiz_slider.value())


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    window = MyWindow()
    window.show()
    
    sys.exit(app.exec_())
