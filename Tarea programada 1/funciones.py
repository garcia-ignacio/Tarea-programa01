import random
import wikipedia
import webbrowser
import xml.etree.ElementTree as ET
import sys
import picke

#Funcion para darle un nombre al zoo y agregar animales al mismo
def agregarAnimales():
    nombreZoo = input("Ingrese un nombre para su zoológico: ")
    try:
        with open('animales.txt', 'r') as f: #se intenta abrir el archivo, Si el archivo no existe, se imprime un mensaje de error y se asigna una lista vacía a la variable animales.
            animales = f.read().splitlines() #si el archivo existe se lee usando read() y se divide en una lista de líneas utilizando el método splitlines()
    except FileNotFoundError:
        print("No se pudo encontrar el archivo de animales.")
        animales = []
    
    numAnimales = input("Ingrese la cantidad de animales que desea agregar: ") #se ingresan la cantidad de animales
    try:
        numAnimales = int(numAnimales) # se intenta convertir a entero y si no se puede tira error
    except ValueError:
        print("Ingrese un número válido.")
        return
    
    if numAnimales > len(animales): #verifica si la cantidad de animales que el usuario desea agregar es mayor que la cantidad de animales disponibles en la lista, si no tira error
        print(f"No hay suficientes animales en la lista. Hay {len(animales)} animales disponibles.")
        return
    
    random.shuffle(animales) #Si hay suficientes animales en la lista se reorganiza aleatoriamente la lista utilizando la función random.shuffle
    animalesZoo = animales[:numAnimales]
    
    print(f"Los siguientes animales han sido agregados a {nombreZoo}:")
    for animal in animalesZoo:
        print(animal) #se imprimen los animales seleccionados
    
    return #animalesZoo

####################################################################################################

#Funcion para crear expediente para los animales del zoo

def expediente(animales):
    print("Lista de animales:")
    for i, animal in enumerate(animales):
        print(f"{i + 1}. {animal}") #muestra los nombres de los animales en la lista
    animalSeleccionado = int(input("Seleccione un animal: ")) - 1 # se selecciona un animal para generar un expediente
    nombreAnimal = animales[animalSeleccionado] #se almacena el nombre del animal seleccionado
    print(f"\nInformación de {nombreAnimal}:\n")
    try:
        wikipedia.set_lang("es") #se intenta obtener información sobre el animal de Wikipedia en español
        pagina = wikipedia.page(nombreAnimal) # se almacena la pagina
        titulo = pagina.title # se almacena el titulo de la pagina
        url = pagina.url #se almacena el url de la pagina
        resumen = wikipedia.summary(nombreAnimal, sentences=2) # se almacena una un resumen sobre el animal
        imagenUrl = pagina.images[0]
        webbrowser.open(imagenUrl) # se abre la primera imagen de la página de Wikipedia en un navegador web utilizando la biblioteca webbrowser y el método open()
        anotaciones = [] #se crea una variable llamada anotaciones para futuras anotaciones
        animal = [nombreAnimal, titulo, url, resumen, anotaciones] #y se almacena todo en una lista en la variable animal
        #print(animal)
        return animal #retorna toda la informacion obtenida
    except wikipedia.exceptions.PageError:
        print(f"No se encontró la página de Wikipedia para {nombreAnimal}.")  #se muestran errores si no encuentra la pagina
    except wikipedia.exceptions.DisambiguationError:
        print(f"La búsqueda de {nombreAnimal} es ambigua. Por favor, sea más específico.")
        
def expedienteAux(): #se crea una funcion para conectar expediente con la funcion agregarAnimales
    listaAnimales = agregarAnimales()
    expediente(listaAnimales)

######################################################################################################

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

def agregarAnotacionesAux():
    while True:
        animal = expediente() #llama a la funcion expediente para elegir un animal
        animal = agregarAnotacion(animal) #permite al usuario añadir nuevas anotaciones
        print(animal)

        continuar = input("¿Desea agregar anotaciones para otro animal? (s/n): ") #pregunta si quiere añadir anotaciones para otro animal
        if continuar.lower() == 'n':
           break

#####################################################################################################

#Funcion para exportar la base de datos

def exportarBaseDeDatos():
    # Obtener la cantidad de animales a exportar
    cantidadAnimales = int(input("Ingrese la cantidad de animales a exportar: "))
    
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
    
    # Obtener la lista de animales
    animales=["oso panda", "ballena azul", "pepino de mar", "nutria", "leon africano", "elefante africano"]
    
    # Seleccionar animales aleatorios
    animalesSeleccionados = random.sample(animales, cantidadAnimales)
    
    # Agregar subelementos para cada animal
    for animal in animalesSeleccionados:
        anotaciones = []#agregarAnotacion([animal])
        animalElemento = ET.SubElement(raiz, "animal", nombre=animal, anotaciones=str(anotaciones))
    
    # Guardar el archivo
    tree = ET.ElementTree(raiz)
    tree.write(nombreArchivo)
    
    print(f"Se ha exportado la base de datos de {cantidadAnimales} animales en el archivo {nombreArchivo}.")
   
#####################################################################################################################################
#Salir del sistema de informacion.
print("La biodiversidad es la base de la vida en nuestro planeta. Cada especie, por pequeña que sea, desempeña un papel vital en el equilibrio de los ecosistemas. Preservar las especies es nuestra responsabilidad, para asegurar un futuro sostenible para nosotros y para las generaciones venideras.")
# Salir del programa
sys.exit()

# Guardar la matriz en un archivo binario
with open("matriz_animales.pkl", "wb") as archivo:
    pickle.dump(matriz_animales, archivo)



        


