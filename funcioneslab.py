import re
import random
#NOTA: tambien me hace falta documentar el codigo.
def registrar_persona():
    datos_personas = {}
    while True:
        cedula = input("Ingrese la cédula en formato #-####-####: ")
        if not re.match(r'^\d{1}-\d{4}-\d{4}$', cedula):
            print("Cédula inválida. Por favor, ingrese la cédula en formato #-####-####.")
            continue
        elif cedula in datos_personas:
            print("La cédula ya ha sido registrada.")
            continue
        nombre = input("Ingrese el nombre completo: ")
        if not re.match(r'^[A-Za-z]+\s+[A-Za-z]+$', nombre):
            print("Nombre inválido. Por favor, ingrese el nombre en formato 'nombre apellido'.")
            continue
        genero = input("¿Es hombre? (sí/no): ")
        if genero.lower() == "sí":
            genero = True
        elif genero.lower() == "no":
            genero = False
        else:
            print("Opción inválida. Por favor, ingrese 'sí' o 'no'.")
            continue
        personalidad = input("Ingrese un número del 1 al 16: ")
        if not re.match(r'^[1-9]|1[0-6]$', personalidad):
            print("Número inválido. Por favor, ingrese un número del 1 al 16.")
            continue
        datos_personas[cedula] = [nombre, genero, int(personalidad)]
        print("Datos registrados satisfactoriamente.")
        break
    return datos_personas
#


#

def registrar_persona(datos_personas):
    while True:
        cedula = input("Ingrese la cédula en formato #-####-####: ")
        if not validar_cedula(cedula):
            print("Cédula inválida. Por favor, ingrese la cédula en formato #-####-####.")
            continue
        elif cedula in datos_personas:
            print("La cédula ya ha sido registrada.")
            continue
        nombre = input("Ingrese el nombre completo: ")
        if not validar_nombre(nombre):
            print("Nombre inválido. Por favor, ingrese el nombre en formato 'nombre apellido'.")
            continue
        genero = input("Ingrese el género (hombre/mujer/otro): ")
        if not validar_genero(genero):
            print("Género inválido. Por favor, ingrese 'hombre', 'mujer' o 'otro'.")
            continue
        personalidad = input("Ingrese un número del 1 al 16: ")
        if not validar_personalidad(personalidad):
            print("Número inválido. Por favor, ingrese un número del 1 al 16.")
            continue
        datos_personas[cedula] = {"nombre": nombre, "genero": genero, "personalidad": int(personalidad)}
        print("Datos registrados satisfactoriamente.")
        break





#
def modificar_persona(datos_personas):
    cedula = input("Ingrese la cédula de la persona que desea modificar: ")
    if not validar_cedula(cedula):
        print("Cédula inválida. Por favor, ingrese la cédula en formato #-####-####.")
        return
    if cedula not in datos_personas:
        print("La cédula no ha sido registrada.")
        return
    print("Datos actuales de la persona:")
    print(f"Nombre: {datos_personas[cedula]['nombre']}")
    print(f"Género: {datos_personas[cedula]['genero']}")
    print(f"Personalidad: {datos_personas[cedula]['personalidad']}")
    nombre = input("Ingrese el nuevo nombre completo: ")
    if not validar_nombre(nombre):
        print("Nombre inválido. Por favor, ingrese el nombre en formato 'nombre apellido'.")
        return
    genero = input("Ingrese el nuevo género (hombre/mujer/otro): ")
    if not validar_genero(genero):
        print("Género inválido. Por favor, ingrese 'hombre', 'mujer' o 'otro'.")
        return
    personalidad = input("Ingrese un nuevo número del 1 al 16: ")
    if not validar_personalidad(personalidad):
        print("Número inválido. Por favor, ingrese un número del 1 al 16.")
        return
    datos_personas[cedula]["nombre"] = nombre
    datos_personas[cedula

#Validaciones
def validar_cedula(cedula):
    return bool(re.match(r'^\d{1}-\d{4}-\d{4}$', cedula))
def validar_nombre(nombre):
    return bool(re.match(r'^[A-Za-z]+\s+[A-Za-z]+$', nombre))

def validar_genero(genero):
    return genero.lower() in ["hombre", "mujer", "otro"]

def validar_personalidad(personalidad):
    return personalidad.isdigit() and int(personalidad) in range(1, 17

