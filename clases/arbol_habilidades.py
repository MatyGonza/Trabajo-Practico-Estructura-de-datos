
#Nodo de las habilidades
class NodoHabilidad:
    def __init__(self, nombre: str, costo_ki: int, daño: int, transformacion_requerida:list,descripcion: str):
        """
        Inicializa una habilidad con su nombre, costo de Ki, daño, y descripción.
        """
        self.nombre = nombre
        self.costo_ki = costo_ki
        self.daño = daño
        self.transformacion_requerida = transformacion_requerida
        self.descripcion = descripcion
        self.hijo= None # Primer hijo de este nodo (habilidad derivada más directa)
        self.hermano = None  #Siguiente habilidad del mismo


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
        print("  " * nivel + str(nodo))  # Imprime el nodo con indentación
        if nodo.hijo:
            self.mostrar_arbol(nodo.hijo, nivel + 1)  # Muestra el primer hijo
        if nodo.hermano:
            self.mostrar_arbol(nodo.hermano, nivel)  # Muestra el siguiente hermano


    def agregar_hijo(self, padre: NodoHabilidad, hijo: NodoHabilidad):
        """
        Agrega un hijo a un nodo existente.
        """
        if padre.hijo is None:
            # Si el padre no tiene hijos, lo asignamos como primer hijo.
            padre.hijo = hijo
        else:
            # Si ya tiene hijos, recorremos hasta el último hermano y lo enlazamos.
            actual = padre.hijo
            while actual.hermano is not None:
                actual = actual.hermano
            actual.hermano = hijo
    
    
    def listar_habilidades(self):
        """
        Devuelve una lista de todas las habilidades en el árbol.
        """
        habilidades = []
        self._listar_habilidades_recursivo(self.raiz, habilidades)
        return habilidades

    def _listar_habilidades_recursivo(self, nodo: NodoHabilidad, habilidades: list):
        if nodo is not None:
            habilidades.append(nodo)  # Agrega la habilidad actual a la lista
            if nodo.hijo:
                self._listar_habilidades_recursivo(nodo.hijo, habilidades)  # Recurre al hijo
            if nodo.hermano:
                self._listar_habilidades_recursivo(nodo.hermano, habilidades)  # Recurre al hermano

    
    def __iter__(self):
            """Permite iterar sobre las habilidades hijas y hermanos."""
            current = self.hijo
            while current is not None:
                yield current  # Devuelve el nodo hijo actual
                current = current.hermano  # Avanza al siguiente hermano
    
    def buscar_habilidad(self, nombre: str, nodo=None):
        """
        Busca una habilidad por nombre en el árbol.
        """
        if nodo is None:
            nodo = self.raiz
        if nodo.nombre == nombre:
            return nodo
        # Buscar en el hijo y luego en el hermano
        if nodo.hijo:
            resultado = self.buscar_habilidad(nombre, nodo.hijo)
            if resultado:
                return resultado
        if nodo.hermano:
            resultado = self.buscar_habilidad(nombre, nodo.hermano)
            if resultado:
                return resultado
        return None

    
def crear_arbol_habilidades(datos):
    def construir_nodo(nombre, info):
        """
        Crea un NodoHabilidad a partir de la información dada.
        
        Args:
            nombre (str): El nombre de la habilidad.
            info (dict): Un diccionario con información sobre la habilidad, 
                         incluyendo costo de ki, poder, transformaciones requeridas y descripción.
        
        Returns:
            NodoHabilidad: Una instancia del nodo creada con los datos proporcionados.
        """
        return NodoHabilidad(
            nombre=nombre,
            costo_ki=info["costo"], # Costo en puntos de ki para usar la habilidad
            daño=info["poder"], # Daño que inflige la habilidad
            transformacion_requerida=info["transformacion_requerida"], # Transformaciones necesarias para usarla
            descripcion=info["descripcion"] # Breve descripción de la habilidad
        )
    
    def construir_arbol_recursivo(data):
        """
        Construye el árbol de habilidades recursivamente desde un nodo raíz.

        Args:
            data (dict): Un diccionario con los datos del nodo actual y sus hijos.
        
        Returns:
            NodoHabilidad: El nodo raíz del subárbol construido.
        """
        # Crear un nodo para la habilidad actual
        nodo = construir_nodo(data["nombre"], data)
        # Procesar los hijos de este nodo
        for hijo_nombre, hijo_info in data["hijos"].items():
            # Crear un nodo hijo recursivamente
            hijo_nodo = construir_arbol_recursivo({**hijo_info, "nombre": hijo_nombre})
            # Agregar el nodo hijo al nodo actual como hijo en el árbol
            arbol.agregar_hijo(nodo, hijo_nodo)
        return nodo # Devuelve el nodo actual como raíz del subárbol
    
    # Construimos el nodo raíz del árbol a partir de los datos iniciales
    raiz = construir_nodo(datos["nombre"], datos)
    # Creamos la instancia del árbol con el nodo raíz
    arbol = ArbolHabilidades(raiz)
    # Procesamos los hijos del nodo raíz y los añadimos al árbol
    for hijo_nombre, hijo_info in datos["hijos"].items():
        # Crear un nodo hijo recursivamente
        hijo_nodo = construir_arbol_recursivo({**hijo_info, 'nombre': hijo_nombre})
        # Agregar el nodo hijo al nodo raíz
        arbol.agregar_hijo(raiz, hijo_nodo)
    return arbol # Devuelve el árbol completo

