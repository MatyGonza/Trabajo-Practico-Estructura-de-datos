import time 
from clases.arbol_transformaciones import ArbolTransformaciones
from clases.arbol_habilidades import ArbolHabilidades









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
        print (f"\nNombre: {self.nombre}\nNivel: {self.nivel}\nTransformacion actual: {self.transformacion_actual.nombre}\nKi: {self.ki}\nRaza: {self.raza}\nEstado: {self.estado}\nMaximo de Ki: {self.max_ki}\nVida: {self.vida} hp\nExperiencia: {self.exp}/{self.max_exp}\nTransformaciones:\nHabilidades: \nnivel de Poder: {self.nivel_de_poder}\n")
    
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
                
   
            
            print(f"{personaje.nombre} Recibiste daño efectivo: {daño_recibido}..Tu vida restante es: {self.vida}")

    def usar_habilidad(self, habilidad_nombre, enemigo):
        # Buscar la habilidad en el árbol
        nodo_habilidad = self.habilidades.buscar_habilidad(habilidad_nombre.lower())
    
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
                print(f"{self.nombre} usó '{habilidad_nombre}', infligiendo {daño} puntos de daño a {enemigo.nombre}.")
                enemigo.recibir_daño(daño,enemigo)  # Ajustamos la llamada para que no pase el enemigo de más
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
        if self.transformacion_actual.nombre is None or self.transformacion_actual.nombre != nodo_transformacion.transformacion_requerida:
            print(f"No puedes transformarte en '{nombre_transformacion}' sin antes estar en '{nodo_transformacion.transformacion_requerida.nombre}'.")
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





 

