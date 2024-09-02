# main.py

from tkinter import Tk
from ui import Simulador


def main():
    # Función principal para inicializar y ejecutar la interfaz gráfica del simulador.
    try:
        # Crear la ventana principal de la aplicación
        root = Tk()
        root.title("Simulador de Planificador de Procesos Round Robin")
        # Ajusta el tamaño de la ventana para que se ajuste al diseño de la UI
        root.geometry("1200x800")
        # Crear una instancia de la clase Simulador
        app = Simulador(root)

        # Iniciar el bucle principal de la interfaz gráfica
        root.mainloop()
    except Exception as e:
        # Mostrar un mensaje de error más detallado en caso de excepción
        print(f"Se produjo un error al iniciar la aplicación: {e}")


if __name__ == "__main__":
    main()
