# Aquí puedes colocar funciones adicionales, como validaciones.

def validate_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
