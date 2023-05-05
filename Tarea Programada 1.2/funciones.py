import random
import wikipedia
import webbrowser
import xml.etree.ElementTree as ET
import sys

#########################################################################################

#Funcion para darle un nombre al zoo y agregar animales al mismo

def procesarAnimales(nombreZoo, animales, numAnimales):
    if numAnimales > len(animales):
        raise ValueError(f"No hay suficientes animales en la lista. Hay {len(animales)} animales disponibles.")
    
    random.shuffle(animales)
    animalesZoo = animales[:numAnimales]
    
    return animalesZoo

def agregarAnimales():
    nombreZoo=input("ingrese el nombre del Zoo: ") # se pide el nombre del zoo
    try:
        with open('animales.txt', 'r') as f: #se carga la lista de animales
            animales = f.read().splitlines()
    except FileNotFoundError:
        print("No se pudo encontrar el archivo de animales.") #error por si no encuentar el archivo
        return []
    
    numAnimales=input("ingrese el numero de animales a añadir: ") # se pide el numero de animales a añadir
    try:
        numAnimales = int(numAnimales)  #se valida que sea entero
    except ValueError:
        print("Ingrese un número válido.")
        return []
    
    try:
        animalesZoo = procesarAnimales(nombreZoo, animales, numAnimales) #se llama a esta funcion para añadir animales aleatorios
    except ValueError as e:                                              #si no hay suficientes animales tira error
        print(e)
        return []
    
    print(f"Los siguientes animales han sido agregados a {nombreZoo}:")  #se imprime la lista de animales
    for animal in animalesZoo:
        print(animal)
    
    return animalesZoo
#################################################################################

#Funcion para crear expediente para los animales del zoo

def expediente(animales):
    if animales is None or len(animales) == 0: #verifica que se hayan añadido animales
        print("Primero debe agregar animales.")
        return None

    while True:
        print("Lista de animales:")
        for i, animal in enumerate(animales):
            print(f"{i + 1}. {animal}")
        animalSeleccionado = input("Seleccione un animal: ") #se pide seleccionar un animal para generar el expediente
        try:
            animalSeleccionado = int(animalSeleccionado) - 1
            if 0 <= animalSeleccionado < len(animales):
                break
            else:
                print("Seleccione un número de la lista.")
        except ValueError:
            print("Ingrese un número válido.")

    nombreAnimal = animales[animalSeleccionado] #se almacena el nombre del animal seleccionado
    print(f"\nInformación de {nombreAnimal}:\n")
    try:
        wikipedia.set_lang("es")#se intenta obtener información sobre el animal de Wikipedia en español
        pagina = wikipedia.page(nombreAnimal)  # se almacena la pagina
        titulo = pagina.title # se almacena el titulo de la pagina
        url = pagina.url #se almacena el url de la pagin
        resumen = wikipedia.summary(nombreAnimal, sentences=2)  # se almacena una un resumen sobre el animal
        imagenUrl = pagina.images[0]
        webbrowser.open(imagenUrl) # se abre la primera imagen de la página de Wikipedia en un navegador web utilizando la biblioteca webbrowser y el método open()
        anotaciones = []  #se crea una variable llamada anotaciones para futuras anotaciones
        animal = [nombreAnimal, titulo, url, resumen, anotaciones] #y se almacena todo en una lista en la variable animal
        return animal #retorna toda la informacion obtenida
    except wikipedia.exceptions.PageError:
        print(f"No se encontró la página de Wikipedia para {nombreAnimal}.") #se muestran errores si no encuentra la pagina
        return None
    except wikipedia.exceptions.DisambiguationError:
        print(f"La búsqueda de {nombreAnimal} es ambigua. Por favor, sea más específico.")
        return None

##############################################################################################

#Funcion para agregar anotacione a los expedientes de los animales
    
def agregarAnotacion(animal): # recibe una lista, en este caso el expediente creado
    anotaciones = animal[-1] # se va al final de la lista donde estan las anotaciones
    while True:
        anotacion = input("Ingrese una anotación para este animal (o escriba 'fin' para terminar): ") #se agregan anotaciones hasta que el usuario quiera parar
        if anotacion.lower() == 'fin':
            break
        else:
            anotaciones.append(anotacion)
    animal[-1] = anotaciones
    return animal #se retorna el expediente actualizado

def agregarAnotacionesAux(b):
    while True:
        #animal = expediente() #llama a la funcion expediente para elegir un animal
        animal = agregarAnotacion(b) #permite al usuario añadir nuevas anotaciones
        print(animal)

        continuar = input("¿Desea agregar anotaciones para otro animal? (s/n): ") #pregunta si quiere añadir anotaciones para otro animal
        if continuar.lower() == 'n':
           break

###################################################################################################
        
#Funcion para exportar la base de datos
        
def exportarBaseDeDatos(animales):
    # Obtener el nombre del archivo de salida
    nombreArchivo = input("Ingrese el nombre del archivo de salida: ")
    nombreArchivo += ".xml"
    
    # Verificar si el archivo ya existe
    try:
        with open(nombreArchivo, 'r'):
            print("El archivo ya existe. Por favor, seleccione otro nombre.")
            return
    except FileNotFoundError:
        pass
    
    # Crear el elemento raíz
    raiz = ET.Element("animales")
    
    # Seleccionar todos los animales
    animalesSeleccionados = animales
    
    # Agregar subelementos para cada animal
    for animal in animalesSeleccionados:
        animalElemento = ET.SubElement(raiz, "animal", nombre=animal)
    
    # Guardar el archivo
    tree = ET.ElementTree(raiz)
    tree.write(nombreArchivo)
    
    print(f"Se ha exportado la base de datos de {len(animalesSeleccionados)} animales en el archivo {nombreArchivo}.")

    




