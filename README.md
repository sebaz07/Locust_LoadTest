### **Instalación de Locust:**
- Primero, necesitas instalar Locust. Puedes hacerlo usando pip:

```
pip install locust
```

- **Crear un Archivo de Prueba:** Crea un archivo Python, por ejemplo locustfile.py, donde definirás el comportamiento de los usuarios simulados.

- **Definir el Comportamiento del Usuario:** En el archivo locustfile.py, define una clase que herede de HttpUser y especifique las tareas que los usuarios realizarán.

### **Inicialización con Docker:**
- **Crear un Archivo Dockerfile:** Crea un archivo Dockerfile en el directorio raíz de tu proyecto con el siguiente contenido:

```
FROM locustio/locust
WORKDIR /app
COPY locustfile.py /app/
CMD ["locust", "-f", "locustfile.py", "--headless", "--host=https://pokeapi.co"]
```

- **Crear la Imagen Docker:** Ejecuta el siguiente comando en la terminal para crear la imagen Docker:

```
docker build -t mi-locust .
```

- **Ejecutar Locust con Docker:** Ejecuta el siguiente comando para iniciar Locust con Docker:

```
docker run -p 8089:8089 mi-locust
```

Acceder a la Interfaz Web de Locust: Abre un navegador web y ve a http://localhost:8089. Aquí podrás configurar el número de usuarios simulados y la tasa de incremento de usuarios.

### Iniciar la Prueba de Carga:
 Introduce el número de usuarios y la tasa de incremento, luego haz clic en "Start Swarming". Locust comenzará a simular usuarios accediendo a la PokeAPI y mostrará estadísticas en tiempo real sobre el rendimiento de la API.