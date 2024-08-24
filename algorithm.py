# ---------------------------------------------
# Aquí se implementa el algoritmo Round Robin.
# ---------------------------------------------

def round_robin(num_processes, quantum):
    # Simulación básica del algoritmo Round Robin
    processes = list(range(num_processes))
    queue = processes[:]
    result = []
    time = 0

    while queue:
        process = queue.pop(0)
        burst_time = min(quantum, 10)  # Supongamos que cada proceso tiene un tiempo de ráfaga de 10 unidades
        result.append(f"Proceso {process} ejecutado por {burst_time} unidades de tiempo.")
        time += burst_time
        if burst_time < 10:
            result.append(f"Proceso {process} completado.")
        else:
            queue.append(process)

    return "\n".join(result)
