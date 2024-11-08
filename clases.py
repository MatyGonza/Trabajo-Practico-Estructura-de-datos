
""" 
Agregue a la clase personaje el atributo vida que es un entero
agregue los nombres de los metodos que estaban en el diagrama 
agregue dos clases una humano y la otra androide como prueba estas heredan de Personaje sus atributos y metodos
"""
class Personaje:
    def __init__(self,nombre:str,vida:int,raza:str,estado:str,velocidad:int,defensa:int,fuerza:int,ki:int,max_ki,nivel:int,transformaciones,habilidades,exp,nivel_pelea):
        self.nombre = nombre
        self.vida = vida
        self.raza = raza
        self.estado = estado
        self.velocidad = velocidad
        self.defensa = defensa
        self.fuerza = fuerza
        self.ki = ki
        self.max_ki = max_ki
        self.nivel = nivel
        self.transformaciones = transformaciones
        self.habilidades = habilidades
        self.exp = exp
        self.nivel_pelea = nivel de pelea #este seria un parametro para la cola de prioridad o para separar personajes
                                           #y que no sea desequlibrada la pelea ejem (satan vs goku) no seria posible    
    
    
    def atacar(self,enemigo): #esto es una implementacion algo basica que puede cambiar.
        if self.ki >= 100:  #el personaje necesita un min de 100/1000 para hacer un ataque normal
            daño = int(self.fuerza * 10)
            print(f"{self.nombre} infligio un daño de: {daño}.")
            daño_efectivo = max(daño - self.defenza, 0) #el daño no puede ser negativo.
            enemigo.recibir_daño(daño_efectivo)
            print(f"{self.nombre} inflinge puntos daño: {daño_efectivo}.")
        print ("No se puede atacar, ya que no contas con la cant. de ki necesario. Te recomiendo cargar el ki.")

    def cargar_ki(self,incremento = 100,enemigo): #se incrementara de 100 en cien
        if self.ki >= self.max_ki: #caso base
            self.ki = self.max_ki
            print(f"{self.nombre} ha cargado su ki al máximo: {self.ki}/{self.max_ki}")
            return
            self.ki += incremento #lo incrementa en 100 cada llamada
            print(f"{self.nombre} está cargando ki... Ki actual: {self.ki}/{self.max_ki}")
            self.cargar_ki (incfemento,enemigo)

    
            
    def defender(self):
      pass
    
    def usar_tecnica(self):
      pass
    
    def recibir_daño(self):
      pass
    
    def mostrar_estado(self):
      pass
  
    
class Humano(Personaje):
    def __init__(self,nombre:str,vida:int,raza:str,estado:str,velocidad:int,defensa:int,fuerza:int,ki:int,max_ki,nivel:int,transformaciones,habilidades,exp,nivel_pelea):
        super().__init__(nombre, vida, "Humano","Normal",velocidad,defensa,fuerza,ki,max_ki,nivel,transformaciones,habilidades,exp,nivel_pelea)
    
class Androide(Personaje):
    def __init__(self,nombre:str,vida:int,raza:str,estado:str,velocidad:int,defensa:int,fuerza:int,ki:int,max_ki;nivel:int,transformaciones,habilidades,exp,nivel_pelea):
        super().__init__(nombre, vida, "Andriode","Normal",velocidad,defensa,fuerza,ki,max_ki,nivel,transformaciones,habilidades,exp,nivel_pelea)
    
class Sayayin(Personaje):
    def __init__(self,nombre:str,vida:int,raza:str,estado:str,velocidad:int,defensa:int,fuerza:int,ki:int,max_ki,nivel:int,transformaciones,habilidades,exp,nivel_pelea):
        super().__init__(nombre, vida, "Sayayin","Normal",velocidad,defensa,fuerza,ki,max_ki,nivel,transformaciones,habilidades,exp,nivel_pelea)
