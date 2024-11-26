import heapq
#usaremos un grafo con matriz de adyacencia
class GrafoDragonBall:
    def __init__(self, planetas):
        """
        Inicializa el grafo con una lista de planetas.
        Crea una matriz de adyacencia donde cada celda almacena el peso (valor) de la ruta.
        Si no hay ruta, el valor será 0.
        """
        self.planetas = planetas  # Lista de planetas (nodos)
        self.num_planetas = len(planetas)
        # Crear una matriz de adyacencia inicializada en 0
        self.matriz_adyacencia = [[0 for _ in range(self.num_planetas)] for _ in range(self.num_planetas)]

    def agregar_ruta(self, origen, destino, peso):
        """
        Agrega una ruta entre dos planetas con un peso (valor) asociado.
        Parámetros:
            - origen: nombre del planeta de inicio.
            - destino: nombre del planeta de destino.
            - peso: valor asociado a la ruta (por ejemplo, distancia o tiempo).
        """
        if origen in self.planetas and destino in self.planetas:
            i = self.planetas.index(origen)  # Índice del planeta de origen
            j = self.planetas.index(destino)  # Índice del planeta de destino
            self.matriz_adyacencia[i][j] = peso  # Establece el peso de la ruta
            self.matriz_adyacencia[j][i] = peso  # Grafo no dirigido: ruta es bidireccional
        else:
            print("Uno o ambos planetas no existen en el grafo.")

    def mostrar_rutas(self):
        """
        Muestra todas las rutas espaciales y sus pesos.
        Recorre la matriz de adyacencia para identificar las conexiones.
        """
        print("Rutas espaciales entre planetas (con pesos):")
        for i, origen in enumerate(self.planetas):
            for j, destino in enumerate(self.planetas):
                peso = self.matriz_adyacencia[i][j]
                if peso > 0:  # Solo muestra rutas con peso mayor a 0
                    print(f"Ruta entre {origen} y {destino} con peso {peso}")

    def obtener_peso(self, origen, destino):
        """
        Devuelve el peso de la ruta entre dos planetas, si existe.
        Parámetros:
            - origen: nombre del planeta de inicio.
            - destino: nombre del planeta de destino.
        Retorna:
            - El peso de la ruta o None si no existe.
        """
        if origen in self.planetas and destino in self.planetas:
            i = self.planetas.index(origen)
            j = self.planetas.index(destino)
            return self.matriz_adyacencia[i][j]
        return None
    
    def dfs(self, origen, destino):
        """
        Algoritmo DFS para encontrar un camino entre dos planetas.

        Parámetros:
            - origen: Planeta de inicio.
            - destino: Planeta de destino.

        Retorno:
            - Una lista con los nombres de los planetas en el camino encontrado
            o None si no hay camino.
        """
        def dfs_recursivo(actual, destino, visitados, camino):
            """
            Función recursiva que realiza la búsqueda en profundidad.

            Parámetros:
                - actual: Índice del nodo actual.
                - destino: Índice del nodo de destino.
                - visitados: Conjunto de nodos ya visitados.
                - camino: Lista que almacena el camino actual.

            Retorno:
                - Lista con el camino encontrado o None si no hay camino.
            """
            if actual == destino:  # Caso base: hemos llegado al destino
                return camino
            visitados.add(actual)  # Marcar el nodo como visitado
            # Explorar los vecinos del nodo actual
            for vecino_idx, peso in enumerate(self.matriz_adyacencia[actual]):
                if peso > 0 and vecino_idx not in visitados:  # Si hay conexión y no está visitado
                    resultado = dfs_recursivo(vecino_idx, destino, visitados, camino + [vecino_idx])
                    if resultado:  # Si encontramos un camino, lo devolvemos
                        return resultado
            return None  # No se encontró un camino desde este nodo

    # Obtener índices de los planetas
        origen_idx = self.planetas.index(origen)
        destino_idx = self.planetas.index(destino)
        visitados = set()  # Conjunto de nodos visitados
        camino = dfs_recursivo(origen_idx, destino_idx, visitados, [origen_idx])
        return [self.planetas[i] for i in camino] if camino else None
    
    def bfs(self, origen, destino):
        """
        Algoritmo BFS para encontrar el camino más corto entre dos planetas.

        Parámetros:
            - origen: Planeta de inicio.
            - destino: Planeta de destino.

        Retorno:
            - Una lista con los nombres de los planetas en el camino más corto
            o None si no hay camino.
        """
        from collections import deque

        # Obtener índices de los planetas
        origen_idx = self.planetas.index(origen)
        destino_idx = self.planetas.index(destino)
        visitados = set()  # Conjunto para rastrear nodos visitados
        cola = deque([[origen_idx]])  # Cola de caminos, cada elemento es una lista que representa un camino

        while cola:  # Mientras haya caminos por explorar
            camino = cola.popleft()  # Obtener el primer camino de la cola
            actual = camino[-1]  # Último nodo en el camino actual
            if actual == destino_idx:  # Si llegamos al destino, devolvemos el camino
                return [self.planetas[i] for i in camino]
            if actual not in visitados:  # Si el nodo no ha sido visitado
                visitados.add(actual)  # Marcarlo como visitado
                # Añadir a la cola nuevos caminos que incluyan a los vecinos no visitados
                for vecino_idx, peso in enumerate(self.matriz_adyacencia[actual]):
                    if peso > 0 and vecino_idx not in visitados:
                        cola.append(camino + [vecino_idx])  # Extender el camino actual
        return None  # Si la cola está vacía y no se encontró el destino
    
    def dijkstra(self, origen):
        """
        Aplica el algoritmo de Dijkstra para encontrar el camino más corto desde el planeta de origen
        hacia todos los demás planetas en el grafo.

        Parámetros:
            - origen: El planeta de inicio (nodo origen).

        Retorno:
            - Un diccionario con las distancias más cortas desde el origen a todos los planetas.
        """
        # Inicializamos las distancias como infinito
        distancias = {planeta: float('inf') for planeta in self.planetas}
        distancias[origen] = 0  # La distancia al planeta de origen es 0

        # Usamos una cola de prioridad para obtener el siguiente nodo más cercano
        cola_prioridad = [(0, origen)]  # (distancia, nodo)

        while cola_prioridad:
            # Obtener el planeta con la menor distancia
            distancia_actual, planeta_actual = heapq.heappop(cola_prioridad)

            # Si la distancia del nodo actual ya es mayor que la registrada, ignoramos
            if distancia_actual > distancias[planeta_actual]:
                continue

            # Recorremos los vecinos del planeta actual
            indice_actual = self.planetas.index(planeta_actual)
            for vecino_idx, peso in enumerate(self.matriz_adyacencia[indice_actual]):
                if peso > 0:  # Si hay una ruta entre los planetas
                    vecino = self.planetas[vecino_idx]
                    nueva_distancia = distancia_actual + peso
                    # Si encontramos una distancia más corta, actualizamos
                    if nueva_distancia < distancias[vecino]:
                        distancias[vecino] = nueva_distancia
                        heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

        return distancias





#Creacion del universo
#se va a utlizar para el torneo

universo_dragonball =  ["Tierra","Namek","Vegeta","Planeta Kaio","Reino de los demonios","Planeta de Bills"]
grafo = GrafoDragonBall(universo_dragonball)
grafo.agregar_ruta("Tierra","Namek",40)
grafo.agregar_ruta("Namek","Vegeta",70)
grafo.agregar_ruta("Tierra","Reino de los demonios",60)
grafo.agregar_ruta("Vegeta","Planeta Kaio",30)
grafo.agregar_ruta("Tierra","Planeta de Bills",200)




