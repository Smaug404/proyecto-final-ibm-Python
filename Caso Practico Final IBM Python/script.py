"""Escribe un programa en Python utilizando Programación Orientada a Objetos que gestione 
    una lista de tareas pendientes.

El programa deberá permitir al usuario realizar las siguientes operaciones:

Agregar una nueva tarea:
El programa deberá permitir al usuario agregar una nueva tarea a la lista de tareas pendientes.

Marcar una tarea como completada:
El programa deberá permitirá al usuario marcar una tarea como completada, dada su posición en la lista.

Mostrar todas las tareas: 
El programa deberá imprimir en pantalla todas las tareas pendientes, numeradas
y mostrando su estado (completada o pendiente).

Eliminar una tarea:
El programa deberá permitir al usuario eliminar una tarea de la lista, dada su posición."""


"""1.0 Se define la clase Tarea con dos atributos 'nombre' para almacenar el nombre de la tarea,
       y 'realizada' para almacenar el estado de realización de la tarea. """

"""1.1 Los métodos 'marcar_como_realizada' y 'marcar_como_no_realizada'se usa
       para cambiar el estado de realización de la tarea según sea necesario."""

class Tarea:
    def __init__(self, nombre):
        self.nombre = nombre
        self.realizada = False
    
    def marcar_como_realizada(self):
        self.realizada = True
    
    def marcar_como_no_realizada(self):
        self.realizada = False

"""2.Se crea la clase 'ListaTareas' que permite al usuario
    agregar, mostrar todas las tareas con su nombre y estado 
    y eliminar una tarea específica por su índice en la lista. """

class ListaTareas:
    def __init__(self):
        self.tareas = []
    
    def agregar_tarea(self, nombre):
        tarea = Tarea(nombre)
        self.tareas.append(tarea)
    
    def mostrar_tareas(self):
        for idx, tarea in enumerate(self.tareas):
            estado = "Hecho" if tarea.realizada else "Pendiente"
            print(f"{idx + 1}. {tarea.nombre} - Estado: {estado}")
    
    def eliminar_tarea(self, indice):
        del self.tareas[indice - 1]

"""3.Se crea una instancia de la clase ListaTareas, 
    -se muestra un menú con diferentes opciones para el usuario, 
    -se solicita al usuario que seleccione una opción y 
    -se realizan diferentes acciones dependiendo de la opción seleccionada. 
    -el bucle while se ejecutara hasta que el usuario decida salir del programa."""

lista = ListaTareas()

#4.Menu principal que estará viendo el usuario en pantalla.

while True:
    print("1. Agregar tarea")
    print("2. Marcar tarea como realizada")
    print("3. Marcar tarea como no realizada")
    print("4. Mostrar tareas")
    print("5. Eliminar tarea")
    print("6. Salir")

#5.Las opciones disponibles que tendra el usuario 

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre_tarea = input("Introduce el nombre de la tarea: ")
        lista.agregar_tarea(nombre_tarea)
    elif opcion == "2":
        lista.mostrar_tareas()
        indice = int(input("Selecciona el índice de la tarea a marcar como realizada: "))
        lista.tareas[indice - 1].marcar_como_realizada()
    elif opcion == "3":
        lista.mostrar_tareas()
        indice = int(input("Selecciona el índice de la tarea a marcar como no realizada: "))
        lista.tareas[indice - 1].marcar_como_no_realizada()
    elif opcion == "4":
        lista.mostrar_tareas()
    elif opcion == "5":
        lista.mostrar_tareas()
        indice = int(input("Selecciona el índice de la tarea a eliminar: "))
        lista.eliminar_tarea(indice)
    elif opcion == "6":
#6. En caso de error se le indica que lo intente otra vez
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")






