import unittest
import aux_functions


class TestAuxFunction(unittest.TestCase):
    def test_check_distance(self):
        self.assertTrue(aux_functions.check_distance(0, 11), True)


if __name__ == "__main__":
    unittest.main()
