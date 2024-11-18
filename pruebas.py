
from clases.sayayin import Sayayin
from clases.juego import Juego

goku = Sayayin("goku")
vegeta = Sayayin("Vegeta", transformaciones=["Super Saiyan", "Super Saiyan Blue"], habilidades=["megaboom"])



#test

combates_ganados = 2   

# Mostrar estadísticas iniciales
goku.mostrar_stats()
vegeta.mostrar_stats()
goku.cargar_ki(100)
vegeta.cargar_ki(100)

# Evolucionar poder tras los combates ganados
poder_final = goku.evolucionar_poder(combates_ganados)
poder_final = vegeta.evolucionar_poder(combates_ganados)
# Mostrar estadísticas después de cargar Ki y evolucionar poder
goku.mostrar_stats()
vegeta.mostrar_stats()

print(f"Nivel final: {goku.nivel}, Max Ki: {goku.max_ki}")

""" 

goku.cargar_ki(100,enemigo)
enemigo.cargar_ki(100,goku)
goku.atacar(enemigo)
enemigo.atacar(goku)
goku.ataque_especial(enemigo)

enemigo.ataque_especial(goku)
goku.mostrar_stats()
enemigo.mostrar_stats()
"""

# Iniciar el combate
juego = Juego(goku,vegeta)
juego.iniciar_combate()