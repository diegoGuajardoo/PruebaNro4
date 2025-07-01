def ingresar_usuario(usuario):
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    if nombre_usuario in usuario:
        print("El nombre de usuario ya existe")
        return usuario
    
    sexo = input("Ingrese el sexo (f/m): ")
    if sexo != "f" and sexo != "m":
        print("Sexo no válido. Debe ser 'f' o 'm'.")
        return usuario
    
    sexo = input("Ingrese el sexo (f/m): ")
    if sexo != "f" and sexo != "m":
        print("Sexo no válido. Debe ser 'f' o 'm'.")
        return usuario
    
    contrasena = input("Ingrese la contrasena: ")
    if len(contrasena) < 8:
        print("La contrasena debe temer al menos 8 caracteres")
        return usuario
    if not any(char.isdigit() for char in contrasena):
        print("La contrasena debe contener al menos un número")
        return usuario
    
    if not any(char.isalpha() for char in contrasena):
        print("La contrasena debe contener al menos una letra")
        return usuario
    
    if " " in contrasena:
        print("La contrasena no puede contener espacios")
        return usuario
    
    usuario[nombre_usuario] = {"sexo": sexo, "contrasena": contrasena}
    print("Usuario ingresado exitosamente")
    return usuario

def buscar_usuario(usuario):
    nombre_usuario = input("Ingrese el nombre de usuario a buscar: ")
    if nombre_usuario in usuario:
        print(f"Usuario encontrado: {nombre_usuario}, Sexo: {usuario[nombre_usuario]['sexo']}")
        print("Contraseña no se muestra por seguridad")
    else:
        print("Usuario no se encuentra")
        
def eliminar_usuario(usuario):
    nombre_usuario = input("Ingrese el nombre de usuario a eliminar: ")
    if nombre_usuario in usuario:
        del usuario[nombre_usuario]
        print("Usuario eliminado exitosamente")
    else:
        print("no se puede eliminar el usuario")
        
def main():
    usuario = {}
    while True:
        print("\nMenu:")
        print("1. Ingresar usuario")
        print("2. Buscar usuario")
        print("3. Eliminar usuario")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            usuario = ingresar_usuario(usuario)
        elif opcion == "2":
            buscar_usuario(usuario)
        elif opcion == "3":
            eliminar_usuario(usuario)
        elif opcion == "4":
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida")
if __name__ == "__main__":
    main()