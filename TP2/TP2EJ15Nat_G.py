#15. Que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. Se debe
#validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter,
#informarle que no se puede procesar el dato.

#se inicia funcion
def esVocal():
    #se declara variable letra donde se pide al usuario ingresar una letra
    letra = input("Ingrese una letra: ")
    #se declara variable vocal donde se almacena la letra ingresada por el usuario
    vocal = "aeiouAEIOU"
    #se examina si la cantidad de letras ingresadas es mayor a 1
    if len(letra) > 1:
        #si no se cumple la condicion se indica al usuario que solo debe ingresar una letra
        print("Debe ingresar solo una letra")
    #se examina si la letra ingresada por el usuario es una vocal
    else:
        if letra in vocal:
            #si se cumple la condicion se indica al usuario que la letra ingresada es una vocal
            print("Es vocal")
        else:
            #si no se cumple la condicion se indica al usuario que la letra ingresada no es una vocal
            print("No es vocal")

#se invoca la funcion para ejecutarla
esVocal()