# Función para modificar los datos de una persona
def modificar_persona():
    cedula = input("Ingrese la cédula de la persona a modificar: ")
    # Aquí iría el código para modificar los datos de la persona
    print("Los datos de la persona con cédula {} han sido modificados exitosamente.".format(cedula))

# Función para eliminar los datos de una persona
def eliminar_persona():
    cedula = input("Ingrese la cédula de la persona a eliminar: ")
    # Aquí iría el código para eliminar los datos de la persona
    print("Los datos de la persona con cédula {} han sido eliminados exitosamente.".format(cedula))

# Función para generar reportes
def generar_reportes():
    # Aquí iría el código para generar los reportes
    print("Generando reportes...")

while True:
    print("---- MENÚ ----")
    print("1. Modificar los datos de una persona")
    print("2. Eliminar los datos de una persona")
    print("3. Reportes")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        modificar_persona()
    elif opcion == "2":
        eliminar_persona()
    elif opcion == "3":
        generar_reportes()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
