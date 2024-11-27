from clases.personaje import Personaje
from clases.personaje import Personaje
from clases.arbol_transformaciones import ArbolTransformaciones,NodoTransformacion
from clases.arbol_habilidades import crear_arbol_habilidades

class Androide(Personaje):
    def __init__(self, nombre: str, arbol_habilidades_data, combates_ganados=0):
        super().__init__(nombre=nombre, vida=1000, raza="Androide", estado="Normal",
                         ki=0, max_ki=10000, transformaciones=self.crear_arbol_transformaciones(),
                         transformacion_inicial=self.crear_arbol_transformaciones().raiz,
                         habilidades=self.crear_arbol_habilidades(arbol_habilidades_data),
                         exp=0, max_exp=100, nivel_de_poder=1, nivel=1, max_ki_base=10000,
                         planeta_actual="Tierra")
        self.combates_ganados = combates_ganados
        self.evolucionar_poder(combates_ganados=self.combates_ganados)
    
    def ataque_especial(self, enemigo):
        """Ataque especial del Saiyajin."""
        if self.ki >= 5000:
            # Calcular el daño potencial basado en la fuerza
            daño_especial = int(self.nivel_de_poder*2)
            
            enemigo.recibir_daño(daño_especial,enemigo)
            
            # Reducir ki al usar el ataque especial
            self.ki -= 5000  
        else:
            print("No tienes suficiente ki para realizar un ataque especial.")
            
        
    
    def crear_arbol_transformaciones(self):
        base = NodoTransformacion("Base", 0, None, 1)
        fase1 = NodoTransformacion("Fase 1", 4000, base, 50)
        fase2 = NodoTransformacion("Fase 2", 5500, fase1, 100)
        fase3 = NodoTransformacion("Fase 3", 7000, fase2, 150)
        fase4 = NodoTransformacion("Fase 4", 8500, fase3, 160)

        base.agregar_hijo(fase1)
        fase1.agregar_hijo(fase2)
        fase2.agregar_hijo(fase3)
        fase3.agregar_hijo(fase4)

        return ArbolTransformaciones(base)

    def crear_arbol_habilidades(self, arbol_habilidades_data):
        return crear_arbol_habilidades(arbol_habilidades_data)
