from pruebas2 import Juego
from clases.personaje import Personaje
from clases.cola_prioridad import ColaDePrioridad
from clases.grafo import GrafoDragonBall
from personajes.personajes_androide import andriode16, andriode17, andriode18
from personajes.personajes_saiyajin import goku, gohan, vegeta

import random



#clase
class Torneo:
    def __init__(self, personajes):
        #se inicia una cola de prioridad
        self.cola_prioridad = ColaDePrioridad()
        #se agregan los personajes
        for personaje in personajes:
            self.cola_prioridad.agregar_personaje(personaje)
        self.ganador = None #aca se guarda el ganador

    def iniciar_torneo(self):
        print("¡Iniciando el Torneo de Artes Marciales!")
        #El torneo se ejecuta hasta que quede un solo personaje en la cola
        while not self.cola_prioridad.esta_vacia():
            # Si solo queda un personaje, es el ganador del torneo
            if len(self.cola_prioridad.heap) == 1:
                self.ganador = self.cola_prioridad.siguiente_enfrentamiento()
                print(f"El ganador del torneo es {self.ganador.nombre} con un nivel de poder de {self.ganador.nivel_de_poder}!")
                break

            #se seleccionan a los dos luchadores        
            contrincante1 = self.cola_prioridad.siguiente_enfrentamiento()
            contrincante2 = self.cola_prioridad.siguiente_enfrentamiento()

            print(f"Enfrentamiento: {contrincante1.nombre} vs {contrincante2.nombre}")

            #se crea el juego
            juego = Juego(contrincante1, contrincante2, None, None)
            ganador = self.simular_combate(juego) #simula el combate
            print(f"Ganador del combate: {ganador.nombre}")
            ganador.ganar_combate() #el ganador mejora sus stats 
            self.cola_prioridad.agregar_personaje(ganador) #vuele a la cola

    def simular_combate(self, juego):
        #simula el combate entre dos personajes turnándose
        while juego.jugador.vida > 0 and juego.maquina.vida > 0:
            juego.turno_jugador()  #turno del jugador
            if juego.maquina.vida <= 0:  #si la máquina pierde toda su vida, el jugador gana
                return juego.jugador
            juego.turno_maquina()  #turno de la máquina
            if juego.jugador.vida <= 0:  #si el jugador pierde toda su vida, la máquina gana
                return juego.maquina

#Representa el juego principal

class MenuPrincipal:
    def __init__(self, personajes, grafo, habilidades):
        self.personajes = personajes #lista de personajes
        self.grafo = grafo #grafo de las esferas o rutas
        self.habilidades = habilidades

    def mostrar_menu(self):
        #Bucle principal para mostrar y gestionar las opciones del menú
        while True:
            print("\n--- Menú Principal ---")
            print("1. Modo Torneo")
            print("2. Modo Batalla Rápida")
            print("3. Buscar Esferas del Dragón")
            print("4. Ver orden de habilidades")
            print("5. Salir")
            opcion = input("Selecciona una opción: ").strip()

            #Según la opción elegida, se ejecuta la funcionalidad correspondiente
            if opcion == "1":
                torneo = Torneo(self.personajes)  #se crea un torneo con los personajes
                torneo.iniciar_torneo()  #se inicia el torneo
            elif opcion == "2":
                self.modo_batalla_rapida()  #se ejecuta una batalla rápida
            elif opcion == "3":
                self.buscar_esferas()  #se busca esferas del dragón
            elif opcion == "4":
                self.ver_habilidades()  #se muestra el orden de habilidades
            elif opcion == "5":
                print("¡Gracias por jugar!")  # Salida del juego
                break
            else:
                print("Opción no válida. Intenta de nuevo.")  #validación de opción inválida

    def modo_batalla_rapida(self):
        # Selección de dos personajes aleatorios para una batalla rápida
        jugador = random.choice(self.personajes)
        maquina = random.choice([p for p in self.personajes if p != jugador])
        # Se crea un juego con el jugador y la máquina
        juego = Juego(jugador, maquina, self.grafo, None)
        juego.iniciar_combate()  # Se inicia el combate

    def buscar_esferas(self):
        # Selección de un personaje para explorar las esferas
        jugador = random.choice(self.personajes)
        # Se crea un juego para la exploración
        juego = Juego(jugador, None, self.grafo, None)
        juego.explorar_esferas()  # Se exploran las esferas del dragón)

    def ver_habilidades(self):
        # Muestra el orden de habilidades utilizando un ordenamiento topológico
        print("\nOrden de habilidades (topológico):")
        habilidades_ordenadas = self.habilidades.ordenamiento_topologico()
        for habilidad in habilidades_ordenadas:
            print(habilidad.nombre)  # Se imprime cada habilidad en el orden obtenido


# Crear los objetos y ejecutar el menú




