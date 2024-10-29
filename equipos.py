from gestion import *
# Llamo al archivo .py que contiene las variables globales que cargo para uso general
from config import equipos


# Verificar si el ID del equipo ya existe
def equipo_existe(id_equipo):
    """Verifica si un equipo con el ID dado ya existe."""
    return any(equipo["id"] == id_equipo for equipo in equipos)

# Agregar un nuevo equipo
def registrar_equipo(id_equipo, nombre, ciudad, director_tecnico):
    """Registra un nuevo equipo y lo guarda en equipos.json si no existe."""
    if equipo_existe(id_equipo):
        print(f"Error: Ya existe un equipo con el ID {id_equipo}.")
        return None
    
    equipo = {
        "id": id_equipo,
        "nombre": nombre,
        "ciudad": ciudad,
        "director_tecnico": director_tecnico,
        "estadisticas": {
            "puntos": 0,
            "jugados": 0,
            "ganados": 0,
            "empatados": 0,
            "perdidos": 0,
            "goles_favor": 0,
            "goles_contra": 0
        }
    }
    equipos.append(equipo)
    print(f"Equipo '{nombre}' registrado con éxito.")
    return equipos

# 
def buscar_equipo(id_equipo):
    return next((e for e in equipos if e["id"] == id_equipo), None)

# Función de actualizar información 
def actualizar_estadisticas_equipo(id_equipo, ganados, empatados, perdidos, goles_favor, goles_contra):
    equipo = buscar_equipo(id_equipo)
    if equipo:
        equipo["estadisticas"]["jugados"] += ganados + empatados + perdidos
        equipo["estadisticas"]["ganados"] += ganados
        equipo["estadisticas"]["empatados"] += empatados
        equipo["estadisticas"]["perdidos"] += perdidos
        equipo["estadisticas"]["goles_favor"] += goles_favor
        equipo["estadisticas"]["goles_contra"] += goles_contra
        equipo["estadisticas"]["puntos"] += ganados * 3 + empatados
    else:
        raise ValueError("Equipo no encontrado.")
