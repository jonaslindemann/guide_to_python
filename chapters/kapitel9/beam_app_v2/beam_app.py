# -*- coding: utf-8 -*-
"""
Huvudmodul för balkprogrammet

Innehåller huvudklassen BeamWindow som är huvudfönstret för programmet samt programmets huvudloop.

@author: Jonas Lindemann
"""

import os
import sys

os.environ["QT_API"] = "pyside6"

from qtpy.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from qtpy import uic

from beam_model import BeamModel
from beam_results import BeamResultsWindow
from beam_widget import BeamWidget
from beam_utils import try_float, close_console
import beam_res



class BeamWindow(QMainWindow):
    """Fönsterklass för balkprogrammet"""

    def __init__(self):
        """BeamWindow konstruktor"""

        super().__init__()

        # Läs in gränssnitt från fil
        self.setup_ui()

        # Klassattribut

        self.filename = ""

        self.support_window = None
        self.segments_window = None
        self.results_window = None

        self.current_segment = 0

        # Skapa och initiera balk modell

        self.beam_model = BeamModel()

        # Skapa en widget för att rita balken

        self.beam_widget = BeamWidget(self.beam_model)
        self.main_layout.addWidget(self.beam_widget)

        self.new_model()

        # Se till att check actions har rätt default värden

        self.moment_action.setChecked(True)
        self.section_force_action.setChecked(True)
        self.displ_action.setChecked(True)
        self.dimension_action.setChecked(True)

        # Koppla händelser till actions

        self.exit_action.triggered.connect(self.on_exit)
        self.new_action.triggered.connect(self.on_new)
        self.open_action.triggered.connect(self.on_open)
        self.save_action.triggered.connect(self.on_save)
        self.save_as_action.triggered.connect(self.on_save_as)
        self.results_view_action.triggered.connect(self.on_results_view)
        self.add_beam_action.triggered.connect(self.on_add_beam)
        self.remove_beam_action.triggered.connect(self.on_remove_beam)
        self.moment_action.triggered.connect(self.on_moment)
        self.section_force_action.triggered.connect(self.on_section_force)
        self.displ_action.triggered.connect(self.on_displ)
        self.update_action.triggered.connect(self.on_editing_finished)
        self.dimension_action.triggered.connect(self.on_dimension)

        # Koppla händelser till kontroller

        self.segment_combo.currentIndexChanged.connect(self.on_segment_combo)
        self.segment_length_text.editingFinished.connect(self.on_editing_finished)
        self.calc_points_spin.valueChanged.connect(self.on_editing_finished)
        self.segment_load_text.editingFinished.connect(self.on_editing_finished)
        self.e_text.editingFinished.connect(self.on_editing_finished)
        self.a_text.editingFinished.connect(self.on_editing_finished)
        self.i_text.editingFinished.connect(self.on_editing_finished)

        self.segment_length_text.returnPressed.connect(self.on_editing_finished)

        self.left_support_xyr_option.clicked.connect(self.on_editing_finished)
        self.left_support_xy_option.clicked.connect(self.on_editing_finished)
        self.left_support_y_option.clicked.connect(self.on_editing_finished)

        self.right_support_xyr_option.clicked.connect(self.on_editing_finished)
        self.right_support_xy_option.clicked.connect(self.on_editing_finished)
        self.right_support_y_option.clicked.connect(self.on_editing_finished)

    def setup_ui(self) -> None:
        """Läs in gränssnitt från fil"""

        uic.loadUi("beam_app.ui", self)


    def new_model(self) -> None:
        """Skapa en ny modell"""

        self.beam_model.new()

        self.update_controls()
        self.update_combo()
        self.segment_combo.setCurrentIndex(0)

        self.beam_widget.on_model_updated()

    def update_controls(self) -> None:
        """Uppdatera kontroller med värden från balkmodell"""

        if not (0 <= self.current_segment < len(self.beam_model.segments)):
            return

        self.segment_length_text.setText(
            str(self.beam_model.lengths[self.current_segment])
        )
        self.calc_points_spin.setValue(self.beam_model.segments[self.current_segment])
        self.segment_load_text.setText(str(self.beam_model.loads[self.current_segment]))

        E_str = f"{self.beam_model.properties[self.current_segment][0]:.4e}"
        A_str = f"{self.beam_model.properties[self.current_segment][1]:.4e}"
        I_str = f"{self.beam_model.properties[self.current_segment][2]:.4e}"

        self.e_text.setText(E_str)
        self.a_text.setText(A_str)
        self.i_text.setText(I_str)

        if self.beam_model.supports[self.current_segment] == BeamModel.FIXED_XY:
            self.left_support_xy_option.setChecked(True)
        elif self.beam_model.supports[self.current_segment] == BeamModel.FIXED_Y:
            self.left_support_y_option.setChecked(True)
        elif self.beam_model.supports[self.current_segment] == BeamModel.FIXED_XYR:
            self.left_support_xyr_option.setChecked(True)

        if self.beam_model.supports[self.current_segment + 1] == BeamModel.FIXED_XY:
            self.right_support_xy_option.setChecked(True)
        elif self.beam_model.supports[self.current_segment + 1] == BeamModel.FIXED_Y:
            self.right_support_y_option.setChecked(True)
        elif self.beam_model.supports[self.current_segment + 1] == BeamModel.FIXED_XYR:
            self.right_support_xyr_option.setChecked(True)

    def update_combo(self) -> None:
        """Uppdatera listbox med balksegment"""

        self.segment_combo.clear()

        for i, item in enumerate(self.beam_model.segments):
            beam_descr = f"{i+1}: {self.beam_model.lengths[i]} m"
            self.segment_combo.addItem(beam_descr)

        self.segment_combo.setCurrentIndex(self.current_segment)

    def update_combo_labels(self) -> None:
        """Uppdatera texter i listbox"""

        for i, item in enumerate(self.beam_model.segments):
            beam_descr = f"{i+1}: {self.beam_model.lengths[i]} m"
            self.segment_combo.setItemText(i, beam_descr)

    def on_editing_finished(self, text: str ="") -> None:
        """Hantera ändringar i kontroller"""

        if self.current_segment != -1:

            l_str = self.segment_length_text.text()
            q_str = self.segment_load_text.text()
            E_str = self.e_text.text()
            A_str = self.a_text.text()
            I_str = self.i_text.text()

            l = self.beam_model.lengths[self.current_segment]
            q = self.beam_model.loads[self.current_segment]
            E = self.beam_model.properties[self.current_segment][0]
            A = self.beam_model.properties[self.current_segment][1]
            I = self.beam_model.properties[self.current_segment][2]

            l = try_float(l_str, l)
            q = try_float(q_str, q)
            E = try_float(E_str, E)
            A = try_float(A_str, A)
            I = try_float(I_str, I)

            self.beam_model.lengths[self.current_segment] = l
            self.beam_model.loads[self.current_segment] = q
            self.beam_model.properties[self.current_segment][0] = E
            self.beam_model.properties[self.current_segment][1] = A
            self.beam_model.properties[self.current_segment][2] = I
            self.beam_model.segments[self.current_segment] = (
                self.calc_points_spin.value()
            )

            if self.left_support_xy_option.isChecked():
                self.beam_model.supports[self.current_segment] = BeamModel.FIXED_XY
            elif self.left_support_y_option.isChecked():
                self.beam_model.supports[self.current_segment] = BeamModel.FIXED_Y
            elif self.left_support_xyr_option.isChecked():
                self.beam_model.supports[self.current_segment] = BeamModel.FIXED_XYR

            if self.right_support_xy_option.isChecked():
                self.beam_model.supports[self.current_segment + 1] = BeamModel.FIXED_XY
            elif self.right_support_y_option.isChecked():
                self.beam_model.supports[self.current_segment + 1] = BeamModel.FIXED_Y
            elif self.right_support_xyr_option.isChecked():
                self.beam_model.supports[self.current_segment + 1] = BeamModel.FIXED_XYR

            self.beam_model.solve()
            self.beam_widget.on_model_updated()

            self.update_controls()
            self.update_combo_labels()

            if self.results_window is not None:
                self.results_window.update()

    def on_segment_combo(self, idx: int) -> None:
        """Händelsemetod för att hantera val i listbox"""

        self.current_segment = idx
        self.update_controls()

    def on_new(self) -> None:
        """Händelsemetod för att skapa en ny modell"""

        self.new_model()
        self.update_controls()

    def on_exit(self) -> None:
        """Händelsemetod för att avsluta programmet"""
        self.close()

    def on_open(self) -> None:
        """Händelsemetod för att öppna en modell"""
        
        try:
            self.filename, _ = QFileDialog.getOpenFileName(
                self, "Öppna modell", "", "Modell filer (*.json *.jpg *.bmp)"
            )

            if self.filename != "":
                self.beam_model.open_from_json(self.filename)
                self.beam_widget.on_model_updated()
                self.update_controls()
        except Exception as e:
            QMessageBox.critical(self, "Fel", f"Kunde inte öppna filen:\n{e}")

    def on_save(self):
        """Händelsemetod för spara modellfil"""

        try:
            if self.filename == "":
                self.filename, _ = QFileDialog.getSaveFileName(
                    self, "Spara modell", "", "Modell filer (*.json)"
                )

            if self.filename != "":
                self.beam_model.save_as_json(self.filename)

        except Exception as e:
            QMessageBox.critical(self, "Fel", f"Kunde inte spara filen:\n{e}")

    def on_save_as(self):
        """Händelsemetod för att spara som ..."""

        try:
            temp_filename, _ = QFileDialog.getSaveFileName(
                self, "Spara modell", "", "Modell filer (*.json)"
            )

            if temp_filename != "":
                self.filename = temp_filename
                self.beam_model.save_as_json(self.filename)

        except Exception as e:
            QMessageBox.critical(self, "Fel", f"Kunde inte spara filen:\n{e}")

    def on_moment(self) -> None:
        """Händelsemetod för att visa momentdiagram."""

        self.beam_widget.show_moments = self.moment_action.isChecked()

    def on_section_force(self) -> None:
        """Händelsemetod för att visa snittkraftsdiagram."""

        self.beam_widget.show_section_force = self.section_force_action.isChecked()

    def on_displ(self) -> None:
        """Händelsemetod för att visa förskjutningsdiagram."""

        self.beam_widget.show_displacement = self.displ_action.isChecked()

    def on_dimension(self) -> None:
        """Händelsemetod för att visa dimensioner."""

        self.beam_widget.show_dimensions = self.dimension_action.isChecked()

    def on_add_beam(self) -> None:
        """Händelsemetod för att lägga till en balk."""

        self.beam_model.add_segment()
        self.beam_widget.on_model_updated()

        self.update_combo()
        self.update_controls()

    def on_remove_beam(self):
        """Händelsemetod för att ta bort en balk."""

        self.beam_model.remove_segment()
        self.beam_widget.on_model_updated()

        self.update_combo()
        self.update_controls()

    def on_results_view(self):
        """Händelsemetod för att visa resultatdialogrutan."""

        if self.results_view_action.isChecked():
            if self.results_window is not None:
                self.results_window.close()

            self.results_window = BeamResultsWindow(self.beam_model)
            self.results_window.on_close = self.on_results_view_close
            self.results_window.show()
        else:
            if self.results_window is not None:
                self.results_window.close()

    def on_results_view_close(self):
        """Händelsemetod för att stänga resultatdialogrutan."""

        self.results_view_action.setChecked(False)


if __name__ == "__main__":

    application = QApplication(sys.argv)

    window = BeamWindow()
    window.show()

    close_console()

    sys.exit(application.exec_())
