#5. Que dado tres números ingresados por el usuario nos devuelva el promedio.

#Se define la función promedio
def promedio():
    #Se pide al usuario que ingrese tres números que se convierten a float
    num1 = float(input("Ingrese un numero: "))
    num2 = float(input("Ingrese otro numero: "))
    num3 = float(input("Ingrese un tercer numero: "))

    #se calcula el promedio de los numeros ingresados
    resultado = (num1 + num2 + num3) / 3.0
    #Se imprime el promedio por consola
    print("El resultado es: ", str(resultado))

#Se invoca a la función para su ejecución
promedio()