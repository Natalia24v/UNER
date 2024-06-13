#2. Pedir al usuario que ingrese 5 números para luego almacenarlos en una lista y ordenarlos.
#Imprimir por pantalla el resultado.

#Se crea una lista vacia para almacenar los números que ingresará el usuario
numeros = []

# Se utiliza un ciclo for para pedir al usuario que ingrese 5 números
for i in range(5):
   # Se pide al usuario que ingrese un número y se almacena en la variable num
    num = int(input("Ingrese un número: "))
    # Se agrega el número ingresado a la lista de números
    numeros.append(num)

#Se ordena la lista de n+umeros ingresados
numeros.sort()

#Se imprime por consola la lista numeros
print("sus numeros son: ", numeros)