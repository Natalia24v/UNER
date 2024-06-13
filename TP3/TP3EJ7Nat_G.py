'''7. Escriba un programa Python que cuente con dos listas, la primera de ellas almacenará strings
con tareas pendientes y la segunda almacenará strings con tareas terminadas. Permita al
usuario:
a. Agregar nuevas tareas pendientes.
b. Marcar las tareas pendientes como terminadas. Al hacer esto, la tarea deberá pasar
de la lista de pendientes a la de terminadas.
Nota: posterior a cada operación deberá mostrar por pantalla el estado actual de ambas
listas.'''

# Se crean las listas vacías de tareas pendientes y terminadas
tPendientes = []
tTerminadas = []

# Función para agregar nuevas tareas pendientes
def agregarTarea(tarea):
    #Se verifica si la tarea ya existe en la lista de pendientes
    if tarea not in tPendientes:
        tPendientes.append(tarea)  # agrega tarea a la lista de pendientes
        mostraTareas() # mostrar el estado actual de ambas listas
    else:
        print("La tarea ya existe en la lista de tareas pendientes.")

# Función para marcar las tareas pendientes como terminadas
def terminarTarea(tarea):
    #Se verifica si la tarea existe en la lista de pendientes
    if tarea in tPendientes:
        tPendientes.remove(tarea) #elimina tarea de la lista de pendientes
        tTerminadas.append(tarea) #agrega tarea a la lista de terminadas
        
    else:
        print("La tarea no existe en la lista de pendientes")

# Función para mostrar el estado actual de ambas listas
def mostraTareas():
    print("Tareas pendientes:", tPendientes)
    print("Tareas terminadas:", tTerminadas)

# Bucle que muestra las opciones al usuario hasta que elija salir
while True:
    print("\nOpciones:")
    print("1. Agregar tarea pendiente")
    print("2. Marcar tarea como terminada")
    print("3. Mostrar tareas")
    print("4. Salir")

    #Se pide al usuario ingresar una opcion    
    opcion = input("Ingrese una opción: ")
    
    # Se comprueba cual opcion elige el usuario y se ejecuta en consecuencia
    if opcion == "1":
        tarea = input("Ingrese la tarea pendiente: ")
        agregarTarea(tarea) #Agrega tarea pendiente
    elif opcion == "2":
        tarea = input("Ingrese la tarea pendiente a marcar como terminada: ")
        if tarea in tPendientes: 
            terminarTarea(tarea) #Marca tarea como terminada
        else:
            print("La tarea no existe en la lista de pendientes")
        mostraTareas()
    elif opcion == "3":
        mostraTareas()
    elif opcion == "4":
        break #sale del bucle
    else:
        print("Opción inválida. Intente de nuevo.")
