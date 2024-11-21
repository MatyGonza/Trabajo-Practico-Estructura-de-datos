
#Nodo de las habilidades
class NodoHabilidad:
    def __init__(self, nombre: str, costo_ki: int, daño: int, transformacion_requerida,descripcion: list):
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

    
def crear_arbol_habilidades(datos):
    def construir_nodo(nombre, info):
        # Crea un NodoHabilidad a partir de la información dada.
        return NodoHabilidad(
            nombre,
            info['costo'],
            info['poder'],
            info['transformacion_requerida'],
            info['descripcion']
        )
    
    def construir_arbol_recursivo(data):
        # Construye el árbol recursivamente.
        nodo = construir_nodo(data['nombre'], data)
        for hijo_nombre, hijo_info in data['hijos'].items():
            hijo_nodo = construir_arbol_recursivo({**hijo_info, 'nombre': hijo_nombre})
            nodo.agregar_hijo(hijo_nodo)
        return nodo
    
    # Comenzamos desde la raíz del árbol.
    raiz_nombre = list(datos.keys())[0]
    raiz_info = datos[raiz_nombre]
    raiz_nodo = construir_arbol_recursivo({**raiz_info, 'nombre': raiz_nombre})
    
    return ArbolHabilidades(raiz_nodo)

