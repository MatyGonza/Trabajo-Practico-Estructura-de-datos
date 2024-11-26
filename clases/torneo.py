import heapq
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



