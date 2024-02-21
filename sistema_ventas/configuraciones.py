def modulo_configuraciones():
    while True:
        print("1. Iniciar Sesión")
        print("2. Registrar Nuevo Usuario")
        print("3. Restablecer Contraseña")
        print("4. Ver Usuarios Registrados")
        print("5. Volver al Menú Principal")
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            iniciar_sesion()
        elif opcion == '2':
            # Solicitar nombre de usuario y contraseña al usuario
            usuario = input("Ingrese el nombre de usuario: ")
            contrasena = input("Ingrese la contraseña: ")
            registrar_nuevo_usuario(usuario, contrasena)  # Llamar a la función para registrar nuevo usuario
        elif opcion == '3':
            usuario = input("Ingrese el nombre de usuario: ")
            nueva_contrasena = input("Ingrese la nueva contraseña: ")
            restablecer_contrasena(usuario, nueva_contrasena)
            print("Contraseña restablecida correctamente.")
        elif opcion == '4':
            ver_usuarios_registrados()
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# Función para encriptar contraseñas
def encriptar_contrasena(contrasena):
    # Implementa aquí tu algoritmo de encriptación
    # Por ejemplo, usando el mapeo de caracteres especificado en el enunciado
    contrasena_encriptada = contrasena.replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0').replace('ñ', '#')
    return contrasena_encriptada

# Función para guardar la contraseña encriptada en un archivo
def guardar_contrasena_en_archivo(usuario, contrasena_encriptada):
    with open('Archivos/contraseñas.txt', 'a') as file:
        file.write(f"{usuario}: {contrasena_encriptada}\n")


# Función para registrar nuevos usuarios
def registrar_nuevo_usuario(usuario, contrasena):
    contrasena_encriptada = encriptar_contrasena(contrasena)
    guardar_contrasena_en_archivo(usuario, contrasena_encriptada)
    print("Usuario registrado correctamente.")

