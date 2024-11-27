import time
import heapq
import random

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
    def ordenamiento_topologico(self):
        """
        Realiza el ordenamiento topológico del árbol de habilidades.
        """
        def dfs(nodo, visitado, pila):
            """
            Realiza un DFS para ordenar topológicamente las habilidades.
            """
            # Marcamos el nodo como visitado
            if nodo not in visitado:
                visitado.add(nodo)
            
                # Recurrimos a los hijos de este nodo
                if nodo.hijo:
                    dfs(nodo.hijo, visitado, pila)
                
                # Recurrimos a los hermanos de este nodo
                if nodo.hermano:
                    dfs(nodo.hermano, visitado, pila)
            
                # Una vez procesado, agregamos el nodo a la pila
                pila.append(nodo)
    
        pila = []  # Esta pila almacenará las habilidades en el orden topológico
        visitado = set()  # Conjunto de nodos visitados para evitar ciclos

        # Realizamos DFS desde la raíz
        dfs(self.raiz, visitado, pila)
    
        # Devolvemos la pila invertida, ya que el último nodo procesado debe aparecer primero
        return pila[::-1]    
    
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
        print("     " * nivel + f"{nodo.nombre} (Ki: {nodo.ki_necesario}, Multiplicador: x{nodo.multiplicador_nivel_de_poder})")
        if nodo.hijo:
            self.mostrar_arbol(nodo.hijo, nivel + 1)
        if nodo.hermano:
            self.mostrar_arbol(nodo.hermano, nivel)

    def buscar_nodo(self, nombre, nodo=None):
        """Busca un nodo por nombre en el árbol."""
        if nodo is None:
            nodo = self.raiz
        if nodo.nombre == nombre:
            return nodo
        if nodo.hijo:
            resultado = self.buscar_nodo(nombre, nodo.hijo)
            if resultado:
                return resultado
        if nodo.hermano:
            return self.buscar_nodo(nombre, nodo.hermano)
        return None


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










