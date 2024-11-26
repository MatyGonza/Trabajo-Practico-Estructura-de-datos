from personajes.personajes_sayayin import goku,gohan,vegeta
from personajes.personajes_androide import andriode16,andriode17,andriode18

from clases.personaje import Personaje
from clases.sayayin import Sayayin  # Asegúrate de importar la clase correcta
import random

class Juego:
    def __init__(self, jugador: Personaje, maquina: Personaje):
        self.jugador = jugador
        self.maquina = maquina

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
            print(f"""\nTurno de {self.jugador.nombre} -- ki:{self.jugador.ki}/{self.jugador.max_ki} -- vida:{self.jugador.vida} -- nivel:{self.jugador.nivel} -- transformacion actual: {self.jugador.transformacion_actual.nombre}\n""")
            print(f"Vida del oponente {self.maquina.nombre}: {self.maquina.vida} HP")
            print("\nHabilidades disponibles:")
            
            habilidades = self.jugador.habilidades.listar_habilidades()
            
            for i, habilidad in enumerate(habilidades):
                print(f"{i + 1}. {habilidad.nombre} (Costo Ki: {habilidad.costo_ki}, Daño: {habilidad.daño})")
            accion = input("¿Quieres usar una habilidad (número) o cargar ki (c)? ").strip().lower()
            
            if accion.isdigit() and 1 <= int(accion) <= len(habilidades):
                habilidad_seleccionada = habilidades[int(accion) - 1]
                self.jugador.usar_habilidad(habilidad_seleccionada.nombre, self.maquina)
                break
            elif accion == 'c':
                self.jugador.cargar_ki(1000)
                break
            else:
                print("\nAcción no válida. Por favor, elige un número válido o 'c' para cargar ki.")
            
        print("---"*20)
    
    

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
        
    
    def turno_maquina(self):
        print(f"""\nTurno del oponente {self.maquina.nombre} -- ki:{self.jugador.ki}/{self.jugador.max_ki} -- vida:{self.jugador.vida} -- nivel:{self.jugador.nivel} -- transformacion actual: {self.jugador.transformacion_actual.nombre}\n""")
        
        if self.maquina.ki >= 100 and random.choice([True, False]):
            # Acceder a las habilidades desde la raíz del árbol
            habilidades = self.maquina.habilidades.listar_habilidades()
            
            habilidad_aleatoria = random.choice(habilidades)
            self.maquina.usar_habilidad(habilidad_aleatoria.nombre, self.jugador)
        else:
            self.maquina.cargar_ki(1000)
            
        print("---"*20)

# Función para seleccionar un contrincante aleatorio
def seleccionar_contrincante(personajes):
    return random.choice(personajes)

# Ejemplo de uso
if __name__ == "__main__":
    personajes = [goku, vegeta]

    # Seleccionar un contrincante aleatorio
    contrincante = seleccionar_contrincante(personajes)

    # Iniciar el juego
    juego = Juego(goku, contrincante)
    juego.iniciar_combate()