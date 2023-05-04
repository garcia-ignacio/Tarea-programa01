#Importamos los animales de la libreria
import random
    
matriz_animales = [
    {"nombre": "León", "especie": "Panthera leo", "edad": 7, "salud": "Buena", "cariño": "Alto"},
    {"nombre": "Elefante", "especie": "Loxodonta africana", "edad": 12, "salud": "Regular", "cariño": "Medio"},
    {"nombre": "Tigre", "especie": "Panthera tigris", "edad": 5, "salud": "Excelente", "cariño": "Bajo"},
    {"nombre": "Jirafa", "especie": "Giraffa camelopardalis", "edad": 3, "salud": "Regular", "cariño": "Alto"},
    {"nombre": "Oso", "especie": "Ursus arctos", "edad": 8, "salud": "Mala", "cariño": "Bajo"}
]

# Se solicita cantidad de animales que se desea mantener
cantidad_atender = int(input("Ingrese la cantidad de animales que se pueden atender en el zoológico: "))
# Representa la cantidad de animales que deben retirarse.
animales_retirar = random.sample(matriz_animales, len(matriz_animales) - cantidad_atender)

animales_atender = [animal for animal in matriz_animales if animal not in animales_retirar]

# Mostrar al usuario la lista de animales que se pueden atender en el zoológico
print("Los animales que se pueden atender en el zoológico son:")
for animal in animales_atender:
    print(animal["nombre"], "-", animal["especie"], "-", animal["edad"], "años")
