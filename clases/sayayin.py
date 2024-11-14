from clases.personaje import Personaje

class Sayayin(Personaje):
    def __init__(self, nombre: str, vida: int, raza: str, estado: str, velocidad: int, defensa: int, fuerza: int, ki: int, max_ki, transformaciones, habilidades, exp, max_exp, nivel_pelea):
        super().__init__(nombre, vida, raza, estado, velocidad, defensa, fuerza, ki, max_ki, transformaciones, habilidades, exp, max_exp, nivel_pelea)

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
