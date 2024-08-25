# Aquí puedes colocar funciones adicionales, como validaciones.

# Example utility function to validate input lengths (used in ui.py)
def validate_process_inputs(number_processes, arrival_times, burst_times):
    if len(arrival_times) != number_processes or len(burst_times) != number_processes:
        raise ValueError(
            "The number of processes does not match the number of arrival or burst times.")


def validate_positive_integer(value):
    """Valida que el valor ingresado sea un número entero positivo."""
    if isinstance(value, int) and value > 0:
        return True
    return False


def calculate_average(values):
    """Calcula el promedio de una lista de números."""
    if not values:
        return 0
    return sum(values) / len(values)
