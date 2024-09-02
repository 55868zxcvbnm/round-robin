class Proceso:
    def __init__(self, id, rafaga, llegada):
        self.id = id
        self.rafaga = rafaga
        self.llegada = llegada
        self.rafaga_tmp = rafaga
        self.espera = 0
        self.retorno = 0
        self.finalizacion = 0
        self.estado = "Esperando"
        self.historial = []

    def actualizar_estado(self, nuevo_estado):
        """Actualiza el estado del proceso."""
        self.estado = nuevo_estado

    def reducir_rafaga_tmp(self, tiempo):
        """Reduce la ráfaga temporal del proceso."""
        self.rafaga_tmp -= tiempo
        if self.rafaga_tmp <= 0:
            self.estado = "Terminado"
        else:
            self.estado = "Esperando"


class PlanificadorRoundRobin:
    def __init__(self, num_procesos, quantum, tiempos_llegada, tiempos_rafaga):
        self.num_procesos = num_procesos
        self.quantum = quantum
        self.procesos = [Proceso(
            i + 1, tiempos_rafaga[i], tiempos_llegada[i]) for i in range(num_procesos)]

    def ordenar_procesos_por_tiempo_llegada(self):
        self.procesos.sort(key=lambda x: x.llegada)

    def ejecutar_simulacion(self):
        self.ordenar_procesos_por_tiempo_llegada()
        procesos_restantes = len(self.procesos)
        tiempo = 0
        cola_procesos = []
        siguiente_proceso = 0
        resultados = []

        while procesos_restantes > 0:
            resultados.append(f"Tiempo: {tiempo}")

            # Añadir procesos a la cola de listos cuando llegan
            while siguiente_proceso < len(self.procesos) and tiempo >= self.procesos[siguiente_proceso].llegada:
                resultados.append(
                    f"El proceso {self.procesos[siguiente_proceso].id} entró en la cola de listos.")
                cola_procesos.append(self.procesos[siguiente_proceso])
                siguiente_proceso += 1

            # Ejecutar el proceso en la cabeza de la cola
            if cola_procesos:
                proceso_en_ejecucion = cola_procesos.pop(0)
                proceso_en_ejecucion.actualizar_estado("Ejecutando")
                proceso_en_ejecucion.historial.append(
                    (tiempo, min(self.quantum, proceso_en_ejecucion.rafaga_tmp)))
                resultados.append(
                    f"El proceso {proceso_en_ejecucion.id} está siendo ejecutado.")

                tiempo_ejecucion = min(
                    self.quantum, proceso_en_ejecucion.rafaga_tmp)
                proceso_en_ejecucion.reducir_rafaga_tmp(tiempo_ejecucion)
                tiempo += tiempo_ejecucion

                if proceso_en_ejecucion.estado == "Terminado":
                    resultados.append(f"El proceso {
                                      proceso_en_ejecucion.id} completó su ejecución en el tiempo {tiempo}.")
                    proceso_en_ejecucion.finalizacion = tiempo
                    proceso_en_ejecucion.retorno = tiempo - proceso_en_ejecucion.llegada
                    proceso_en_ejecucion.espera = proceso_en_ejecucion.retorno - \
                        proceso_en_ejecucion.rafaga
                    procesos_restantes -= 1
                else:
                    cola_procesos.append(proceso_en_ejecucion)
            else:
                tiempo += 1

        # Calcular resultados finales
        total_retorno = sum(p.retorno for p in self.procesos)
        total_espera = sum(p.espera for p in self.procesos)
        promedio_retorno = total_retorno / len(self.procesos)
        promedio_espera = total_espera / len(self.procesos)

        resultados_str = '\n'.join(resultados)
        resultados_str += f"\n\nTiempo promedio de retorno: {
            promedio_retorno:.2f}"
        resultados_str += f"\nTiempo promedio de espera: {promedio_espera:.2f}"

        return resultados_str
