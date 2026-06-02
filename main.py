

from menu import mostrar_menu



def main():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pass
        elif opcion == "2":
            pass
        elif opcion == "3":
            print("Gracias por usar el programa. ¡Hasta luego!")
        

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

