import random

def InsertaRAnimales():
    
    with open("animales.txt", "r") as f:
        nombres_animales = [line.strip() for line in f]

    cantidad_animales = random.choice(range(1, len(nombres_animales)))
    animales_zoologico = random.sample(nombres_animales, cantidad_animales)

    respuesta = input("¿Desea cargar datos de un archivo binario previo? (s/n)")

    if respuesta == "s":
        ruta_archivo = input("Ingrese la ruta del archivo binario: ")
        # Cargar datos en una matriz y crear una lista simple con los nombres de los animales
    else:
        animales_zoologico = []
        
    print(f"El zoológico '{nombre_zoologico}' tiene los siguientes animales:")
    for animal in animales_zoologico:
        print(animal)

    import random

    nombre_zoologico = input("Ingrese un nombre para su zoológico: ")

    with open("nombres_animales.txt", "r") as f:
        nombres_animales = [line.strip() for line in f]

    cantidad_animales = random.choice(range(1, len(nombres_animales)))
    animales_zoologico = random.sample(nombres_animales, cantidad_animales)

    respuesta = input("¿Desea cargar datos de un archivo binario previo? (s/n)")

    if respuesta == "s":
        ruta_archivo = input("Ingrese la ruta del archivo binario: ")
        # Cargar datos en una matriz y crear una lista simple con los nombres de los animales
    else:
        animales_zoologico = []

    print(f"El zoológico '{nombre_zoologico}' tiene los siguientes animales:")
    for animal in animales_zoologico:
        print(animal)

InsertaRAnimales()
