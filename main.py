# ------------------------------------------------------------------------------------------------------
# Este archivo es el punto de entrada para el simulador y se encarga de inicializar la interfaz gráfica.
# ------------------------------------------------------------------------------------------------------

from ui import Simulador
from tkinter import Tk

if __name__ == "__main__":
    root = Tk()
    app = Simulador(root)
    root.mainloop()
