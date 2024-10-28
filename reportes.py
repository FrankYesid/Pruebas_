from config import equipos, jugadores, arbitros
import pandas as pd

def generar_tabla_posiciones():
    # Ordenar por la cantidad de puntos ganados en orden descendente
    # Lambda 
    posiciones_ordenados = sorted(equipos, key=lambda x: x["estadisticas"]["puntos"], reverse=True)
    print(pd.DataFrame(posiciones_ordenados))

def generar_lista_goleadores():
    # Ordenar por la cantidad de goles realizados en orden descendente
    goleadores_ordenados = sorted(jugadores, key=lambda j: j["estadisticas"]["goles"], reverse=True)
    print(goleadores_ordenados)

def generar_reporte_arbitros():
    # Ordenar por la cantidad de partidos dirigidos en orden descendente
    arbitros_ordenados = sorted(arbitros, key=lambda a: a['partidos_dirigidos'], reverse=True)
    print(arbitros_ordenados)
