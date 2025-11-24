# test_beam_model.py
import unittest
from beam_model import BeamModel

class TestBeamModel(unittest.TestCase):
    def test_total_length(self):
        model = BeamModel()
        self.assertAlmostEqual(model.total_length, sum(model.lengths))

    def test_max_load(self):
        model = BeamModel()
        self.assertEqual(model.max_load, max(model.loads))

    def test_min_load(self):
        model = BeamModel()
        self.assertEqual(model.min_load, min(model.loads))

    def test_max_abs_load(self):
        model = BeamModel()
        self.assertEqual(model.max_abs_load, max(abs(load) for load in model.loads))

    def test_max_y_displ(self):
        model = BeamModel()
        self.assertEqual(model.max_y_displ, max(model.y_displ))

    def test_min_y_displ(self):
        model = BeamModel()
        self.assertEqual(model.min_y_displ, min(model.y_displ))

    def test_max_abs_y_displ(self):
        model = BeamModel()
        self.assertEqual(model.max_abs_y_displ, max(abs(displ) for displ in model.y_displ))

    def test_max_abs_M(self):
        model = BeamModel()
        self.assertEqual(model.max_abs_M, max(abs(moment) for moment in model.NVM[:, 2]))
    
    def test_max_abs_V(self):
        model = BeamModel()
        self.assertEqual(model.max_abs_V, max(abs(shear) for shear in model.NVM[:, 1]))

    def test_save_as_json(self):
        model = BeamModel()
        try:
            model.save_as_json("test_data.json")
            self.assertTrue(True)  # If no exception, test passes
        except Exception as e:
            self.fail(f"save_to_json raised an exception: {e}")

    def test_open_from_json(self):
        model = BeamModel()
        try:
            model.open_from_json("test_data.json")
            self.assertTrue(True)  # If no exception, test passes
        except Exception as e:
            self.fail(f"open_from_json raised an exception: {e}")

    def test_add_segment(self):
        model = BeamModel()
        initial_length = len(model.lengths)
        model.add_segment()
        self.assertEqual(len(model.lengths), initial_length + 1)

    def test_remove_segment(self):
        model = BeamModel()
        initial_length = len(model.lengths)
        if initial_length > 1:
            model.remove_segment()
            self.assertEqual(len(model.lengths), initial_length - 1)
        else:
            with self.assertRaises(ValueError):
                model.remove_segment()

    def test_new(self):
        model = BeamModel()
        initial_properties = model._default_properties()
        model.new()
        self.assertEqual(model.properties[0], initial_properties)
        self.assertEqual(len(model.properties), 3)

if __name__ == '__main__':
    unittest.main()
