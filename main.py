# Estas son las librerias creadas y utlizadas para el sistema de clases de futbol
from equipos import *
from jugadores import *
from partidos import *
from arbitros import *
from gestion import *
from reportes import *
# Agregar comentarios de cada sección y en readme.md agregar la explicación de que contiene cada bloque

# Menú principal con lo solicitado de registrar, buscar, actualizar y visualizar reportes
def menu():
    """
    Menú con las opciones relacionadas con la gestión de cada item solicitado, 
    para agregar, actualizar y visualizar los datos de cada equipo, jugador, 
    árbitro o partido realizado en el torneo.
    """
    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestión de Equipos")
        print("2. Gestión de Jugadores")
        print("3. Gestión de Árbitros")
        print("4. Gestión de Partidos")
        print("5. Generar Reportes")

        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_equipos()
        elif opcion == '2':
            menu_jugadores()
        elif opcion == '3':
            menu_arbitros()
        elif opcion == '4':
            menu_partidos()
        elif opcion == '5':
            menu_reportes()
        elif opcion == '0':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Menú de equipos 
def menu_equipos():
    while True:
        print("\n--- Gestión de Equipos ---")
        print("1. Registrar nuevo equipo")
        print("2. Buscar equipo")
        print("3. Actualizar información de equipo")
        print("4. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Registrar un nuevo equipo
            id_equipo = verificar_numero("ID del equipo: ")
            nombre = verificar_string("Nombre del equipo: ").title()
            ciudad = verificar_string("Ciudad del equipo: ").title()
            director_tecnico = verificar_string("Director técnico: ").title()
            data  = registrar_equipo(id_equipo, nombre, ciudad, director_tecnico)
            if data != None:
                guardar_datos('data/equipos.json', data) 
    
        elif opcion == '2':
            # Buscar un equipo
            id_equipo = verificar_numero("ID del equipo que desea buscar: ")
            equipo = buscar_equipo(id_equipo)
            if equipo:
                print(f"\nInformación del equipo {equipo['nombre']}:")
                print(f"ID: {equipo['id']}, Ciudad: {equipo['ciudad']}, "
                      f"Director Técnico: {equipo['director_tecnico']}")
            else:
                print(f"No se encontró ningún equipo con ID {id_equipo}.")

        elif opcion == '3':
            # Actualizar la información de un equipo
            id_equipo = verificar_numero("ID del equipo a actualizar: ")
            equipo = buscar_equipo(id_equipo)
            if equipo:
                print(f"\nInformación actual del equipo {equipo['nombre']}:")
                print(f"Ciudad: {equipo['ciudad']}, Director Técnico: {equipo['director_tecnico']}")
                
                ganados = verificar_numero("Nueva cantidad de partidos ganados (deje vacío para no cambiar): ") or equipo['estadisticas']['ganados']
                if ganados != '':
                    ganados = int(ganados)
                else:
                    ganados = equipo['estadisticas']['ganados']
                empatados = verificar_numero("Nueva cantidad de partidos empatados (deje vacío para no cambiar): ") or equipo['estadisticas']['empatados']
                if empatados != '':
                    empatados = int(empatados)
                else:
                    empatados = equipo['estadisticas']['empatados']
                perdidos = verificar_numero("Nueva cantidad de partidos perdidos (deje vacío para no cambiar): ") or equipo['estadisticas']['perdidos']
                if perdidos != '':
                    perdidos = int(perdidos)
                else:
                    perdidos = equipo['estadisticas']['perdidos']
                goles_favor = verificar_numero("Nueva cantidad de goles a favor (deje vacío para no cambiar): ") or equipo['estadisticas']['goles_favor']
                if goles_favor != '':
                    goles_favor = int(goles_favor)
                else:
                    goles_favor = equipo['estadisticas']['goles_favor']
                goles_contra = verificar_numero("Nueva cantidad de goles en contra (deje vacío para no cambiar): ") or equipo['estadisticas']['goles_contra']
                if goles_contra != '':
                    goles_contra = int(goles_contra)
                else:
                    goles_contra = equipo['estadisticas']['goles_contra']

                # agregar las demás varriables del equipo.
                actualizar_estadisticas_equipo(id_equipo, ganados, empatados, perdidos, goles_favor, goles_contra)
                print(f"Equipo '{equipo['nombre']}' actualizado con éxito.")
            else:
                print(f"No se encontró ningún equipo con ID {id_equipo}.")

        elif opcion == '4':
            # Salir del menú de equipos
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

# Menú de jugadores
def menu_jugadores():
    while True:
        print("\n--- Gestión de Jugadores ---")
        print("1. Registrar nuevo jugador")
        print("2. Buscar jugador")
        print("3. Actualizar información de un jugador")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Registrar nuevo jugador
            id_jugador = verificar_numero("ID del jugador: ")
            nombre = verificar_string("Nombre del jugador: ")
            numero = verificar_numero("Número del jugador: ")
            posicion = verificar_string("Posición del jugador: ")
            equipo_id = verificar_numero("ID del equipo al que pertenece: ")
            data = registrar_jugador(id_jugador, nombre, numero, posicion, equipo_id)
            if data != None:
                guardar_datos('data/jugadores.json', data) 

        elif opcion == "2":
            # Buscar jugador
            id_jugador = verificar_numero("Ingrese el ID del jugador a buscar: ")
            buscar_jugador(id_jugador)
        elif opcion == "3":
            # Actualizar información de un jugador
            id_jugador = verificar_numero("Ingrese el ID del jugador a actualizar: ")
            actualizar_estadisticas_jugador(id_jugador)
        elif opcion == "4":
            # Salir del menú
            print("Saliendo del menú de gestión de jugadores.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

# Menú de arbitros
def menu_arbitros():
    while True:
        print("\n--- Gestión de Árbitros ---")
        print("1. Registrar nuevo árbitro")
        print("2. Buscar árbitro")
        print("3. Actualizar información de un árbitro")
        print("4. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Registrar nuevo árbitro
            id_arbitro = verificar_numero("ID del árbitro: ")
            nombre = verificar_string("Nombre del árbitro: ")
            experiencia = verificar_numero("Años de experiencia del árbitro: ")
            categoria = verificar_categoria_arbitro()
            data = registrar_arbitro(id_arbitro, nombre, experiencia, categoria)
            if data != None:
                guardar_datos('data/arbitros.json', data) 
            # print(f"Árbitro {nombre} registrado con éxito.")

        elif opcion == "2":
            # Buscar árbitro
            id_arbitro = verificar_numero("Ingrese el ID del árbitro a buscar: ")
            buscar_arbitro_por_id(id_arbitro)
        elif opcion == "3":
            # Actualizar información de un árbitro
            id_arbitro = verificar_numero("Ingrese el ID del árbitro a actualizar: ")
            actualizar_partidos_arbitro(id_arbitro)
        elif opcion == "4":
            # Salir del menú
            print("Saliendo del menú de gestión de árbitros.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

# Menú de partidos
def menu_partidos():
    while True:
        print("\n--- Gestión de Partidos ---")
        print("1. Registrar nuevo partido")
        print("2. Buscar partido")
        print("3. Actualizar resultados")
        print("4. Registrar evento en un partido")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_partido = verificar_numero("ID del partido: ")
            fecha = verificar_string("Fecha del partido (YYYY-MM-DD): ")
            id_arbitro = verificar_numero("ID del árbitro: ")
            equipo_local = verificar_string("Equipo local: ")
            equipo_visitante = verificar_string("Equipo visitante: ")
            data = registrar_partido(id_partido, fecha, id_arbitro, equipo_local, equipo_visitante)
            if data != None:
                guardar_datos('data/partidos.json', data) 

        elif opcion == "2":
            id_partido = verificar_numero("Ingrese el ID del partido a buscar: ")
            buscar_partido(id_partido)
        elif opcion == "3":
            id_partido = verificar_numero("Ingrese el ID del partido a actualizar: ")
            goles_local = verificar_numero("Goles del equipo local: ")
            goles_visitante = verificar_numero("Goles del equipo visitante: ")
            actualizar_resultados(id_partido, goles_local, goles_visitante)
        elif opcion == "4":
            id_partido = verificar_numero("Ingrese el ID del partido: ")
            minuto = verificar_numero("Minuto del evento: ")
            tipo_evento = verificar_string("Tipo de evento (gol, tarjeta, sustitución, etc.): ").title()
            jugador = verificar_string("Jugador involucrado: ").title()
            equipo = verificar_string("Equipo del jugador: ").title()
            registrar_evento(id_partido, minuto, tipo_evento, jugador, equipo)
        elif opcion == "5":
            print("Saliendo del menú de gestión de partidos.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

# Menú de reportes
def menu_reportes():
    print("\n--- Generación de Reportes ---")
    print("1. Tabla de posiciones")
    print("2. Lista de goleadores")
    print("3. Reporte de árbitros")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        generar_tabla_posiciones()
        
    elif opcion == '2':
        generar_lista_goleadores()
        
    elif opcion == '3':
        generar_reporte_arbitros()
        
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    menu()
