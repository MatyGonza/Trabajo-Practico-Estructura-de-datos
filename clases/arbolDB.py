





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
        if personaje.nivel_de_poder < nodo.personaje.nivel_de_poder:
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
    def buscar_personaje(self, nivel_de_poder):
        return self._buscar_personaje_recursivo(self.raiz, nivel_de_poder)
    
    def _buscar_personaje_recursivo(self, nodo, nivel_de_poder):
        # Si hemos llegado a un nodo vacío, significa que el personaje no está en el árbol
        if nodo is None:
            return None
        if nodo.personaje.nivel_de_poder == nivel_de_poder:
            return nodo.personaje
        elif nivel_de_poder < nodo.personaje.nivel_de_poder:
            return self._buscar_personaje_recursivo(nodo.izquierda, nivel_de_poder)
        else:
            return self._buscar_personaje_recursivo(nodo.derecha, nivel_de_poder)
 
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
# Método para mostrar todas las ramas desde la raíz hasta las hojas
    def mostrar_ramas(self):
        if self.raiz is None:
            print("El árbol está vacío.")
        else:
            print("Ramas del árbol:")
            ramas = []
            self._mostrar_ramas_recursivo(self.raiz, [], ramas)
            for rama in ramas:
                print(" -> ".join([f"{nodo.nombre} (Poder: {nodo.nivel_de_poder})" for nodo in rama]))

    def _mostrar_ramas_recursivo(self, nodo, camino_actual, ramas):
        if nodo is not None:
            # Agregar el nodo actual al camino
            camino_actual.append(nodo.personaje)
            # Si es un nodo hoja, guardar el camino actual como una rama
            if nodo.izquierda is None and nodo.derecha is None:
                ramas.append(list(camino_actual))
            else:
                # Continuar con los hijos izquierdo y derecho
                self._mostrar_ramas_recursivo(nodo.izquierda, camino_actual, ramas)
                self._mostrar_ramas_recursivo(nodo.derecha, camino_actual, ramas)
            # Eliminar el nodo actual al regresar (backtracking)
            camino_actual.pop()
