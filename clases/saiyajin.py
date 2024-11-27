
from clases.personaje import Personaje
from clases.arbol_transformaciones import ArbolTransformaciones,NodoTransformacion
from clases.arbol_habilidades import crear_arbol_habilidades

class Saiyajin(Personaje):
    def __init__(self, nombre: str, arbol_habilidades_data, combates_ganados=0):
        transformaciones = self.crear_arbol_transformaciones()
        habilidades = self.crear_arbol_habilidades(arbol_habilidades_data)
    
        super().__init__(nombre=nombre, vida=1000, raza="Saiyajin", estado="Normal",
                         ki=0, max_ki=10000, transformaciones=transformaciones,
                         transformacion_inicial=transformaciones.raiz, habilidades=habilidades,
                         exp=0, max_exp=100, nivel_de_poder=1, nivel=1, max_ki_base=10000,
                         planeta_actual="Tierra")
        self.combates_ganados = combates_ganados
        self.evolucionar_poder(combates_ganados=self.combates_ganados)

    def ataque_especial(self, enemigo):
        """Ataque especial del Saiyajin."""
        if self.ki >= 5000:
            daño_especial = int(self.nivel_de_poder * 2)
            enemigo.recibir_daño(daño_especial, enemigo)
            self.ki -= 5000
        else:
            print("No tienes suficiente ki para realizar un ataque especial.")


    
    def crear_arbol_transformaciones(self):
        """Crea el árbol de transformaciones para el Saiyajin."""
        base = NodoTransformacion("Base", 0, None, 1)
        ssj = NodoTransformacion("Super Saiyajin", 4000, base, 50)
        ssj2 = NodoTransformacion("Super Saiyajin 2", 5500, ssj, 100)
        ssj3 = NodoTransformacion("Super Saiyajin 3", 7000, ssj2, 150)
        ssj4 = NodoTransformacion("Super Saiyajin 4", 8500, ssj3, 160)

        base.agregar_hijo(ssj)
        ssj.agregar_hijo(ssj2)
        ssj2.agregar_hijo(ssj3)
        ssj3.agregar_hijo(ssj4)

        return ArbolTransformaciones(base)
    
    def crear_arbol_habilidades(self, arbol_habilidades_data):
        return crear_arbol_habilidades(arbol_habilidades_data)

#saiyajin = Saiyajin()
#saiyajin.crear_arbol_transformaciones()