
#time, que se utiliza para pausar la ejecución del programa durante un período específico, creando efectos de animación.
import time

class Personaje:
    """
    La clase Personaje es la clase base que define las características y comportamientos comunes de todos los personajes en el juego.
    """
    def __init__(self, nombre:str, vida:int, raza:str, estado:str, velocidad:int, defensa:int, fuerza:int, ki:int, transformaciones:list, habilidades:list, exp:int, max_exp:int,nivel_pelea:int,nivel:int=1,max_ki_base:int=10000,max_ki:int=10000):
        #Si no se le pasan los parametros se crea una lista vacia, esta bueno porque al empezar todos los personajes empezaran sin habilidades
        #Esta parte creo que se implementa con otra estructura de datos a revisar
        if transformaciones is None:
            transformaciones = []
        if habilidades is None:
            habilidades = []
        self.nombre = nombre
        self.vida = vida
        self.raza = raza
        self.estado = estado
        self.velocidad = velocidad
        self.defensa = defensa
        self.fuerza = fuerza
        self.ki = ki
        self.max_ki = max_ki #Inicializa el maximo de ki
        self.transformaciones = transformaciones
        self.habilidades = habilidades
        self.exp = exp
        self.max_exp = max_exp
        self.nivel_pelea = nivel_pelea #este seria un parametro para la cola de prioridad o para separar personajes
          #y que no sea desequlibrada la pelea ejem (satan vs goku) no seria posible    
        self.nivel = nivel  # Se agrego nivel para tener una referencia de nivel del personaje y el max ki, ya que el nivel de pelea puede variar si realiza una transformacion pero el nivel de personaje no cambia
        self.max_ki_base = max_ki_base# se agrego este atributo para tener una base al cual multiplicar cuando se actualiza el max ki segun el nivel del personaje
    def mostrar_stats(self):
        """ 
        estas listas se convierten en cadenas separadas por comas utilizando ', '.join(...).
        si esta vacia imprime ninguna
        """
                # Convertir las listas a cadenas separadas por comas
        habilidades_str = ', '.join(self.habilidades) if self.habilidades else "Ninguna"
        transformaciones_str = ', '.join(self.transformaciones) if self.transformaciones else "Ninguna"
      
        print (f"Nombre: {self.nombre}\nRaza: {self.raza}\nEstado: {self.estado}\nKi: {self.ki}\nMaximo de Ki: {self.max_ki}\nNivel de pelea: {self.nivel_pelea}\nVida: {self.vida} hp\nFuerza: {self.fuerza}\nVelocidad: {self.velocidad}\nDefensa: {self.defensa}\nExperiencia: {self.exp}/{self.max_exp}\nTransformaciones: {transformaciones_str}\nHabilidades: {habilidades_str}\n")
    
    def atacar(self,enemigo): #esto es una implementacion algo basica que puede cambiar.
        if self.ki >=   100:  #el personaje necesita un min de 100/1000 para hacer un ataque normal
            daño = int(self.fuerza * 10)
            print(f"{self.nombre} infligio un daño de: {daño}.")
            daño_efectivo = max(daño - self.defensa, 0) #el daño no puede ser negativo.
            enemigo.recibir_daño(daño_efectivo)
            print(f"{self.nombre} inflinge puntos daño: {daño_efectivo}.")
            self.ki -= 100  # Reduce ki al atacar
        else:
          print ("No se puede atacar, ya que no contas con la cant. de ki necesario. Te recomiendo cargar el ki.")

    
    def cargar_ki(self, incremento):  # Se incrementará de 100 en cien
        while self.ki < self.max_ki:
            self.ki += incremento
            # Asegurarse de que ki no supere max_ki
            if self.ki > self.max_ki:
                self.ki = self.max_ki
            # Imprimir la carga actual
            print(f"\r{self.nombre} está cargando ki... Ki actual: {self.ki}/{self.max_ki}", end="") #el \r acualiza la linea en lugar de generar una sobre otra
            time.sleep(0.02) #pasa 0.5 segundos antes de cargar para hacer tipo una animacion
        
        print(f"\n{self.nombre} ha cargado su ki al máximo: {self.ki}/{self.max_ki}")
        
    #Agrega una habilidad, se puede aprender con los entrenamientos o al subir nivel
    def aprender_habilidad(self, habilidad):
        self.habilidades.append(habilidad)
        
    
            
    def defender(self):
      pass
    
    def usar_tecnica(self):
      pass
    
    def recibir_daño(self,daño_recibido):

      if self.defensa >= daño_recibido:
        print("No se recibio daño")
        return
      else:
        self.vida -=daño_recibido
        if self.vida < 0 :
          #No puede llegar la vida a menos de 0 
          self.vida = 0 
        
      print(f"Recibiste daño efectivo: {daño_recibido}\nTu vida restante es: {self.vida}")

    def ataque_especial(self, enemigo):
        """Método para realizar un ataque especial (por definir en subclases)."""
        raise NotImplementedError("Este método debe ser implementado en las subclases.")

    ################################################################
    
    def calcular_max_ki(self):
          """Calcula el máximo de Ki basado en el nivel."""
          return (self.nivel * self.max_ki_base)  # Ejemplo: 100 + 50 por cada nivel
        
      
    def subir_nivel(self):
        #Sube el nivel del personaje si alcanza la experiencia necesaria.
        if self.exp >= self.nivel * 100:  # Ejemplo: 100 exp por nivel
            self.nivel += 1
            self.max_ki = self.calcular_max_ki()  # Actualiza el máximo de Ki
            print(f"{self.nombre} ha subido al nivel {self.nivel}!")
            # Llamada recursiva para verificar si se puede subir nuevamente
            self.subir_nivel()
    
    def evolucionar_poder(self, combates_ganados, multiplicador=1):
        """
        Método recursivo para calcular la evolución del poder tras cada combate.
        
        :param combates_ganados: Número de combates ganados.
        :param multiplicador: Multiplicador actual (por defecto es 1).
        :return: Poder total tras los combates.
        """
        if combates_ganados <= 0:
            return self.nivel_pelea
        
        # Calcular el nuevo poder
        nuevo_poder = self.nivel_pelea * multiplicador
        
        # Actualizar el poder actual
        self.nivel_pelea = nuevo_poder
        
        # Aumentar experiencia tras cada combate
        self.exp += 50  # Ejemplo: ganar 50 exp por combate
        print(f"{self.nombre} ganó experiencia. Total exp: {self.exp}")
        
        # Verificar si se debe subir de nivel
        self.subir_nivel()
        
        # Llamada recursiva para el siguiente combate
        return self.evolucionar_poder(combates_ganados - 1, multiplicador)
      
      