# ------------------------------------------------------------
# Aquí se define la interfaz del usuario utilizando Tkinter.
# ------------------------------------------------------------

import tkinter as tk
from tkinter import ttk
from algorithm import round_robin


class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Simulador Round Robin")

        # Crear widgets
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta y entrada para procesos
        ttk.Label(self.window, text="Número de procesos:").grid(
            column=0, row=0, padx=10, pady=10)
        self.process_entry = ttk.Entry(self.window)
        self.process_entry.grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(self.window, text="Tiempo de quantum:").grid(
            column=0, row=1, padx=10, pady=10)
        self.quantum_entry = ttk.Entry(self.window)
        self.quantum_entry.grid(column=1, row=1, padx=10, pady=10)

        # Botón para iniciar simulación
        self.start_button = ttk.Button(
            self.window, text="Iniciar Simulación", command=self.start_simulation)
        self.start_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

        # Área de resultados
        self.results_text = tk.Text(self.window, height=10, width=50)
        self.results_text.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

    def start_simulation(self):
        processes = int(self.process_entry.get())
        quantum = int(self.quantum_entry.get())
        results = round_robin(processes, quantum)
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, results)

    def run(self):
        self.window.mainloop()
