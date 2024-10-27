import json

def guardar_datos(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def cargar_datos(filename):
    with open(filename, 'r') as file:
        return json.load(file)
