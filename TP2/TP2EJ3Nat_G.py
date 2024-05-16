#3. Que nos calcule el total de una factura tras aplicarle el IVA. La función 
#debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver 
#el total de la factura. Si se invoca la función sin pasarle el porcentaje de 
#IVA, deberá aplicar un 21%.

#Se define la función calcularIva
def calcularIva():
    #Se pide al usuario que ingrese el monto de la factura y lo convertimos a float
    monto = float(input("Ingrese el monto de la factura: "))
    #Se pide al usuario que ingrese el porcentaje de IVA a aplicar como una cadena
    ivaInput = input("Ingrese el porcentaje de IVA: ")
    #Se verifica si el usuario ingresó un valor para el IVA
    if ivaInput == '':
        #Si el usuario no ingresó un valor, aplicamos un IVA del 21%
        iva = 21
    else:
        #Si el usuario ingresó un valor, lo convertimos a float y lo usamos como el valor del IVA
        iva = float(ivaInput)
    #Se calcula el total de la factura sumando el monto original y el monto del IVA
    total = monto + (monto * iva / 100)
    #Se imprime el total de la factura
    print("El total de la factura es: " + str(total))

#Se llama a la función para que se ejecute
calcularIva()
