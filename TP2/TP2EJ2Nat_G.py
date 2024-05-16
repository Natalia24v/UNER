#2. Que reciba un número entero positivo y una potencia a elevar y que nos 
#devuelva el resultado.

#Se define la función
def potenciado():
    #Se pide al usuario que ingrese un número entero positivo
    numero = int(input("Por favor ingrese un numero: "))
    #Se pide al usuario que ingrese una potencia a elevar
    potencia = int(input("Por favor ingrese una potencia: "))
    # Se verifica si el número ingresado es positivo
    if numero <= 0:
        # Si el número no es positivo, se imprime un mensaje de error
        print("El numero debe ser positivo")
    else:
        # Si el número es positivo, se calcula la potencia del número
        resultado = numero ** potencia
        # Se imprime el resultado por consola
        print("El resultado es: " + str(resultado))
#Se llama a la función para que se ejecute
potenciado()