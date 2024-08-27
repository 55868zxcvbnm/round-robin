# ------------------------------------------------------------------------------------------------------
# Este archivo es el punto de entrain para el simulador y se encarga de inicializar la interfaz gráfica.
# ------------------------------------------------------------------------------------------------------

from ui import SimuladorRoundRobinUI
from tkinter import Tk

if __name__ == "__main__":
    root = Tk()
    app = SimuladorRoundRobinUI(root)
    root.mainloop()
