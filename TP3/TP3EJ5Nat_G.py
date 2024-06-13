'''5. Escriba un programa Python que solicite al usuario el ingreso de números enteros. Cuando el
usuario ingrese la palabra “fin” el programa deberá concluir con la carga de datos. Cada uno
de los números ingresados por el usuario deberá ser almacenado en una lista. A continuación, 
realice las siguientes tareas:
a. Determinar el máximo.
b. Obtener segundo valor máximo. Es decir el que le sigue al máximo.
c. Determinar el mínimo.
d. Calcular la multiplicación de todos los números de la lista.
e. Contar los valores pares e impares.
f. Remover los elementos repetidos.'''

# Inicializamos la lista vacía
numeros = []
# Se utiliza un ciclo while para pedir al usuario que ingrese números enteros
while True:
    # Se pide al usuario que ingrese un número entero o 'fin' para concluir
    entrada = input("Ingrese un número entero o 'fin' para concluir: ")
    #se verifica si el usuario ingresa "fin"
    if entrada.lower() == "fin":
        # Se sale del ciclo cuando el usuario ingresa 'fin'
        break
    try:
        # Se intenta convertir la entrada a un número entero
        numero = int(entrada)
        # Se agrega el número ingresado a la lista de números
        numeros.append(numero)
    except ValueError:
        # Se imprime un mensaje de error si la entrada no es un número entero
        print("Error: Debe ingresar un número entero o 'fin' para concluir.")

# a. Determinar el máximo
maximo = max(numeros)
print("El máximo es:", maximo)

# b. Obtener segundo valor máximo
numeros_sin_maximo = [x for x in numeros if x != maximo]
segundo_maximo = max(numeros_sin_maximo) if numeros_sin_maximo else None
print("El segundo máximo es:", segundo_maximo)

# c. Determinar el mínimo
minimo = min(numeros)
print("El mínimo es:", minimo)

# d. Calcular la multiplicación de todos los números de la lista
multiplicacion = 1
for numero in numeros:
    multiplicacion *= numero
    
print("La multiplicación de todos los números es:", multiplicacion)

# e. Contar los valores pares e impares
pares = [x for x in numeros if x % 2 == 0]
impares = [x for x in numeros if x % 2 != 0]
print("Valores pares:", pares)
print("Valores impares:", impares)

# f. Remover los elementos repetidos
numeros_sin_repetidos = list(set(numeros)) 
print("Lista sin elementos repetidos:", numeros_sin_repetidos)