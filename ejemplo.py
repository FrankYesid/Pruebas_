from equipos import *
from jugadores import *
from partidos import *
from arbitros import *
from gestion import *

if __name__ == "__main__":
    # Registro de un equipo
    registrar_equipo(1, "Equipo A", "Ciudad A", "DT A")
    registrar_equipo(2, "Equipo B", "Ciudad B", "DT B")

    # Registro de un jugador
    registrar_jugador(1, "Jugador 1", 10, "Delantero", 1)
    registrar_jugador(2, "Jugador 2", 9, "Delantero", 2)

    # Registro de un árbitro
    registrar_arbitro(1, "Arbitro 1", "5 años", "Primera División")

    # Registro de un partido
    registrar_partido(1, "2024-10-26", 1, "Equipo A", "Equipo B")

    # Actualización de estadísticas del jugador
    actualizar_estadisticas_jugador(1, 2, 1, 0, 0, 90)

    # Generar tabla de posiciones
    print("Tabla de posiciones:", generar_tabla_posiciones())

    # Generar lista de goleadores
    print("Lista de goleadores:", generar_lista_goleadores())

    # Guardar y cargar datos de ejemplo
    guardar_datos("equipos.json", equipos)
    print("Equipos cargados:", cargar_datos("equipos.json"))
