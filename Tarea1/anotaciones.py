import wikipedia
import webbrowser

def expediente():
    animales=["oso panda","ballena azul","pepino de mar", "nutria","leon","elefante africano"]
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


while True:
    animal = expediente()
    animal = agregarAnotacion(animal)
    print(animal)

    continuar = input("¿Desea agregar anotaciones para otro animal? (s/n): ")
    if continuar.lower() == 'n':
        break
