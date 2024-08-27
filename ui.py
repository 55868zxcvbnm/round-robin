# ------------------------------------------------------------
# Aquí se define la interfaz del usuario utilizando Tkinter.
# ------------------------------------------------------------

import tkinter as tk
from algorithm import PlanificadorRoundRobin


class SimuladorRoundRobinUI:
    def __init__(self, master):
        self.master = master
        master.title("Simulador de Planificador de Procesos Round Robin")

        # Etiquetas y Entradas para la entrada de procesos
        self.etiqueta_procesos = tk.Label(master, text="Número de Procesos")
        self.etiqueta_procesos.grid(row=0, column=0)

        self.entrada_procesos = tk.Entry(master)
        self.entrada_procesos.grid(row=0, column=1)

        self.etiqueta_quantum = tk.Label(master, text="Quantum")
        self.etiqueta_quantum.grid(row=1, column=0)

        self.entrada_quantum = tk.Entry(master)
        self.entrada_quantum.grid(row=1, column=1)

        # Nuevas etiquetas y entradas para tiempos de llegada y ráfaga
        self.etiqueta_llegada = tk.Label(
            master, text="Tiempos de Llegada (separados por comas)")
        self.etiqueta_llegada.grid(row=2, column=0)

        self.entrada_llegada = tk.Entry(master)
        self.entrada_llegada.grid(row=2, column=1)

        self.etiqueta_rafaga = tk.Label(
            master, text="Tiempos de Ráfaga (separados por comas)")
        self.etiqueta_rafaga.grid(row=3, column=0)

        self.entrada_rafaga = tk.Entry(master)
        self.entrada_rafaga.grid(row=3, column=1)

        # Botón para iniciar la simulación
        self.boton_iniciar = tk.Button(
            master, text="Iniciar Simulación", command=self.iniciar_simulacion)
        self.boton_iniciar.grid(row=4, column=0, columnspan=2)

        # Botón para limpiar la pantalla
        self.boton_limpiar = tk.Button(
            master, text="Limpiar Pantalla", command=self.limpiar_pantalla)
        self.boton_limpiar.grid(row=4, column=1, columnspan=2)

        # Caja de texto para mostrar los resultados
        self.texto_resultados = tk.Text(
            master, state='disabled', width=50, height=20)
        self.texto_resultados.grid(row=5, column=0, columnspan=2)

    def iniciar_simulacion(self):
        try:
            numero_procesos = int(self.entrada_procesos.get())
            quantum = int(self.entrada_quantum.get())
            tiempos_llegada = list(
                map(int, self.entrada_llegada.get().split(',')))
            tiempos_rafaga = list(
                map(int, self.entrada_rafaga.get().split(',')))

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
        """Limpia todos los campos de entrada y el área de resultados."""
        self.entrada_procesos.delete(0, tk.END)
        self.entrada_quantum.delete(0, tk.END)
        self.entrada_llegada.delete(0, tk.END)
        self.entrada_rafaga.delete(0, tk.END)
        self.texto_resultados.config(state='normal')
        self.texto_resultados.delete('1.0', tk.END)
        self.texto_resultados.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    app = SimuladorRoundRobinUI(root)
    root.mainloop()
