
#utilizamos el modulo de cola de phyton

import heapq
#test con la clase personaje
class Personaje:
    def __init__(self,nombre:str,vida:int,raza:str,estado:str,ki:int,max_ki,transformaciones:None,transformacion_inicial,habilidades:None,exp,max_exp,nivel_de_poder,nivel:int=1,max_ki_base:int=10000):
        
        self.nombre = nombre
        self.vida = vida
        self.raza = raza
        self.estado = estado
        self.ki = ki
        self.max_ki = max_ki
        self.transformaciones = transformaciones
        self.transformacion_actual =transformacion_inicial 
        self.habilidades = habilidades
        self.exp = exp
        self.max_exp = max_exp
        self.nivel_de_poder = nivel_de_poder #este parametro se usara
        self.nivel = nivel
        self.max_ki_base = max_ki_base

    def __str__(self):
        """
        Representación en texto del personaje.
        """
        return f"{self.nombre} (Nivel de Poder: {self.nivel_de_poder})"
    

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

if __name__ == "__main__":


    # Crear personajes
    goku = Personaje("Goku", 1000, "Saiyajin", "Normal", 500, 1000, None,
                     "Base", None, 0, 100, 9000)
    vegeta = Personaje("Vegeta", 1000, "Saiyajin", "Normal", 400, 900, None,
                       "Base", None, 0, 100, 8500)

    # Crear cola de prioridad
    cola = ColaDePrioridad()
    cola.agregar_personaje(goku)
    cola.agregar_personaje(vegeta)

    # Simular enfrentamientos
    while not cola.esta_vacia():
        personaje = cola.siguiente_enfrentamiento()
        print(f"¡Enfrentamiento con: {personaje}!")




