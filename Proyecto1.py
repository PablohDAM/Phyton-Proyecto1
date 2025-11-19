def agregar_alumno(lista):
    # Solicita al usuario los datos del alumno y los añade a la lista
    nombre = input("Nombre del alumno: ").strip()  # Eliminamos espacios en blanco al inicio y al final
    edad = input("Edad del alumno: ").strip()
    curso = input("Curso que realiza: ").strip()
    
    # Validación básica: nombre y curso no pueden estar vacíos, edad debe ser un número
    if not nombre or not edad.isdigit() or not curso:
        print("Datos inválidos. Intenta de nuevo.")  # Punto crítico: evitar datos incorrectos en la lista
        return
    
    # Añadimos el alumno a la lista como un diccionario con claves nombre, edad y curso
    lista.append({"nombre": nombre, "edad": int(edad), "curso": curso})

def mostrar_alumnos(lista):
    # Verificamos si hay alumnos registrados para evitar mostrar lista vacía
    if not lista:
        print("No hay alumnos registrados.")
        return
    
    # Mostramos la lista de alumnos con índice para mejor legibilidad
    for i, alumno in enumerate(lista, start=1):
        print(f"{i}. Nombre: {alumno['nombre']}, Edad: {alumno['edad']}, Curso: {alumno['curso']}")

def buscar_alumno(lista):
    # Pedimos el criterio de búsqueda y convertimos a minúsculas para búsqueda insensible a mayúsculas
    criterio = input("Introduce el nombre o parte del nombre a buscar: ").strip().lower()
    
    # Filtramos alumnos cuyo nombre contenga el criterio de búsqueda
    resultados = [a for a in lista if criterio in a['nombre'].lower()]
    
    # Mostramos los resultados o indicamos si no hay coincidencias
    if resultados:
        for alumno in resultados:
            print(f"Nombre: {alumno['nombre']}, Edad: {alumno['edad']}, Curso: {alumno['curso']}")
    else:
        print("No se encontró ningún alumno.")

def menu():
    # Lista principal que almacena todos los alumnos
    alumnos = []
    
    # Bucle infinito que se mantiene hasta que el usuario decida salir
    while True:
        # Mostramos el menú de opciones para que el usuario seleccione una acción
        print("\n--- Menú de gestión de alumnos ---")
        print("1. Añadir alumno")
        print("2. Mostrar todos los alumnos")
        print("3. Buscar alumno")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")  # Recogemos opción del usuario
        
        # Control básico de flujo según la opción elegida
        if opcion == "1":
            agregar_alumno(alumnos)  # Añadir alumno a la lista
        elif opcion == "2":
            mostrar_alumnos(alumnos)  # Mostrar todos los alumnos
        elif opcion == "3":
            buscar_alumno(alumnos)  # Buscar alumno por nombre
        elif opcion == "4":
            print("Saliendo del programa.")
            break  # Punto crítico: terminamos el bucle y salimos del programa
        else:
            print("Opción inválida. Intenta de nuevo.")  # Manejo de errores para opciones no válidas

if __name__ == "__main__":
    # Punto de entrada del programa: se ejecuta el menú principal
    menu()
