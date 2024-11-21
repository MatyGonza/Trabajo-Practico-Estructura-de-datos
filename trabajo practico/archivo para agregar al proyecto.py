import time

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
class ArbolGeneral: 
    
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

class Personaje:
    def __init__(self,nombre:str,vida:int,raza:str,estado:str,velocidad:int,defensa:int,fuerza:int,ki:int,max_ki,transformaciones,transformacion_inicial,habilidades,exp,max_exp,nivel_de_poder,nivel:int=1,max_ki_base:int=10000):
        
        self.nombre = nombre
        self.vida = vida
        self.raza = raza
        self.estado = estado
        self.velocidad = velocidad
        self.defensa = defensa
        self.fuerza = fuerza
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
        
    
    
    def mostrar_stats(self):
        print (f"Nombre: {self.nombre}\nNivel: {self.nivel}\nRaza: {self.raza}\nEstado: {self.estado}\nMaximo de Ki: {self.max_ki}\nVida: {self.vida} hp\nFuerza: {self.fuerza}\nVelocidad: {self.velocidad}\nDefensa: {self.defensa}\nExperiencia: {self.exp}/{self.max_exp}\nTransformaciones: {self.transformaciones}\nHabilidades: {self.habilidades}\nnivel de Poder: {self.nivel_de_poder}")
    
    def ataque_basico(self,enemigo): #esto es una implementacion algo basica que puede cambiar.
        if self.ki >=   1000:  #el personaje necesita un min de 1000/100000 para hacer un ataque normal
            daño = int((self.nivel_de_poder))
            print(f"{self.nombre} infligio un daño de: {daño}.")
            daño_efectivo = max(daño - self.defensa, 0) #el daño no puede ser negativo.
            enemigo.recibir_daño(daño_efectivo)
            print(f"{self.nombre} inflinge puntos daño: {daño_efectivo}.")
        print ("No se puede ataque_basico, ya que no contas con la cant. de ki necesario. Te recomiendo cargar el ki.")

    def cargar_ki(self, incremento:int, enemigo):  # Se incrementará de 1000 en cien
        while self.ki < self.max_ki:
            self.ki += incremento
            # Asegurarse de que ki no supere max_ki
            if self.ki > self.max_ki:
                self.ki = self.max_ki
            # Imprimir la carga actual
            print(f"\r{self.nombre} está cargando ki... Ki actual: {self.ki}/{self.max_ki}", end="") #el \r acualiza la linea en lugar de generar una sobre otra
            time.sleep(0.2) #pasa 0.5 segundos antes de cargar para hacer tipo una animacion
        
        print(f"\n{self.nombre} ha cargado su ki al máximo: {self.ki}/{self.max_ki}")
                
    def defender(self):
      self.estado = "Defensivo"
      print(f"{self.nombre} esta en guardia y el proximo turno del oponente el daño se reducira a la mitad.")

    def recibir_daño(self,daño_recibido):

        if self.estado == "defensivo":
            self.vida -= (daño_recibido/2)
            self.estado = "Normal"

        print(f"{self.nombre} recibio daño reducido debido a su defensa y su vida se redujo a: {self.vida}.")
      
        if self.estodo != "defensivo":
            self.vida -=daño_recibido
            print(f"Recibiste daño efectivo: {daño_recibido}\nTu vida restante es: {self.vida}")

    def usar_habilidad(self, habilidad_nombre, enemigo):
    # Buscar la habilidad en el árbol
        nodo_habilidad = self.habilidades.buscar_habilidad(habilidad_nombre)
    
    # Verificar si la habilidad existe
        if nodo_habilidad is None:
            print(f"La habilidad '{habilidad_nombre}' no existe.")
            return

    # Verificar si cumple con la transformación requerida
        if nodo_habilidad.transformacion_requerida != self.transformacion_actual:
            print(f"No puedes usar '{habilidad_nombre}' sin estar en la transformación '{nodo_habilidad.transformacion_requerida.nombre}'.")
            return

    # Verificar si tiene suficiente Ki
        if self.ki < nodo_habilidad.costo_ki:
            
            print(f"No tienes suficiente Ki para usar '{habilidad_nombre}'. Necesitas {nodo_habilidad.costo_ki}.")
            return

    # Usar la habilidad
        self.ki -= nodo_habilidad.costo_ki
        daño = nodo_habilidad.daño
        enemigo.recibir_daño(daño)
        print(f"{self.nombre} usó '{habilidad_nombre}', infligiendo {daño} puntos de daño a {enemigo.nombre}.")

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

        if self.transformacion_actual != nodo_transformacion.transformacion_requerida:
            print(f"No puedes transformarte en '{nombre_transformacion}' sin antes estar en '{nodo_transformacion.transformacion_requerida.nombre}'.")
            return

    # Realizar la transformación
        self.ki -= nodo_transformacion.ki_necesario
        self.transformacion_actual = nodo_transformacion
        #self.nivel_de_poder *= nodo_transformacion.multiplicador_nivel_de_poder
        self.evolucionar_poder(multiplicador=nodo_transformacion.multiplicador_nivel_de_poder)
        print(f"{self.nombre} se ha transformado en '{nombre_transformacion}', con nivel de poder multiplicado por {nodo_transformacion.multiplicador_nivel_de_poder}.")
        ################################################################
    def actualizar_max_exp(self):
        exp_base = 100
        max_exp_actualizada = self.nivel * exp_base
        self.max_exp = max_exp_actualizada
        return self.max_exp
    

    def incrementar_atributos(self):
        """Aumenta gradualmente los atributos de velocidad, defensa y fuerza."""
        incremento = 5  # Define cuánto se incrementarán los atributos por cada nivel de poder
        self.nivel_de_poder += incremento
        self.vida += incremento*100

    def calcular_max_ki(self,multiplicador=None):
        """Calcula el máximo de Ki basado en el nivel."""
        if multiplicador :#Al estar tranformado utiliza un multiplicador que multiplica el ki
            return (self.nivel * self.max_ki_base)*multiplicador
        else:
            return (self.nivel * self.max_ki_base)  # Ejemplo: 100 + 50 por cada nivel
        

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
            print("tranfomacion")
            return nuevo_poder


