#17. Que muestre todos los números primos entre 0 y 100 e imprima cuántos números primos hay.

#Se inicia la funcion para contar y mostrar numeros primos
def cuentaPrimos(num):
    #para llevar la cuenta de los números primos
    contador = 0
    #el ciclo for recorre los numeros del 0 al 100
    for i in range(2, num+1):
        es_primo = True
        #el ciclo for  verifica si los numeros del 2 al 100
        for j in range(2, i):
            #Si el resto de la division entre i y j es 0, es porque i no es primo
            if i % j == 0:
                es_primo = False
                break
        # Si el número actual es primo lo imprime e incrementar el contador
        if es_primo:
            print(i)
            contador += 1
    #Se imprime la cuenta de números primos
    print("Cantidad de números primos:", contador)

#Se llama a la funcion
cuentaPrimos(100)

