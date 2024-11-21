
#Nodo de las habilidades
class NodoHabilidad:
    def __init__(self, nombre: str, costo_ki: int, daño: int, transformacion_requerida,descripcion: str):
        """
        Inicializa una habilidad con su nombre, costo de Ki, daño, y descripción.
        """
        self.nombre = nombre
        self.costo_ki = costo_ki
        self.daño = daño
        self.transformacion_requerida = transformacion_requerida
        self.descripcion = descripcion
        self.hijos = []  # Lista de habilidades derivadas (hijos)

    def agregar_hijo(self, nodo_hijo):
        """
        Agrega una mejora o habilidad derivada como hijo.
        """
        self.hijos.append(nodo_hijo)

    def __str__(self):
        return f"{self.nombre} (Ki: {self.costo_ki}, Daño: {self.daño}) - {self.descripcion}"

#Arbol general de habilidades
class ArbolHabilidades:
    def __init__(self, raiz: NodoHabilidad):
        self.raiz = raiz

    def mostrar_arbol(self, nodo=None, nivel=0):
        """
        Muestra el árbol de habilidades de forma jerárquica.
        """
        if nodo is None:
            nodo = self.raiz
        print("  " * nivel + str(nodo))  # Muestra la habilidad con indentación según su nivel
        for hijo in nodo.hijos:
            self.mostrar_arbol(hijo, nivel + 1)

    def buscar_habilidad(self, nombre, nodo=None):
        """
        Busca una habilidad por nombre en el árbol.
        """
        if nodo is None:
            nodo = self.raiz
        if nodo.nombre == nombre:
            return nodo
        for hijo in nodo.hijos:
            resultado = self.buscar_habilidad(nombre, hijo)
            if resultado:
                return resultado
        return None
