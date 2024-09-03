import tkinter as tk
from tkinter import ttk, messagebox
from algorithm import PlanificadorRoundRobin


class Process:
    def __init__(self, id, tiempos_llegada, tiempos_rafaga):
        self.id = id
        self.tiempos_llegada = tiempos_llegada
        self.tiempos_rafaga = tiempos_rafaga
        self.estado = 'esperando'
        self.tiempo_restante = tiempos_rafaga

    def actualizar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def reducir_tiempo_restante(self, tiempo):
        self.tiempo_restante -= tiempo
        if self.tiempo_restante <= 0:
            self.estado = 'terminado'


class Simulador:
    def __init__(self, master):
        self.master = master
        master.title("Simulador de Planificador de Procesos Round Robin")
        master.geometry("1200x800")

        self.processes = []
        self.last_id = 0

        self.create_widgets()

    def create_widgets(self):
        # Estilo moderno
        style = ttk.Style()
        style.configure('TButton', background='#4CAF50', foreground='black', padding=10, font=('Helvetica', 12))
        style.configure('TLabel', font=('Helvetica', 12))
        style.configure('TFrame', background='#f4f4f4')

        # Frame principal
        main_frame = ttk.Frame(self.master, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Título centrado
        title_label = ttk.Label(
            main_frame, text="Simulador Round Robin", font=('Helvetica', 24, 'bold'))
        title_label.pack(pady=10, anchor='center')

        # Frame de la izquierda
        left_frame = ttk.Frame(main_frame, padding=10)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Frame para añadir procesos
        add_process_frame = ttk.Frame(left_frame, padding=10)
        add_process_frame.pack(fill=tk.X, pady=10)

        ttk.Label(add_process_frame, text="Añadir un nuevo proceso:", font=(
            'Helvetica', 12, 'bold')).grid(row=0, column=0, padx=5)

        self.tiempos_llegada_entry = tk.Entry(add_process_frame, width=10)
        self.tiempos_llegada_entry.grid(row=0, column=1, padx=5)
        self.set_placeholder(self.tiempos_llegada_entry, "Tiempo de Llegada")

        self.tiempos_rafaga_entry = tk.Entry(add_process_frame, width=10)
        self.tiempos_rafaga_entry.grid(row=0, column=2, padx=5)
        self.set_placeholder(self.tiempos_rafaga_entry, "Tiempo de Ráfaga")

        button_frame = ttk.Frame(add_process_frame)
        button_frame.grid(row=0, column=3, padx=5)

        add_button = ttk.Button(
            button_frame, text="Añadir", command=self.add_process)
        add_button.pack(side=tk.LEFT, padx=5)

        clear_button = ttk.Button(
            button_frame, text="Limpiar", command=self.clear_processes)
        clear_button.pack(side=tk.LEFT, padx=5)

        # Tabla de procesos con tamaño fijo
        self.processes_table = ttk.Treeview(left_frame, columns=(
            "ID", "Tiempo de Llegada", "Tiempo de Ráfaga"), show='headings')
        self.processes_table.heading("ID", text="ID")
        self.processes_table.heading(
            "Tiempo de Llegada", text="Tiempo de Llegada")
        self.processes_table.heading(
            "Tiempo de Ráfaga", text="Tiempo de Ráfaga")

        # Definir ancho fijo para las columnas
        self.processes_table.column("ID", width=20, anchor=tk.CENTER)
        self.processes_table.column(
            "Tiempo de Llegada", width=50, anchor=tk.CENTER)
        self.processes_table.column(
            "Tiempo de Ráfaga", width=50, anchor=tk.CENTER)

        self.processes_table.pack(pady=5, fill=tk.X)

        # Frame de configuración de Round Robin
        config_frame = ttk.Frame(left_frame, padding=5)
        config_frame.pack(fill=tk.X, pady=10)

        ttk.Label(config_frame, text="Valor de Q:", font=(
            'Helvetica', 12, 'bold')).grid(row=0, column=0, padx=5)
        self.q_value_entry = tk.Entry(config_frame, width=10)
        self.q_value_entry.grid(row=0, column=1, padx=5)
        self.q_value_entry.insert(0, "2")

        solve_button = ttk.Button(
            config_frame, text="Resolver", command=self.iniciar_simulacion)
        solve_button.grid(row=0, column=2, padx=5)

        # Frame de la derecha para detalles de la simulación
        right_frame = ttk.Frame(main_frame, padding=10)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Frame para detalle de la simulación y área de texto
        detail_frame = ttk.Frame(right_frame)
        detail_frame.pack(fill=tk.BOTH, expand=True)

        self.detail_label = ttk.Label(
            detail_frame, text="Detalle de la Simulación", font=('Helvetica', 14, 'bold'))
        self.detail_label.pack(pady=10)

        #self.simulation_details = tk.Text(
         #   detail_frame, wrap=tk.WORD, height=10)
        #self.simulation_details.pack(expand=True, fill=tk.BOTH)

        # Información de tiempo
        self.info_label = ttk.Label(
            right_frame, text="", font=('Helvetica', 12))
        self.info_label.pack(pady=10)

        # Salida de Texto dentro del frame de detalles
        self.salida_texto = tk.Text(
            detail_frame, height=200, wrap='word')
        self.salida_texto.pack( pady = 10, fill=tk.BOTH)

        # Canvas para gráficos de Gantt en la parte inferior
        self.canvas_frame = ttk.Frame(left_frame)
        self.canvas_frame.pack(
            side=tk.BOTTOM, fill=tk.BOTH, expand=True, pady=10)

        self.canvas = tk.Canvas(self.canvas_frame, bg="white", height=40, borderwidth=2, relief="groove")
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def set_placeholder(self, entry, placeholder):
        entry.insert(0, placeholder)
        entry.bind("<FocusIn>", lambda event: self.on_entry_click(
            event, placeholder))
        entry.bind("<FocusOut>", lambda event: self.on_focusout(
            event, placeholder))

    def on_entry_click(self, event, placeholder):
        if event.widget.get() == placeholder:
            event.widget.delete(0, "end")
            event.widget.config(fg='black')

    def on_focusout(self, event, placeholder):
        if event.widget.get() == '':
            event.widget.insert(0, placeholder)
            event.widget.config(fg='grey')

    def add_process(self):
        try:
            tiempo_llegada = int(self.tiempos_llegada_entry.get())
            tiempo_rafaga = int(self.tiempos_rafaga_entry.get())
        except ValueError:
            messagebox.showerror(
                "Error", "Por favor ingrese valores numéricos válidos.")
            return

        self.last_id += 1
        new_process = Process(self.last_id, [tiempo_llegada], [tiempo_rafaga])
        self.processes.append(new_process)
        self.processes_table.insert("", "end", values=(
            new_process.id, tiempo_llegada, tiempo_rafaga))
        self.tiempos_llegada_entry.delete(0, "end")
        self.tiempos_rafaga_entry.delete(0, "end")

    def clear_processes(self):
        self.processes.clear()
        self.processes_table.delete(*self.processes_table.get_children())

    def iniciar_simulacion(self):
        tiempos_llegada = [p.tiempos_llegada[0] for p in self.processes]
        tiempos_rafaga = [p.tiempos_rafaga[0] for p in self.processes]
        quantum = int(self.q_value_entry.get())

        if not tiempos_llegada or not tiempos_rafaga:
            messagebox.showwarning(
                "Advertencia", "Por favor añada procesos antes de iniciar la simulación.")
            return

        planificador = PlanificadorRoundRobin(
            len(self.processes), quantum, tiempos_llegada, tiempos_rafaga)
        resultado = planificador.ejecutar_simulacion()

        self.salida_texto.delete(1.0, tk.END)
        self.salida_texto.insert(tk.END, resultado)

        # Limpiar canvas antes de dibujar
        self.canvas.delete("all")

        # Dibujar gráfico de Gantt
        y_start = 1
        x_start = 20
        bar_height = 20
        for p in planificador.procesos:
            for (start_time, duration) in p.historial:
                self.canvas.create_rectangle(x_start + start_time * 10, y_start,
                                             x_start +
                                             (start_time + duration) *
                                             10, y_start + bar_height,
                                             fill='blue')
                self.canvas.create_text(x_start + (start_time + duration / 2) * 10, y_start + bar_height / 2,
                                        text=f"P{p.id}", fill="white")

        self.canvas.update_idletasks()
