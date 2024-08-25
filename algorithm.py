# ---------------------------------------------
# Aquí se implementa el algoritmo Round Robin.
# ---------------------------------------------

class Process:
    def __init__(self, id, burst, arrival):
        self.id = id
        self.burst = burst
        self.arrival = arrival
        self.burst_tmp = burst
        self.wait = 0
        self.return_ = 0
        self.ending = 0


class RoundRobinScheduler:
    def __init__(self, num_processes, quantum, arrival_times, burst_times):
        self.num_processes = num_processes
        self.quantum = quantum
        self.processes = [Process(i+1, burst_times[i], arrival_times[i])
                          for i in range(num_processes)]

    def order_process_for_time_arrival(self, processes):
        processes.sort(key=lambda x: x.arrival)
        return processes

    def run_simulation(self):
        process_list = self.order_process_for_time_arrival(self.processes)
        mirror_process = len(process_list)
        time = 0
        tail_processes = []
        currently_execution_proccess = None
        next_process = 0
        results = []

        while mirror_process > 0:
            results.append(
                f"*************************** Time: {time} ************************")
            if len(process_list) > next_process and time >= process_list[next_process].arrival:
                results.append(
                    f"Process {process_list[next_process].id} entered the ready queue.")
                tail_processes.append(process_list[next_process])
                next_process += 1
            else:
                if next_process > 0 or len(tail_processes) > 0:
                    if currently_execution_proccess is None:
                        currently_execution_proccess = tail_processes.pop(0)
                        results.append(
                            f"Process {currently_execution_proccess.id} is now being executed.")

                    if currently_execution_proccess.burst_tmp >= self.quantum:
                        currently_execution_proccess.burst_tmp -= self.quantum
                        time += self.quantum
                    else:
                        time += currently_execution_proccess.burst_tmp
                        currently_execution_proccess.burst_tmp = 0

                    if currently_execution_proccess.burst_tmp < 1:
                        results.append(
                            f"Process {currently_execution_proccess.id} completed at time {time}.")
                        currently_execution_proccess.ending = time
                        currently_execution_proccess.return_ = time - \
                            currently_execution_proccess.arrival
                        currently_execution_proccess.wait = currently_execution_proccess.return_ - \
                            currently_execution_proccess.burst
                        mirror_process -= 1
                        currently_execution_proccess = None
                    else:
                        tail_processes.append(currently_execution_proccess)
                        currently_execution_proccess = None
                else:
                    time += 1

        # Generate final results
        total_return = sum(p.return_ for p in process_list)
        total_wait = sum(p.wait for p in process_list)
        average_return = total_return / len(process_list)
        average_wait = total_wait / len(process_list)

        result_str = '\n'.join(results)
        result_str += f"\n\nAverage return time: {average_return}"
        result_str += f"\nAverage wait time: {average_wait}"

        return result_str
