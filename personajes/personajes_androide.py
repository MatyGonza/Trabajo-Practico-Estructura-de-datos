from clases.andriode import Androide

arbol_habilidades_data_16 = {
    "nombre": "Ataque basico",
    "poder": 1000,
    "costo": 1000,
    "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
    "descripcion": "Un golpe básico con Ki.",
    "hijos": {
        "Super Dodonpa": {
            "nombre": "Super Dodonpa",
            "poder": 2000,
            "costo": 4000,
            "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
            "descripcion": "Un ataque de energía que lanza un rayo devastador, capaz de causar un gran daño a sus oponentes.",
            "hijos": {
                "Absorcion de Ki": { #Faltaria un atributo que absorba el ki o lo podriamos cambiar por absorcion de energia.
                    "nombre": "Absorcion de Ki",
                    "poder": 1500,
                    "costo": 3000,
                    "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
                    "descripcion": "Tiene la capacidad de absorber ataques de energía, lo que le permite recuperarse y utilizar esa energía en su contra.",
                    "hijos": {
                        "Autodestruccion": {
                            "nombre": "Autodestruccion",
                            "poder": 50000, #le agregue un cero mas
                            "costo": 40000,
                            "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
                            "descripcion": "En situaciones críticas, el Androide 16 puede activar un mecanismo de autodestrucción que libera una gran cantidad de energía, causando daños masivos en el área.",
                            "hijos": {}
                        }
                    }
                }
            }
        }
    }
}

arbol_habilidades_data_17 = {
    "nombre": "Ataque basico",
    "poder": 1000,
    "costo": 1000,
    "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
    "descripcion": "Un golpe básico con Ki.",
    "hijos": {
        "Barrera de energia": {
            "nombre": "Barrera de energia",
            "poder": 2000,
            "costo": 4000,
            "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
            "descripcion": "Puede crear una barrera de energía defensiva que le protege de ataques enemigos, permitiéndole contrarrestar con ataques propios.",
            "hijos": {
                "Rayo energetico": {
                    "nombre": "Rayo energetico",
                    "poder": 1500,
                    "costo": 3000,
                    "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
                    "descripcion": "Un ataque rápido y potente que dispara un rayo de energía hacia su oponente, con una precisión y velocidad notables.",
                    "hijos": {
                        "Autodestruccion": {
                            "nombre": "Autodestruccion",
                            "poder": 5000,
                            "costo": 40000,
                            "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
                            "descripcion": "En situaciones críticas, el Androide puede activar un mecanismo de autodestrucción que libera una gran cantidad de energía, causando daños masivos en el área.",
                            "hijos": {}
                        }
                    }
                }
            }
        }
    }
}

arbol_habilidades_data_18 = {
    "nombre": "Ataque basico",
    "poder": 1000,
    "costo": 1000,
    "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
    "descripcion": "Un golpe básico con Ki.",
    "hijos": {
        "Destruccion rapida": {
            "nombre": "Destruccion rapida",
            "poder": 2000,
            "costo": 4000,
            "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
            "descripcion": "Utiliza movimientos rápidos y precisos para desatar una serie de golpes devastadores en sus oponentes, combinando técnicas de artes marciales con ataques energéticos.",
            "hijos": {
                "Kienzan": {
                    "nombre": "Kienzan",
                    "poder": 1500,
                    "costo": 3000,
                    "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
                    "descripcion": "Lanza un disco de energía afilado que puede cortar a través de casi cualquier cosa, siendo un ataque tanto ofensivo como defensivo.",
                    "hijos": {
                        "Autodestruccion": {
                            "nombre": "Autodestruccion",
                            "poder": 5000,
                            "costo": 40000,
                            "transformacion_requerida": ["Base", "Fase 1", "Fase 2", "Fase 3", "Fase 4"],
                            "descripcion": "En situaciones críticas, el Androide puede activar un mecanismo de autodestrucción que libera una gran cantidad de energía, causando daños masivos en el área.",
                            "hijos": {}
                        }
                    }
                }
            }
        }
    }
}

andriode16=Androide("Androide 16",arbol_habilidades_data_16,20)

andriode17=Androide("Androide 17",arbol_habilidades_data_17,8)

andriode18=Androide("Androide 18",arbol_habilidades_data_18,4)

# Puedes exportar las instancias si lo deseas
__all__ = ['androide16', 'androide17', 'androide18']