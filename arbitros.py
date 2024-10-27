
#
arbitros = []
def arbitro_existe(id_arbitro):
    """Busca un árbitro por su ID y muestra su información."""
    return any(equipo["id"] == id_arbitro for equipo in arbitros)
 
def registrar_arbitro(id_arbitro, nombre, experiencia, categoria):
    """Registra un nuevo equipo y lo guarda en equipos.json si no existe."""
    if arbitro_existe(id_arbitro):
        print(f"Error: Ya existe un arbitro con el ID {id_arbitro}.")
        return None
    
    arbitro = {
        'id': id_arbitro,
        'nombre': nombre,
        'experiencia': experiencia,  # Años de experiencia
        'categoria': categoria,      # Categoría del árbitro
        'partidos_dirigidos': 0      # Inicialmente en 0
    }
    arbitros.append(arbitro)
    print(f"Arbitro '{nombre}' registrado con éxito.")
    return arbitros


#
def buscar_arbitro_por_id(id_arbitro):
    for arbitro in arbitros:
        if arbitro['id'] == id_arbitro:
            return arbitro
    return None

def actualizar_partidos_arbitro(id_arbitro):
    arbitro = buscar_arbitro_por_id(id_arbitro)
    if arbitro:
        arbitro['partidos_dirigidos'] += 1

