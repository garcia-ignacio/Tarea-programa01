# Función para imprimir el menú
def imprimir_menu():
    print("╔════════════════════════════════════════════╗")
    print("║             BIENVENIDO AL ZOOLÓGICO        ║")
    print("╠════════════════════════════════════════════╣")
    print("║ Seleccione una opción:                     ║")
    print("║                                            ║")
    print("║ 1. Agregar animales                        ║")
    print("║ 2. Crear expediente                        ║")
    print("║ 3. Registrar anotaciones                   ║")
    print("║ 4. Apartar animales de mi zoológico        ║")
    print("║ 5. Exportando la base de datos             ║")
    print("║ 6. Mostrar la base de datos del zoológico  ║")
    print("║ 7. Salir del sistema de Información        ║")
    print("║                                            ║")
    print("╚════════════════════════════════════════════╝")

# Función principal del programa
def main():
    imprimir_menu()
    opcion = input("Ingrese el número de la opción que desea seleccionar: ")
    
    # Resto del código para ejecutar la opción seleccionada
    # ...
    
# Llamado a la función principal
main()
