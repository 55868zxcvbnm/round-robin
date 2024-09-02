import unittest
from algorithm import PlanificadorRoundRobin


class PruebasPlanificadorRoundRobin(unittest.TestCase):

    def prueba_un_proceso(self):
        planificador = PlanificadorRoundRobin(
            num_procesos=1, quantum=5, tiempos_llegada=[0], tiempos_rafaga=[10])
        resultado = planificador.ejecutar_simulacion()
        self.assertIn("El proceso 1 completó su ejecución en el tiempo 10", resultado,
                      "Error: El tiempo de finalización del único proceso es incorrecto.")
        self.assertIn("Tiempo promedio de retorno: 10.0", resultado,
                      "Error: El tiempo promedio de retorno es incorrecto.")
        self.assertIn("Tiempo promedio de espera: 0.0", resultado,
                      "Error: El tiempo promedio de espera es incorrecto.")

    def prueba_varios_procesos(self):
        planificador = PlanificadorRoundRobin(num_procesos=3, quantum=4, tiempos_llegada=[
                                              0, 1, 2], tiempos_rafaga=[5, 9, 6])
        resultado = planificador.ejecutar_simulacion()
        self.assertIn("El proceso 1 completó su ejecución en el tiempo 13", resultado,
                      "Error: El tiempo de finalización del proceso 1 es incorrecto.")
        self.assertIn("El proceso 2 completó su ejecución en el tiempo 18", resultado,
                      "Error: El tiempo de finalización del proceso 2 es incorrecto.")
        self.assertIn("El proceso 3 completó su ejecución en el tiempo 20", resultado,
                      "Error: El tiempo de finalización del proceso 3 es incorrecto.")
        self.assertIn("Tiempo promedio de retorno: 15.67", resultado,
                      "Error: El tiempo promedio de retorno es incorrecto.")
        self.assertIn("Tiempo promedio de espera: 7.67", resultado,
                      "Error: El tiempo promedio de espera es incorrecto.")

    def prueba_quantum_mayor_que_rafaga(self):
        planificador = PlanificadorRoundRobin(
            num_procesos=2, quantum=10, tiempos_llegada=[0, 2], tiempos_rafaga=[6, 8])
        resultado = planificador.ejecutar_simulacion()
        self.assertIn("El proceso 1 completó su ejecución en el tiempo 6", resultado,
                      "Error: El tiempo de finalización del proceso 1 es incorrecto.")
        self.assertIn("El proceso 2 completó su ejecución en el tiempo 14", resultado,
                      "Error: El tiempo de finalización del proceso 2 es incorrecto.")
        self.assertIn("Tiempo promedio de retorno: 9.0", resultado,
                      "Error: El tiempo promedio de retorno es incorrecto.")
        self.assertIn("Tiempo promedio de espera: 3.0", resultado,
                      "Error: El tiempo promedio de espera es incorrecto.")

    def prueba_todos_procesos_mismo_tiempo_llegada(self):
        planificador = PlanificadorRoundRobin(num_procesos=3, quantum=3, tiempos_llegada=[
                                              0, 0, 0], tiempos_rafaga=[7, 4, 9])
        resultado = planificador.ejecutar_simulacion()
        self.assertIn("El proceso 1 completó su ejecución en el tiempo 19", resultado,
                      "Error: El tiempo de finalización del proceso 1 es incorrecto.")
        self.assertIn("El proceso 2 completó su ejecución en el tiempo 10", resultado,
                      "Error: El tiempo de finalización del proceso 2 es incorrecto.")
        self.assertIn("El proceso 3 completó su ejecución en el tiempo 22", resultado,
                      "Error: El tiempo de finalización del proceso 3 es incorrecto.")
        self.assertIn("Tiempo promedio de retorno: 17.0", resultado,
                      "Error: El tiempo promedio de retorno es incorrecto.")
        self.assertIn("Tiempo promedio de espera: 10.67", resultado,
                      "Error: El tiempo promedio de espera es incorrecto.")

    def prueba_proceso_llega_tarde(self):
        planificador = PlanificadorRoundRobin(num_procesos=3, quantum=4, tiempos_llegada=[
                                              0, 5, 8], tiempos_rafaga=[10, 5, 12])
        resultado = planificador.ejecutar_simulacion()
        self.assertIn("El proceso 1 completó su ejecución en el tiempo 20", resultado,
                      "Error: El tiempo de finalización del proceso 1 es incorrecto.")
        self.assertIn("El proceso 2 completó su ejecución en el tiempo 25", resultado,
                      "Error: El tiempo de finalización del proceso 2 es incorrecto.")
        self.assertIn("El proceso 3 completó su ejecución en el tiempo 29", resultado,
                      "Error: El tiempo de finalización del proceso 3 es incorrecto.")
        self.assertIn("Tiempo promedio de retorno: 22.67", resultado,
                      "Error: El tiempo promedio de retorno es incorrecto.")
        self.assertIn("Tiempo promedio de espera: 13.67", resultado,
                      "Error: El tiempo promedio de espera es incorrecto.")


if __name__ == '__main__':
    unittest.main()
