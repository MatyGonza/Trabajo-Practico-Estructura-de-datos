# Segunda fase de pruebas

from personajes.personajes_saiyajin import goku,gohan,vegeta
from personajes.personajes_androide import andriode16,andriode17,andriode18
from clases.grafo import GrafoDragonBall

from clases.torneo import MenuPrincipal,Torneo
import random
    
# Función para seleccionar un contrincante aleatorio
def seleccionar_contrincante(personajes):
    return random.choice(personajes)

# Ejemplo de uso
if __name__ == "__main__":
    personajes = [gohan, vegeta]

    # Seleccionar un contrincante aleatorio
    contrincante = seleccionar_contrincante(personajes)

    # Iniciar el juego
personajes = [andriode16, andriode17, andriode18, goku, vegeta, gohan]
grafo = GrafoDragonBall(["Tierra", "Namek", "Vegeta", "Planeta Kaio", "Reino de los demonios", "Planeta de Bills", "La habitacion del tiempo", "Planeta Yadarat"], False)
grafo.armar_grafo()
torneo=Torneo(personajes)
menu = MenuPrincipal(personajes, grafo, goku.habilidades,torneo)
menu.mostrar_menu()