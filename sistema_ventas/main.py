# main.py

from configuraciones import modulo_configuraciones
from clientes import modulo_clientes
from inventarios import modulo_inventario
from ventas import modulo_ventas

def main():
    while True:
        print("1. Configuraciones")
        print("2. Clientes")
        print("3. Inventario")
        print("4. Ventas")
        print("5. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            modulo_configuraciones()
        elif opcion == '2':
            modulo_clientes()
        elif opcion == '3':
            modulo_inventario()
        elif opcion == '4':
            modulo_ventas()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
