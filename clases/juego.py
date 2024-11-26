from personajes.personajes_saiyajin import goku, gohan, vegeta
from personajes.personajes_androide import andriode16, andriode17, andriode18
from clases.personaje import Personaje
from clases.grafo import GrafoDragonBall
from clases.arbolDB import ArbolBinario
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
            while True:  # Bucle para repetir hasta que se ingrese una opción válida
                print(f"\nTurno de {self.jugador.nombre}.")
                print(f"Vida de {self.maquina.nombre}: {self.maquina.vida} HP")
                
                accion = input("¿Quieres atacar (a) o cargar ki (c) o defenderse (d)?").strip().lower()
                
                if accion == 'a':
                    self.jugador.ataque_basico(self.maquina)
                    break  # Salir del bucle si la acción es válida
                if accion == 'c':
                    self.jugador.cargar_ki(1000)
                    break  # Salir del bucle si la acción es válida
                elif accion == 'd':
                    self.jugador.defender()
                else: 
                    print("Acción no válida. Por favor, elige 'a' para atacar o 'c' para cargar ki.")

    def turno_maquina(self):
        print(f"\nTurno de {self.maquina.nombre}.")
        if self.maquina.ki >= 100 and random.choice([True, False]):
            self.maquina.ataque_basico(self.jugador)
        else:
            self.maquina.cargar_ki(1000)

    def buscar_oponentes(self,grafo:GrafoDragonBall):
        print(f"El enemigo {self.enemigo.nombre} escapo, {self.jugador.nombre} fue a buscarlo...")

        camino_bfs = grafo.bfs(self.jugador.planeta_actual,self.maquina.planeta_actual)
        print(f"Se hizo un viaje por: {camino_bfs} y se encontro al oponente... en el planeta: {self.maquina.planeta_actual}")


            


            

