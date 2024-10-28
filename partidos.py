from config import partidos

# Función para verificar si exite el partido
def verificar_partido(id_partido):
    """Verifica si un partido con el ID dado ya existe."""
    for partido in partidos:
        if partido["id"] == id_partido:
            return True
    return False

# Función para agregar un partido
def registrar_partido(id_partido, fecha, id_arbitro, equipo_local, equipo_visitante):
    """Registra un nuevo partido y lo guarda en la lista."""
    if verificar_partido(id_partido):
        print(f"Error: Ya existe un equipo con el ID {id_partido}.")
        return None

    partido = {
        "id": id_partido,
        "fecha": fecha,
        "arbitro_id": id_arbitro,
        "equipo_local": equipo_local,
        "equipo_visitante": equipo_visitante,
        "goles_local": 0,
        "goles_visitante": 0,
        "eventos": []
    }
    partidos.append(partido)
    print(f"Partido registrado entre {equipo_local} y {equipo_visitante}.")
    return partidos

# Función para buscar un partido
def buscar_partido(id_partido):
    """Busca un partido por su ID y muestra su información."""
    for partido in partidos:
        if partido["id"] == id_partido:
            print("\n--- Información del Partido ---")
            print(f"ID: {partido['id']}")
            print(f"Fecha: {partido['fecha']}")
            print(f"Árbitro ID: {partido['arbitro_id']}")
            print(f"Equipo Local: {partido['equipo_local']}")
            print(f"Equipo Visitante: {partido['equipo_visitante']}")
            print(f"Goles Local: {partido['goles_local']}")
            print(f"Goles Visitante: {partido['goles_visitante']}")
            print(f"Eventos: {partido['eventos']}")
            return
    print(f"No se encontró ningún partido con ID: {id_partido}.")

# función para actualizar resultados del artido
def actualizar_resultados(id_partido, goles_local, goles_visitante):
    """Actualiza los resultados de un partido."""
    for partido in partidos:
        if partido["id"] == id_partido:
            partido["goles_local"] = goles_local
            partido["goles_visitante"] = goles_visitante
            print("Resultados actualizados.")
            return
    print(f"No se encontró ningún partido con ID: {id_partido}.")

# función para colocar el evento sucedido
def registrar_evento(id_partido, minuto, tipo_evento, jugador, equipo):
    """Registra un evento en un partido."""
    for partido in partidos:
        if partido["id"] == id_partido:
            evento = {
                "minuto": minuto,
                "tipo": tipo_evento,
                "jugador": jugador,
                "equipo": equipo
            }
            partido["eventos"].append(evento)
            print(f"Evento registrado en el minuto {minuto}.")
            return
    print(f"No se encontró ningún partido con ID: {id_partido}.")