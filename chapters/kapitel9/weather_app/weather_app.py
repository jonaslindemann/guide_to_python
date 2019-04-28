# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 23:42:08 2018

@author: Jonas Lindemann
"""

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QStyle, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from PyQt5 import uic

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import matplotlib.pyplot as plt
import numpy as np

import smhi

class WeatherWindow(QMainWindow):
    """Main window class for the Flow application"""

    def __init__(self):
        """Class constructor"""
        super().__init__()

        # Load and show our user interface

        uic.loadUi("weather_app.ui", self)

        # Define some class attributes
        
        self.smhi = smhi.SMHI()        
        
        self.current_param = "t"
        
        # Create a figure and a canvas for drawing in

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)      
        self.figure_toolbar = NavigationToolbar(self.canvas, self)
        
        self.main_widget.layout().addWidget(self.canvas)
        self.canvas.setSizePolicy(QSizePolicy.Expanding , QSizePolicy.Expanding)
        self.main_widget.layout().addWidget(self.figure_toolbar)
        
        self.param_combo.currentTextChanged.connect(self.on_text_changed)
        self.refresh_button.clicked.connect(self.on_refresh)
        
        self.request_forecast()
        self.update_controls()
        self.plot()
               
    def update_controls(self):
        self.param_combo.clear()
        for name in self.params.keys():
            self.param_combo.addItem(name)
            
        print(self.smhi.longitude)
            
        self.lon_edit.setText(str(self.smhi.longitude))
        self.lat_edit.setText(str(self.smhi.latitude))
        
    def update_model(self):
        self.smhi.latitude = self.lat_edit.text()
        self.smhi.longitude = self.lon_edit.text()
        self.current_param = self.param_combo.text()        
        
    def request_forecast(self):
        self.params = self.smhi.extract_param_names()
        self.values = self.smhi.extract_param(self.current_param)
        
    def plot(self):
        
        self.figure.clear()
        axes = self.figure.gca()

        axes.plot_date(self.values[:, 0], self.values[:, 1], xdate=True, fmt="r-")
        plt.title(self.current_param+" ("+self.params[self.current_param]+")")

        self.figure.canvas.draw()
        self.figure.canvas.flush_events()                
        
    def refresh(self):
        self.update_model()
        self.request_forecast()
        self.plot()
        
    def on_refresh(self):
        self.refresh()
        
    def on_text_changed(self, text):
        self.current_param = text
        self.refresh()
                        
if __name__ == '__main__':

    application = QApplication(sys.argv)

    window = WeatherWindow()
    window.show()

    sys.exit(application.exec_())
