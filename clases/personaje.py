
#time, que se utiliza para pausar la ejecución del programa durante un período específico, creando efectos de animación.
import time

class Personaje:
    """
    La clase Personaje es la clase base que define las características y comportamientos comunes de todos los personajes en el juego.
    """
    def __init__(self, nombre:str, vida:int, raza:str, estado:str, velocidad:int, defensa:int, fuerza:int, ki:int, max_ki:int, transformaciones:list, habilidades:list, exp:int, max_exp:int,nivel_pelea:int):
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
        self.max_ki = max_ki
        self.transformaciones = transformaciones
        self.habilidades = habilidades
        self.exp = exp
        self.max_exp = max_exp
        self.nivel_pelea = nivel_pelea #este seria un parametro para la cola de prioridad o para separar personajes
          #y que no sea desequlibrada la pelea ejem (satan vs goku) no seria posible    
    def mostrar_stats(self):
        """ 
        estas listas se convierten en cadenas separadas por comas utilizando ', '.join(...).
        si esta vacia imprime ninguna
        """
                # Convertir las listas a cadenas separadas por comas
        habilidades_str = ', '.join(self.habilidades) if self.habilidades else "Ninguna"
        transformaciones_str = ', '.join(self.transformaciones) if self.transformaciones else "Ninguna"
      
        print (f"Nombre: {self.nombre}\nRaza: {self.raza}\nEstado: {self.estado}\nMaximo de Ki: {self.max_ki}\nNivel de pelea: {self.nivel_pelea}\nVida: {self.vida} hp\nFuerza: {self.fuerza}\nVelocidad: {self.velocidad}\nDefensa: {self.defensa}\nExperiencia: {self.exp}/{self.max_exp}\nTransformaciones: {transformaciones_str}\nHabilidades: {habilidades_str}\n")
    
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

    
    def cargar_ki(self, incremento, enemigo):  # Se incrementará de 100 en cien
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



