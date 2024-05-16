#8. Pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

#Se define la función mayorDeEdad
def mayorDeEdad():
    #se pide al usuario que ingrese su edad
    edad = int(input("Ingrese su edad: "))
    #se evalua si la edad es mayor o igual a 18
    if edad >= 18:
        #si lo es se imprime por consola el mensaje "es mayor de edad"
        print("Es mayor de edad!")
    #sino se cumple la condición if pasa a else   
    else:
        #que mostrará el mensaje "no es mayor de edad"
        print("No es mayor de edad!")

#se llama a la función para su ejecución
mayorDeEdad()