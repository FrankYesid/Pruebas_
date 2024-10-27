def generar_tabla_posiciones():
    return sorted(equipos, key=lambda x: x["estadisticas"]["puntos"], reverse=True)

def generar_lista_goleadores():
    return sorted(jugadores, key=lambda j: j["estadisticas"]["goles"], reverse=True)

def generar_reporte_arbitros():
    # Ordenar por la cantidad de partidos dirigidos en orden descendente
    arbitros_ordenados = sorted(arbitros, key=lambda a: a['partidos_dirigidos'], reverse=True)
    print(arbitros_ordenados)
