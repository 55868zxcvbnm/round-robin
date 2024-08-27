# Aquí puedes colocar funciones adicionales, como validaciones.

# Ejemplo de función de utilidad para validar la longitud de las entradas (usada en ui.py)
def validar_entradas_procesos(numero_procesos, tiempos_llegada, tiempos_rafaga):
    if len(tiempos_llegada) != numero_procesos or len(tiempos_rafaga) != numero_procesos:
        raise ValueError(
            "El número de procesos no coincide con la cantidad de tiempos de llegada o tiempos de ráfaga.")


def validar_entero_positivo(valor):
    """Valida que el valor ingresado sea un número entero positivo."""
    if isinstance(valor, int) and valor > 0:
        return True
    return False


def calcular_promedio(valores):
    """Calcula el promedio de una lista de números."""
    if not valores:
        return 0
    return sum(valores) / len(valores)
