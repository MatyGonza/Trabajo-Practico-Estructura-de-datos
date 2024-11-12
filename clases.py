

import time
class Personaje:
    def __init__(self,nombre:str,vida:int,raza:str,estado:str,velocidad:int,defensa:int,fuerza:int,ki:int,max_ki,transformaciones,habilidades,exp,max_exp,nivel_pelea):
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
        print (f"Nombre: {self.nombre}\nRaza: {self.raza}\nEstado: {self.estado}\nMaximo de Ki: {self.max_ki}\nNivel de pelea: {self.nivel_pelea}\nVida: {self.vida} hp\nFuerza: {self.fuerza}\nVelocidad: {self.velocidad}\nDefensa: {self.defensa}\nExperiencia: {self.exp}/{self.max_exp}\nTransformaciones: {self.transformaciones}\nHabilidades: {self.habilidades}")
    
    def atacar(self,enemigo): #esto es una implementacion algo basica que puede cambiar.
        if self.ki >=   100:  #el personaje necesita un min de 100/1000 para hacer un ataque normal
            daño = int(self.fuerza * 10)
            print(f"{self.nombre} infligio un daño de: {daño}.")
            daño_efectivo = max(daño - self.defensa, 0) #el daño no puede ser negativo.
            enemigo.recibir_daño(daño_efectivo)
            print(f"{self.nombre} inflinge puntos daño: {daño_efectivo}.")
        print ("No se puede atacar, ya que no contas con la cant. de ki necesario. Te recomiendo cargar el ki.")

    def cargar_ki(self, incremento, enemigo):  # Se incrementará de 100 en cien
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
      pass
    
    def usar_tecnica(self):
      pass
    
    def recibir_daño(self,daño_recibido):

      if self.defensa >= daño_recibido:
         print("No se recibio daño")
      self.vida -=daño_recibido
      print(f"Recibiste daño efectivo: {daño_recibido}\nTu vida restante es: {self.vida}")

    def ataque_especial():
      pass




  
""" 
Agregue a la clase personaje el atributo vida que es un entero
agregue los nombres de los metodos que estaban en el diagrama 
agregue dos clases una humano y la otra androide como prueba estas heredan de Personaje sus atributos y metodos
"""
class Humano(Personaje):
    def __init__(self,nombre:str,vida:int,raza:str,estado:str,velocidad:int,defensa:int,fuerza:int,ki:int,max_ki,nivel:int,transformaciones,habilidades,exp,nivel_pelea):
      super().__init__(nombre, vida, "Humano","Normal",velocidad,defensa,fuerza,ki,max_ki,nivel,transformaciones,habilidades,exp,nivel_pelea) #esto ahi que cambiarlo le quite metodos y agregue unos nuevos y no tuve tiempo de corregirlo (en todos)
    
class Androide(Personaje):
    def __init__(self,nombre:str,vida:int,raza:str,estado:str,velocidad:int,defensa:int,fuerza:int,ki:int,max_ki:int,transformaciones,habilidades,exp,nivel_pelea):
      super().__init__(nombre, vida, "Andriode","Normal",velocidad,defensa,fuerza,ki,max_ki,transformaciones,habilidades,exp,nivel_pelea)
    
class Sayayin(Personaje):
    def __init__(self,nombre:str,vida:int,raza:str,estado:str,velocidad:int,defensa:int,fuerza:int,ki:int,max_ki,nivel:int,transformaciones,habilidades,exp,nivel_pelea):
      super().__init__(nombre, vida, "Sayayin","Normal",velocidad,defensa,fuerza,ki,max_ki,nivel,transformaciones,habilidades,exp,nivel_pelea)
    
goku = Personaje("Son Guku",10000,"Saiyayin","Normal",70,70,70,0,10000,None,None,0,100,2)
enemigo = Personaje("Cell",10000,"Androide","Normal",70,70,50,0,10000,None,None,0,100,3)


#test
goku.atacar(enemigo)
goku.cargar_ki(100,enemigo)
enemigo.cargar_ki(100,goku)
goku.atacar(enemigo)
enemigo.atacar(goku)
