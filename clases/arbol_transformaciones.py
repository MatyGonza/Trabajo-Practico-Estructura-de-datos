
#Nodo del arbol general
class NodoTransformacion:
    def __init__(self, nombre: str, ki_necesario: int, transformacion_requerida: str, multiplicador_nivel_de_poder: float):
        self.nombre = nombre
        self.ki_necesario = ki_necesario
        self.transformacion_requerida = transformacion_requerida
        self.multiplicador_nivel_de_poder = multiplicador_nivel_de_poder  # Multiplica el nivel de poder
        self.hijo = None  # Primer hijo (enlace a la siguiente transformación jerárquica)
        self.hermano = None  # Hermano (otro nodo al mismo nivel)

    def agregar_hijo(self, nodo_hijo):
        """Agrega un nodo hijo. Si ya hay hijos, lo enlaza como último hermano."""
        if not self.hijo:
            self.hijo = nodo_hijo
        else:
            actual = self.hijo
            while actual.hermano:
                actual = actual.hermano
            actual.hermano = nodo_hijo

#Arbol general de las tranformaciones
class ArbolTransformaciones:
    def __init__(self, nodo_raiz: NodoTransformacion):
        self.raiz = nodo_raiz

    def mostrar_arbol(self, nodo=None, nivel=0):
        """Muestra el árbol de manera jerárquica usando enlaces."""
        if nodo is None:
            nodo = self.raiz
        print(f"{nodo.nombre} (Ki: {nodo.ki_necesario}, Multiplicador: x{nodo.multiplicador_nivel_de_poder})")
        if nodo.hijo:
            self.mostrar_arbol(nodo.hijo, nivel + 1)
        if nodo.hermano:
            self.mostrar_arbol(nodo.hermano, nivel)

    def buscar_nodo(self, nombre, nodo=None):
        """Busca un nodo por nombre en el árbol."""
        if nodo is None:
            nodo = self.raiz
        if nodo.nombre.lower() == nombre.lower():
            return nodo
        if nodo.hijo:
            resultado = self.buscar_nodo(nombre, nodo.hijo)
            if resultado:
                return resultado
        if nodo.hermano:
            return self.buscar_nodo(nombre, nodo.hermano)
        return None

    
    def obtener_proxima_transformacion(self, personaje):
        """Devuelve la próxima transformación disponible para el personaje."""
        return self._obtener_proxima_transformacion(self.raiz, personaje)

    def _obtener_proxima_transformacion(self, nodo, personaje):
        """Método recursivo para encontrar la próxima transformación."""
        if nodo is None:
            return None
        
        # Verificar si el personaje tiene la transformación requerida
        if nodo.transformacion_requerida == personaje.transformacion_actual.nombre:
            return nodo
        
        # Buscar en los hijos y hermanos
        proxima_transformacion = self._obtener_proxima_transformacion(nodo.hijo, personaje)
        if proxima_transformacion:
            return proxima_transformacion
        
        return self._obtener_proxima_transformacion(nodo.hermano, personaje)