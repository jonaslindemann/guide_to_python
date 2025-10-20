import unittest
from qtpy.QtWidgets import QApplication
from beam_widget import BeamWidget
from beam_model import BeamModel
from draw_widget import DrawWidget
import sys

# Ensure a QApplication exists for widget tests
app = QApplication.instance() or QApplication(sys.argv)

class TestDrawWidget(unittest.TestCase):
    def setUp(self):
        self.widget = DrawWidget()

    def test_initial_properties(self):
        self.assertEqual(self.widget.stroke_color, self.widget.stroke_pen.color())
        self.assertEqual(self.widget.fill_color, self.widget.fill_brush.color())
        self.assertEqual(self.widget.stroke_width, self.widget.stroke_pen.width())

    def test_set_properties(self):
        from qtpy.QtCore import Qt
        self.widget.stroke_color = Qt.red
        self.widget.fill_color = Qt.green
        self.widget.stroke_width = 3
        self.assertEqual(self.widget.stroke_color, self.widget.stroke_pen.color())
        self.assertEqual(self.widget.fill_color, self.widget.fill_brush.color())
        self.assertEqual(self.widget.stroke_width, self.widget.stroke_pen.width())

    def test_transform_update(self):
        old_scale = self.widget.scale
        self.widget.resize(400, 400)
        self.widget.update()
        self.assertNotEqual(old_scale, self.widget.scale)

class TestBeamWidget(unittest.TestCase):
    def setUp(self):
        # Minimal BeamModel stub for testing
        self.model = BeamModel()
        self.widget = BeamWidget(self.model)

    def test_widget_init(self):
        self.assertIsNotNone(self.widget.beam_model)
        self.assertTrue(hasattr(self.widget, 'draw_beams'))

    def test_update_scale_factors(self):
        self.widget.update_scale_factors()
        self.assertTrue(hasattr(self.widget, 'max_height'))

if __name__ == '__main__':
    unittest.main()
