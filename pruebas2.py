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
            print(f"""\n
                  Turno de {self.jugador.nombre} 
-- ki:{self.jugador.ki}/{self.jugador.max_ki} -- vida:{self.jugador.vida} -- nivel:{self.jugador.nivel} -- transformacion actual: {self.jugador.transformacion_actual.nombre}
combates ganados: {self.jugador.combates_ganados} -- experiencia: {self.jugador.exp}/{self.jugador.max_exp} -- nivel de poder: {self.jugador.nivel_de_poder} -- \n""")
            print(f"Vida del oponente {self.maquina.nombre}: {self.maquina.vida} HP")
            print("\nHabilidades disponibles:")
            
            self.jugador.habilidades.mostrar_arbol()
            

            accion = input("¿Quieres usar una habilidad (Escribela) o cargar ki (c)? ").lower()
            
            if accion == 'c':
                self.jugador.cargar_ki(1000)
                break
            elif accion :
                self.jugador.usar_habilidad(accion, self.maquina)
                break
            else:
                print("\nAcción no válida. Por favor, elige un número válido o 'c' para cargar ki.")
            
        print("---"*20)
    import random

    def turno_maquina(self):
        print(f"""\n
                Turno de {self.maquina.nombre} 
        -- ki:{self.maquina.ki}/{self.maquina.max_ki} -- vida:{self.maquina.vida} -- nivel:{self.maquina.nivel} -- transformación actual: {self.maquina.transformacion_actual.nombre}
        combates ganados: {self.maquina.combates_ganados} -- experiencia: {self.maquina.exp}/{self.maquina.max_exp} -- nivel de poder: {self.maquina.nivel_de_poder} -- \n""")
        
        # Obtener todas las transformaciones disponibles
        transformaciones_disponibles = self.maquina.transformaciones.obtener_transformaciones_disponibles(self.maquina)
        
        # Mensaje de depuración sobre las transformaciones disponibles
        print(f"Transformaciones disponibles: {[t.nombre for t in transformaciones_disponibles]}")

        # Seleccionar una acción al azar: transformación o habilidad
        if transformaciones_disponibles and self.maquina.ki > 0:
            # Elegir aleatoriamente entre transformar o usar habilidad
            accion = random.choice(['transformar', 'usar_habilidad'])

            if accion == 'transformar':
                # Seleccionar una transformación aleatoria
                transformacion_aleatoria = random.choice(transformaciones_disponibles)
                if self.maquina.ki >= transformacion_aleatoria.ki_necesario:
                    print(f"Transformación aleatoria seleccionada: {transformacion_aleatoria.nombre}, Ki necesario: {transformacion_aleatoria.ki_necesario}")
                    self.maquina.transformarse(transformacion_aleatoria.nombre)
                else:
                    print(f"No hay suficiente Ki para la transformación aleatoria: {transformacion_aleatoria.nombre}. Ki disponible: {self.maquina.ki}")

            elif accion == 'usar_habilidad':
                # Usar habilidades al azar si hay suficiente Ki
                if self.maquina.ki >= 1000:
                    habilidad_aleatoria = self.maquina.habilidades.seleccionar_habilidad_aleatoria()  # Obtener la habilidad aleatoria
                    if habilidad_aleatoria:
                        print(f"Usando habilidad aleatoria: {habilidad_aleatoria.nombre}")
                        self.maquina.usar_habilidad(habilidad_aleatoria.nombre, self.jugador)
                else:
                    print("No hay suficiente Ki para usar habilidades. Cargando Ki...")
                    self.maquina.cargar_ki(1000)
        
        else:
            print("No hay transformaciones disponibles o no hay Ki para actuar.")    
    
# Función para seleccionar un contrincante aleatorio
def seleccionar_contrincante(personajes):
    return random.choice(personajes)

# Ejemplo de uso
if __name__ == "__main__":
    personajes = [gohan, vegeta]

    # Seleccionar un contrincante aleatorio
    contrincante = seleccionar_contrincante(personajes)

    # Iniciar el juego
    juego = Juego(goku, contrincante)
    juego.iniciar_combate()