from clases.personaje import Personaje
from clases.juego import Juego
from clases.cola_prioridad import ColaDePrioridad
from clases.grafo import GrafoDragonBall
from clases.arbolDB import ArbolBinario

class JuegoTorneo(Juego):
    def __init__(self, jugador: Personaje, personajes_disponibles):
        super().__init__(jugador, None)  # Inicia con un jugador y sin máquina
        self.personajes_disponibles = personajes_disponibles  # Lista de personajes disponibles

    def elegir_personaje(self):
        print("Selecciona un personaje para el torneo:")
        for i, personaje in enumerate(self.personajes_disponibles):
            print(f"{i+1}. {personaje.nombre} (Poder: {personaje.nivel_de_poder})")
        opcion = int(input("Elige un número de personaje: ")) - 1
        self.maquina = self.personajes_disponibles[opcion]
        print(f"Has seleccionado a {self.maquina.nombre} para el torneo.")

    def iniciar_torneo(self):
        # Crear cola de prioridad
        cola = ColaDePrioridad()
        
        # Agregar personajes a la cola de prioridad (según su nivel de poder)
        for personaje in self.personajes_disponibles:
            cola.agregar_personaje(personaje)

        # Simular combates
        print("Comienza el torneo!")
        while not cola.esta_vacia():
            oponente = cola.siguiente_enfrentamiento()  # Personaje con mayor poder
            print(f"El siguiente combate es entre {self.jugador.nombre} y {oponente.nombre}.")
            self.iniciar_combate()  # Iniciar combate con el oponente


class TorneoArbolBinario:
    def __init__(self, personajes_disponibles):
        self.arbol = ArbolBinario()
        self.personajes_disponibles = personajes_disponibles

    def organizar_torneo(self):
        for personaje in self.personajes_disponibles:
            self.arbol.insertar(personaje)  # Insertar personajes al árbol según su poder
        print("Torneo organizado. El árbol de combate se ha construido.")
    
    def mostrar_arbol(self):
        self.arbol.mostrar_ramas()

class TorneoGrafo:
    def __init__(self, planetas):
        self.grafo = GrafoDragonBall(planetas)

    def agregar_rutas(self):
        # Agregar rutas entre planetas (por ejemplo, entre diferentes lugares del torneo)
        self.grafo.agregar_ruta("Planeta A", "Planeta B", 10)
        self.grafo.agregar_ruta("Planeta B", "Planeta C", 5)
        self.grafo.agregar_ruta("Planeta A", "Planeta C", 15)
    
    def simular_ubicacion(self):
        # Aquí se puede hacer una simulación de viajes entre planetas
        print("Simulando ubicaciones en el torneo...")
        self.grafo.mostrar_rutas()  # Mostrar las rutas entre planetas

def main():
    # Crear personajes
    personaje1 = Personaje("Goku", 1000, "Saiyan", 50)
    personaje2 = Personaje("Vegeta", 950, "Saiyan", 55)
    personaje3 = Personaje("Freezer", 1200, "Alien", 40)
    personajes_disponibles = [personaje1, personaje2, personaje3]
    
    # Seleccionar personaje y iniciar el torneo
    jugador = personaje1  # El jugador elige a Goku, por ejemplo
    juego = JuegoTorneo(jugador, personajes_disponibles)
    juego.elegir_personaje()
    juego.iniciar_torneo()

    # Organizar y mostrar árbol de combate
    torneo_arbol = TorneoArbolBinario(personajes_disponibles)
    torneo_arbol.organizar_torneo()
    torneo_arbol.mostrar_arbol()

    # Simular ubicación de los combates
    torneo_grafo = TorneoGrafo(["Planeta A", "Planeta B", "Planeta C"])
    torneo_grafo.agregar_rutas()
    torneo_grafo.simular_ubicacion()