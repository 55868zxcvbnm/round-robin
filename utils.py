# -----------------------------------------
# Funciones adicionales, como validaciones.
# ------------------------------------------

def validar_entero_positivo(valor):
    """
    Valida que el valor ingresado sea un número entero positivo.
    Args:
        valor (int): El valor a validar.
    Returns:
        bool: True si el valor es un entero positivo, False en caso contrario.
    """
    return isinstance(valor, int) and valor > 0


def calcular_promedio(valores):
    """
    Calcula el promedio de una lista de números.
    Args:
        valores (list): Lista de números para calcular el promedio.
    Returns:
        float: El promedio de los valores. Retorna 0 si la lista está vacía.
    """
    if not valores:
        return 0
    if not all(isinstance(x, (int, float)) for x in valores):
        raise ValueError("Todos los valores deben ser números.")
    return sum(valores) / len(valores)
