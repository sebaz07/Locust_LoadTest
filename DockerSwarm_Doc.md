# Principal diferencia entre docker compose y docker swarm
`Docker compose:` define un grupo de servicios que funcionan juntos y se ejecutan en una sola maquina. estos servicios se agrupan y se gestionan desde un solo archivo *Docker-compose.yml*

``Docker swarm:`` Podemos crear multiples clusters llamados **stacks** que consisten en varios servicios distribuidos entre diferentes nodos (maquinas). cada stack puede tener muchos contenedores que trabajen juntos y docker swarm se encarga de distribuirlos por los nodos del cluster de forma automatica.  

*Recordemos que un nodo de un cluster se refiere a una maquina o una instancia*


# Inicializar proyecto con docker swarm
En primer lugar se debe utilizar el comando

````
Docker swarm init
````

En caso que querramos cerrar swarm se utiliza el siguiente comando: 
````
docker swarm leave --force
````

Antes de continuar es necesario recordar algunos comandos
- `Docker service ls: ` Muestra todos los servicios en ejecucion dentro de l cluster swarm.
- `docker stack ls`
- `docker stack rm my_stack`
- `docker service scale nombre_servicio=numero_replicas` : aumenta el numero de replicas de un servicio

Para construir el proyecto a base del archivo `Docker-compose` se ejecuta el siguiente comando.
````
docker stack deploy -c docker-compose.yml locust  #locust se refiere al stack
````

Para detener y eliminar la pila(stack)
````
docker stack rm locust #locust es el nombre el stack
````


## Estructura

El ejemplo se ejecuta de la siguiente forma:

1. Se crea una pila llamada locust
2. la Pila contiene 3 servicios dentro que fueron definidos en el archivo .yml (visualizer,master, worker)
3. En el archivo .yml se definio que el servicio worker tendra 5 replicas
4. El servicio master de locust distribuira la carga entre las 5 replicas siempre y cuando sea necesario.

- **Nota:** Cuando se inicializa docker swarm, se crea automaticamente una red llamada `ingress` 