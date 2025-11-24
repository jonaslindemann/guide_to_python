# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 23:42:08 2018

@author: Jonas Lindemann
"""

import sys, os


from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic


from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

import matplotlib.pyplot as plt

# Importera alla numpy funktioner direkt i namnrymden för att undvika
# att användaren måste ange np framför alla funktioner.

from numpy import *

class GraphPlotWindow(QMainWindow):
    """Main window class for the Flow application"""

    def __init__(self):
        """Class constructor"""
        super().__init__()

        # Load and show our user interface

        uic.loadUi("graph_plot.ui", self)

        # Define some class attributes

        self.filename = ""
        self.x_start = -6.3
        self.x_end = 6.3
        self.steps = 600
        self.expression = "sin(x)"

        # Create a figure and a canvas for drawing plots

        self.figure = plt.figure(dpi=150)
        self.canvas = FigureCanvas(self.figure)

        # Create a matplotlib toolbar

        self.figure_toolbar = NavigationToolbar(self.canvas, self)

        self.main_widget.layout().addWidget(self.canvas)
        self.main_widget.layout().addWidget(self.figure_toolbar)

        # Update controls to reflect our properties

        self.update_controls()

        # Connect events to methods

        self.exit_action.triggered.connect(self.on_exit)
        self.plot_button.clicked.connect(self.on_plot)
        self.expression_edit.returnPressed.connect(self.on_plot)
        self.x_start_edit.returnPressed.connect(self.on_plot)
        self.x_end_edit.returnPressed.connect(self.on_plot)
        self.step_edit.returnPressed.connect(self.on_plot)

        # Update our plot

        self.update_plot()

    def get_input_values(self):
        """Get class properties from controls"""
        self.x_start = float(self.x_start_edit.text())
        self.x_end = float(self.x_end_edit.text())
        self.steps = int(self.step_edit.text())
        self.expression = self.expression_edit.text()

    def update_controls(self):
        """Update controls from class properties"""
        self.x_start_edit.setText(str(self.x_start))
        self.x_end_edit.setText(str(self.x_end))
        self.step_edit.setText(str(self.steps))
        self.expression_edit.setText(self.expression)

    def update_plot(self):
        """Method for evaluating and plotting"""

        # Reset error flag

        eval_error = False

        # Get plot parameters from controls

        self.get_input_values()

        # Define our plot range

        x = linspace(self.x_start, self.x_end, self.steps)

        # Evaluate our plot expression

        try:
            y = eval(self.expression, globals(), locals())
        except Exception as e:
            QMessageBox.information(self, "Fel", str(e))
            eval_error = True

        # Clear figure

        self.figure.clear()

        # Only plot if there was no evaluation error

        if not eval_error:
            axes = self.figure.gca()
            axes.plot(x, y)

        # Make sure our canvas is redrawn (really)

        self.figure.canvas.draw()
        self.figure.canvas.flush_events()
        self.figure.canvas.update()

    def on_plot(self):
        """Event method for plotting"""
        self.update_plot()

    def on_exit(self):
        """Event method for exiting application"""
        self.close()


if __name__ == '__main__':
    #os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1.5"
    #os.environ["QT_SCALE_FACTOR"] = "1.5"

    font = QFont()
    font.setPointSize(10)

    application = QApplication(sys.argv)
    application.setFont(font)

    window = GraphPlotWindow()
    window.show()

    sys.exit(application.exec_())
