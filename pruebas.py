from clases.personaje import Personaje
from clases.humano import Humano
from clases.sayayin import Sayayin
from clases.andriode import Androide

goku = Sayayin("goku")
vegueta = Sayayin("Vegeta", transformaciones=["Super Saiyan", "Super Saiyan Blue"], habilidades=["megaboom"])
#goku = Sayayin("Son Guku",10000,"Saiyayin","Normal",70,70,70,0,["Supersayayin","Supersayayin2","Supersayayin3"],["kamekameha,genkidama"],0,100,2)
#enemigo = Humano("Cell",10000,"Androide","Normal",70,70,50,0,None,None,0,100,3)




#test

# Supongamos que Goku gana 5 combates y usa el multiplicador de Super Saiyajin (2x)
combates_ganados = 20
multiplicador_super_saiyajin = 1

print(f"Nivel final: {goku.nivel}, Max Ki: {goku.max_ki}")
goku.mostrar_stats()
vegueta.mostrar_stats()
goku.cargar_ki(100)
#poder_final = goku.evolucionar_poder(combates_ganados)

goku.mostrar_stats()


goku.subir_nivel()
#print(f"Poder final de {goku.nombre} tras {combates_ganados} combates: {poder_final}")

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