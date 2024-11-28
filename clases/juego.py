from personajes.personajes_saiyajin import goku, gohan, vegeta
from personajes.personajes_androide import andriode16, andriode17, andriode18
from clases.personaje import Personaje
from clases.grafo import GrafoDragonBall
from clases.arbol_transformaciones import NodoTransformacion, ArbolTransformaciones
import random
import os
import time





class Juego:
    def __init__(self, jugador: Personaje, maquina: Personaje, grafo: GrafoDragonBall, transformaciones: ArbolTransformaciones):
        self.jugador = jugador
        self.maquina = maquina
        self.grafo = grafo
        self.transformaciones = transformaciones
        self.esferas_recolectadas = 0



    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

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
            self.limpiar_pantalla()
            print(f"""\n
                  Turno de {self.jugador.nombre} 
-- ki:{self.jugador.ki}/{self.jugador.max_ki} -- vida:{self.jugador.vida} -- nivel:{self.jugador.nivel} -- transformacion actual: {self.jugador.transformacion_actual.nombre}
combates ganados: {self.jugador.combates_ganados} -- experiencia: {self.jugador.exp}/{self.jugador.max_exp} -- nivel de poder: {self.jugador.nivel_de_poder} -- \n""")
            print(f"Vida del oponente {self.maquina.nombre}: {self.maquina.vida} HP")
            print("\nHabilidades disponibles:")
            
            
            self.jugador.habilidades.mostrar_arbol()  # Mostrar el árbol de habilidades
            
            print("\nTransformaciones disponibles:")
            self.jugador.transformaciones.mostrar_arbol(self.jugador.transformaciones.raiz)
            
            accion = input("\n¿Quieres usar una habilidad (Escríbela), cargar ki (c) o transformar (t) o defenderse (d)? ").lower()
            
            if accion == 'c':
                self.jugador.cargar_ki(1000)
                break
            if accion == 't':
                nombre_transformacion = input("Escribe el nombre de la transformación que deseas usar: ")
                if self.jugador.transformarse(nombre_transformacion):
                    print(f"{self.jugador.nombre} se ha transformado en {nombre_transformacion}!")
                else:
                    print("Transformación no válida o no tienes suficiente ki.")
                break
            elif accion == 'd':
                self.jugador.defender()
                
            else:
                if accion:
                    self.jugador.usar_habilidad(accion, self.maquina)
                    break
                else:
                    print("\nAcción no válida o no tienes suficiente ki para usar esa habilidad.")
            
        print("---" * 20)

    def turno_maquina(self):
        time.sleep(1)
        print(f"""\n
                Turno de {self.maquina.nombre} 
        -- ki:{self.maquina.ki}/{self.maquina.max_ki} -- vida:{self.maquina.vida} -- nivel:{self.maquina.nivel} -- transformación actual: {self.maquina.transformacion_actual.nombre}
        combates ganados: {self.maquina.combates_ganados} -- experiencia: {self.maquina.exp}/{self.maquina.max_exp} -- nivel de poder: {self.maquina.nivel_de_poder} -- \n""")

        # Mensaje de depuración sobre Ki
        if self.maquina.ki < 100:
            print("Cargando Ki...")
            self.maquina.cargar_ki(1000)

        # Seleccionar aleatoriamente entre transformar o usar habilidad
        accion = random.choice(['transformar', 'usar_habilidad', 'cargar_ki'])

        if accion == 'cargar_ki':
            self.maquina.cargar_ki(1000)
            
        if accion == 'transformar':
            
            # Opción de transformarse o usar habilidad
            proxima_transformacion = self.maquina.transformaciones.obtener_proxima_transformacion(self.maquina)
            # Mensaje de depuración sobre la transformación

            if proxima_transformacion and (self.maquina.ki >= proxima_transformacion.ki_necesario):
                print(f"Transformación disponible: {proxima_transformacion.nombre}, Ki necesario: {proxima_transformacion.ki_necesario}")
                # Realizar la transformación
                self.maquina.transformarse(proxima_transformacion.nombre)
                #print(f"{self.maquina.nombre} se ha transformado en {proxima_transformacion}!")
            
            
        if accion == 'usar_habilidad':
            # Usar habilidades al azar si hay suficiente Ki
            if self.maquina.ki >= 100:
                habilidad_aleatoria = self.maquina.habilidades.seleccionar_habilidad_aleatoria()  # Obtener la habilidad aleatoria
                if habilidad_aleatoria:
                    print(f"Usando habilidad aleatoria: {habilidad_aleatoria.nombre}")
                    self.maquina.usar_habilidad(habilidad_aleatoria.nombre, self.jugador)
            else:
                print("No hay suficiente Ki para usar habilidades.")

        print("---" * 20)
        time.sleep(5)



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
            
    def explorar_esferas(self):
        """
        Método para que el jugador busque las Esferas del Dragón en el grafo. El jugador debe recolectar las 7 esferas 
        viajando entre planetas, usando DFS para encontrar una esfera y Dijkstra para encontrar el camino más corto hacia ella.

        Una vez que el jugador recolecte las siete esferas, podrá hacer un deseo.
        """
        print("Explorando el mundo en busca de las Esferas del Dragón...")
        
        planetas_dragonball = ["Tierra", "Namek", "Vegeta", "Planeta Kaio", "Reino de los demonios", 
                               "Planeta de Bills", "La habitación del tiempo", "Planeta Yadarat"]
        
        # Buscar las esferas
        while self.esferas_recolectadas < 7:
            # El jugador elige un planeta desde el cual partir
            planeta_origen = self.jugador.planeta_actual
            print(f"\nBuscando una esfera desde el planeta {planeta_origen}...")

            # Usamos DFS para encontrar un planeta donde haya una esfera
            camino_dfs = self.grafo.dfs(planeta_origen, random.choice(planetas_dragonball))
            if camino_dfs:
                print(f"Camino DFS encontrado: {camino_dfs}")
            
            # Usamos Dijkstra para encontrar el camino más corto
            distancias = self.grafo.dijkstra(planeta_origen)
            planeta_destino = min(distancias, key=distancias.get)  # El planeta con la distancia más corta
            print(f"Camino más corto con Dijkstra hacia: {planeta_destino} (Distancia: {distancias[planeta_destino]})")

            # Simulamos la recolección de una esfera
            print(f"¡Has encontrado una esfera en el planeta {planeta_destino}!")
            self.esferas_recolectadas += 1



        # Cuando el jugador haya recolectado las 7 esferas, puede hacer un deseo
        self.hacer_deseo()

    def hacer_deseo(self):
        """
        Una vez que el jugador haya recolectado las 7 esferas, puede hacer un deseo.
        El deseo es un aumento importante en sus habilidades o poderes.
        """
        print("¡Has recolectado las 7 Esferas del Dragón!")
        print("¡Es hora de hacer un deseo!")
        intentos = 1
        while intentos < 3: #el jugador tiene hasta tres intentos
            deseo = input("¿Qué deseas? (Aumentar poder (1) o incrementar atributos (2)): ")

            if deseo == '1':
                print("Tu poder ha aumentado enormemente gracias al deseo del Dragón!")
                self.jugador.aumentar_nivel_de_poder(100000)  # Aumento significativo de poder
                break
            elif deseo == '2':
                print("¡Gracias al deseo de las esferas aumentaste tus atributos!")
                self.jugador.incrementar_atributos() #aumento de atributos como vida y nivel de poder
            else:
                intentos +=1
                print("Deseo no válido. No se ha hecho ningún deseo.")
                if intentos ==3:
                    print("Demasiados intentos el deseo no se cumple.")
                    break

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


            


            

