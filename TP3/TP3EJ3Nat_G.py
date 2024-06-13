#3. Dada la siguiente lista de frutas [“banana”, “manzana”, “pera”], permitir al usuario ingresar 3
#frutas más para agregarlas al final de lista. Luego, mostrar por pantalla la lista completa y
#debajo la misma lista pero sólo con las frutas que añadió el usuario.

#se crea la lista predefinida frutas
frutas = ["banana", "manzana", "pera"]

#se crea una lista vacía para almacenar las frutas que el usuario añadirá las suyas
frutas_usuario = []

#Se pide al usuario que ingrese 3 frutas
for i in range(3):
    # se pide al usuario que ingrese una fruta y se almacena en la variable fruta
    fruta = input("Por favor, ingresa una fruta: ")
    # se agrega la fruta ingresada a la lista de frutas del usuario
    frutas_usuario.append(fruta)

#se agrega las frutas del usuario a la lista de frutas
frutas += frutas_usuario

#Se imprime la lista completa
print("La lista completa de frutas es: ", frutas)

#Se Imprime sólo las frutas que añadió el usuario
print("Las frutas que añadiste son: ", frutas_usuario)
