# -*- coding: utf-8 -*-
"""
Modul för klassen BeamSegmentsWindow

@author: Jonas Lindemann
"""

from qtpy.QtWidgets import QMainWindow, QApplication, QFileDialog, QWidget
from qtpy.QtCore import *
from qtpy import uic

class BeamSegmentsWindow(QWidget):
    """Dialogruta för att redigera segment egenskaper"""

    def __init__(self, beam_model, beam_view):
        """Klasskonstruktor"""

        super().__init__()

        # Tilldelning av klassattribut
                
        self.beam_model = beam_model
        self.beam_view = beam_view

        # Anger aktivt segment

        self.current_segment = 0

        # Flagga för att indikera om någon av
        # kontrollerna har ändrats.

        self.controls_changed = False

        # Läs in gränssnittsdefinition

        uic.loadUi("beam_segments.ui", self)

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

        self.segment_list.currentRowChanged.connect(self.on_current_row_changed)
        self.segment_list.setCurrentRow(self.current_segment)
        self.segment_length_text.textEdited.connect(self.on_edit_text)
        self.segment_load_text.textEdited.connect(self.on_edit_text)
        self.e_text.textEdited.connect(self.on_edit_text)
        self.a_text.textEdited.connect(self.on_edit_text)
        self.i_text.textEdited.connect(self.on_edit_text)
        self.calc_points_spin.valueChanged.connect(self.on_value_changed)
        self.update_button.clicked.connect(self.on_update)

    def update_list(self):
        """Uppdatera listbox med balksegment"""

        self.segment_list.clear()

        for i, item in enumerate(self.beam_model.segments):
            self.segment_list.addItem(str(i+1))

    def update_controls(self):
        """Uppdatera kontroller med värden från balkmodell"""

        self.segment_length_text.setText(str(self.beam_model.lengths[self.current_segment]))
        self.calc_points_spin.setValue(self.beam_model.segments[self.current_segment])
        self.segment_load_text.setText(str(self.beam_model.loads[self.current_segment]))
        self.e_text.setText(str(self.beam_model.properties[self.current_segment][0]))
        self.a_text.setText(str(self.beam_model.properties[self.current_segment][1]))
        self.i_text.setText(str(self.beam_model.properties[self.current_segment][2]))

    def update_model(self):
        """Uppdatera BeamModel med värden från kontroller"""

        if self.controls_changed:

            try:
                self.beam_model.lengths[self.current_segment] = float(self.segment_length_text.text())
                self.beam_model.segments[self.current_segment] = int(self.calc_points_spin.value())
                self.beam_model.loads[self.current_segment] = float(self.segment_load_text.text())
                self.beam_model.properties[self.current_segment][0] = float(self.e_text.text())
                self.beam_model.properties[self.current_segment][1] = float(self.a_text.text())
                self.beam_model.properties[self.current_segment][2] = float(self.i_text.text())
            except ValueError:

                # Om det blev något fel vid konverteringen återställer
                # vi värdena från balkmodellen.

                self.update_controls()

            # Vi utför en beräkning och ritar upp direkt

            self.beam_model.solve()
            self.beam_view.draw()

            # Nu är kontrollerna "rena"

            self.controls_changed = False

    def on_current_row_changed(self, idx):
        """Händelsemetod för att hantera val i listbox"""

        self.update_model()
        self.current_segment = idx
        self.update_controls()

    def on_update(self):
        """Händelsmetod för att hantera klick på Uppdatera knapp"""

        self.update_model()

    def on_edit_text(self):
        """Händelsemetod för att indikera att kontrollen ändrats"""

        self.controls_changed = True

    def on_value_changed(self):
        """Händelsemetod för att hantera att spinkontrolen uppdaterats"""

        self.controls_changed = True

    def closeEvent(self, event):
        """Händelsemetod för att uppdatera modellen innan fönstret stängs"""

        self.update_model()
        event.accept()
