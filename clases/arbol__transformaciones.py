
#Nodo del arbol general
class NodoTransformacion():
    def __init__(self,nombre:str,ki_necesario:int,transformacion_requerida:str,multiplicador_nivel_de_poder):
        self.nombre = nombre
        self.ki_necesario = ki_necesario
        self.transformacion_requerida = transformacion_requerida
        self.multiplicador_nivel_de_poder = multiplicador_nivel_de_poder #Aca multiplica el nivel de poder ejem: en el supersaiyayin se multiplica por 50
        self.padre = None
        self.hijos = []
    def agregar_hijo(self, nodo_hijo):
        """Agrega un nodo hijo y establece la relación de parentesco."""
        nodo_hijo.padre = self
        self.hijos.append(nodo_hijo)

#Arbol general de las tranformaciones
class ArbolTransformaciones: 
    
    def __init__(self, nodo_raiz: NodoTransformacion):
        self.raiz = nodo_raiz

    def mostrar_arbol(self, nodo=None, nivel=0):
        """Muestra el árbol de manera jerárquica."""
        if nodo is None:
            nodo = self.raiz
        print("     " * nivel + f"{nodo.nombre} (Ki: {nodo.ki_necesario}, Multiplicador: x{nodo.multiplicador_nivel_de_poder})")
        for hijo in nodo.hijos:
            self.mostrar_arbol(hijo, nivel + 1)

    def buscar_nodo(self, nombre, nodo=None):
        """Busca un nodo por nombre."""
        if nodo is None:
            nodo = self.raiz
        if nodo.nombre == nombre:
            return nodo
        for hijo in nodo.hijos:
            resultado = self.buscar_nodo(nombre, hijo)
            if resultado:
                return resultado
        return None
