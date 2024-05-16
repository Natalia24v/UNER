#4. Que dada la base y altura de un triángulo nos calcule su área.

#Se define la funcion para calcular el área de un triángulo
def areaTriangulo():
    #se pide que se ingresen la base y la altura del triangulo
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    #se calcula el área del triángulo
    area = (base * altura) / 2 
    #se imprime el resultado por consola
    print("El área del triángulo es: ", area) 

# Se llama a la función para que se ejecute
areaTriangulo()
