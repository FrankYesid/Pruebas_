# Librerias utilizadas para el proceso
import os
import json

# Función par cargar los datos de un archivo .json
def cargar_datos(ruta):
    """Carga datos desde un archivo JSON. Si no existe, crea un archivo vacío."""
    if os.path.exists(ruta):
        with open(ruta, 'r') as archivo:
            return json.load(archivo)
    else:
        print(f"No se encontró {ruta}, creando un archivo vacío.")
        # Crear un archivo vacío JSON
        with open(ruta, 'w') as archivo:
            json.dump([], archivo)  # Escribir una lista vacía en el archivo
        return []

# Función para guardar los datos en un archivo de formato .json
def guardar_datos(ruta, datos):
    """Guarda los datos en un archivo JSON."""
    with open(ruta, 'w') as archivo:
        json.dump(datos, archivo, indent=4)

# Función para verificar que se agrega un número 
def verificar_numero(messege):
    while True:
        entrada = input(messege)
        try:
            return int(entrada)  # Intentamos convertir a entero
        except ValueError:
            print("Error: Por favor, ingresa un número entero válido.")

# Función para verificar si ingresa un string
def verificar_string(messege):
    while True:
        entrada = input(messege).strip()  # Quitamos espacios al inicio y al final
        if entrada:  # Verifica si no está vacío
            return entrada
        else:
            print("Error: Por favor, ingresa una cadena de texto válida.")

# Función para verificar que el número sea mayor a cero
def verificar_numero_no_negativo():
    while True:
        try:
            numero = int(input("Ingresa un número entero mayor o igual a 0: "))
            if numero >= 0:
                return numero  # Retorna el número si es válido
            else:
                print("Error: El número no puede ser negativo.")
        except ValueError:
            print("Error: Por favor, ingresa un número entero válido.")
