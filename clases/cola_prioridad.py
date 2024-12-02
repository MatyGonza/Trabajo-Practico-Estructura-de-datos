
import heapq

    

# Clase que implementa una cola de prioridades utilizando un heap binario
class ColaDePrioridad:
    def __init__(self):
        """
        Inicializa una cola de prioridades con un heap vacío.
        """
        self.heap = []  # Lista que usaremos como heap binario

    def agregar_personaje(self, personaje):
        """
        Agrega un personaje al heap con prioridad basada en su nivel de poder.
        Negamos el nivel de poder para convertir el min-heap en max-heap.
        """
        heapq.heappush(self.heap, (-personaje.nivel_de_poder, personaje))

    def siguiente_enfrentamiento(self):
        """
        Retira y devuelve al personaje con el mayor nivel de poder.
        Si el heap está vacío, devuelve None.
        """
        if self.heap:
            return heapq.heappop(self.heap)[1]  # Sacamos el personaje (índice 1)
        else:
            return None

    def esta_vacia(self):
        """
        Verifica si la cola de prioridades está vacía.
        """
        return len(self.heap) == 0    




