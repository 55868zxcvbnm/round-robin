# ---------------------------------------------
# Aquí se implementa el algoritmo Round Robin.
# ---------------------------------------------

class Proceso:
    def __init__(self, id, rafaga, llegada):
        self.id = id
        self.rafaga = rafaga
        self.llegada = llegada
        self.rafaga_tmp = rafaga
        self.espera = 0
        self.retorno = 0
        self.finalizacion = 0


class PlanificadorRoundRobin:
    def __init__(self, num_procesos, quantum, tiempos_llegada, tiempos_rafaga):
        self.num_procesos = num_procesos
        self.quantum = quantum
        self.procesos = [Proceso(i+1, tiempos_rafaga[i], tiempos_llegada[i])
                         for i in range(num_procesos)]

    def ordenar_procesos_por_tiempo_llegada(self, procesos):
        procesos.sort(key=lambda x: x.llegada)
        return procesos

    def ejecutar_simulacion(self):
        lista_procesos = self.ordenar_procesos_por_tiempo_llegada(
            self.procesos)
        procesos_restantes = len(lista_procesos)
        tiempo = 0
        cola_procesos = []
        proceso_en_ejecucion = None
        siguiente_proceso = 0
        resultados = []

        while procesos_restantes > 0:
            resultados.append(
                f"Tiempo: {tiempo} ")
            if len(lista_procesos) > siguiente_proceso and tiempo >= lista_procesos[siguiente_proceso].llegada:
                resultados.append(
                    f"El proceso {lista_procesos[siguiente_proceso].id} entró en la cola de listos.")
                cola_procesos.append(lista_procesos[siguiente_proceso])
                siguiente_proceso += 1
            else:
                if siguiente_proceso > 0 or len(cola_procesos) > 0:
                    if proceso_en_ejecucion == None:
                        proceso_en_ejecucion = cola_procesos.pop(0)
                        resultados.append(
                            f"El proceso {proceso_en_ejecucion.id} está siendo ejecutado.")

                    if proceso_en_ejecucion.rafaga_tmp >= self.quantum:
                        proceso_en_ejecucion.rafaga_tmp -= self.quantum
                        tiempo += self.quantum
                    else:
                        tiempo += proceso_en_ejecucion.rafaga_tmp
                        proceso_en_ejecucion.rafaga_tmp = 0

                    if proceso_en_ejecucion.rafaga_tmp < 1:
                        resultados.append(
                            f"El proceso {proceso_en_ejecucion.id} completó su ejecución en el tiempo {tiempo}.")
                        proceso_en_ejecucion.finalizacion = tiempo
                        proceso_en_ejecucion.retorno = tiempo - \
                            proceso_en_ejecucion.llegada
                        proceso_en_ejecucion.espera = proceso_en_ejecucion.retorno - \
                            proceso_en_ejecucion.rafaga
                        procesos_restantes -= 1
                        proceso_en_ejecucion = None
                    else:
                        cola_procesos.append(proceso_en_ejecucion)
                        proceso_en_ejecucion = None
                else:
                    tiempo += 1

        # Generar resultados finales
        total_retorno = sum(p.retorno for p in lista_procesos)
        total_espera = sum(p.espera for p in lista_procesos)
        promedio_retorno = total_retorno / len(lista_procesos)
        promedio_espera = total_espera / len(lista_procesos)

        resultados_str = '\n'.join(resultados)
        resultados_str += f"\n\nTiempo promedio de retorno: {promedio_retorno}"
        resultados_str += f"\nTiempo promedio de espera: {promedio_espera}"

        return resultados_str