base = NodoTransformacion("Base",0,None,1)
ssj = NodoTransformacion("Super Saiyajin",4000,base,50)
ssj2 = NodoTransformacion("Super Saiyayin",5500,ssj,100)
ssj3 = NodoTransformacion("Super Saiyajin 3",7000,ssj2,150)
ssj4 = NodoTransformacion("Super Saiyajin 4",8500,ssj3,160)

#Creamos el arbol
arbol_transformaciones = ArbolGeneral(base)

#jerarquias
base.agregar_hijo(ssj)
ssj.agregar_hijo(ssj2)
ssj2.agregar_hijo(ssj3)

#Nodos de el arbol habilidad
base_habilidad = NodoHabilidad("Ataque básico", 1000, 1000,base, "Un golpe básico con Ki.\n")
kamehameha = NodoHabilidad("Kamehameha", 2000, 4000, base,"Un rayo de energia muy poderoso.")
genkidama = NodoHabilidad("Genkidama", 1500, 3000, base,"El poder de todos los seres vivos en un solo ataque, que no te alcanze ya que te dejara destrozado \n¡Levanta las manos necesito un poco de tu energia!.\n")
kamehameha_x10 = NodoHabilidad("Kamehameha",5000,40000,ssj4,"El Kamehameha aumentado 10 veces.")
#test
base_habilidad.agregar_hijo(kamehameha)
kamehameha.agregar_hijo(kamehameha_x10)
arbol_habilidad = ArbolHabilidades(base_habilidad)


goku = Personaje(nombre="Goku",vida=100000,raza="Saiyajin",estado="Normal",velocidad=50,defensa=60,fuerza=70,ki=0,max_ki=10000,transformaciones=arbol_transformaciones,transformacion_inicial=base,habilidades=arbol_habilidad,exp=0,max_exp=100,nivel_de_poder=8000,nivel=1, max_ki_base=10000)

gohan = Personaje(nombre="Gohan",vida=100000,raza="Saiyajin",estado="Normal",velocidad=50,defensa=60,fuerza=70,ki=0,max_ki=10000,transformaciones=arbol_transformaciones,transformacion_inicial=base,habilidades=arbol_habilidad,exp=0,max_exp=100,nivel_de_poder=8000,nivel=1, max_ki_base=10000)

combates_ganados = 2   
gohan.evolucionar_poder(combates_ganados)
goku.cargar_ki(1500,gohan)

gohan.cargar_ki(1500,goku)
gohan.mostrar_stats()
#goku.usar_habilidad(genkidama,gohan)

gohan.transformarse(ssj.nombre)

gohan.mostrar_stats()
