#16. Que imprima el siguiente patrón: 
# 54321
#  4321
#   321
#    21
#     1 

def patronNum(): 
    # Este bucle se ejecuta desde 5 hasta 1
    for i in range(5,0,-1):  
        # Este bucle imprime los espacios al principio de cada línea
        for j in range(5,i,-1):  
            print(" ", end="")
        # Este bucle imprime los números
        for k in range(i,0,-1):  
            print(k, end="")
        # Esto crea una nueva línea después de cada serie de números
        print()  
patronNum()
