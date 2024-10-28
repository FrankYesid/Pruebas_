# Estas son las librerias creadas y utlizadas para el sistema de clases de futbol
from equipos import *
from jugadores import *
from partidos import *
from arbitros import *
from gestion import *
from reportes import *
# agregar comentarios de cada sección 

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
            id_equipo = int(input("ID del equipo: "))
            nombre = input("Nombre del equipo: ").title()
            ciudad = input("Ciudad del equipo: ").title()
            director_tecnico = input("Director técnico: ").title()
            data  = registrar_equipo(id_equipo, nombre, ciudad, director_tecnico)
            if data != None:
                guardar_datos('data/equipos.json', data) 
    
        elif opcion == '2':
            # Buscar un equipo
            id_equipo = int(input("ID del equipo que desea buscar: "))
            equipo = buscar_equipo(id_equipo)
            if equipo:
                print(f"\nInformación del equipo {equipo['nombre']}:")
                print(f"ID: {equipo['id']}, Ciudad: {equipo['ciudad']}, "
                      f"Director Técnico: {equipo['director_tecnico']}")
            else:
                print(f"No se encontró ningún equipo con ID {id_equipo}.")

        elif opcion == '3':
            # Actualizar la información de un equipo
            id_equipo = int(input("ID del equipo a actualizar: "))
            equipo = buscar_equipo(id_equipo)
            if equipo:
                print(f"\nInformación actual del equipo {equipo['nombre']}:")
                print(f"Ciudad: {equipo['ciudad']}, Director Técnico: {equipo['director_tecnico']}")
                
                nuevo_nombre = input("Nuevo nombre (deje vacío para no cambiar): ") or equipo['nombre']
                nueva_ciudad = input("Nueva ciudad (deje vacío para no cambiar): ") or equipo['ciudad']
                nuevo_director = input("Nuevo director técnico (deje vacío para no cambiar): ") or equipo['director_tecnico']
                # agregar las demás varriables del equipo.
                actualizar_estadisticas_equipo(id_equipo, nuevo_nombre, nueva_ciudad, nuevo_director)
                print(f"Equipo '{nuevo_nombre}' actualizado con éxito.")
            else:
                print(f"No se encontró ningún equipo con ID {id_equipo}.")

        elif opcion == '4':
            # Salir del menú de equipos
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

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
            id_jugador = int(input("ID del jugador: "))
            nombre = input("Nombre del jugador: ")
            numero = int(input("Número del jugador: "))
            posicion = input("Posición del jugador: ")
            equipo_id = int(input("ID del equipo al que pertenece: "))
            data = registrar_jugador(id_jugador, nombre, numero, posicion, equipo_id)
            if data != None:
                guardar_datos('data/jugadores.json', data) 

        elif opcion == "2":
            # Buscar jugador
            id_jugador = int(input("Ingrese el ID del jugador a buscar: "))
            buscar_jugador(id_jugador)
        elif opcion == "3":
            # Actualizar información de un jugador
            id_jugador = int(input("Ingrese el ID del jugador a actualizar: "))
            actualizar_estadisticas_jugador(id_jugador)
        elif opcion == "4":
            # Salir del menú
            print("Saliendo del menú de gestión de jugadores.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

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
            id_arbitro = int(input("ID del árbitro: "))
            nombre = input("Nombre del árbitro: ")
            experiencia = input("Experiencia del árbitro: ")
            categoria = input("Categoría del árbitro: ")
            data = registrar_arbitro(id_arbitro, nombre, experiencia, categoria)
            if data != None:
                guardar_datos('data/arbitros.json', data) 
            # print(f"Árbitro {nombre} registrado con éxito.")

        elif opcion == "2":
            # Buscar árbitro
            id_arbitro = int(input("Ingrese el ID del árbitro a buscar: "))
            buscar_arbitro_por_id(id_arbitro)
        elif opcion == "3":
            # Actualizar información de un árbitro
            id_arbitro = int(input("Ingrese el ID del árbitro a actualizar: "))
            actualizar_partidos_arbitro(id_arbitro)
        elif opcion == "4":
            # Salir del menú
            print("Saliendo del menú de gestión de árbitros.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

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
            id_partido = int(input("ID del partido: "))
            fecha = input("Fecha del partido (YYYY-MM-DD): ")
            id_arbitro = int(input("ID del árbitro: "))
            equipo_local = input("Equipo local: ")
            equipo_visitante = input("Equipo visitante: ")
            data = registrar_partido(id_partido, fecha, id_arbitro, equipo_local, equipo_visitante)
            if data != None:
                guardar_datos('data/partidos.json', data) 

        elif opcion == "2":
            id_partido = int(input("Ingrese el ID del partido a buscar: "))
            buscar_partido(id_partido)
        elif opcion == "3":
            id_partido = int(input("Ingrese el ID del partido a actualizar: "))
            goles_local = int(input("Goles del equipo local: "))
            goles_visitante = int(input("Goles del equipo visitante: "))
            actualizar_resultados(id_partido, goles_local, goles_visitante)
        elif opcion == "4":
            id_partido = int(input("Ingrese el ID del partido: "))
            minuto = int(input("Minuto del evento: "))
            tipo_evento = input("Tipo de evento (gol, tarjeta, sustitución, etc.): ")
            jugador = input("Jugador involucrado: ")
            equipo = input("Equipo del jugador: ")
            registrar_evento(id_partido, minuto, tipo_evento, jugador, equipo)
        elif opcion == "5":
            print("Saliendo del menú de gestión de partidos.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

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
