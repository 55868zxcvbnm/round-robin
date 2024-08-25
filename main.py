# ------------------------------------------------------------------------------------------------------
# Este archivo es el punto de entrain para el simulador y se encarga de inicializar la interfaz gráfica.
# ------------------------------------------------------------------------------------------------------

from ui import RoundRobinSimulatorUI
from tkinter import Tk

if __name__ == "__main__":
    root = Tk()
    app = RoundRobinSimulatorUI(root)
    root.mainloop()
