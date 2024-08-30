# ------------------------------------------------------------
# Aquí se define la interfaz del usuario utilizando Tkinter.
# ------------------------------------------------------------

import tkinter as tk
from tkinter import ttk
from algorithm import PlanificadorRoundRobin


class Simulador:
    def __init__(self, master):
        self.master = master
        master.title("Simulador de Planificador de Procesos Round Robin")
        master.geometry("800x600")

        # Título principal
        self.titulo = tk.Label(
            master,
            text="Simulador de Planificador de Procesos Round Robin",
            font=("Helvetica", 16, "bold"),
            fg="#333333",  # Color del texto
            pady=20
        )
        self.titulo.pack()

        # Frame contenedor que se utiliza para organizar otros widgets (como etiquetas, campos de entrada, botones, etc.) en una ventana.
        self.frame_config = tk.Frame(master, padx=10, pady=10)
        self.frame_config.pack(fill="x")

        # Etiquetas y entradas dentro del frame de configuración
        tk.Label(self.frame_config, text="Cantidad de Procesos:", font=("Helvetica", 11)).grid(row=0, column=0, sticky="w")
        self.entrada_procesos = tk.Entry(self.frame_config, width=10)
        self.entrada_procesos.grid(row=0, column=1, padx=10)

        tk.Label(self.frame_config, text="Quantum:", font=("Helvetica", 11)).grid(row=1, column=0, sticky="w")
        self.entrada_quantum = tk.Entry(self.frame_config, width=10)
        self.entrada_quantum.grid(row=1, column=1, padx=10)

        tk.Label(self.frame_config, text="Tiempos de Llegada (separados por comas):", font=("Helvetica", 11)).grid(row=2, column=0, sticky="w")
        self.entrada_llegada = tk.Entry(self.frame_config, width=25)
        self.entrada_llegada.grid(row=2, column=1, padx=10)

        tk.Label(self.frame_config, text="Tiempos de Ráfaga (separados por comas):", font=("Helvetica", 11)).grid(row=3, column=0, sticky="w")
        self.entrada_rafaga = tk.Entry(self.frame_config, width=25)
        self.entrada_rafaga.grid(row=3, column=1, padx=10)

        # Frame para botones
        self.frame_botones = tk.Frame(master, pady=10)
        self.frame_botones.pack()

        self.boton_iniciar = tk.Button(self.frame_botones, text="Start",
                                       command=self.iniciar_simulacion, width=10, bg="#4CAF50", fg="white")
        self.boton_iniciar.grid(row=0, column=0, padx=5, pady=5)

        self.boton_limpiar = tk.Button(self.frame_botones, text="Clear",
                                       command=self.limpiar_pantalla, width=10, bg="#f44336", fg="white")
        self.boton_limpiar.grid(row=0, column=1, padx=5, pady=5)

        # Caja de texto para mostrar los resultados
        self.texto_resultados = tk.Text(
            master, state='normal', width=70, height=23, wrap="word")
        self.texto_resultados.pack(padx=10, pady=10)

#-----------------------------------------------------------------------------------------
    def iniciar_simulacion(self):
        try:
            numero_procesos = int(self.entrada_procesos.get())
            quantum = int(self.entrada_quantum.get())
            tiempos_llegada = list(map(int, self.entrada_llegada.get().split(',')))
            tiempos_rafaga = list(map(int, self.entrada_rafaga.get().split(',')))

            # Validación de la longitud de las entradas
            if len(tiempos_llegada) != numero_procesos or len(tiempos_rafaga) != numero_procesos:
                raise ValueError(
                    "El número de tiempos de llegada y tiempos de ráfaga debe coincidir con el número de procesos.")

            planificador = PlanificadorRoundRobin(
                numero_procesos, quantum, tiempos_llegada, tiempos_rafaga)
            resultados = planificador.ejecutar_simulacion()

            self.mostrar_resultados(resultados)

        except ValueError as ve:
            self.mostrar_resultados(f"Error en la entrada: {ve}")
        except Exception as e:
            self.mostrar_resultados(f"Error: {e}")


    def mostrar_resultados(self, resultados):
        self.texto_resultados.config(state='normal')
        self.texto_resultados.delete('1.0', tk.END)
        self.texto_resultados.insert(tk.END, resultados)
        self.texto_resultados.config(state='disabled')


    def limpiar_pantalla(self):
        # Limpia todos los campos de entrada y el área de resultados.
        self.entrada_procesos.delete(0, tk.END)
        self.entrada_quantum.delete(0, tk.END)
        self.entrada_llegada.delete(0, tk.END)
        self.entrada_rafaga.delete(0, tk.END)
        self.texto_resultados.config(state='normal')
        self.texto_resultados.delete('1.0', tk.END)
        self.texto_resultados.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    app = Simulador(root)
    root.mainloop()
