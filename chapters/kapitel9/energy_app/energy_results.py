# -*- coding: utf-8 -*-
"""
Fönsterklass för att visa resultat från en värmeflödesberäkning i tabellform.
"""

import sys

from qtpy.QtWidgets import QWidget, QTableWidgetItem
from qtpy.QtCore import Qt
from qtpy import uic

from energy_utils import resource_path, load_ui

class EnergyResultsWindow(QWidget):
    """Fönsterklass för energiprogrammet"""

    def __init__(self, heat_model):
        """EnergyResultsWindow konstruktor"""

        super().__init__()

        self.heat_model = heat_model

        # Läs in gränssnitt från fil
        load_ui("energy_results.ui", self)

        self.setWindowFlags(
            Qt.Tool
            | Qt.WindowTitleHint
            | Qt.WindowCloseButtonHint
            | Qt.WindowStaysOnTopHint
        )
        # Uppdatera kontroller

        self.update()

    def update(self):
        """Uppdatera tabell"""

        # Rensa tabell

        self.result_table.clear()

        if self.heat_model.temperatures is None:
            return

        # Ange antal rader och kolumner

        self.result_table.verticalHeader().setVisible(False)
        num_nodes = len(self.heat_model.temperatures)
        self.result_table.setRowCount(num_nodes)
        self.result_table.setColumnCount(3)

        # Ange kolumnrubriker

        self.result_table.setHorizontalHeaderLabels(
            ["x (m)", "Temperatur (°C)", "Värmeflöde (W)"]
        )

        # Fyll tabell med data

        for i in range(num_nodes):

            x_item = QTableWidgetItem(f"{self.heat_model.coords[i]:.4f}")
            x_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            T_item = QTableWidgetItem(f"{self.heat_model.temperatures[i]:.4f}")
            T_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            
            # Värmeflöde finns för element, inte noder
            if i < len(self.heat_model.heat_flux):
                q_item = QTableWidgetItem(f"{self.heat_model.heat_flux[i]:.4f}")
            else:
                q_item = QTableWidgetItem("-")
            q_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

            self.result_table.setItem(i, 0, QTableWidgetItem(x_item))
            self.result_table.setItem(i, 1, QTableWidgetItem(T_item))
            self.result_table.setItem(i, 2, QTableWidgetItem(q_item))

        # Justera tabellstorlek

        self.result_table.resizeColumnsToContents()
        self.result_table.resizeRowsToContents()

    def on_close(self):
        """Hantera stängning av fönster"""

        pass

    def closeEvent(self, event):
        """Hantera stängning av fönster"""

        self.on_close()
        self.close()
