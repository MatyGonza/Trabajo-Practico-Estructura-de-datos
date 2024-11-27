from clases.sayayin import Sayayin

arbol_habilidades_data_goku = {
    "nombre": "Ataque basico",
    "poder": 1000,
    "costo": 100,
    "transformacion_requerida": ["Base", "Super Saiyajin", "Super Saiyajin 2", "Super Saiyajin 3"],
    "descripcion": "Un golpe básico con Ki.",
    "hijos": {
        "Kamehameha": {
            "nombre": "Kamehameha",
            "poder": 2000,
            "costo": 4000,
            "transformacion_requerida": ["Base", "Super Saiyajin", "Super Saiyajin 2", "Super Saiyajin 3"],
            "descripcion": "Un rayo de energía muy poderoso.",
            "hijos": {
                "Genkidama": {
                    "nombre": "Genkidama",
                    "poder": 1500,
                    "costo": 3000,
                    "transformacion_requerida": ["Base", "Super Saiyajin", "Super Saiyajin 2", "Super Saiyajin 3"],
                    "descripcion": "El poder de todos los seres vivos en un solo ataque.",
                    "hijos": {
                        "Kamehameha 10": {
                            "nombre": "Kamehameha 10",
                            "poder": 5000,
                            "costo": 40000,
                            "transformacion_requerida": ["Base", "Super Saiyajin", "Super Saiyajin 2", "Super Saiyajin 3"],
                            "descripcion": "El Kamehameha aumentado 10 veces.",
                            "hijos": {}
                        }
                    }
                }
            }
        }
    }
}

arbol_habilidades_data_vegeta = {
        "nombre": "Ataque basico",
        "poder": 1000,
        "costo": 100,
        "transformacion_requerida":  ["Base","Super Saiyajin","Super Saiyajin 2","Super Saiyajin 3"],
        "descripcion": "Un golpe básico con Ki.",
        "hijos": {
            "Resplandor final": {
                "poder": 2000,
                "costo": 4000,
                "transformacion_requerida":  ["Base","Super Saiyajin","Super Saiyajin 2","Super Saiyajin 3"],
                "descripcion": "Un ataque devastador que concentra una gran cantidad de energía en un rayo destructivo.",
                "hijos": {
                    "Galick gun": {
                        "poder": 1500,
                        "costo": 3000,
                        "transformacion_requerida":  ["Base","Super Saiyajin","Super Saiyajin 2","Super Saiyajin 3"],
                        "descripcion": "Un poderoso rayo de energía",
                        "hijos": {
                            "Hakai": {
                                "poder": 5000,
                                "costo": 40000,
                                "transformacion_requerida":  ["Base","Super Saiyajin","Super Saiyajin 2","Super Saiyajin 3"],
                                "descripcion": "Una técnica destructiva utilizada por los dioses de la destrucción",
                                "hijos": {}
                            }
                        }
                    }
                }
            }
        }
    }



arbol_habilidades_data_gohan = {
    "nombre": "Ataque basico",
    "poder": 1000,
    "costo": 100,
    "transformacion_requerida": ["Base", "Super Saiyajin", "Super Saiyajin 2", "Super Saiyajin 3"],
    "descripcion": "Un golpe básico con Ki.",
    "hijos": {
        "Masenko": {
            "nombre": "Masenko",
            "poder": 2000,
            "costo": 4000,
            "transformacion_requerida": ["Base", "Super Saiyajin", "Super Saiyajin 2", "Super Saiyajin 3"],
            "descripcion": "Un ataque rápido y poderoso donde lanza un rayo de energía.",
            "hijos": {
                "Kamehameha": {
                    "nombre": "Kamehameha",
                    "poder": 1500,
                    "costo": 3000,
                    "transformacion_requerida": ["Base", "Super Saiyajin", "Super Saiyajin 2", "Super Saiyajin 3"],
                    "descripcion": "Un rayo de energía muy poderoso.",
                    "hijos": {
                        "Kamehameha 10": {
                            "nombre": "Kamehameha 10",
                            "poder": 5000,
                            "costo": 40000,
                            "transformacion_requerida": ["Base", "Super Saiyajin", "Super Saiyajin 2", "Super Saiyajin 3"],
                            "descripcion": "El Kamehameha aumentado 10 veces.",
                            "hijos": {}
                        }
                    }
                }
            }
        }
    }
}
# Instanciando los personajes
goku = Sayayin("Goku", arbol_habilidades_data_goku,8)
vegeta = Sayayin("Vegeta", arbol_habilidades_data_vegeta,10)
gohan = Sayayin("Gohan", arbol_habilidades_data_gohan,20)

# Puedes exportar las instancias si lo deseas
__all__ = ['goku', 'vegeta', 'gohan']