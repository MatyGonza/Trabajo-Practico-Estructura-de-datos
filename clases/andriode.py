from clases.personaje import Personaje
from clases.personaje import Personaje
from clases.arbol__transformaciones import ArbolTransformaciones,NodoTransformacion
from clases.arbol_habilidades import crear_arbol_habilidades

class Androide(Personaje):
    def __init__(self, nombre: str,arbol_habilidades_data,combates_ganados):
        super().__init__(nombre, vida=1000, raza="Androide", estado="Normal", ki=0, max_ki=100, transformaciones=self.crear_arbol_transformaciones(), transformacion_inicial=self.crear_arbol_transformaciones().raiz, habilidades=self.crear_arbol_habilidades(arbol_habilidades_data), exp=0, max_exp=100, nivel_de_poder=1, nivel=1, max_ki_base=1000)
        self.combates_ganados = combates_ganados
        self.evolucionar_poder(combates_ganados=self.combates_ganados)
    
    def ataque_especial(self, enemigo):
        """Ataque especial del Andriode."""
        if self.ki >= 300:
            # Calcular el daño potencial basado en la fuerza
            daño_especial = int(self.fuerza * 18)
            
            # Calcular el daño efectivo restando la defensa del enemigo
            daño_efectivo = daño_especial - enemigo.defensa
            
            # Asegurarse de que el daño no sea negativo
            if daño_efectivo < 0:
                daño_efectivo = 0
            
            # Aplicar el daño al enemigo
            enemigo.recibir_daño(daño_efectivo)
            
            # Mensaje de resultado
            print(f"{self.nombre} realizó un ataque especial infligiendo {daño_efectivo} puntos de daño a {enemigo.nombre}.")
            
            # Reducir ki al usar el ataque especial
            self.ki -= 300  
        else:
            print("No tienes suficiente ki para realizar un ataque especial.")
            
        
    
    def crear_arbol_transformaciones(self):
        """Crea el árbol de transformaciones para el Saiyajin."""
        base = NodoTransformacion("Base", 0, None, 1)
        fase1 = NodoTransformacion("Fase 1", 4000, base, 50)
        fase2 = NodoTransformacion("Fase 2", 5500, fase1, 100)
        fase3 = NodoTransformacion("Fase 3", 7000, fase2, 150)
        fase4 = NodoTransformacion("Fase 4", 8500, fase3, 160)

        # Jerarquías
        base.agregar_hijo(fase1)
        fase1.agregar_hijo(fase2)
        fase2.agregar_hijo(fase3)
        fase3.agregar_hijo(fase4)
        return ArbolTransformaciones(base)

    def crear_arbol_habilidades(self,arbol_habilidades_data):
            return crear_arbol_habilidades(arbol_habilidades_data)
