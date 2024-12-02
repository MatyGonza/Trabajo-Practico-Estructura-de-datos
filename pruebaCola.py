from clases.cola_prioridad import ColaDePrioridad
from personajes.personajes_saiyajin import gohan,goku,vegeta

    # Crear cola de prioridad
cola = ColaDePrioridad()
cola.agregar_personaje(goku)
cola.agregar_personaje(vegeta)

    # Simular enfrentamientos
while not cola.esta_vacia():
    personaje = cola.siguiente_enfrentamiento()
    print(f"¡Enfrentamiento con: {personaje}!")
