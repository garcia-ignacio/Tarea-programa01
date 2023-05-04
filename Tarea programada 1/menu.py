from funciones import *

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
    while True:
        imprimir_menu()
        opcion = int(input("Ingrese el número de la opción que desea seleccionar: "))
        if opcion >=0 and opcion <=4:
            
            if opcion == 1:
                return agregarAnimales()
            elif opcion == 2 :
                return expedienteAux()
            elif opcion == 3:
                return agregarAnotaciones2()
            elif opcion == 4:
                return "apartar animales"
            else:
                break
        else:
            print ("Opción inválida, indique una opción según las opciones indicadas.")
        main()
    
        
               
# Llamado a la función principal
main()
