import tkinter as tk
from tkinter import messagebox, simpledialog
# import json
import os
from src.controllers.equipo_controller import registrar_equipo
from src.controllers.jugador_controller import registrar_jugador
from src.controllers.arbitro_controller import registrar_arbitro
# from src.controllers.sancion_controller import generar_reporte_sanciones
from src.controllers.arbitro_controller import generar_reporte_arbitros
from src.utils.file_manager import guardar_datos

DATA_DIR = 'data/'  # Directorio para almacenar archivos JSON

# Asegúrate de que el directorio exista
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Crear ventana principal
ventana = tk.Tk()
# Agregar titulo a la ventana
ventana.title("Sistema de Gestión de Torneo de Fútbol")
# Asignar el tamaño de la ventana
ventana.geometry("400x350")

# Funciones para manejar 
# Función para
def mostrar_mensaje(titulo, mensaje):
    messagebox.showinfo(titulo, mensaje)

# Función para
def registrar_equipo_func():
    nombre = simpledialog.askstring("Registrar Equipo", "Ingrese el nombre del equipo:")
    ciudad = simpledialog.askstring("Registrar Equipo", "Ingrese la ciudad del equipo:")
    director_tecnico = simpledialog.askstring("Registrar Equipo", "Ingrese el nombre del director técnico:")

    if nombre and ciudad and director_tecnico:
        # Convertir nombres a Title Case
        nombre = nombre.title()
        ciudad = ciudad.title()
        director_tecnico = director_tecnico.title()

        equipo_id = nombre.lower().replace(" ", "_")
        ruta_equipo = os.path.join(DATA_DIR, f"equipos.json")
        print(ruta_equipo)
        # Verificar si el equipo ya está registrado
        if os.path.exists(ruta_equipo):
            mostrar_mensaje("Error", f"El equipo '{nombre}' ya está registrado.")
            return

        # Estructura del equipo
        equipo = {
            "id": equipo_id,
            "nombre": nombre,
            "ciudad": ciudad,
            "director_tecnico": director_tecnico,
            "jugadores": [],
            "estadisticas": {
                "puntos": 0,
                "partidos_jugados": 0,
                "ganados": 0,
                "empatados": 0,
                "perdidos": 0,
                "goles_a_favor": 0,
                "goles_en_contra": 0
            }
        }

        try:
            guardar_datos(equipo, ruta_equipo)  # Guarda en JSON
            mostrar_mensaje("Registro de Equipo", f"Equipo '{nombre}' registrado exitosamente.")
        except Exception as e:
            mostrar_mensaje("Error", f"Ocurrió un problema al registrar: {str(e)}")
    else:
        mostrar_mensaje("Error", "Todos los campos son obligatorios.")

# Función para buscar equipos por ciudad
def buscar_equipos():
    ciudad = simpledialog.askstring("Buscar Equipos", "Ingrese la ciudad a buscar:")
    
    if not ciudad:
        mostrar_mensaje("Error", "Debe ingresar una ciudad.")
        return

    ciudad = ciudad.title()  # Formatear en Title Case
    equipos_encontrados = []

    # Buscar en todos los archivos de equipo
    for archivo in os.listdir(DATA_DIR):
        if archivo.endswith('.json'):
            equipo = cargar_datos(archivo)
            if equipo.get("ciudad") == ciudad:
                equipos_encontrados.append(equipo)

    if equipos_encontrados:
        mostrar_resultados_busqueda(equipos_encontrados)
    else:
        mostrar_mensaje("Sin resultados", f"No se encontraron equipos en la ciudad '{ciudad}'.")

# Función para
def registrar_jugador_func():
    nombre = simpledialog.askstring("Registrar Jugador", "Ingrese el nombre del jugador:")
    numero = simpledialog.askstring("Registrar Jugador", "Ingrese el número del jugador:")
    equipo_id = simpledialog.askstring("Registrar Jugador", "Ingrese el ID del equipo:")
    
    if nombre and numero and equipo_id:
        jugador = {
            "id": nombre.lower().replace(" ", "_"),  # Genera un ID simple
            "nombre": nombre,
            "numero": numero,
            "equipo_id": equipo_id,
            "estadisticas": {
                "tarjetas_amarillas": 0,
                "tarjetas_rojas": 0,
                "minutos_jugados": 0,
                "goles": 0,
                "asistencias": 0
            }
        }
        registrar_jugador(jugador)
        guardar_datos(f"jugador_{jugador['id']}.json", jugador)
        mostrar_mensaje("Registro de Jugador", "Jugador registrado exitosamente.")
    else:
        mostrar_mensaje("Error", "Todos los campos son obligatorios.")

# Función para
def registrar_arbitro_func():
    nombre = simpledialog.askstring("Registrar Árbitro", "Ingrese el nombre del árbitro:")
    experiencia = simpledialog.askstring("Registrar Árbitro", "Ingrese los años de experiencia:")
    categoria = simpledialog.askstring("Registrar Árbitro", "Ingrese la categoría:")
    
    if nombre and experiencia and categoria:
        arbitro = {
            "id": nombre.lower().replace(" ", "_"),  # Genera un ID simple
            "nombre": nombre,
            "experiencia": experiencia,
            "categoria": categoria
        }
        registrar_arbitro(arbitro)
        guardar_datos(f"arbitro_{arbitro['id']}.json", arbitro)
        mostrar_mensaje("Registro de Árbitro", "Árbitro registrado exitosamente.")
    else:
        mostrar_mensaje("Error", "Todos los campos son obligatorios.")

# Función para
def generar_reporte_arbitros_func():
    reporte = generar_reporte_arbitros()
    mostrar_mensaje("Reporte de Árbitros", reporte)

# def generar_reporte_sanciones_func():
#     reporte = generar_reporte_sanciones()
#     mostrar_mensaje("Reporte de Sanciones", reporte)

# Menú principal
def crear_menu():
    menu_frame = tk.Frame(ventana)
    menu_frame.pack(pady=20)
    # Subtitulo de la ventana indicando la ventana
    tk.Label(menu_frame, text="Seleccione una opción:", font=("Arial", 16)).pack()
    # Generar botones con el contenido
    tk.Button(menu_frame, text="Registrar Equipo", command=registrar_equipo_func).pack(pady=5)
    tk.Button(menu_frame, text="Buscar Equipos por Ciudad", command=buscar_equipos).pack(pady=5)
    tk.Button(menu_frame, text="Registrar Jugador", command=registrar_jugador_func).pack(pady=5)
    tk.Button(menu_frame, text="Registrar Árbitro", command=registrar_arbitro_func).pack(pady=5)
    tk.Button(menu_frame, text="Generar Reporte de Árbitros", command=generar_reporte_arbitros_func).pack(pady=5)
    # tk.Button(menu_frame, text="Generar Reporte de Sanciones", command=generar_reporte_sanciones_func).pack(pady=5)

# Crear el menú en la interfaz
crear_menu()

# Ejecutar la aplicación
ventana.mainloop()
