#9. Que el usuario ingrese dos números y muestre cuál de los dos es menor. 
#Considerar el caso en que ambos números son iguales.

#se inicializa la funcion menorNum
def menorNum():
    #se inicializa la variable num1
    num1 = int(input("Ingrese el primer numero: "))
    #se inicializa la variable num2
    num2 = int(input("Ingrese el segundo numero: "))
    
    #se comprueba si el primer numero es mayor al segundo
    if (num1 < num2):
        #si se cumple la condición se imprimira el mensaje "El primer numero es menor"
        print("El primer numero es menor")
    #se comprueba si el segundo numero es menor al primero
    elif (num1 > num2):
        #en cambio si se cumple esta condición se imprimira el mensaje "El segundo numero es menor"
        print("El segundo numero es menor")
        
    #en caso de que ambos numeros sean iguales se imprimira el mensaje "Los numeros son iguales"
    else:
        print("Los numeros son iguales")

#Se invoca a la función para ser ejecutada
menorNum()