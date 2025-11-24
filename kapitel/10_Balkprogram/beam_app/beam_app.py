# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 23:42:08 2018

@author: Jonas Lindemann
"""

import sys

from qtpy.QtWidgets import QMainWindow, QApplication, QFileDialog, QStyle
from qtpy.QtGui import QIcon
from qtpy.QtCore import *
from qtpy import uic

# Matplotlib

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import beam_model as bm
import beam_view as bv
import beam_segments as bs
import beam_supports as bspt
import beam_res 

class BeamWindow(QMainWindow):
    """Fönsterklass för balkprogrammet"""

    def __init__(self):
        """BeamWindow konstruktor"""

        super().__init__()

        # Läs in gränssnitt från fil

        uic.loadUi("beam_app.ui", self)

        # Klassattribut

        self.filename = ""

        self.support_window = None
        self.segments_window = None
        
        # Skapa och initiera balk modell

        self.new_model()

        # Skapa en figur som vi kan använda för att rita på

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)      
        self.main_layout.addWidget(self.canvas)

        # Lägg till Matplotlibs verktygsfält

        self.figure_toolbar = NavigationToolbar(self.canvas, self)
        self.main_layout.addWidget(self.figure_toolbar)

        # Skapa en BeamView instans som vi kopplar till BeamModel och
        # Aktuell figur.

        self.beam_view = bv.BeamView(self.beam_model, self.figure)
        self.beam_view.draw()
                
        # Koppla händelser till metoder

        self.exit_action.triggered.connect(self.on_exit)
        self.new_action.triggered.connect(self.on_new)
        self.open_action.triggered.connect(self.on_open)
        self.save_action.triggered.connect(self.on_save)
        self.save_as_action.triggered.connect(self.on_save_as)
        self.segments_action.triggered.connect(self.on_segments)
        self.bc_action.triggered.connect(self.on_bc)
        
    def new_model(self):
        """Create a new model"""

        # Variabler som används för att skapa
        # vår modell

        E = 2.1e9
        A = 0.1 * 0.1
        I = 0.1 * (0.1 ** 3) / 12

        # Skapa en instans av BeamModel med
        # standardvärden.

        self.beam_model = bm.BeamModel()
        self.beam_model.lengths = [2.0, 2.0, 3.0]
        self.beam_model.segments = [100, 100, 100]
        self.beam_model.supports = [bm.BeamModel.FIXED_XY,
                                    bm.BeamModel.FIXED_Y,
                                    bm.BeamModel.FIXED_Y,
                                    bm.BeamModel.FIXED_XYR]
        self.beam_model.loads = [-1.0e3, -1.0e3, -0.5e3]
        self.beam_model.properties = [[E, A, I], [E, A, I], [E, A, I]]
        self.beam_model.solve()

    def on_new(self):
        """Händelsemetod för att skapa en ny modell"""

        self.new_model()
        self.beam_view.draw()

    def on_exit(self):
        """Händelsemetod för att avsluta programmet"""
        self.close()

    def on_open(self):
        """Händelsemetod för att öppna en modell"""

        self.filename, _ = QFileDialog.getOpenFileName(self,
                                                       "Öppna modell", "",
                                                       "Modell filer (*.json *.jpg *.bmp)")

        if self.filename != "":
            self.beam_model.new()
            self.beam_model.open_from_json(self.filename)
            self.beam_model.solve()
            self.beam_view.draw()

    def on_save(self):
        """Händelsemetod för spara modellfil"""

        if self.filename == "":
            self.filename, _ = QFileDialog.getSaveFileName(self,
                                                           "Spara modell", "",
                                                           "Modell filer (*.json)")

        if self.filename != "":
            self.beam_model.save_as_json(self.filename)

    def on_save_as(self):
        """Händelsemetod för att spara som ..."""

        temp_filename, _ = QFileDialog.getSaveFileName(self,
                                                       "Spara modell", "",
                                                       "Modell filer (*.json)")

        if temp_filename != "":
            self.filename = temp_filename
            self.beam_model.save_as_json(self.filename)

    def on_segments(self):
        """Händelsemetod för att visa balksegmentsdialogrutan"""

        self.segments_window = bs.BeamSegmentsWindow(self.beam_model, self.beam_view)
        self.segments_window.show()

    def on_bc(self):
        """Händelsemetod för att visa upplagsdialogrutan"""

        self.support_window = bspt.BeamSupportWindow(self.beam_model, self.beam_view)
        self.support_window.show()


if __name__ == '__main__':

    #QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True) 
    #QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)         

    application = QApplication(sys.argv)

    window = BeamWindow()
    window.show()

    sys.exit(application.exec_())
