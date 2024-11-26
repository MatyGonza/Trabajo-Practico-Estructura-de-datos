from clases.personaje import Personaje
from clases.arbol__transformaciones import ArbolTransformaciones,NodoTransformacion
from clases.arbol_habilidades import crear_arbol_habilidades

class Sayayin(Personaje):
    def __init__(self, nombre: str,arbol_habilidades_data):
        super().__init__(nombre, vida=1000, raza="Sayayin", estado="Normal", ki=0, max_ki=10000, transformaciones=self.crear_arbol_transformaciones(), transformacion_inicial=self.crear_arbol_transformaciones().raiz, habilidades=self.crear_arbol_habilidades(arbol_habilidades_data), exp=0, max_exp=100, nivel_de_poder=1, nivel=1, max_ki_base=1000)
    
    def ataque_especial(self, enemigo):
        """Ataque especial del Sayayin."""
        if self.ki >= 500:
            # Calcular el daño potencial basado en la fuerza
            daño_especial = int(self.fuerza * 20)
            
            daño_efectivo = daño_especial - int(enemigo.defensa)
            
            # Asegurarse de que el daño no sea negativo
            if daño_efectivo < 0:
                daño_efectivo = 0
            
            # Aplicar el daño al enemigo
            enemigo.recibir_daño(daño_efectivo)
            
            # Mensaje de resultado
            print(f"{self.nombre} desató un poderoso ataque especial infligiendo {daño_efectivo} puntos de daño a {enemigo.nombre}.")
            
            # Reducir ki al usar el ataque especial
            self.ki -= 500  
        else:
            print("No tienes suficiente ki para realizar un ataque especial.")


    
    def crear_arbol_transformaciones(self):
        """Crea el árbol de transformaciones para el Saiyajin."""
        base = NodoTransformacion("Base", 0, None, 1)
        ssj = NodoTransformacion("Super Saiyajin", 4000, base, 50)
        ssj2 = NodoTransformacion("Super Saiyajin 2", 5500, ssj, 100)
        ssj3 = NodoTransformacion("Super Saiyajin 3", 7000, ssj2, 150)
        ssj4 = NodoTransformacion("Super Saiyajin 4", 8500, ssj3, 160)

        # Jerarquías
        base.agregar_hijo(ssj)
        ssj.agregar_hijo(ssj2)
        ssj2.agregar_hijo(ssj3)
        ssj3.agregar_hijo(ssj4)

        return ArbolTransformaciones(base)
    
    def crear_arbol_habilidades(self,arbol_habilidades_data):
        return crear_arbol_habilidades(arbol_habilidades_data)
