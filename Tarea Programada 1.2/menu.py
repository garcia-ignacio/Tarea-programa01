from funciones import *


def imprimirMenu():
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
def menu():
    animalesSeleccionados = None  # Inicializa la variable para que tenga un valor por defecto
    while True:  # Ciclo infinito para que el menú se repita hasta que se elija la opción de salir
        imprimirMenu()
        opcion = int(input("Escoja una opción: "))
        if opcion >= 1 and opcion <= 7:
            if opcion == 1:
                animalesSeleccionados = agregarAnimales()
            elif opcion == 2 :
                if animalesSeleccionados:
                    a = expediente(animalesSeleccionados)
                    print(a)
                else:
                    print("Primero debe agregar animales.")
            elif opcion == 3:
                agregarAnotacionesAux(expediente(animalesSeleccionados))
            elif opcion == 5:
                exportarBaseDeDatos(animalesSeleccionados)
            elif opcion == 6:
                print("por hacer")
            else:
                print("La biodiversidad es la base de la vida en nuestro planeta. Cada especie, por pequeña que sea, desempeña un papel vital en el equilibrio de los ecosistemas.")
                print("Preservar las especies es nuestra responsabilidad, para asegurar un futuro sostenible para nosotros y para las generaciones venideras.")
                return
        else:
            print("Opción inválida, indique una opción según las opciones indicadas.")


#Programa Principal
menu()

















