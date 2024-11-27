import random
from personajes.personajes_sayayin import goku,gohan,vegeta
from personajes.personajes_androide import andriode16,andriode17,andriode18
from clases.juego import Juego

def seleccionar_contrincante(personajes):
    return random.choice(personajes)

# Ejemplo de uso
if __name__ == "__main__":
    personajes = [gohan, vegeta,andriode16,andriode17]

    # Seleccionar un contrincante aleatorio
    contrincante = seleccionar_contrincante(personajes)

    # Iniciar el juego
    juego = Juego(goku, contrincante)
    juego.iniciar_combate()
  