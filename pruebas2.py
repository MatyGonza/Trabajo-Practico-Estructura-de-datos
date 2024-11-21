from personajes.personajes_sayayin import goku,gohan,vegeta
from personajes.personajes_androide import andriode16,andriode17,andriode18

from clases.personaje import Personaje
from clases.sayayin import Sayayin  # Asegúrate de importar la clase correcta
#from clases.habilidades import crear_arbol_habilidades  # Importar la función para crear habilidades
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
            print(f"\nTurno de {self.jugador.nombre}.")
            print(f"Vida de {self.maquina.nombre}: {self.maquina.vida} HP")
            print("Habilidades disponibles:")
            
            # Acceder a las habilidades desde la raíz del árbol
            for i, habilidad in enumerate(self.jugador.habilidades.raiz.hijos):
                print(f"{i + 1}. {habilidad.nombre} (Costo Ki: {habilidad.costo_ki}, Daño: {habilidad.daño})")

            accion = input("¿Quieres usar una habilidad (número) o cargar ki (c)? ").strip().lower()
            
            if accion.isdigit() and 1 <= int(accion) <= len(self.jugador.habilidades.raiz.hijos):
                habilidad_seleccionada = self.jugador.habilidades.raiz.hijos[int(accion) - 1]
                self.jugador.usar_habilidad(habilidad_seleccionada, self.maquina)
                break
            elif accion == 'c':
                self.jugador.cargar_ki(1000)
                break
            else:
                print("Acción no válida. Por favor, elige un número válido o 'c' para cargar ki.")
    def turno_maquina(self):
        print(f"\nTurno de {self.maquina.nombre}.")
        if self.maquina.ki >= 100 and random.choice([True, False]):
            # Acceder a las habilidades desde la raíz del árbol
            habilidad_aleatoria = random.choice(self.maquina.habilidades.raiz.hijos)
            self.maquina.usar_habilidad(habilidad_aleatoria, self.jugador)
        else:
            self.maquina.cargar_ki(1000)

# Función para seleccionar un contrincante aleatorio
def seleccionar_contrincante(personajes):
    return random.choice(personajes)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear personajes (asegúrate de que estas clases existan y estén correctamente definidas)
    #goku = Sayayin("Goku", arbol_habilidades_data)
    #vegeta = Sayayin("Vegeta", arbol_habilidades_data)
    personajes = [goku, vegeta]

    # Seleccionar un contrincante aleatorio
    contrincante = seleccionar_contrincante(personajes)

    # Iniciar el juego
    juego = Juego(goku, contrincante)
    juego.iniciar_combate()