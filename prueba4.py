

def seleccionar_contrincante(personajes):
    return random.choice(personajes)


personajes = [gohan, vegeta]

    # Seleccionar un contrincante aleatorio
contrincante = seleccionar_contrincante(personajes)

    # Iniciar el juego
personajes = [andriode16, andriode17, andriode18, goku, vegeta, gohan]
grafo = GrafoDragonBall(["Tierra", "Namek", "Vegeta", "Planeta Kaio", "Reino de los demonios", "Planeta de Bills", "La habitación del tiempo", "Planeta Yadarat"], False)
grafo.armar_grafo()

menu = MenuPrincipal(personajes, grafo, goku.habilidades)
menu.mostrar_menu()