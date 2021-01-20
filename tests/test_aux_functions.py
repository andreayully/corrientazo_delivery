import unittest
import aux_functions


class TestAuxFunction(unittest.TestCase):
    def test_check_distance(self):
        self.assertTrue(aux_functions.check_distance(-2, 4))

    def test_check_distance_false(self):
        self.assertFalse(aux_functions.check_distance(-12, 4))


if __name__ == "__main__":
    unittest.main()
