from clases.personaje import Personaje

class Sayayin(Personaje):
    #def __init__(self, nombre: str, vida: int, raza: str, estado: str, velocidad: int, defensa: int, fuerza: int, ki: int, transformaciones: list, habilidades: list, exp: int, max_exp: int, nivel_pelea: int, nivel: int = 1, max_ki_base: int = 10000, max_ki: int = 10000):
        #super().__init__(nombre, vida=1000, raza="Sayayin", estado="Normal", velocidad=15, defensa=70, fuerza=70, ki=0, transformaciones=None, habilidades=None, exp=0, max_exp=100, nivel_pelea=1, nivel=1, max_ki_base=10000, max_ki=None)
    def __init__(self, nombre: str, transformaciones=None, habilidades=None):
        super().__init__(nombre, vida=1000, raza="Sayayin", estado="Normal", velocidad=15, defensa=70, fuerza=70, ki=0,habilidades = habilidades if not None else [],transformaciones = transformaciones if not None else [],  exp=0, max_exp=100, nivel_pelea=1)
        
    def ataque_especial(self, enemigo):
        """Ataque especial del Sayayin."""
        if self.ki >= 500:
            # Calcular el daño potencial basado en la fuerza
            daño_especial = int(self.fuerza * 20)
            
            daño_efectivo = daño_especial - int(enemigo.defensa)
            
            # Asegurarse de que el daño no sea negativo
            if daño_efectivo < 0:
                daño_efectivo = 0
            
            # Aplicar el daño al enemigo
            enemigo.recibir_daño(daño_efectivo)
            
            # Mensaje de resultado
            print(f"{self.nombre} desató un poderoso ataque especial infligiendo {daño_efectivo} puntos de daño a {enemigo.nombre}.")
            
            # Reducir ki al usar el ataque especial
            self.ki -= 500  
        else:
            print("No tienes suficiente ki para realizar un ataque especial.")
