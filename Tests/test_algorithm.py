import unittest
from algorithm import round_robin


class TestAlgorithm(unittest.TestCase):
    def test_round_robin(self):
        result = round_robin(3, 4)
        self.assertIn("Proceso 0 ejecutado por", result)
        self.assertIn("Proceso 2 ejecutado por", result)


if __name__ == "__main__":
    unittest.main()
