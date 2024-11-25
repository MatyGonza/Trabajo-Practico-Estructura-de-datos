# Se define la clase "Personaje" que contendrá como atributos el nombre y nivel de poder de los personajes. 
#class Personaje:
    #def __init__(self, nombre, nivel_poder):
        #self.nombre = nombre
        #self.nivel_poder = nivel_poder





# Se define la estructura de cada nodo del árbol binario. Cada nodo contendrá la información del personaje (nombre y nivel de poder) y las referencias a sus hijos (izquierdo y derecho).
class Nodo:
    def __init__(self, personaje):
        """
        El nodo contiene los atributos un personaje y dos hijos,
        uno a la izquierda y otro a la izquierda.

        """
        self.personaje = personaje
        self.izquierda = None 
        self.derecha = None

# Se crea la clase del árbol binario, la cual se encargará de gestionar la inserción de nuevos nodos y la búsqueda de personajes.
# Para comparar valores, se tomará como parámetro el nivel de poder. Es decir, si el nivel de poder del nuevo personaje es menor que el del nodo actual, se colocará en el subárbol izquierdo. De lo contrario, se insertará en el derecho.
class ArbolBinario:
    def __init__(self):
        self.raiz = None

# Método de inserción para agregar personajes al árbol, utilizando un método recursivo que ubica al nodo correcto según el nivel de poder.
    def insertar(self, personaje):
        if self.raiz is None:
            self.raiz : Nodo
        else:
            self._insertar_recursivo(self.raiz, personaje)
    
    def _insertar_recursivo(self, nodo, personaje):
        #Si el nivel de poder del personaje es menor que el del nodo actual
        if personaje.nivel_poder < nodo.personaje.nivel_poder:
            if nodo.izquierda is None:
                # Si el hijo izquierdo está vacío, colocamos al personaje allí
                nodo.izquierda = Nodo(personaje)
            else:
                # Si el hijo izquierdo ya tiene un nodo, seguimos buscando recursivamente en la izquierda
                self._insertar_recursivo(nodo.izquierda, personaje)
        else:
            # Si el nivel de poder del personaje es mayor o igual, lo insertamos en el subárbol derecho
            if nodo.derecha is None:
                # Si el hijo derecho está vacío, colocamos al personaje allí
                nodo.derecha = Nodo(personaje)
            else:
                 # Si el hijo derecho ya tiene un nodo, seguimos buscando recursivamente en la derecha
                self._insertar_recursivo(nodo.derecha, personaje)

# Método de búsqueda que permite encontrar personajes según su nivel de poder, utilizando un método recursivo.
    def buscar_personaje(self, nivel_poder):
        return self._buscar_personaje_recursivo(self.raiz, nivel_poder)
    
    def _buscar_personaje_recursivo(self, nodo, nivel_poder):
        # Si hemos llegado a un nodo vacío, significa que el personaje no está en el árbol
        if nodo is None:
            return None
        if nodo.personaje.nivel_poder == nivel_poder:
            return nodo.personaje
        elif nivel_poder < nodo.personaje.nivel_poder:
            return self._buscar_personaje_recursivo(nodo.izquierda, nivel_poder)
        else:
            return self._buscar_personaje_recursivo(nodo.derecha, nivel_poder)
 
# Método que permite acceder a los personajes en el árbol ordenados según su nivel de poder (forma ascendente).  
# Llama al método inorden que recorre el árbol y llena la lista con los nodos en el orden correcto.     
    def obtener_personajes_poder(self):
        personajes = []
        self._inorden(self.raiz, personajes)
        return personajes
    
# Método de recorrido en orden que devuelve los personajes en orden ascendente según su nivel de poder.
# Primero recorre el subárbol izquierdo, luego el nodo actual, y finalmente el subárbol derecho.
    def _inorden(self, nodo, lista):
        if nodo is not None:
            self._inorden(nodo.izquierda, lista)
            lista.append(nodo.personaje)
            self._inorden(nodo.derecha, lista)
            