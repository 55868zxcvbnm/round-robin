# ------------------------------------------------------------
# Aquí se define la interfaz del usuario utilizando Tkinter.
# ------------------------------------------------------------

import tkinter as tk
from algorithm import RoundRobinScheduler


class RoundRobinSimulatorUI:
    def __init__(self, master):
        self.master = master
        master.title("Round Robin Process Scheduler Simulator")

        # Labels and Entries for process input
        self.processes_label = tk.Label(master, text="Number of Processes")
        self.processes_label.grid(row=0, column=0)

        self.processes_entry = tk.Entry(master)
        self.processes_entry.grid(row=0, column=1)

        self.quantum_label = tk.Label(master, text="Quantum")
        self.quantum_label.grid(row=1, column=0)

        self.quantum_entry = tk.Entry(master)
        self.quantum_entry.grid(row=1, column=1)

        # New labels and entries for arrival time and burst time
        self.arrival_label = tk.Label(
            master, text="Arrival Times (comma-separated)")
        self.arrival_label.grid(row=2, column=0)

        self.arrival_entry = tk.Entry(master)
        self.arrival_entry.grid(row=2, column=1)

        self.burst_label = tk.Label(
            master, text="Burst Times (comma-separated)")
        self.burst_label.grid(row=3, column=0)

        self.burst_entry = tk.Entry(master)
        self.burst_entry.grid(row=3, column=1)

        # Start button
        self.start_button = tk.Button(
            master, text="Start Simulation", command=self.start_simulation)
        self.start_button.grid(row=4, column=0, columnspan=2)

        # Button to clear the screen
        self.clear_button = tk.Button(
            master, text="Clear Screen", command=self.clear_screen)
        self.clear_button.grid(row=4, column=1, columnspan=2)

        # Textbox to display results
        self.results_text = tk.Text(
            master, state='disabled', width=50, height=20)
        self.results_text.grid(row=5, column=0, columnspan=2)

    def start_simulation(self):
        try:
            number_processes = int(self.processes_entry.get())
            quantum = int(self.quantum_entry.get())
            arrival_times = list(map(int, self.arrival_entry.get().split(',')))
            burst_times = list(map(int, self.burst_entry.get().split(',')))

            # Validation of input lengths
            if len(arrival_times) != number_processes or len(burst_times) != number_processes:
                raise ValueError(
                    "Number of arrival times and burst times must match the number of processes.")

            scheduler = RoundRobinScheduler(
                number_processes, quantum, arrival_times, burst_times)
            results = scheduler.run_simulation()

            self.display_results(results)

        except ValueError as ve:
            self.display_results(f"Input Error: {ve}")
        except Exception as e:
            self.display_results(f"Error: {e}")

    def display_results(self, results):
        self.results_text.config(state='normal')
        self.results_text.delete('1.0', tk.END)
        self.results_text.insert(tk.END, results)
        self.results_text.config(state='disabled')

    def clear_screen(self):
        """Clear all the input fields and the result display."""
        self.processes_entry.delete(0, tk.END)
        self.quantum_entry.delete(0, tk.END)
        self.arrival_entry.delete(0, tk.END)
        self.burst_entry.delete(0, tk.END)
        self.results_text.config(state='normal')
        self.results_text.delete('1.0', tk.END)
        self.results_text.config(state='disabled')


if __name__ == "__main__":
    root = tk.Tk()
    app = RoundRobinSimulatorUI(root)
    root.mainloop()
