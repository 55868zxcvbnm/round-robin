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
    # Constructor
    def __init__(self, master):
        self.master = master
        master.title("Simulador de Planificador de Procesos Round Robin")
        master.geometry("1200x800")
        self.processes = []# lista
        self.last_id = 0
        self.create_widgets()
    # metodos ↓↓↓
    def create_widgets(self):
        # Estilo general para widgets
        style = ttk.Style()
        style.configure('TButton', foreground='black', font=('Helvetica', 11, 'italic', 'bold'), width=18)
        style.configure('TLabel', background='#0D0D0D', foreground='white')
        style.configure('TFrame', background='#0D0D0D')

        # Frame principal
        main_frame = ttk.Frame(self.master, padding=12, style='TFrame')
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Título
        title_label = ttk.Label(main_frame, text="Simulador Round Robin", font=('Helvetica', 28, 'bold'), background='#2A8C82', anchor="center", foreground= 'white')
        title_label.pack(pady=15, fill=tk.X)

        # Frame izquierdo para agregar procesos y configuración
        left_frame = ttk.Frame(main_frame, padding=15,relief="solid", borderwidth=0)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)


        # Frame para añadir procesos
        add_process_frame = ttk.Frame(left_frame, padding=15)
        add_process_frame.pack(fill=tk.X, pady=15)

        # Etiqueta de "Añadir un nuevo proceso"
        ttk.Label(add_process_frame, text="Añadir un nuevo proceso:", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, padx=5, pady=5)

        # Campo de entrada para Tiempo de Llegada
        self.tiempos_llegada_entry = tk.Entry(add_process_frame, width=18)
        self.tiempos_llegada_entry.grid(row=1, column=0, padx=5, pady=5)
        self.set_placeholder(self.tiempos_llegada_entry, "Tiempo de Llegada")

        # Campo de entrada para Tiempo de Ráfaga
        self.tiempos_rafaga_entry = tk.Entry(add_process_frame, width=18)
        self.tiempos_rafaga_entry.grid(row=2, column=0, padx=5, pady=5)
        self.set_placeholder(self.tiempos_rafaga_entry, "    Tiempo Ráfaga")

        # Botones para agregar y limpiar procesos
        button_frame = ttk.Frame(add_process_frame)
        button_frame.grid(row=3, column=0, padx=5, pady=15)

        add_button = ttk.Button(button_frame, text="Añadir", command=self.add_process)
        add_button.pack(side=tk.LEFT, padx=5)

        clear_button = ttk.Button(button_frame, text="Limpiar",
                                command=self.clear_processes)
        clear_button.pack(side=tk.LEFT, padx=5)


        # Tabla de procesos
        self.processes_table = ttk.Treeview(left_frame, columns=(
            "ID", "Tiempo de Llegada", "Tiempo de Ráfaga"), show='headings')
        self.processes_table.heading("ID", text="ID")
        self.processes_table.heading(
            "Tiempo de Llegada", text="Tiempo de Llegada")
        self.processes_table.heading(
            "Tiempo de Ráfaga", text="Tiempo de Ráfaga")
        self.processes_table.column("ID", width=30, anchor=tk.CENTER)
        self.processes_table.column(
            "Tiempo de Llegada", width=50, anchor=tk.CENTER)
        self.processes_table.column(
            "Tiempo de Ráfaga", width=50, anchor=tk.CENTER)
        self.processes_table.pack(pady=5, fill=tk.BOTH, expand=True)

        # Frame de configuración de Round Robin
        config_frame = ttk.Frame(left_frame, padding=5)
        config_frame.pack(fill=tk.X, pady=10)

        ttk.Label(config_frame, text="Valor Quantum:", font=('Helvetica', 12, 'bold')).grid(row=0, column=0, padx=5)
        self.q_value_entry = tk.Entry(config_frame, width=5)
        self.q_value_entry.grid(row=0, column=1, padx=5)
        self.q_value_entry.insert(0, "2")

        solve_button = ttk.Button(config_frame, text="Iniciar Simulación", command=self.iniciar_simulacion)
        solve_button.grid(row=1, column=0, padx=10,pady=10)

        # Frame derecho para detalles de la simulación
        right_frame = ttk.Frame(main_frame, padding=15)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Detalles de la simulación
        ttk.Label(right_frame, text="Detalle de la Simulación",
                  font=('Helvetica', 16, 'bold')).pack(pady=15)
        self.salida_texto = tk.Text(right_frame, height=100, wrap='word')
        self.salida_texto.pack(pady=15, fill=tk.BOTH, expand=True)

        # Canvas para gráficos de Gantt en la parte inferior
        self.canvas_frame = ttk.Frame(left_frame)
        self.canvas_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, pady=15)
        self.canvas = tk.Canvas(self.canvas_frame, bg="white", height=20, borderwidth=2, relief="groove")
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
                self.canvas.create_rectangle(x_start + start_time * 15, y_start,
                                             x_start +
                                             (start_time + duration) *
                                             15, y_start + bar_height,
                                             fill='blue')
                self.canvas.create_text(x_start + (start_time + duration / 2) * 15, y_start + bar_height / 2,
                                        text=f"P{p.id}", fill="white")

        self.canvas.update_idletasks()
