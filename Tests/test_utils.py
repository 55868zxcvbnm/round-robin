import unittest
from utils import validate_integer

class TestUtils(unittest.TestCase):
    def test_validate_integer(self):
        self.assertTrue(validate_integer("5"))
        self.assertFalse(validate_integer("abc"))

if __name__ == "__main__":
    unittest.main()
