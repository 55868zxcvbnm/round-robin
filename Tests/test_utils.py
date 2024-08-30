import unittest
from utils import calcular_promedio, validar_entero_positivo


class TestUtils(unittest.TestCase):

    def test_validar_entero_positivo(self):
        # Pruebas para la función validar_entero_positivo
        self.assertTrue(validar_entero_positivo(5))
        self.assertTrue(validar_entero_positivo(1))
        self.assertFalse(validar_entero_positivo(0))
        self.assertFalse(validar_entero_positivo(-3))
        self.assertFalse(validar_entero_positivo("string"))
        self.assertFalse(validar_entero_positivo(4.5))

    def test_calcular_promedio(self):
        # Pruebas para la función calcular_promedio
        self.assertEqual(calcular_promedio([2, 4, 6]), 4)
        self.assertEqual(calcular_promedio([10]), 10)
        self.assertEqual(calcular_promedio([]), 0)
        self.assertEqual(calcular_promedio([3, 3, 3]), 3)
        self.assertAlmostEqual(calcular_promedio([2.5, 3.5, 4.0]), 3.3333333, places=6)


if __name__ == '__main__':
    unittest.main()

