import random
import wikipedia
import webbrowser

def agregarAnimales():
    nombreZoo = input("Ingrese un nombre para su zoológico: ")
    try:
        with open('animales.txt', 'r') as f:
            animales = f.read().splitlines()
    except FileNotFoundError:
        print("No se pudo encontrar el archivo de animales.")
        animales = []
    
    numAnimales = input("Ingrese la cantidad de animales que desea agregar: ")
    try:
        numAnimales = int(numAnimales)
    except ValueError:
        print("Ingrese un número válido.")
        return
    
    if numAnimales > len(animales):
        print(f"No hay suficientes animales en la lista. Hay {len(animales)} animales disponibles.")
        return
    
    random.shuffle(animales)
    animalesZoo = animales[:numAnimales]
    
    print(f"Los siguientes animales han sido agregados a {nombreZoo}:")
    for animal in animalesZoo:
        print(animal)
    
    return animalesZoo


def expediente(animales):
    print("Lista de animales:")
    for i, animal in enumerate(animales):
        print(f"{i + 1}. {animal}")
    animalSeleccionado = int(input("Seleccione un animal: ")) - 1
    nombreAnimal = animales[animalSeleccionado]
    print(f"\nInformación de {nombreAnimal}:\n")
    try:
        wikipedia.set_lang("es")
        pagina = wikipedia.page(nombreAnimal)
        titulo = pagina.title
        url = pagina.url
        resumen = wikipedia.summary(nombreAnimal, sentences=2)
        imagenUrl = pagina.images[0]
        webbrowser.open(imagenUrl)
        anotaciones = []
        animal = [nombreAnimal, titulo, url, resumen, anotaciones]
        #print(animal)
        return animal
    except wikipedia.exceptions.PageError:
        print(f"No se encontró la página de Wikipedia para {nombreAnimal}.")
    except wikipedia.exceptions.DisambiguationError:
        print(f"La búsqueda de {nombreAnimal} es ambigua. Por favor, sea más específico.")
        
def expedienteAux():
    listaAnimales = agregarAnimales()
    expediente(listaAnimales)


def agregarAnotacion(animal):
    anotaciones = animal[-1]
    while True:
        anotacion = input("Ingrese una anotación para este animal (o escriba 'fin' para terminar): ")
        if anotacion.lower() == 'fin':
            break
        else:
            anotaciones.append(anotacion)
    animal[-1] = anotaciones
    return animal

def agregarAnotaciones2():
    while True:
        animal = expediente()
        animal = agregarAnotacion(animal)
        print(animal)

        continuar = input("¿Desea agregar anotaciones para otro animal? (s/n): ")
        if continuar.lower() == 'n':
            break

def apartarAnimales():
    cantidadAnimales=int(input("ingrese la cantidad de animales que será posible atender: "))
    animales = ["oso panda", "ballena azul", "pepino de mar", "nutria", "leon", "elefante africano"]
    if cantidadAnimales >= len(animales):
        print("No hay animales para retirar.")
        return animales
    
    animalesRetirados = random.sample(animales, cantidadAnimales)
    for animal in animalesRetirados:
        animales.remove(animal)
    
    print(f"Los siguientes animales han sido retirados del zoológico: {', '.join(animalesRetirados)}")
    print(f"Los siguientes animales son los únicos que se pueden atender ahora: {', '.join(animales)}")
    
    return animales

def apartarAnimales():
    listaAnimales = agregarAnimales()
    apartarAnimales(listaAnimales)  

        


