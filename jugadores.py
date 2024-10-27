import json

# Verificar si el ID del jugador ya existe
def jugador_existe(id_jugador):
    """Verifica si un jugador con el ID dado ya existe."""
    return any(jugador["id"] == id_jugador for jugador in jugadores)

jugadores = []
def registrar_jugador(id_jugador, nombre, numero, posicion, equipo_id):
    """Registra un nuevo jugador y lo guarda en jugadores.json si no existe."""
    if jugador_existe(id_jugador):
        print(f"Error: Ya existe un jugador con el ID {id_jugador}.")
        return None

    jugador = {
        "id": id_jugador,
        "nombre": nombre,
        "numero": numero,
        "posicion": posicion,
        "equipo_id": equipo_id,
        "estadisticas": {
            "partidos": 0,
            "goles": 0,
            "asistencias": 0,
            "amarillas": 0,
            "rojas": 0,
            "minutos": 0
        }
    }
    jugadores.append(jugador)
    print(f"Jugador '{nombre}' registrado con éxito.")
    return jugadores

# Cargar jugadores desde el archivo jugadores.json al iniciar el programa
def cargar_jugadores():
    try:
        with open("jugadores.json", "r") as archivo:
            global jugadores
            jugadores = json.load(archivo)
    except FileNotFoundError:
        jugadores = []  # Si no existe el archivo, inicializa una lista vacía

def buscar_jugador(id_jugador):
    return next((j for j in jugadores if j["id"] == id_jugador), None)

def actualizar_estadisticas_jugador(id_jugador, goles, asistencias, amarillas, rojas, minutos):
    jugador = buscar_jugador(id_jugador)
    if jugador:
        jugador["estadisticas"]["partidos"] += 1
        jugador["estadisticas"]["goles"] += goles
        jugador["estadisticas"]["asistencias"] += asistencias
        jugador["estadisticas"]["amarillas"] += amarillas
        jugador["estadisticas"]["rojas"] += rojas
        jugador["estadisticas"]["minutos"] += minutos
    else:
        raise ValueError("Jugador no encontrado.")

def generar_lista_goleadores():
    # Ordenar la lista de jugadores por la cantidad de goles en orden descendente
    jugadores_ordenados = sorted(jugadores, key=lambda j: j['estadisticas']['goles'], reverse=True)
    return jugadores_ordenados
