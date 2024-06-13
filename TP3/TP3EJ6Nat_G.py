'''6. Programe una aplicación de consola Python que brinde al usuario la posibilidad de a partir
de una lista vacía:
a. Agregar un elemento al final.
b. Agregar un elemento al principio.
c. Quitar un elemento al final.
d. Quitar un elemento al principio.'''

#Se crea una lista vacía para almacenar los elementos
lista = []

#Se inicia un bucle infinito para mantener la aplicación en ejecución hasta que el usuario decida salir
while True:
    # Se muestran las opciones disponibles al usuario
    print("\n1. Agregar un elemento al final.")
    print("2. Agregar un elemento al principio.")
    print("3. Quitar un elemento al final.")
    print("4. Quitar un elemento al principio.")
    print("5. Mostrar la lista.")
    print("6. Salir.")
    
    # Se solicita al usuario que elija una opción
    opcion = input("Elige una opción: ")
    
    # Se agrega un elemento al final de la lista si la opción es 1
    if opcion == '1':
        elemento = input("Ingresa el elemento a agregar al final: ")
        lista.append(elemento)
        # Se agrega un elemento al principio de la lista si la opción es 2
    elif opcion == '2':
        elemento = input("Ingresa el elemento a agregar al principio: ")
        lista.insert(0, elemento)
    # Se quita el último elemento de la lista si la opción es 3
    elif opcion == '3':
        if lista:
            lista.pop()
            print("Se quitó el último elemento.")
        else:
            print("La lista está vacía.")
            # Se quita el primer elemento de la lista si la opción es 4
    elif opcion == '4':
        if lista:
            lista.pop(0)
            print("Se quitó el primer elemento.")
        else:
            print("La lista está vacía.")
    # Se muestra la lista actual si la opción es 5
    elif opcion == '5':
        print("La lista es:", lista)
    
    # Se sale del bucle si la opción es 6
    elif opcion == '6':
        break
    # Se muestra un mensaje de error si la opción no es válida
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")
        
# Se muestra un mensaje de despedida
print("Fin del programa, adios!")