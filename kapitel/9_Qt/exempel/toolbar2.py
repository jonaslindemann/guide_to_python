# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 09:44:29 2016

@author: lindemann
"""

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    """Huvudklass för vårt fönster"""

    def __init__(self):
        """Klassens konstruktor"""
        super().__init__()

        self.init_gui()

    def init_gui(self):
        """Initiera gränssnitt"""

        self.resize(400, 200)
        self.move(50, 50)
        self.setWindowTitle("MyWindow")

        # Definiera actions

        self.new_file_action = QAction("Ny", self)
        self.new_file_action.setIcon(QIcon("icons8-new-document.png"))
        self.new_file_action.setShortcut("Ctrl+N")
        self.new_file_action.triggered.connect(self.on_new_file_action)

        self.open_file_action = QAction("Öppna...", self)
        self.open_file_action.setIcon(QIcon("icons8-open.png"))
        self.open_file_action.setShortcut("Ctrl+O")
        self.open_file_action.triggered.connect(self.on_open_file_action)

        self.save_file_action = QAction("Spara", self)
        self.save_file_action.setIcon(QIcon("icons8-save.png"))
        self.save_file_action.setShortcut("Ctrl+S")
        self.save_file_action.triggered.connect(self.on_save_file_action)

        self.exit_action = QAction("Avsluta", self)
        self.exit_action.setIcon(QIcon("icons8-exit.png"))
        self.exit_action.setShortcut("Alt+F4")
        self.exit_action.triggered.connect(self.on_exit)

        self.cut_action = QAction("Klipp ut", self)
        self.cut_action.setIcon(QIcon("icons8-cut.png"))
        self.cut_action.setShortcut("Ctrl+X")
        self.cut_action.triggered.connect(self.on_cut_action)

        self.copy_action = QAction("Klipp ut", self)
        self.copy_action.setIcon(QIcon("icons8-copy.png"))
        self.copy_action.setShortcut("Ctrl+C")
        self.copy_action.triggered.connect(self.on_copy_action)

        self.past_action = QAction("Klista in", self)
        self.past_action.setIcon(QIcon("icons8-paste.png"))
        self.past_action.setShortcut("Ctrl+V")
        self.past_action.triggered.connect(self.on_paste_action)

        # Koppla menyer till actions

        self.file_menu = self.menuBar().addMenu("Arkiv")
        self.file_menu.addAction(self.new_file_action)
        self.file_menu.addAction(self.open_file_action)
        self.file_menu.addAction(self.save_file_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.exit_action)

        self.edit_menu = self.menuBar().addMenu("Redigera")
        self.edit_menu.addAction(self.cut_action)
        self.edit_menu.addAction(self.copy_action)
        self.edit_menu.addAction(self.past_action)

        # Skapa verktygsfält och lägg till actions

        self.file_toolbar = self.addToolBar("Arkiv")
        self.file_toolbar.addAction(self.new_file_action)
        self.file_toolbar.addAction(self.open_file_action)
        self.file_toolbar.addAction(self.save_file_action)
        self.file_toolbar.addSeparator()
        self.file_toolbar.addAction(self.exit_action)

        self.edit_toolbar = self.addToolBar("Redigera")
        self.edit_toolbar.addAction(self.cut_action)
        self.edit_toolbar.addAction(self.copy_action)
        self.edit_toolbar.addAction(self.past_action)

        # Visa fönster

        self.show()

    def on_new_file_action(self):
        """Händelsemetod för menyhändelse"""
        print("Ny fil!")

    def on_open_file_action(self):
        """Händelsemetod för menyhändelse"""
        print("Öppna fil")

    def on_save_file_action(self):
        """Händelsemetod för menyhändelse"""
        print("Spara fil")

    def on_exit(self):
        """Händelsemetod för menyhändelse"""
        self.close()

    def on_cut_action(self):
        """Händelsemetod för menyhändelse"""
        print("Klipp ut")

    def on_copy_action(self):
        """Händelsemetod för menyhändelse"""
        print("Kopiera")

    def on_paste_action(self):
        """Händelsemetod för menyhändelse"""
        print("Klistra in")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
