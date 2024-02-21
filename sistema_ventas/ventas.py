def registrar_venta():
    # Lógica para registrar una venta
    pass

def visualizar_historial_ventas():
    # Lógica para visualizar el historial de ventas
    pass

def eliminar_venta():
    # Lógica para eliminar una venta
    pass

def buscar_venta_por_cliente():
    # Lógica para buscar una venta por número de ID de cliente
    pass

def modulo_ventas():
    while True:
        print("1. Registrar Venta")
        print("2. Visualizar Historial de Ventas")
        print("3. Eliminar Venta")
        print("4. Buscar Venta por ID de Cliente")
        print("5. Volver al Menú Principal")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            registrar_venta()
        elif opcion == '2':
            visualizar_historial_ventas()
        elif opcion == '3':
            eliminar_venta()
        elif opcion == '4':
            buscar_venta_por_cliente()
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente nuevamente.")
