# Llamo al archivo .py que contiene las variables globales que cargo para uso general
from config import equipos, jugadores, arbitros

# Funcion para visualizar la información de la tabla de las posiciones
def generar_tabla_posiciones():
    """
    """
    # Ordenar por la cantidad de puntos ganados en orden descendente
    # Lambda 
    posiciones_ordenados = sorted(equipos, key=lambda x: x["estadisticas"]["puntos"], reverse=True)
    print("\nTabla de posiciones:")
    for idx, equipo in enumerate(posiciones_ordenados, start=1):
        estadisticas = equipo['estadisticas']
        print(f"{idx}. {equipo['nombre']} - {estadisticas['puntos']} pts | "
                f"{estadisticas['ganados']}G-{estadisticas['empatados']}E-{estadisticas['perdidos']}P | "
                f"GF: {estadisticas['goles_favor']} GC: {estadisticas['goles_contra']}")

def generar_lista_goleadores():
    """
    """
    # Ordenar por la cantidad de goles realizados en orden descendente
    goleadores_ordenados = sorted(jugadores, key=lambda j: j["estadisticas"]["goles"], reverse=True)
    print("\nLista de goleadores:")
    for jugador in goleadores_ordenados:
        print(f"{jugador['nombre']} - {jugador['estadisticas']['goles']} goles")

def generar_reporte_arbitros():
    """
    """
    # Ordenar por la cantidad de partidos dirigidos en orden descendente
    arbitros_ordenados = sorted(arbitros, key=lambda a: a['partidos_dirigidos'], reverse=True)
    print("\nReporte de Árbitros:")
    for arbitro in arbitros_ordenados:
        print(f"{arbitro['nombre']} - {arbitro['partidos_dirigidos']} partidos dirigidos "
                f"(Experiencia: {arbitro['experiencia']} años, Categoría: {arbitro['categoria']})")
