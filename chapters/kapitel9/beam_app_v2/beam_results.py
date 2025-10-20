# -*- coding: utf-8 -*-
"""
Fönsterklass för att visa resultat från en balkberäkning i tabellform.
"""

import sys

from qtpy.QtWidgets import QWidget, QTableWidgetItem
from qtpy.QtCore import Qt
from qtpy import uic

from beam_utils import resource_path, load_ui

class BeamResultsWindow(QWidget):
    """Fönsterklass för balkprogrammet"""

    def __init__(self, beam_model):
        """BeamResultsWindow konstruktor"""

        super().__init__()

        self.beam_model = beam_model

        # Läs in gränssnitt från fil
        load_ui("beam_results.ui", self)

        self.setWindowFlags(
            Qt.Tool
            | Qt.WindowTitleHint
            | Qt.WindowCloseButtonHint
            | Qt.WindowStaysOnTopHint
        )
        # Uppdatera kontroller

        self.update()

    def update(self):
        """Uppdatera fönster"""

        self.update_table()

    def update_table(self):
        """Uppdatera tabell"""

        # Rensa tabell

        self.result_table.clear()

        if self.beam_model.NVM is None:
            return

        # Ange antal rader och kolumner

        self.result_table.verticalHeader().setVisible(False)
        self.result_table.setRowCount(self.beam_model.NVM.shape[0])
        self.result_table.setColumnCount(5)

        # Ange kolumnrubriker

        self.result_table.setHorizontalHeaderLabels(
            ["x (m)", "N (N)", "V (N)", "M (Nm)", "u (m)"]
        )

        # Fyll tabell med data

        for i in range(self.beam_model.NVM.shape[0]):

            x_item = QTableWidgetItem(f"{self.beam_model.x[i]:.4f}")
            x_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            N_item = QTableWidgetItem(f"{self.beam_model.NVM[i, 0]:.4f}")
            N_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            V_item = QTableWidgetItem(f"{self.beam_model.NVM[i, 1]:.4f}")
            V_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            M_item = QTableWidgetItem(f"{self.beam_model.NVM[i, 2]:.4f}")
            M_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            y_item = QTableWidgetItem(f"{self.beam_model.y_displ[i, 0]:.4f}")
            y_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

            self.result_table.setItem(i, 0, QTableWidgetItem(x_item))
            self.result_table.setItem(i, 1, QTableWidgetItem(N_item))
            self.result_table.setItem(i, 2, QTableWidgetItem(V_item))
            self.result_table.setItem(i, 3, QTableWidgetItem(M_item))
            self.result_table.setItem(i, 4, QTableWidgetItem(y_item))

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
