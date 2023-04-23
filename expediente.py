import wikipedia

def buscar_animal():
    animales=["oso panda","ballena azul","pepino de mar", "langosta","leon","elefante africano"]
    print("Lista de animales:")
    for i, animal in enumerate(animales):
        print(f"{i+1}. {animal}")
    while True:
        try:
            opcion = int(input("Seleccione el número del animal que desea buscar: "))
            if opcion < 1 or opcion > len(animales):
                raise ValueError()
            break
        except ValueError:
            print("Ingrese un número válido.")
    animal = animales[opcion-1]
    pagina = wikipedia.page(animal)
    print("Título: ", pagina.title)
    print("URL: ", pagina.url)
    resumen = pagina.summary.replace('\n','')
    resumen = re.sub(r'\[\d+\]', '', resumen)
    print("Resumen: ", resumen)
    imagen = pagina.images[0]
    print("Imagen: ", imagen)
    return [animal, pagina.title, pagina.url, resumen, []]
