# Basic Load Testing with Locust  
``Locust`` es una herramienta de pruebas de carga que permite simular múltiples usuarios accediendo a una API para medir su ``rendimiento bajo carga.``

## Paso a Paso para Configurar Locust
### **Instalación de Locust:**
- Primero, necesitas instalar Locust. Puedes hacerlo usando pip:

````
pip install locust
````

- **Crear un Archivo de Prueba:** Crea un archivo Python, por ejemplo locustfile.py, donde definirás el comportamiento de los usuarios simulados.

- **Definir el Comportamiento del Usuario:** En el archivo locustfile.py, define una clase que herede de HttpUser y especifique las tareas que los usuarios realizarán. 


Ejecutar Locust: Ejecuta Locust desde la línea de comandos:

````
locust -f locustfile.py --host=https://pokeapi.co
````
Acceder a la Interfaz Web de Locust: Abre un navegador web y ve a http://localhost:8089. Aquí podrás configurar el número de usuarios simulados y la tasa de incremento de usuarios.

### Iniciar la Prueba de Carga:
 Introduce el número de usuarios y la tasa de incremento, luego haz clic en "Start Swarming". Locust comenzará a simular usuarios accediendo a la PokeAPI y mostrará estadísticas en tiempo real sobre el rendimiento de la API.

