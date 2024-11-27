from clases.saiyajin import Saiyajin

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
                        "Kamehameha x10": {
                            "nombre": "Kamehameha x10",
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
        "poder": 10000,
        "costo": 1500,
        "transformacion_requerida":  ["Base","Super Saiyajin","Super Saiyajin 2","Super Saiyajin 3"],
        "descripcion": "Un golpe básico con Ki.",
        "hijos": {
            "Resplandor Final": {
                "poder": 3000,
                "costo": 4000,
                "transformacion_requerida":  ["Base","Super Saiyajin","Super Saiyajin 2","Super Saiyajin 3"],
                "descripcion": "Un ataque devastador que concentra una gran cantidad de energía en un rayo destructivo.",
                "hijos": {
                    "Galick Gun": {
                        "poder": 4500,
                        "costo": 3000,
                        "transformacion_requerida":  ["Base","Super Saiyajin","Super Saiyajin 2","Super Saiyajin 3"],
                        "descripcion": "Un poderoso rayo de energía",
                        "hijos": {
                            "Hakai": {
                                "poder": 5500,
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
    "poder": 1500,
    "costo": 1000,
    "transformacion_requerida": ["Base", "Super Saiyajin", "Super Saiyajin 2", "Super Saiyajin 3"],
    "descripcion": "Un golpe básico con Ki.",
    "hijos": {
        "Masenko": {
            "nombre": "Masenko",
            "poder": 2500,
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
                        "Kamehameha x10": {
                            "nombre": "Kamehameha x10",
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
goku = Saiyajin("Goku", arbol_habilidades_data_goku,4)
vegeta = Saiyajin("Vegeta", arbol_habilidades_data_vegeta,10)
gohan = Saiyajin("Gohan", arbol_habilidades_data_gohan,20)

# Puedes exportar las instancias si lo deseas
__all__ = ['goku', 'vegeta', 'gohan']