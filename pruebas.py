from clases.personaje import Personaje
from clases.humano import Humano
from clases.sayayin import Sayayin
from clases.andriode import Androide



goku = Sayayin("Son Guku",10000,"Saiyayin","Normal",70,70,70,0,10000,["Supersayayin","Supersayayin2","Supersayayin3"],["kamekameha,genkidama"],0,100,2)
enemigo = Humano("Cell",10000,"Androide","Normal",70,70,50,0,10000,None,None,0,100,3)




#test

goku.cargar_ki(100,enemigo)
enemigo.cargar_ki(100,goku)
goku.atacar(enemigo)
enemigo.atacar(goku)
goku.ataque_especial(enemigo)

enemigo.ataque_especial(goku)
goku.mostrar_stats()
enemigo.mostrar_stats()