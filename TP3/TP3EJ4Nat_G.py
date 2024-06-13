'''4. Dada la siguiente lista: paises = [“Argentina,”Brasil”, “Bolivia”,”Paraguay”,”Venezuela”],
realizar lo siguiente:
a. Imprimir la cantidad de elementos que tiene la lista.
b. Imprimir el primer y último elemento./c. Imprimir el resto.
d. Permitir que el usuario ingrese un país e imprimir el índice si el país se encuentra en
la lista. Si no se encuentra, imprimir un mensaje advirtiendo al usuario.
e. Permitir al usuario ingresar un número igual o menor a la cantidad de elementos de la lista. Quitar el elemento correspondiente de esa posición.
f. Imprimir la lista en orden inverso.
g. Vaciar la lista.'''

paises = ["Argentina", "Brasil", "Bolivia", "Paraguay", "Venezuela"]

#Se imprime ñla cantidad de elementos de la lista
print("a. La cantidad de elementos que tiene la lista es:", len(paises))
#Se imprime el primer y último elemento
print("b. El primer elemento es:", paises[0], "y el último es:", paises[-1])
#Se imprime el resto de los elementos
print("c. El resto de la lista es:", paises[1:-1])

#d. Se pide al usuario ingresar un país
pais_usuario = input("d. Ingrese un país: ")
# Se verifica si el país ingresado se encuentra en la lista
if pais_usuario in paises:
    # Se imprime el índice del país en la lista
    print("El país se encuentra en la lista en la posición", paises.index(pais_usuario))
else:
    # Se imprime un mensaje advirtiendo al usuario que el pais no se encuentra en la lista
    print("El país no se encuentra en la lista")
#e Se pide al usuario ingresar una posición para eliminar un elemento
posicion_usuario = int(input("e. Ingrese una posición (0-" + str(len(paises) - 1) + "): "))
# Se verifica si la posición ingresada es válida
if 0 <= posicion_usuario < len(paises):
    # Se elimina el elemento en la posición ingresada
    del paises[posicion_usuario]
    print("Se eliminó el elemento en la posición", posicion_usuario)
else:
    # Se imprime un mensaje advirtiendo al usuario que la posición ingresada no es válida
    print("La posición ingresada no es válida")

#f. Se imprime la lista en orden inverso
print("f. La lista en orden inverso es:", paises[::-1])

# g. Se vacía la lista
paises.clear()
print("g. La lista ha sido vaciada:", paises)
