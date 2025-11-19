# Phyton Proyecto 1
Por Pablo Herrero y Carlos Sibilio

## Descripción del proyecto
Este proyecto es una aplicación de consola desarrollada en Python que permite registrar, buscar y mostrar alumnos de una academia. Utiliza estructuras de datos simples como listas y diccionarios, además de funciones, condicionales y bucles para gestionar la lógica del programa. Está orientado a estudiantes de 2º Desarrollo de Aplicaciones Multiplataforma (DAM).

## Funcionalidades principales
- Añadir alumnos con nombre, edad y curso.
- Mostrar todos los alumnos registrados.
- Buscar alumnos por nombre (total o parcial).
- Interacción con el usuario mediante un menú en consola.
- Control básico de errores en la entrada de datos.

## Explicación de las funciones del código

### `agregar_alumno(lista)`
Solicita al usuario el nombre, edad y curso del alumno. Valida que los datos no estén vacíos y que la edad sea numérica. Si los datos son correctos, añade un diccionario con la información del alumno a la lista principal.

### `mostrar_alumnos(lista)`
Muestra en pantalla todos los alumnos registrados, enumerados para facilitar su visualización. Indica si la lista está vacía.

### `buscar_alumno(lista)`
Permite introducir un nombre o parte del nombre para buscar en la lista de alumnos. La búsqueda es insensible a mayúsculas y muestra todos los resultados coincidentes o un mensaje si no se encuentran coincidencias.

### `menu()`
Controla el flujo principal del programa, mostrando un menú iterativo con opciones para añadir, mostrar, buscar alumnos o salir. Gestiona la interacción usuario y llama a las funciones correspondientes según la opción seleccionada.

## Cómo ejecutar el programa
Ejecuta el archivo Python en una terminal o consola compatible. El menú se mostrará y podrás interactuar escribiendo las opciones deseadas.

## Capturas de pantalla recomendadas para el informe técnico

- Captura del menú principal en ejecución: mostrar las opciones disponibles para el usuario.
- Captura del proceso de añadir un alumno: entradas realizadas y confirmación de registro.
- Captura mostrando la lista de alumnos registrados tras añadir varios.
- Captura del proceso de búsqueda con resultados encontrados.
- Captura del proceso de búsqueda sin resultados (mensaje de no encontrado).

*Añade aquí las imágenes o imágenes incrustadas según el formato que uses para el informe.*

## Tecnologías utilizadas
- Python 3
- Uso de listas y diccionarios para manipulación de datos
- Manejo de entrada y salida por consola
- Estructuras condicionales y bucles para lógica de programa

