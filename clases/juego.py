from clases.personaje import Personaje
import random
import os
import time

class Juego:
    def __init__(self, jugador: Personaje, maquina: Personaje):
        self.jugador = jugador
        self.maquina = maquina

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
            
            accion = input("\n¿Quieres usar una habilidad (Escríbela), cargar ki (c) o transformar (t)? ").lower()
            
            if accion == 'c':
                self.jugador.cargar_ki(1000)
                break
            elif accion == 't':
                nombre_transformacion = input("Escribe el nombre de la transformación que deseas usar: ")
                if self.jugador.transformarse(nombre_transformacion):
                    print(f"{self.jugador.nombre} se ha transformado en {nombre_transformacion}!")
                else:
                    print("Transformación no válida o no tienes suficiente ki.")
                break
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
