import unittest
from utils import calcular_promedio, validar_entero_positivo


class TestUtils(unittest.TestCase):

    def test_validar_entero_positivo(self):
        # Pruebas para la función validar_entero_positivo
        self.assertTrue(validar_entero_positivo(5), "Error: 5 debería ser considerado un entero positivo.")
        self.assertTrue(validar_entero_positivo(1), "Error: 1 debería ser considerado un entero positivo.")
        self.assertFalse(validar_entero_positivo(0), "Error: 0 no debería ser considerado un entero positivo.")
        self.assertFalse(validar_entero_positivo(-3),"Error: -3 no debería ser considerado un entero positivo.")
        self.assertFalse(validar_entero_positivo("string"), "Error: 'string' no debería ser considerado un entero positivo.")
        self.assertFalse(validar_entero_positivo(4.5), "Error: 4.5 no debería ser considerado un entero positivo.")

    def test_calcular_promedio(self):
        # Pruebas para la función calcular_promedio
        self.assertEqual(calcular_promedio([2, 4, 6]), 4, "Error: El promedio de [2, 4, 6] debería ser 4.")
        self.assertEqual(calcular_promedio([10]), 10, "Error: El promedio de [10] debería ser 10.")
        self.assertEqual(calcular_promedio([]), 0, "Error: El promedio de una lista vacía debería ser 0.")
        self.assertEqual(calcular_promedio([3, 3, 3]), 3, "Error: El promedio de [3, 3, 3] debería ser 3.")
        self.assertAlmostEqual(calcular_promedio([2.5, 3.5, 4.0]), 3.3333333, places=6,
                               msg="Error: El promedio de [2.5, 3.5, 4.0] debería ser aproximadamente 3.3333333.")


if __name__ == '__main__':
    unittest.main()
