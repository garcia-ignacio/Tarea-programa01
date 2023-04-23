import random

def agregar_animales():
    nombre_zoo = input("Ingrese un nombre para su zoológico: ")
    try:
        with open('animales.txt', 'r') as f:
            animales = f.read().splitlines()
    except FileNotFoundError:
        print("No se pudo encontrar el archivo de animales.")
        animales = []
    
    num_animales = input("Ingrese la cantidad de animales que desea agregar: ")
    try:
        num_animales = int(num_animales)
    except ValueError:
        print("Ingrese un número válido.")
        return
    
    if num_animales > len(animales):
        print(f"No hay suficientes animales en la lista. Hay {len(animales)} animales disponibles.")
        return
    
    random.shuffle(animales)
    animales_zoo = animales[:num_animales]
    
    print(f"Los siguientes animales han sido agregados a {nombre_zoo}:")
    for animal in animales_zoo:
        print(animal)
    
    return animales_zoo


agregar_animales()
