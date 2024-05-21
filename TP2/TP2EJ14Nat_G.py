#14. Que pida un año y que escriba si es bisiesto o no. Les recordamos que los años bisiestos son
#múltiplos de 4, pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. Algunos
#ejemplos de posibles respuestas: 2012 es bisiesto, 2010 no es bisiesto, 2000 es bisiesto, 1900
#no es bisiesto.

#se inicia funcion
def anioBisiesto():
    #se pide al usuario ingresar un año
    anio = int(input("Ingrese un año: "))
    #se verifica si el año es bisiesto
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        #si se cumple la condición se imprime un mensaje
        print("El año", anio, "es bisiesto")
    #sino se cumple la condicion se imprime que no es bisiesto    
    else:
        print("El año", anio, "no es bisiesto")

anioBisiesto()