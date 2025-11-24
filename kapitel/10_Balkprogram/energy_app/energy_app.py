# -*- coding: utf-8 -*-
"""
Huvudmodul för energiprogrammet

Innehåller huvudklassen EnergyWindow som är huvudfönstret för programmet samt programmets huvudloop.

@author: Jonas Lindemann
"""

import os
import sys

os.environ["QT_API"] = "pyside6"

from energy_utils import try_float, close_console
from energy_widget import EnergyWidget
from energy_results import EnergyResultsWindow
from energy_model import HeatFlow1DModel, MaterialLayer

from qtpy import uic
from qtpy.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from qtpy.QtGui import QPalette, QIcon, QPixmap, QPainter
from qtpy.QtCore import Qt

import energy_res

class EnergyWindow(QMainWindow):
    """Fönsterklass för energiprogrammet"""

    def __init__(self):
        """EnergyWindow konstruktor"""

        super().__init__()

        # Läs in gränssnitt från fil
        uic.loadUi("energy_app.ui", self)

        # Klassattribut

        self.filename = ""
        self.current_layer = 0
        self.results_window = None

        # Skapa och initiera värmeflödesmodell

        self.heat_model = HeatFlow1DModel()

        # Skapa en widget för att rita modellen

        self.energy_widget = EnergyWidget(self.heat_model)
        self.main_layout.addWidget(self.energy_widget)

        self.new_model()        

        # Se till att check actions har rätt default värden

        self.temperature_action.setChecked(True)
        self.heat_flux_action.setChecked(True)
        self.dimension_action.setChecked(True)

        # Koppla händelser till actions

        self.exit_action.triggered.connect(self.on_exit)
        self.new_action.triggered.connect(self.on_new)
        self.open_action.triggered.connect(self.on_open)
        self.save_action.triggered.connect(self.on_save)
        self.save_as_action.triggered.connect(self.on_save_as)
        self.results_view_action.triggered.connect(self.on_results_view)
        self.add_layer_action.triggered.connect(self.on_add_layer)
        self.remove_layer_action.triggered.connect(self.on_remove_layer)
        self.temperature_action.triggered.connect(self.on_temperature)
        self.heat_flux_action.triggered.connect(self.on_heat_flux)
        self.update_action.triggered.connect(self.on_editing_finished)
        self.dimension_action.triggered.connect(self.on_dimension)

        # Koppla händelser till kontroller

        self.layer_combo.currentIndexChanged.connect(self.on_layer_combo)
        self.thickness_text.editingFinished.connect(
            self.on_editing_finished)
        self.calc_points_spin.valueChanged.connect(self.on_editing_finished)
        self.conductivity_text.editingFinished.connect(
            self.on_editing_finished)
        self.h_left_text.editingFinished.connect(self.on_editing_finished)
        self.h_right_text.editingFinished.connect(self.on_editing_finished)
        self.T_left_text.editingFinished.connect(self.on_editing_finished)
        self.T_right_text.editingFinished.connect(self.on_editing_finished)

        self.thickness_text.returnPressed.connect(
            self.on_editing_finished)

        # Justera ikoner för mörkt tema om nödvändigt

        self.adjust_icons_for_theme()

    def adjust_icons_for_theme(self) -> None:
        """Adjust toolbar icons to match the current theme (light/dark mode)"""
        
        # Kontrollera om vi är i mörkt läge genom att titta på fönstrets textfärg

        palette = self.palette()
        text_color = palette.color(QPalette.ColorRole.WindowText)
        bg_color = palette.color(QPalette.ColorRole.Window)

        # Beräkna ljusstyrka för att avgöra om mörkt läge.
        # Om bakgrund är mörkare än text, är det mörkt läge.
        
        is_dark_mode = bg_color.lightness() < text_color.lightness()
        
        if is_dark_mode:
            
            # Loppa över alla actions i verktygsfältet och justera deras ikoner

            for action in self.toolBar.actions():
                if not action.isSeparator() and not action.icon().isNull():
                    original_icon = action.icon()
                    
                    # Skapa en ny ikon med inverterade färger för mörkt läge

                    inverted_icon = self.create_inverted_icon(original_icon)
                    action.setIcon(inverted_icon)

        # Tala om för energy widgeten om vi skall använda mörkt läge.

        self.energy_widget.dark_mode = is_dark_mode
    
    def create_inverted_icon(self, icon: QIcon) -> QIcon:
        """Skapa en vit version av en ikon för mörkt läge"""
        
        # Hämta pixmap från ikonen

        pixmap = icon.pixmap(24, 24)  
        
        # Konvertera till bild för pixelmanipulation

        image = pixmap.toImage()
        
        # Skapa en ny pixmap för den färgade ikonen

        colored_pixmap = QPixmap(pixmap.size())
        colored_pixmap.fill(Qt.GlobalColor.transparent)
        
        # Använd QPainter för att färga ikonen vit

        painter = QPainter(colored_pixmap)
        painter.drawImage(0, 0, image)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
        painter.fillRect(colored_pixmap.rect(), Qt.GlobalColor.white)
        painter.end()
        
        return QIcon(colored_pixmap)

    def new_model(self) -> None:
        """Skapa en ny modell"""

        self.heat_model.new()

        self.update_controls()
        self.update_combo()
        self.layer_combo.setCurrentIndex(0)

        self.energy_widget.on_model_updated()

    def update_controls(self) -> None:
        """Uppdatera kontroller med värden från värmeflödesmodell"""

        if not (0 <= self.current_layer < len(self.heat_model.layers)):
            return

        layer = self.heat_model.layers[self.current_layer]

        self.thickness_text.setText(
            str(layer.thickness)
        )
        self.calc_points_spin.setValue(
            layer.num_elements)
        self.conductivity_text.setText(
            str(layer.conductivity))

        # Uppdatera globala randvillkor (visas alltid)
        self.h_left_text.setText(f"{self.heat_model.h_left:.4f}")
        self.h_right_text.setText(f"{self.heat_model.h_right:.4f}")
        self.T_left_text.setText(f"{self.heat_model.T_left:.4f}")
        self.T_right_text.setText(f"{self.heat_model.T_right:.4f}")

    def update_combo(self) -> None:
        """Uppdatera listbox med materiallager"""

        self.layer_combo.clear()

        for i, layer in enumerate(self.heat_model.layers):
            layer_descr = f"{i+1}: {layer.thickness} m"
            self.layer_combo.addItem(layer_descr)

        self.layer_combo.setCurrentIndex(self.current_layer)

    def on_editing_finished(self, text: str = "") -> None:
        """Hantera ändringar i kontroller"""

        if self.current_layer == -1 or self.current_layer >= len(self.heat_model.layers):
            return
        
        layer = self.heat_model.layers[self.current_layer]
        
        thickness = layer.thickness
        conductivity = layer.conductivity
        num_elements = layer.num_elements

        thickness = try_float(self.thickness_text.text(), thickness)
        conductivity = try_float(self.conductivity_text.text(), conductivity)
        num_elements = self.calc_points_spin.value()

        layer.thickness = thickness
        layer.conductivity = conductivity
        layer.num_elements = num_elements

        # Uppdatera globala randvillkor
        self.heat_model.h_left = try_float(self.h_left_text.text(), self.heat_model.h_left)
        self.heat_model.h_right = try_float(self.h_right_text.text(), self.heat_model.h_right)
        self.heat_model.T_left = try_float(self.T_left_text.text(), self.heat_model.T_left)
        self.heat_model.T_right = try_float(self.T_right_text.text(), self.heat_model.T_right)

        self.heat_model.solve()
        self.energy_widget.on_model_updated()

        self.update_controls()
        self.update_combo()

        if self.results_window is not None:
            self.results_window.update()

    def on_layer_combo(self, idx: int) -> None:
        """Händelsemetod för att hantera val i listbox"""

        self.current_layer = idx
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
                self.heat_model.open_from_json(self.filename)
                self.energy_widget.on_model_updated()
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
                self.heat_model.save_as_json(self.filename)

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
                self.heat_model.save_as_json(self.filename)

        except Exception as e:
            QMessageBox.critical(self, "Fel", f"Kunde inte spara filen:\n{e}")

    def on_temperature(self) -> None:
        """Händelsemetod för att visa temperaturfördelning."""

        self.energy_widget.show_temperature = self.temperature_action.isChecked()

    def on_heat_flux(self) -> None:
        """Händelsemetod för att visa värmeflöde."""

        self.energy_widget.show_heat_flux = self.heat_flux_action.isChecked()

    def on_dimension(self) -> None:
        """Händelsemetod för att visa dimensioner."""

        self.energy_widget.show_dimensions = self.dimension_action.isChecked()

    def on_add_layer(self) -> None:
        """Händelsemetod för att lägga till ett lager."""

        self.heat_model.add_layer(0.1, 1.0)
        self.energy_widget.on_model_updated()

        self.update_combo()
        self.update_controls()

    def on_remove_layer(self):
        """Händelsemetod för att ta bort ett lager."""

        self.heat_model.remove_layer()
        self.energy_widget.on_model_updated()

        self.update_combo()
        self.update_controls()

    def on_results_view(self):
        """Händelsemetod för att visa resultatdialogrutan."""

        if self.results_view_action.isChecked():
            if self.results_window is not None:
                self.results_window.close()

            self.results_window = EnergyResultsWindow(self.heat_model)
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

    window = EnergyWindow()
    window.show()

    # close_console()  # Commented out to see debug print statements

    sys.exit(application.exec_())
