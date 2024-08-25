import unittest
from utils import validate_positive_integer, calculate_average


class TestUtils(unittest.TestCase):

    def test_validate_positive_integer(self):
        # Pruebas para la función validate_positive_integer
        self.assertTrue(validate_positive_integer(5))
        self.assertTrue(validate_positive_integer(1))
        self.assertFalse(validate_positive_integer(0))
        self.assertFalse(validate_positive_integer(-3))
        self.assertFalse(validate_positive_integer("string"))
        self.assertFalse(validate_positive_integer(4.5))

    def test_calculate_average(self):
        # Pruebas para la función calculate_average
        self.assertEqual(calculate_average([2, 4, 6]), 4)
        self.assertEqual(calculate_average([10]), 10)
        self.assertEqual(calculate_average([]), 0)
        self.assertEqual(calculate_average([3, 3, 3]), 3)
        self.assertAlmostEqual(calculate_average(
            [2.5, 3.5, 4.0]), 3.3333333, places=6)


if __name__ == '__main__':
    unittest.main()
