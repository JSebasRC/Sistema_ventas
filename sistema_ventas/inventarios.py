def crear_inventario():
    # Lógica para crear un inventario
    pass

def agregar_producto_inventario():
    # Lógica para agregar productos al inventario
    pass

def listar_inventarios():
    # Lógica para listar los inventarios con cada producto
    pass

def modulo_inventario():
    while True:
        print("1. Crear Inventario")
        print("2. Agregar Productos al Inventario")
        print("3. Listar Inventarios")
        print("4. Volver al Menú Principal")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            crear_inventario()
        elif opcion == '2':
            agregar_producto_inventario()
        elif opcion == '3':
            listar_inventarios()
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente nuevamente.")
