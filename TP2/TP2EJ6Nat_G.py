#PARTE 2 - ESTRUCTURAS DE CONTROL- En esta segunda parte deberán utilizar estructuras de control condicionales 
#(y en lo posible y dado el caso funciones) para escribir programas que lleven a cabo lo siguiente:
#6. Que pida al usuario una palabra y la muestre por pantalla 10 veces.

#Se pide al usuario que ingrese una palabra.
palabra = input("Ingrese una palabra: ")

# Se inicia un bucle for que se ejecutará 10 veces. La función range(10) genera una secuencia de números del 0 al 9.
for i in range(10):
    # En cada iteración se imprime la palabra que el usuario ingresó, dando untotal de 10 veces
    print(palabra)
