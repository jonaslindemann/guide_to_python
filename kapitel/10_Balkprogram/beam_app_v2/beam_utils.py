# -*- coding: utf-8 -*-
"""
Modul med diverse hjälpfunktioner för att hantera strängar, tal och listor.

Innehåller även en liten 'sanitizer' för .ui-filer från Qt Creator där
enums ibland skrivs med Qt6-stil (t.ex. "Qt::Orientation::Horizontal"),
som kan ställa till det när de laddas via Python/Qt bindningar.
"""

import os, sys
import ctypes
import re
import tempfile
from qtpy import uic


def try_float(text, default=0.0):
    try:
        return float(text)
    except ValueError:
        return default
    
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def close_console():
    if os.name != 'nt':
        return
    
    kernel32 = ctypes.WinDLL('kernel32')
    console_hwnd = kernel32.GetConsoleWindow()
    
    if console_hwnd != 0:
        # This will properly close the console window
        kernel32.FreeConsole()


# ---------- UI helpers ----------

_ENUM_FIXES = (
    # Qt global enums
    (re.compile(r"Qt::Orientation::(Horizontal|Vertical)"), r"Qt::\1"),
    (re.compile(r"Qt::ToolButtonStyle::(\w+)"), r"Qt::\1"),
    (re.compile(r"Qt::AlignmentFlag::"), r"Qt::"),
    # Widget-specific enums written with extra scope
    (re.compile(r"QFrame::Shape::"), r"QFrame::"),
    (re.compile(r"QFrame::Shadow::"), r"QFrame::"),
    (re.compile(r"QTabWidget::TabPosition::"), r"QTabWidget::"),
    (re.compile(r"QTabWidget::TabShape::"), r"QTabWidget::"),
    (re.compile(r"QAction::MenuRole::"), r"QAction::"),
)


def _sanitize_ui_xml(xml_text: str) -> str:
    """Replace Qt6-style enum spellings with Qt4/5-compatible ones.

    This makes uic.loadUi happier across PyQt/PySide backends.
    """
    fixed = xml_text
    for pattern, repl in _ENUM_FIXES:
        fixed = pattern.sub(repl, fixed)
    return fixed


def load_ui(ui_filename: str, baseinstance=None):
    """Load a .ui file after sanitizing known problematic enum attributes.

    Usage: load_ui("beam_app.ui", self)
    """
    full_path = resource_path(ui_filename)

    # Read and sanitize
    with open(full_path, "r", encoding="utf-8") as f:
        xml_text = f.read()
    xml_text = _sanitize_ui_xml(xml_text)

    # Write to a temporary .ui and load via uic
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".ui", mode="w", encoding="utf-8")
    try:
        tmp.write(xml_text)
        tmp.flush()
        tmp.close()
        return uic.loadUi(tmp.name, baseinstance)
    finally:
        try:
            os.unlink(tmp.name)
        except Exception:
            # Best-effort cleanup on Windows
            pass

