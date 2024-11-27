from personajes.personajes_saiyajin import goku, gohan, vegeta
from personajes.personajes_androide import andriode16, andriode17, andriode18
from clases.personaje import Personaje
from clases.grafo import GrafoDragonBall
from clases.arbol_transformaciones import NodoTransformacion, ArbolTransformaciones
import random





class Juego:
    def __init__(self, jugador: Personaje, maquina: Personaje, grafo: GrafoDragonBall, transformaciones: ArbolTransformaciones):
        self.jugador = jugador
        self.maquina = maquina
        self.grafo = grafo
        self.transformaciones = transformaciones
        self.esferas_recolectadas = 0



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
            print(f"""\nTurno de {self.jugador.nombre} -- Vida: {self.jugador.vida} -- Ki: {self.jugador.ki}/{self.jugador.max_ki}""")
            print("Opciones: (1) Usar habilidad, (2) Cargar Ki, (3) Transformarse, (4) Escapar")
            accion = input("Elige tu acción: ").strip()
            if accion == "1":
                habilidades = self.jugador.habilidades.listar_habilidades()
                for i, habilidad in enumerate(habilidades):
                    print(f"{i + 1}. {habilidad.nombre} (Ki: {habilidad.costo_ki}, Daño: {habilidad.daño})")
                seleccion = int(input("Selecciona una habilidad: "))
                self.jugador.usar_habilidad(habilidades[seleccion - 1].nombre, self.maquina)
                break
            elif accion == "2":
                self.jugador.cargar_ki(1000)
                break
            elif accion == "3":
                transformacion = input("¿A qué transformación deseas ir? ")
                self.jugador.transformarse(transformacion)
                break
            elif accion == "4":
                print("¡Has escapado del combate!")
                return
            else:
                print("Opción inválida, intenta de nuevo.")
        print("------"*20)

    def turno_maquina(self):
        if self.maquina.ki >= 100 and random.choice([True, False]):
            habilidades = self.maquina.habilidades.listar_habilidades()
            habilidad = random.choice(habilidades)
            self.maquina.usar_habilidad(habilidad.nombre, self.jugador)
        else:
            self.maquina.cargar_ki(1000)

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


            


            

