#Paso 1: Estructura Básica del Sistema
#Vamos a empezar creando un menú principal desde el cual el usuario pueda elegir diferentes opciones.

estudiantes = []

def menu():
    
    print("\nBienvenido al Sistema de Registro de Matrículas")
    print("1. Registrar nuevo estudiante")
    print("2. Mostrar estudiantes registrados")
    print("3. Actualizar información de un estudiante")
    print("4. Eliminar un estudiante")
    print("5. Salir")
    opcion = input("Elige una opción: ")
    return opcion

#Paso 2: Función para Registrar Estudiantes
#Ahora crearemos una función que permita al usuario registrar nuevos estudiantes. Esta función pedirá al usuario que ingrese el nombre y la edad del estudiante, y luego almacenará esta información en una lista de diccionarios.

def registrar_estudiante():
    
    nombre = input("Ingresa el nombre del estudiante: ")
    edad = int(input("Ingresa la edad del estudiante: "))
    estudiante = {'nombre': nombre, 'edad': edad}
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} registrado con éxito.")
    
#Paso 3: Función para Mostrar Estudiantes
#Después, necesitamos una función que muestre todos los estudiantes que han sido registrados.

def mostrar_estudiantes():

    if len(estudiantes) == 0:
        print("No se encuentran estudiantes registrados.")
    else:
        print("Lista de estudiantes registrados:")
        for i, estudiante in enumerate(estudiantes, start=1):
            print(f"{i}. Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")
            
#Paso 4: Función para Actualizar Estudiantes
#Ahora vamos a crear una función que permita al usuario actualizar la información de un estudiante existente. El usuario deberá ingresar el nombre del estudiante que desea actualizar, y luego podrá modificar sus datos.

def actualizar_estudiante():
    
    nombre = input("Ingresa el nombre del estudiante que deseas actualizar: ")
    for estudiante in estudiantes:
        if estudiante['nombre'] == nombre:
            print(f"Estudiante encontrado: {nombre}")
            nuevo_nombre = input("Ingresa el nuevo nombre (o presiona Enter si no deseas cambiarlo): ")
            nueva_edad = input("Ingresa la nueva edad (o presiona Enter si no deseas cambiarla): ")

            if nuevo_nombre:
                estudiante['nombre'] = nuevo_nombre
            if nueva_edad:
                estudiante['edad'] = int(nueva_edad)

            print(f"Estudiante {nombre} actualizado con éxito.")
            return
    
    print(f"No se encontró ningún estudiante con el nombre {nombre}.")
    
#Paso 5: Función para Eliminar Estudiantes
#Finalmente, crearemos una función que permita al usuario eliminar un estudiante de la lista. El usuario deberá ingresar el nombre del estudiante a eliminar.

def eliminar_estudiante():
    
    nombre = input("Ingresa el nombre del estudiante que deseas eliminar: ")
    for estudiante in estudiantes:
        if estudiante['nombre'] == nombre:
            estudiantes.remove(estudiante)
            print(f"Estudiante {nombre} eliminado con éxito.")
            return
    
    print(f"No se encontró ningún estudiante con el nombre {nombre}.")    

#Paso 6: Bucle Principal del Programa
#Con todas las funciones creadas, podemos ahora construir el bucle principal que permitirá al usuario interactuar con el sistema hasta que decida salir.   

def main():
    
    while True:
        opcion = menu()
        if opcion == '1':
            registrar_estudiante()
        elif opcion == '2':
            mostrar_estudiantes()
        elif opcion == '3':
            actualizar_estudiante()
        elif opcion == '4':
            eliminar_estudiante()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

main()

