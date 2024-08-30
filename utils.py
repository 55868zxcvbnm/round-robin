# -----------------------------------------
# funciones adicionales, como validaciones.
# ------------------------------------------

def validar_entero_positivo(valor):
    # Valida que el valor ingresado sea un número entero positivo.
    if isinstance(valor, int) and valor > 0:
        return True
    return False


def calcular_promedio(valores):
    # Calcula el promedio de una lista de números.
    if not valores:
        return 0
    return sum(valores) / len(valores)
