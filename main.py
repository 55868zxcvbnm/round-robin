# main.py
from tkinter import Tk
from ui import Simulador


def main():
    # Función principal para inicializar y ejecutar la interfaz gráfica del simulador.
    try:
        # Crear la ventana principal de la aplicación
        root = Tk()
        root.title("Simulador de Planificador de Procesos Round Robin")
        root.geometry("1200x800")
        app = Simulador(root)
        root.mainloop()
    except Exception as e:
        print(f"Se produjo un error al iniciar la aplicación: {e}")


if __name__ == "__main__":
    main()