class Personaje:
    def __init__(self,nombre:str,vida:int,raza:str,estado:str,ki:int,max_ki,transformaciones:ArbolTransformaciones,transformacion_inicial,habilidades:ArbolHabilidades,exp,max_exp,nivel_de_poder,nivel:int=1,max_ki_base:int=10000,combates_ganados=1,planeta_actual = "Tierra"):
        
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
        self.nivel_de_poder = nivel_de_poder
        self.nivel = nivel
        self.max_ki_base = max_ki_base
        self.combates_ganados = combates_ganados
        self.evolucionar_poder(combates_ganados=self.combates_ganados)
        self.planeta_actual = planeta_actual
    
    def ganar_combate(self):
        """Método para registrar un combate ganado y evolucionar el poder."""
        self.combates_ganados += 1  # Incrementa el contador de combates ganados
        print(f"{self.nombre} ha ganado un combate!")
        
        # Llamar a evolucionar poder después de ganar un combate
        nuevo_poder = self.evolucionar_poder(combates_ganados=self.combates_ganados)
        
        
        
    def mostrar_stats(self):
        #Hay que arreglar que sea vea bien las habliidades y transformaciones
        print (f"\nNombre: {self.nombre}\nNivel: {self.nivel}\nTransformacion actual: {self.transformacion_actual.nombre}\nKi: {self.ki}\nRaza: {self.raza}\nEstado: {self.estado}\nMaximo de Ki: {self.max_ki}\nVida: {self.vida} hp\nExperiencia: {self.exp}/{self.max_exp}\nTransformaciones: {self.transformaciones.mostrar_arbol()}\nHabilidades: {self.habilidades.mostrar_arbol()}\nnivel de Poder: {self.nivel_de_poder}\n")
    
    def ataque_basico(self,enemigo): #esto es una implementacion algo basica que puede cambiar.
        if self.ki >=   1000:  #el personaje necesita un min de 1000/100000 para hacer un ataque normal
            daño = int((self.nivel_de_poder))
            print(f"{self.nombre} infligio un daño de: {daño}.\n")
            
            daño_efectivo = max(daño,0) #el daño no puede ser negativo.
            enemigo.recibir_daño(daño_efectivo,enemigo)
            
            self.ki -= 1000
            
        else:
            print ("No se puede ataque_basico, ya que no contas con la cant. de ki necesario. Te recomiendo cargar el ki.")
    
        
    def cargar_ki(self, incremento:int):  # Se incrementará de 1000 en cien
        
        while self.ki < self.max_ki:
            self.ki += incremento
            # Asegurarse de que ki no supere max_ki
            #if self.ki > self.max_ki:
            #   self.ki = self.max_ki
            # Imprimir la carga actual
            print(f"\r{self.nombre} está cargando ki... Ki actual: {self.ki}/{self.max_ki}", end="") #el \r acualiza la linea en lugar de generar una sobre otra
            time.sleep(0.2) #pasa 0.5 segundos antes de cargar para hacer tipo una animacion
        
        print(f"\n{self.nombre} ha cargado su ki al máximo: {self.ki}/{self.max_ki}")
                
    def defender(self):
        self.estado = "defensivo"
        print(f"{self.nombre} esta en guardia y el proximo turno del oponente el daño se reducira a la mitad.")
        return 0

    def recibir_daño(self,daño_recibido,personaje):

        if self.estado == "defensivo":
            self.vida -= (daño_recibido//2)

            
            self.estado = "Normal"

            print(f"{self.nombre} recibio daño reducido debido a su defensa y su vida se redujo a: {self.vida}.")
      
        else: #self.estodo != "defensivo":
            self.vida -=daño_recibido
                
   
            
            print(f"{self.nombre} Recibiste daño efectivo de {personaje.nombre}: {daño_recibido}\nTu vida restante es: {self.vida}")

    def usar_habilidad(self, habilidad_nombre, enemigo):
        # Buscar la habilidad en el árbol
        nodo_habilidad = self.habilidades.buscar_habilidad(habilidad_nombre)
    
        # Verificar si la habilidad existe
        if nodo_habilidad is None:
            print(f"La habilidad '{habilidad_nombre}' no existe.")
            return

        # Verificar si cumple con la transformación requerida
        if any(transformacion in self.transformacion_actual.nombre for transformacion in nodo_habilidad.transformacion_requerida):
            # Verificar si tiene suficiente Ki
            if self.ki >= nodo_habilidad.costo_ki:
                # Usar la habilidad
                self.ki -= nodo_habilidad.costo_ki
                daño = nodo_habilidad.daño
                enemigo.recibir_daño(daño,enemigo)  # Ajustamos la llamada para que no pase el enemigo de más
                print(f"{self.nombre} usó '{habilidad_nombre}', infligiendo {daño} puntos de daño a {enemigo.nombre}.")
            else:
                print(f"\nNo tienes suficiente Ki para usar '{habilidad_nombre}'. Necesitas {nodo_habilidad.costo_ki}.")
            
        else:
            # Si no tiene la transformación requerida
            print(f"No puedes usar '{habilidad_nombre}' sin estar en una de las transformaciones requeridas: {', '.join(nodo_habilidad.transformacion_requerida)}.")
            
    def transformarse(self, nombre_transformacion):
        # Buscar la transformación en el árbol
        nodo_transformacion = self.transformaciones.buscar_nodo(nombre_transformacion)
        
        if nodo_transformacion is None:
            print(f"La transformación '{nombre_transformacion}' no existe.")
            return

        # Verificar si cumple con los requisitos de transformación
        if self.ki < nodo_transformacion.ki_necesario:
            print(f"No tienes suficiente Ki para transformarte en '{nombre_transformacion}'. Necesitas {nodo_transformacion.ki_necesario}.")
            return

        # Verificar si la transformación requerida es la actual del personaje
        if self.transformacion_actual is None or self.transformacion_actual.nombre != nodo_transformacion.transformacion_requerida:
            print(f"No puedes transformarte en '{nombre_transformacion}' sin antes estar en '{nodo_transformacion.transformacion_requerida}'.")
            return

        # Realizar la transformación
        self.ki -= nodo_transformacion.ki_necesario
        self.transformacion_actual = nodo_transformacion
        
        # Evolucionar el poder del personaje con el multiplicador de la transformación
        self.evolucionar_poder(nodo_transformacion.multiplicador_nivel_de_poder)
        
        print(f"{self.nombre} se ha transformado en '{nombre_transformacion}', con nivel de poder multiplicado por {nodo_transformacion.multiplicador_nivel_de_poder}.")
        exp_base = 100
        max_exp_actualizada = self.nivel * exp_base
        self.max_exp = max_exp_actualizada
        return self.max_exp
    

    def incrementar_atributos(self):
        """Aumenta gradualmente los atributos de velocidad, defensa y fuerza."""
        incremento = 5000 # Define cuánto se incrementarán los atributos por cada nivel de poder
        self.nivel_de_poder += incremento
        self.vida += incremento*2
    
    def aumentar_nivel_de_poder(self,incremento):
        self.nivel_de_poder += incremento

    def calcular_max_ki(self,multiplicador=None):
        """Calcula el máximo de Ki basado en el nivel."""
        if multiplicador :#Al estar tranformado utiliza un multiplicador que multiplica el ki
            
            max_ki= (self.nivel * self.max_ki_base)*multiplicador
            
            return max_ki
        else:
            return (self.nivel * self.max_ki_base)  # Ejemplo: 100 + 50 por cada nivel
        
    def actualizar_max_exp(self):
        """Actualiza la experiencia máxima necesaria para subir de nivel."""
        exp_base = 100  # Base de experiencia por nivel
        self.max_exp = self.nivel * exp_base
        
    def subir_nivel(self):
        #Sube el nivel del personaje si alcanza la experiencia necesaria.
        if self.exp >= self.nivel * 100:  # Ejemplo: 100 exp por nivel
            self.nivel += 1
            self.max_ki = self.calcular_max_ki()  # Actualiza el máximo de Ki
            self.incrementar_atributos()  # Aumenta los atributos al subir de nivel
            self.actualizar_max_exp()#Actualiza la experiencia maxima para subir de nivel
            # Llamada recursiva para verificar si se puede subir nuevamente
            self.subir_nivel()
    
    def evolucionar_poder(self, combates_ganados= None, multiplicador=2):
        """
        Método recursivo para calcular la evolución del poder tras cada combate.
        
        :param combates_ganados: Número de combates ganados.
        :param multiplicador: Multiplicador actual (por defecto es 2).
        :return: Poder total tras los combates.
        """
        
        if combates_ganados is not None:
            if combates_ganados <= 0:
                return self.nivel_de_poder
                
            # Calcular el nuevo poder
            nuevo_poder = self.nivel_de_poder * multiplicador
            nuevo_poder = round(nuevo_poder)
            # Actualizar el poder actual
            self.nivel_de_poder = nuevo_poder
            
            # Aumentar experiencia tras cada combate
            self.exp += 50  # Ejemplo: ganar 50 exp por combate
            
            # Verificar si se debe subir de nivel
            self.subir_nivel()
            
            # Llamada recursiva para el siguiente combate
            return self.evolucionar_poder(combates_ganados - 1, multiplicador)
        else:
            
            nuevo_poder = self.nivel_de_poder * multiplicador
            nuevo_poder = round(nuevo_poder)
            # Actualizar el poder actual en una transformacion
            self.nivel_de_poder = nuevo_poder
            
            self.max_ki = self.calcular_max_ki(multiplicador)
            self.vida *= multiplicador
            print("tranfomacion")
            return nuevo_poder

    def escapar_a(self, grafo, planeta_destino):
        """
        Permite al personaje escapar a un planeta especificado, sin necesidad de verificar las rutas (cambia el planeta directamente).
        
        :param grafo: El grafo de planetas.
        :param planeta_destino: El planeta al que el personaje quiere escapar.
        """
        # Verificar si el planeta destino existe en el grafo
        if planeta_destino in grafo.planetas:
            self.planeta_actual = planeta_destino
            print(f"{self.nombre} ha escapado a {planeta_destino}.")
        else:
            print(f"El planeta {planeta_destino} no existe en el grafo.")

    
    def viajar_a(self, grafo, planeta_destino, metodo_busqueda='bfs'):

        """
        Permite al personaje viajar a un planeta conectado al planeta actual,
        si existe una ruta entre los planetas usando el algoritmo de búsqueda especificado.
        
        :param grafo: El grafo de planetas.
        :param planeta_destino: El planeta al que el personaje quiere viajar.
        :param metodo_busqueda: El algoritmo de búsqueda ('bfs' o 'dfs') a utilizar para encontrar la ruta.
        """
        # Verificar si el planeta destino está conectado al planeta actual usando el algoritmo de búsqueda
        if metodo_busqueda == 'bfs':
            camino = grafo.bfs(self.planeta_actual, planeta_destino)
        elif metodo_busqueda == 'dfs':
            camino = grafo.dfs(self.planeta_actual, planeta_destino)
        else:
            print("Método de búsqueda no válido. Usa 'bfs' o 'dfs'.")
            return
        
        if camino:  # Si encontramos un camino
            self.planeta_actual = planeta_destino
            print(f"{self.nombre} ha viajado a {planeta_destino}. Camino encontrado: {camino}")
        else:
            print(f"No hay ruta entre {self.planeta_actual} y {planeta_destino} usando {metodo_busqueda}.")

arbol_habilidades_data_16 = {
    "nombre": "Ataque básico",
    "poder": 1000,
    "costo": 1000,
    "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
    "descripcion": "Un golpe básico con Ki.",
    "hijos": {
        "Súper Dodonpa": {
            "nombre": "Súper Dodonpa",
            "poder": 2000,
            "costo": 4000,
            "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
            "descripcion": "Un ataque de energía que lanza un rayo devastador, capaz de causar un gran daño a sus oponentes.",
            "hijos": {
                "Absorción de Ki": { #Faltaria un atributo que absorba el ki o lo podriamos cambiar por absorcion de energia.
                    "nombre": "Absorción de Ki",
                    "poder": 1500,
                    "costo": 3000,
                    "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
                    "descripcion": "Tiene la capacidad de absorber ataques de energía, lo que le permite recuperarse y utilizar esa energía en su contra.",
                    "hijos": {
                        "Autodestrucción": {
                            "nombre": "Autodestrucción",
                            "poder": 50000, #le agregue un cero mas
                            "costo": 40000,
                            "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
                            "descripcion": "En situaciones críticas, el Androide 16 puede activar un mecanismo de autodestrucción que libera una gran cantidad de energía, causando daños masivos en el área.",
                            "hijos": {}
                        }
                    }
                }
            }
        }
    }
}

arbol_habilidades_data_17 = {
    "nombre": "Ataque básico",
    "poder": 1000,
    "costo": 1000,
    "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
    "descripcion": "Un golpe básico con Ki.",
    "hijos": {
        "Barrera de Energía": {
            "nombre": "Barrera de Energía",
            "poder": 2000,
            "costo": 4000,
            "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
            "descripcion": "Puede crear una barrera de energía defensiva que le protege de ataques enemigos, permitiéndole contrarrestar con ataques propios.",
            "hijos": {
                "Rayo Energético": {
                    "nombre": "Rayo Energético",
                    "poder": 1500,
                    "costo": 3000,
                    "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
                    "descripcion": "Un ataque rápido y potente que dispara un rayo de energía hacia su oponente, con una precisión y velocidad notables.",
                    "hijos": {
                        "Autodestrucción": {
                            "nombre": "Autodestrucción",
                            "poder": 5000,
                            "costo": 40000,
                            "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
                            "descripcion": "En situaciones críticas, el Androide puede activar un mecanismo de autodestrucción que libera una gran cantidad de energía, causando daños masivos en el área.",
                            "hijos": {}
                        }
                    }
                }
            }
        }
    }
}

arbol_habilidades_data_18 = {
    "nombre": "Ataque básico",
    "poder": 1000,
    "costo": 1000,
    "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
    "descripcion": "Un golpe básico con Ki.",
    "hijos": {
        "Destrucción Rápida": {
            "nombre": "Destrucción Rápida",
            "poder": 2000,
            "costo": 4000,
            "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
            "descripcion": "Utiliza movimientos rápidos y precisos para desatar una serie de golpes devastadores en sus oponentes, combinando técnicas de artes marciales con ataques energéticos.",
            "hijos": {
                "Kienzan": {
                    "nombre": "Kienzan",
                    "poder": 1500,
                    "costo": 3000,
                    "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
                    "descripcion": "Lanza un disco de energía afilado que puede cortar a través de casi cualquier cosa, siendo un ataque tanto ofensivo como defensivo.",
                    "hijos": {
                        "Autodestrucción": {
                            "nombre": "Autodestrucción",
                            "poder": 5000,
                            "costo": 40000,
                            "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
                            "descripcion": "En situaciones críticas, el Androide puede activar un mecanismo de autodestrucción que libera una gran cantidad de energía, causando daños masivos en el área.",
                            "hijos": {}
                        }
                    }
                }
            }
        }
    }
}



arbol_habilidades_data_goku = {
    "nombre": "Ataque básico",
    "poder": 1000,
    "costo": 100,
    "transformacion_requerida": ["Base", "Super Saiyajin", "Super Saiyajin 2", "Super Saiyajin 3"],
    "descripcion": "Un golpe básico con Ki.",
    "hijos": {
        "Kamehameha": {
            "nombre": "Kamehameha",
            "poder": 2000,
            "costo": 4000,
            "transformacion_requerida": ["Base", "Super Saiyajin", "Super Saiyajin 2", "Super Saiyajin 3"],
            "descripcion": "Un rayo de energía muy poderoso.",
            "hijos": {
                "Genkidama": {
                    "nombre": "Genkidama",
                    "poder": 1500,
                    "costo": 3000,
                    "transformacion_requerida": ["Base", "Super Saiyajin", "Super Saiyajin 2", "Super Saiyajin 3"],
                    "descripcion": "El poder de todos los seres vivos en un solo ataque.",
                    "hijos": {
                        "Kamehameha x10": {
                            "nombre": "Kamehameha x10",
                            "poder": 5000,
                            "costo": 40000,
                            "transformacion_requerida": ["Base", "Super Saiyajin", "Super Saiyajin 2", "Super Saiyajin 3"],
                            "descripcion": "El Kamehameha aumentado 10 veces.",
                            "hijos": {}
                        }
                    }
                }
            }
        }
    }
}

arbol_habilidades_data_vegeta = {
        "nombre": "Ataque básico",
        "poder": 10000,
        "costo": 1500,
        "transformacion_requerida":  ["Base","Super Saiyajin","Super Saiyajin 2","Super Saiyajin 3"],
        "descripcion": "Un golpe básico con Ki.",
        "hijos": {
            "Resplandor Final": {
                "poder": 3000,
                "costo": 4000,
                "transformacion_requerida":  ["Base","Super Saiyajin","Super Saiyajin 2","Super Saiyajin 3"],
                "descripcion": "Un ataque devastador que concentra una gran cantidad de energía en un rayo destructivo.",
                "hijos": {
                    "Galick Gun": {
                        "poder": 4500,
                        "costo": 3000,
                        "transformacion_requerida":  ["Base","Super Saiyajin","Super Saiyajin 2","Super Saiyajin 3"],
                        "descripcion": "Un poderoso rayo de energía",
                        "hijos": {
                            "Hakai": {
                                "poder": 5500,
                                "costo": 40000,
                                "transformacion_requerida":  ["Base","Super Saiyajin","Super Saiyajin 2","Super Saiyajin 3"],
                                "descripcion": "Una técnica destructiva utilizada por los dioses de la destrucción",
                                "hijos": {}
                            }
                        }
                    }
                }
            }
        }
    }



arbol_habilidades_data_gohan = {
    "nombre": "Ataque básico",
    "poder": 1500,
    "costo": 1000,
    "transformacion_requerida": ["Base", "Super Saiyajin", "Super Saiyajin 2", "Super Saiyajin 3"],
    "descripcion": "Un golpe básico con Ki.",
    "hijos": {
        "Masenko": {
            "nombre": "Masenko",
            "poder": 2500,
            "costo": 4000,
            "transformacion_requerida": ["Base", "Super Saiyajin", "Super Saiyajin 2", "Super Saiyajin 3"],
            "descripcion": "Un ataque rápido y poderoso donde lanza un rayo de energía.",
            "hijos": {
                "Kamehameha": {
                    "nombre": "Kamehameha",
                    "poder": 1500,
                    "costo": 3000,
                    "transformacion_requerida": ["Base", "Super Saiyajin", "Super Saiyajin 2", "Super Saiyajin 3"],
                    "descripcion": "Un rayo de energía muy poderoso.",
                    "hijos": {
                        "Kamehameha x10": {
                            "nombre": "Kamehameha x10",
                            "poder": 5000,
                            "costo": 40000,
                            "transformacion_requerida": ["Base", "Super Saiyajin", "Super Saiyajin 2", "Super Saiyajin 3"],
                            "descripcion": "El Kamehameha aumentado 10 veces.",
                            "hijos": {}
                        }
                    }
                }
            }
        }
    }
}







class Saiyajin(Personaje):
    def __init__(self, nombre: str, arbol_habilidades_data, combates_ganados=0):
        transformaciones = self.crear_arbol_transformaciones()
        habilidades = self.crear_arbol_habilidades(arbol_habilidades_data)
    
        super().__init__(nombre=nombre, vida=1000, raza="Saiyajin", estado="Normal",
                         ki=0, max_ki=10000, transformaciones=transformaciones,
                         transformacion_inicial=transformaciones.raiz, habilidades=habilidades,
                         exp=0, max_exp=100, nivel_de_poder=1, nivel=1, max_ki_base=10000,
                         planeta_actual="Tierra")
        self.combates_ganados = combates_ganados
        self.evolucionar_poder(combates_ganados=self.combates_ganados)

    def ataque_especial(self, enemigo):
        """Ataque especial del Saiyajin."""
        if self.ki >= 5000:
            daño_especial = int(self.nivel_de_poder * 2)
            enemigo.recibir_daño(daño_especial, enemigo)
            self.ki -= 5000
        else:
            print("No tienes suficiente ki para realizar un ataque especial.")


    
    def crear_arbol_transformaciones(self):
        """Crea el árbol de transformaciones para el Saiyajin."""
        base = NodoTransformacion("Base", 0, None, 1)
        ssj = NodoTransformacion("Super Saiyajin", 4000, base, 50)
        ssj2 = NodoTransformacion("Super Saiyajin 2", 5500, ssj, 100)
        ssj3 = NodoTransformacion("Super Saiyajin 3", 7000, ssj2, 150)
        ssj4 = NodoTransformacion("Super Saiyajin 4", 8500, ssj3, 160)

        base.agregar_hijo(ssj)
        ssj.agregar_hijo(ssj2)
        ssj2.agregar_hijo(ssj3)
        ssj3.agregar_hijo(ssj4)

        return ArbolTransformaciones(base)
    
    def crear_arbol_habilidades(self, arbol_habilidades_data):
        return crear_arbol_habilidades(arbol_habilidades_data)
        return crear_arbol_habilidades(arbol_habilidades_data)


class Androide(Personaje):
    def __init__(self, nombre: str, arbol_habilidades_data, combates_ganados=0):
        super().__init__(nombre=nombre, vida=1000, raza="Androide", estado="Normal",
                         ki=0, max_ki=10000, transformaciones=self.crear_arbol_transformaciones(),
                         transformacion_inicial=self.crear_arbol_transformaciones().raiz,
                         habilidades=self.crear_arbol_habilidades(arbol_habilidades_data),
                         exp=0, max_exp=100, nivel_de_poder=1, nivel=1, max_ki_base=10000,
                         planeta_actual="Tierra")
        self.combates_ganados = combates_ganados
        self.evolucionar_poder(combates_ganados=self.combates_ganados)
    
    def ataque_especial(self, enemigo):
        """Ataque especial del Saiyajin."""
        if self.ki >= 5000:
            # Calcular el daño potencial basado en la fuerza
            daño_especial = int(self.nivel_de_poder*2)
            
            enemigo.recibir_daño(daño_especial,enemigo)
            
            # Reducir ki al usar el ataque especial
            self.ki -= 5000  
        else:
            print("No tienes suficiente ki para realizar un ataque especial.")
            
        
    
    def crear_arbol_transformaciones(self):
        base = NodoTransformacion("Base", 0, None, 1)
        fase1 = NodoTransformacion("Fase 1", 4000, base, 50)
        fase2 = NodoTransformacion("Fase 2", 5500, fase1, 100)
        fase3 = NodoTransformacion("Fase 3", 7000, fase2, 150)
        fase4 = NodoTransformacion("Fase 4", 8500, fase3, 160)

        base.agregar_hijo(fase1)
        fase1.agregar_hijo(fase2)
        fase2.agregar_hijo(fase3)
        fase3.agregar_hijo(fase4)

        return ArbolTransformaciones(base)

    def crear_arbol_habilidades(self, arbol_habilidades_data):
        return crear_arbol_habilidades(arbol_habilidades_data)




#utilizamos el modulo de cola de phyton
    

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



#usaremos un grafo con matriz de adyacencia
class GrafoDragonBall:
    def __init__(self, planetas,dirigido):
        """
        Inicializa el grafo con una lista de planetas.
        Crea una matriz de adyacencia donde cada celda almacena el peso (valor) de la ruta.
        Si no hay ruta, el valor será 0.
        """
        self.planetas = planetas  # Lista de planetas (nodos)
        self.num_planetas = len(planetas)
        self.dirigido = dirigido # Define si el grafo es dirigido
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
            if not self.dirigido:  # Si es un grafo no dirigido
                self.matriz_adyacencia[j][i] = peso  # Añadir la ruta en dirección opuesta

        if not self.dirigido:
            self.matriz_adyacencia[j][i] = peso  # Para grafos no dirigidos

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

    def armar_grafo(self):
        """
        Configura el grafo con las rutas dadas.
        Parámetros:
            - rutas: Lista de tuplas (origen, destino, peso) que definen las rutas.
        """

        #lista a utiilizar para armar el grafo
        planetas_dragonball =  ["Tierra","Namek","Vegeta","Planeta Kaio","Reino de los demonios","Planeta de Bills","La habitacion del tiempo","Planeta Yadarat"]
        
        rutas = [("Tierra","Namek",40),("Namek","Vegeta",90),("Namek","Reino de los demonios",70),("Tierra","La habitacion del tiempo",10),("Tierra","Planeta de Bills",180),("Reino de los demonios","Planeta Kaio",90),("Vegeta","Planeta Yadarat",50)]
        for origen, destino, peso in rutas:
            self.agregar_ruta(origen, destino, peso)
        return



    def obtener_peso(self, origen, destino):
        """
        Devuelve el peso de la ruta entre dos planetas, si existe.
        """
        if origen not in self.planetas or destino not in self.planetas:
            print("Error: Uno o ambos planetas no existen en el grafo.")
            return None

        i = self.planetas.index(origen)
        j = self.planetas.index(destino)
        return self.matriz_adyacencia[i][j]

    
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







class Juego:
    def __init__(self, jugador: Personaje, maquina: Personaje, grafo: GrafoDragonBall, transformaciones: ArbolTransformaciones):
        self.jugador = jugador
        self.maquina = maquina
        self.grafo = grafo
        self.transformaciones = transformaciones
        self.esferas_recolectadas = 0



    def iniciar_combate(self):
        print(f"Iniciando combate entre {self.jugador.nombre} y {self.maquina.nombre}!")
        while self.jugador.vida > 0 and self.maquina.vida > 0:
            self.turno_jugador()
            if self.maquina.vida <= 0:
                print(f"{self.maquina.nombre} ha sido derrotado!")
                return self.jugador.mostrar_stats()
            self.turno_maquina()
            if self.jugador.vida <= 0:
                print(f"{self.jugador.nombre} ha sido derrotado!")
                return self.maquina.mostrar_stats()
        print("El combate ha terminado.")

    def turno_jugador(self):
        while True:
            print(f"""\nTurno de {self.jugador.nombre} -- Vida: {self.jugador.vida} -- Ki: {self.jugador.ki}/{self.jugador.max_ki}""")
            print("Opciones: (1) Usar habilidad, (2) Cargar Ki, (3) Transformarse, (4) Escapar")
            accion = input("Elige tu acción: ").strip()
            if accion == "1":
                habilidades = self.jugador.habilidades.listar_habilidades()
                for i, habilidad in enumerate(habilidades):
                    print(f"{i + 1}. {habilidad.nombre} (Ki: {habilidad.costo_ki}, Daño: {habilidad.daño})")
                seleccion = int(input("Selecciona una habilidad: "))
                self.jugador.usar_habilidad(habilidades[seleccion - 1].nombre, self.maquina)
                break
            elif accion == "2":
                self.jugador.cargar_ki(1000)
                break
            elif accion == "3":
                transformacion = input("¿A qué transformación deseas ir? ")
                self.jugador.transformarse(transformacion)
                break
            elif accion == "4":
                print("¡Has escapado del combate!")
                return
            else:
                print("Opción inválida, intenta de nuevo.")
        print("------"*20)

    def turno_maquina(self):
        if self.maquina.ki >= 100 and random.choice([True, False]):
            habilidades = self.maquina.habilidades.listar_habilidades()
            habilidad = random.choice(habilidades)
            self.maquina.usar_habilidad(habilidad.nombre, self.jugador)
        else:
            self.maquina.cargar_ki(1000)

    def busqueda_habilidades(self,hijos):
        habilidades=[]
        for c in hijos:
            if c in hijos is None:
                return None
            else:
                habilidades.append(c)
                print(c)
                self.busqueda_habilidades(c.hijos)
                return habilidades
            
    def explorar_esferas(self):
        """
        Método para que el jugador busque las Esferas del Dragón en el grafo. El jugador debe recolectar las 7 esferas 
        viajando entre planetas, usando DFS para encontrar una esfera y Dijkstra para encontrar el camino más corto hacia ella.

        Una vez que el jugador recolecte las siete esferas, podrá hacer un deseo.
        """
        print("Explorando el mundo en busca de las Esferas del Dragón...")
        
        planetas_dragonball = ["Tierra", "Namek", "Vegeta", "Planeta Kaio", "Reino de los demonios", 
                               "Planeta de Bills", "La habitación del tiempo", "Planeta Yadarat"]
        
        # Buscar las esferas
        while self.esferas_recolectadas < 7:
            # El jugador elige un planeta desde el cual partir
            planeta_origen = self.jugador.planeta_actual
            print(f"\nBuscando una esfera desde el planeta {planeta_origen}...")

            # Usamos DFS para encontrar un planeta donde haya una esfera
            camino_dfs = self.grafo.dfs(planeta_origen, random.choice(planetas_dragonball))
            if camino_dfs:
                print(f"Camino DFS encontrado: {camino_dfs}")
            
            # Usamos Dijkstra para encontrar el camino más corto
            distancias = self.grafo.dijkstra(planeta_origen)
            planeta_destino = min(distancias, key=distancias.get)  # El planeta con la distancia más corta
            print(f"Camino más corto con Dijkstra hacia: {planeta_destino} (Distancia: {distancias[planeta_destino]})")

            # Simulamos la recolección de una esfera
            print(f"¡Has encontrado una esfera en el planeta {planeta_destino}!")
            self.esferas_recolectadas += 1



        # Cuando el jugador haya recolectado las 7 esferas, puede hacer un deseo
        self.hacer_deseo()

    def hacer_deseo(self):
        """
        Una vez que el jugador haya recolectado las 7 esferas, puede hacer un deseo.
        El deseo es un aumento importante en sus habilidades o poderes.
        """
        print("¡Has recolectado las 7 Esferas del Dragón!")
        print("¡Es hora de hacer un deseo!")
        intentos = 1
        while intentos < 3: #el jugador tiene hasta tres intentos
            deseo = input("¿Qué deseas? (Aumentar poder (1) o incrementar atributos (2)): ")

            if deseo == '1':
                print("Tu poder ha aumentado enormemente gracias al deseo del Dragón!")
                self.jugador.aumentar_nivel_de_poder(100000)  # Aumento significativo de poder
                break
            elif deseo == '2':
                print("¡Gracias al deseo de las esferas aumentaste tus atributos!")
                self.jugador.incrementar_atributos() #aumento de atributos como vida y nivel de poder
            else:
                intentos +=1
                print("Deseo no válido. No se ha hecho ningún deseo.")
                if intentos ==3:
                    print("Demasiados intentos el deseo no se cumple.")
                    break

#clase
class Torneo:
    def __init__(self, personajes):
        #se inicia una cola de prioridad
        self.cola_prioridad = ColaDePrioridad()
        #se agregan los personajes
        for personaje in personajes:
            self.cola_prioridad.agregar_personaje(personaje)
        self.ganador = None #aca se guarda el ganador

    def iniciar_torneo(self):
        print("¡Iniciando el Torneo de Artes Marciales!")
        #El torneo se ejecuta hasta que quede un solo personaje en la cola
        while not self.cola_prioridad.esta_vacia():
            # Si solo queda un personaje, es el ganador del torneo
            if len(self.cola_prioridad.heap) == 1:
                self.ganador = self.cola_prioridad.siguiente_enfrentamiento()
                print(f"El ganador del torneo es {self.ganador.nombre} con un nivel de poder de {self.ganador.nivel_de_poder}!")
                break

            #se seleccionan a los dos luchadores        
            contrincante1 = self.cola_prioridad.siguiente_enfrentamiento()
            contrincante2 = self.cola_prioridad.siguiente_enfrentamiento()

            print(f"Enfrentamiento: {contrincante1.nombre} vs {contrincante2.nombre}")

            #se crea el juego
            juego = Juego(contrincante1, contrincante2, None, None)
            ganador = self.simular_combate(juego) #simula el combate
            print(f"Ganador del combate: {ganador.nombre}")
            ganador.ganar_combate() #el ganador mejora sus stats 
            self.cola_prioridad.agregar_personaje(ganador) #vuele a la cola

    def simular_combate(self, juego):
        #simula el combate entre dos personajes turnándose
        while juego.jugador.vida > 0 and juego.maquina.vida > 0:
            juego.turno_jugador()  #turno del jugador
            if juego.maquina.vida <= 0:  #si la máquina pierde toda su vida, el jugador gana
                return juego.jugador
            juego.turno_maquina()  #turno de la máquina
            if juego.jugador.vida <= 0:  #si el jugador pierde toda su vida, la máquina gana
                return juego.maquina

#Representa el juego principal

class MenuPrincipal:
    def __init__(self, personajes, grafo, habilidades):
        self.personajes = personajes #lista de personajes
        self.grafo = grafo #grafo de las esferas o rutas
        self.habilidades = habilidades

    def mostrar_menu(self):
        #Bucle principal para mostrar y gestionar las opciones del menú
        while True:
            print("\n--- Menú Principal ---")
            print("1. Modo Torneo")
            print("2. Modo Batalla Rápida")
            print("3. Buscar Esferas del Dragón")
            print("4. Ver orden de habilidades")
            print("5. Salir")
            opcion = input("Selecciona una opción: ").strip()

            #Según la opción elegida, se ejecuta la funcionalidad correspondiente
            if opcion == "1":
                torneo = Torneo(self.personajes)  #se crea un torneo con los personajes
                torneo.iniciar_torneo()  #se inicia el torneo
            elif opcion == "2":
                self.modo_batalla_rapida()  #se ejecuta una batalla rápida
            elif opcion == "3":
                self.buscar_esferas()  #se busca esferas del dragón
            elif opcion == "4":
                self.ver_habilidades()  #se muestra el orden de habilidades
            elif opcion == "5":
                print("¡Gracias por jugar!")  # Salida del juego
                break
            else:
                print("Opción no válida. Intenta de nuevo.")  #validación de opción inválida

    def modo_batalla_rapida(self):
        # Selección de dos personajes aleatorios para una batalla rápida
        jugador = random.choice(self.personajes)
        maquina = random.choice([p for p in self.personajes if p != jugador])
        # Se crea un juego con el jugador y la máquina
        juego = Juego(jugador, maquina, self.grafo, None)
        juego.iniciar_combate()  # Se inicia el combate

    def buscar_esferas(self):
        # Selección de un personaje para explorar las esferas
        jugador = random.choice(self.personajes)
        # Se crea un juego para la exploración
        juego = Juego(jugador, None, self.grafo, None)
        juego.explorar_esferas()  # Se exploran las esferas del dragón)

    def ver_habilidades(self):
        # Muestra el orden de habilidades utilizando un ordenamiento topológico
        print("\nOrden de habilidades (topológico):")
        habilidades_ordenadas = self.habilidades.ordenamiento_topologico()
        for habilidad in habilidades_ordenadas:
            print(habilidad.nombre)  # Se imprime cada habilidad en el orden obtenido


# Función para seleccionar un contrincante aleatorio
def seleccionar_contrincante(personajes):
    return random.choice(personajes)


andriode16=Androide("Androide 16",arbol_habilidades_data_16,20)

andriode17=Androide("Androide 17",arbol_habilidades_data_17,8)

andriode18=Androide("Androide 18",arbol_habilidades_data_18,4)



goku = Saiyajin("Goku", arbol_habilidades_data_goku,4)
vegeta = Saiyajin("Vegeta", arbol_habilidades_data_vegeta,10)
gohan = Saiyajin("Gohan", arbol_habilidades_data_gohan,20)
