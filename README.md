# Simulador de Planificación de Procesos Round Robin

Este proyecto es un simulador que implementa el algoritmo de planificación de procesos Round Robin. Permite a los usuarios visualizar cómo se gestionan los procesos en un sistema operativo utilizando este algoritmo.

## Instalación

1. Asegúrate de tener Python 3.x instalado.
2. Clona este repositorio.
3. Navega al directorio del proyecto.
4. Ejecuta `pip install -r requirements.txt` para instalar las dependencias.

## Estructura del Proyecto

round_robin_simulator/
    main.py                    - Archivo principal que ejecuta el simulador
    ui.py                      - Archivo para la interfaz gráfica utilizando Tkinter
    algorithm.py               - Archivo que contiene la implementación del algoritmo Round Robin
    utils.py                   - Archivo con funciones auxiliares (e.g., para validaciones)

    assets/                    - Carpeta para recursos adicionales
        icons/                 - Iconos para la interfaz
        images/                - Imágenes utilizadas en el simulador

    tests/                     - Carpeta para pruebas
        test_algorithm.py      - Pruebas para el módulo del algoritmo
        test_utils.py          - Pruebas para funciones auxiliares

    README.md                  - Archivo de documentación del proyecto

## Archivos Principales

#### `main.py`

- **Descripción:**
  Este es el archivo principal del proyecto. Su función es inicializar e iniciar la aplicación del simulador. Cuando se ejecuta este archivo, se instancia la clase principal de la interfaz gráfica (`Application`) y se llama al método `run` para mostrar la ventana de la aplicación.
- **Funcionalidad:**
  Actúa como el punto de entrada del simulador, coordinando la ejecución del mismo.

#### `ui.py`

- **Descripción:**
  Este archivo contiene todo el código relacionado con la interfaz gráfica de usuario (GUI) del simulador. Utiliza el módulo Tkinter de Python para construir la interfaz visual que los usuarios interactúan.
- **Funcionalidad:**
  Permite a los usuarios ingresar parámetros como el número de procesos y el tiempo de quantum, y visualizar los resultados de la simulación. Aquí se manejan los eventos de la interfaz y se comunica con el módulo que implementa el algoritmo para obtener los resultados de la simulación.

#### `algorithm.py`

- **Descripción:**
  Este archivo implementa el algoritmo Round Robin, que es el núcleo del simulador. Contiene la lógica que gestiona cómo los procesos son planificados y ejecutados en función del quantum y otros parámetros.
- **Funcionalidad:**
  Ejecuta el algoritmo Round Robin, simulando la planificación de procesos y devolviendo los resultados en forma de texto que describe cómo cada proceso fue manejado.

#### `utils.py`

- **Descripción:**
  Este archivo contiene funciones auxiliares o utilitarias que no forman parte directa de la interfaz ni del algoritmo, pero que son necesarias para tareas específicas dentro del proyecto, como validaciones.
- **Funcionalidad:**
  Provee funciones adicionales que ayudan a simplificar el código principal y mantener la modularidad. Por ejemplo, puede validar entradas de usuario o realizar transformaciones de datos.

### Carpetas

#### `assets/`

- **Descripción:**
  Esta carpeta contiene recursos adicionales que la aplicación podría necesitar, como iconos y imágenes que se utilizan en la interfaz gráfica.
- **Funcionalidad:**
  Facilita la organización de todos los archivos de recursos gráficos para que sean fácilmente accesibles desde cualquier parte del proyecto.

##### `icons/`

- **Descripción:**
  Subcarpeta específica para almacenar iconos que pueden ser utilizados en botones, menús, o cualquier otro componente de la GUI.
- **Funcionalidad:**
  Mantiene los iconos organizados y separados de otros tipos de recursos.

##### `images/`

- **Descripción:**
  Subcarpeta para almacenar imágenes utilizadas en la interfaz del simulador, como logotipos o fondos.
- **Funcionalidad:**
  Asegura que todas las imágenes estén centralizadas y accesibles, facilitando su gestión.

#### `tests/`

- **Descripción:**
  Carpeta dedicada a almacenar todos los archivos de pruebas unitarias. Aquí se verifican las funcionalidades del simulador para asegurar que todo funcione como se espera.
- **Funcionalidad:**
  Contiene los casos de prueba que permiten verificar el correcto funcionamiento del algoritmo y otras partes del código, asegurando la calidad del software.

##### `test_algorithm.py`

- **Descripción:**
  Archivo específico para pruebas unitarias del módulo `algorithm.py`.
- **Funcionalidad:**
  Valida que el algoritmo Round Robin funcione correctamente con diferentes entradas y escenarios.

##### `test_utils.py`

- **Descripción:**
  Archivo para pruebas unitarias del módulo `utils.py`.
- **Funcionalidad:**
  Verifica que las funciones auxiliares, como las de validación, operen correctamente bajo diversas condiciones.
