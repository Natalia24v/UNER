#11. Que solicite al usuario ingresar una frase. Luego, que imprima la cantidad de vocales que se
#encuentran en dicha frase.

#Se define la funcion vocales
def cuentaVocales():
    #Se pide al usuario que ingrese una frase y se la convierte a minuscula para contar todas las vocales
    frase = input("Ingrese una frase: ").lower()
    #Se crea una lista con las vocales a contar
    vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    
    contador = 0
    #Se recorre la frase
    for letra in frase:
        #Se verifica si la letra es una vocal
        if letra in vocales:
            #Se incrementa el contador en 1
            contador += 1
    #Se imprime por consola el resultado
    print("La cantidad de vocales en la frase es: ", contador)

cuentaVocales()