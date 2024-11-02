

""" 
Agregue a la clase personaje el atributo vida que es un entero
agregue los nombres de los metodos que estaban en el diagrama 
agregue dos clases una humano y la otra androide como prueba estas heredan de Personaje sus atributos y metodos
"""

class Personaje:
  def __init__(self,nombre:str,vida:int,raza:str,nivel_de_poder:int,habilidades):
    self.nombre = nombre
    self.vida = vida
    self.raza = raza
    self.nivel_de_poder = nivel_de_poder
    self.habilidades = []
    
    def atacar(self):
      pass
    
    def defender(self):
      pass
    
    def usar_tecnica(self):
      pass
    
    def recibir_daño(self):
      pass
    
    def mostrar_estado(self):
      pass
    
class Humano(Personaje):
  def __init__(self, nombre: str, vida: int, raza: str, nivel_de_poder: int, habilidades):
    super().__init__(nombre, vida, "Humano", nivel_de_poder, habilidades)
    
class Androide(Personaje):
  def __init__(self, nombre: str, vida: int, raza: str, nivel_de_poder: int, habilidades):
    super().__init__(nombre, vida, "Andriode", nivel_de_poder, habilidades)