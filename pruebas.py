# La primera fase de pruebas
from clases.saiyajin import Saiyajin
from clases.andriode import Androide
from clases.juego import Juego

arbol_habilidades_data = {
        "nombre":"Ataque básica",
        "poder": 1000,
        "costo": 1000,
        "transformacion_requerida":  ["Base","Super Saiyajin","Super Saiyajin 2","Super Saiyajin 3"],
        "descripcion": "Un golpe básico con Ki.",
        "hijos": {
            "Kamehameha": {
                "poder": 2000,
                "costo": 4000,
                "transformacion_requerida":  ["Base","Super Saiyajin","Super Saiyajin 2","Super Saiyajin 3"],
                "descripcion": "Un rayo de energía muy poderoso.",
                "hijos": {
                    "Genkidama": {
                        "poder": 1500,
                        "costo": 3000,
                        "transformacion_requerida":  ["Base","Super Saiyajin","Super Saiyajin 2","Super Saiyajin 3"],
                        "descripcion": "El poder de todos los seres vivos en un solo ataque.",
                        "hijos": {
                            "Kamehameha x10": {
                                "poder": 5000,
                                "costo": 40000,
                                "transformacion_requerida":  ["Base","Super Saiyajin","Super Saiyajin 2","Super Saiyajin 3"],
                                "descripcion": "El Kamehameha aumentado 10 veces.",
                                "hijos": {}
                            }
                        }
                    }
                }
            }
        }
    }

#se instancias 2 clases de sayayin que ya tienen todos sus atributos cargados por defecto
goku = Saiyajin("goku",arbol_habilidades_data)
#vegeta = Sayayin("Vegeta")


#test
#Se le agregan cierta cantidad de combates a cada uno para que evolucionen su nivel, por cada combato ganado ganan experiencia, vida y nivel de poder y aumentan su ki
combates_ganados = 6   

# Mostrar estadísticas iniciales
goku.mostrar_stats()
#vegeta.mostrar_stats()
""" 

#cargan el ki ya que inician en 0 
goku.cargar_ki(1000)
vegeta.cargar_ki(1000)

# Evolucionar poder tras los combates ganados
poder_final = goku.evolucionar_poder(combates_ganados)
poder_final = vegeta.evolucionar_poder(combates_ganados)
# Mostrar estadísticas después de cargar Ki y evolucionar poder

goku.mostrar_stats()
vegeta.mostrar_stats()

goku.cargar_ki(1000)
vegeta.cargar_ki(1000)
#goku.transformarse("Base")
goku.transformarse("Super Saiyajin")
vegeta.transformarse("Super Saiyajin")
goku.mostrar_stats()
vegeta.mostrar_stats()
goku.cargar_ki(10000)
vegeta.cargar_ki(10000)
goku.transformarse("Super Saiyajin 2")
vegeta.transformarse("Super Saiyajin 2")
vegeta.usar_habilidad("Genkidama",goku)
vegeta.mostrar_stats()
goku.mostrar_stats()

andriode17 = Androide("Androide17")
andriode17.mostrar_stats()
andriode17.evolucionar_poder(combates_ganados)
andriode17.cargar_ki(1000)
andriode17.transformarse("Fase 1")
andriode17.mostrar_stats()
# Intanciamos el juego
juego = Juego(goku,vegeta)

#Iniciamos el combate
#juego.iniciar_combate()
"""