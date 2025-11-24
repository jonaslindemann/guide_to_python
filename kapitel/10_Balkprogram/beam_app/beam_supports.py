# -*- coding: utf-8 -*-
"""
Modul för klassen BeamSupportWindow

@author: Jonas Lindemann
"""

from qtpy.QtWidgets import QMainWindow, QApplication, QFileDialog, QWidget
from qtpy.QtCore import Qt
from qtpy import uic

import beam_model as bm

class BeamSupportWindow(QWidget):
    """Klass för att implementera dialogrutan för upplagsvillkor"""

    def __init__(self, beam_model, beam_view):
        """Klasskonstruktor"""

        super().__init__()

        # Tilldelning av klassattribut
               
        self.beam_model = beam_model
        self.beam_view = beam_view

        # Anger aktivt segment

        self.current_support = 0

        # Flagga för att indikera om någon av
        # kontrollerna har ändrats.

        self.controls_changed = False

        # Läs in gränssnittsdefinition

        uic.loadUi("beam_supports.ui", self)

        # Konfigurera fönstrets egenskaper. I detta
        # fall en dialogruta.

        self.setWindowFlags(
                Qt.Tool |
                Qt.WindowTitleHint |
                Qt.WindowCloseButtonHint 
        )        

        # Uppdatera kontroller från BeamModel

        self.update_list()
        self.update_controls()

        # Koppla händelsemetoder

        self.support_list.currentRowChanged.connect(self.on_current_row_changed)
        self.support_list.setCurrentRow(self.current_support)
        self.update_button.clicked.connect(self.on_update)
        self.xyr_option.clicked.connect(self.on_option_clicked)
        self.xy_option.clicked.connect(self.on_option_clicked)
        self.y_option.clicked.connect(self.on_option_clicked)

    def update_list(self):
        """Uppdatera listbox med lista över stöd"""

        self.support_list.clear()

        for i, item in enumerate(self.beam_model.supports):
            self.support_list.addItem(str(i+1))

    def update_controls(self):
        """Uppdatera kontroller med värden från balkmodell"""

        if self.beam_model.supports[self.current_support] == bm.BeamModel.FIXED_XYR:
            self.xyr_option.setChecked(True)
        elif self.beam_model.supports[self.current_support] == bm.BeamModel.FIXED_XY:
            self.xy_option.setChecked(True)
        else:
            self.y_option.setChecked(True)

    def update_model(self):
        """Uppdatera modellen med värden från kontroller"""

        if self.controls_changed:

            if self.xyr_option.isChecked():
                self.beam_model.supports[self.current_support] = bm.BeamModel.FIXED_XYR
            elif self.xy_option.isChecked():
                self.beam_model.supports[self.current_support] = bm.BeamModel.FIXED_XY
            else:
                self.beam_model.supports[self.current_support] = bm.BeamModel.FIXED_Y

            # Vi utför en beräkning och ritar upp direkt

            self.beam_model.solve()
            self.beam_view.draw()

            # Nu är kontrollerna "rena"

            self.controls_changed = False

    def on_current_row_changed(self, idx):
        """Händelsemetod för att hantera val i listbox"""

        self.update_model()
        self.current_support = idx
        self.update_controls()

    def on_option_clicked(self):
        """Händelsemetod för att hantera val av alternativ"""

        self.controls_changed = True

    def on_update(self):
        """Händelsemetod för att hantera klick på Uppdatera knapp"""

        self.update_model()

    def closeEvent(self, event):
        """Händelsemetod för att uppdatera modellen innan fönstret stängs"""

        self.update_model()
        event.accept()
