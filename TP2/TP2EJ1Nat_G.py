#1. Que al pasarle una cadena <nombre> nos muestre por pantalla el saludo 
#¡Hola <nombre>!.

#Se define la función
def saludo():
    #Se pide al usuario ingresar su nombre
    nombre = input("Ingrese su nombre: ")
    #Se imprime el saludo por consola
    print("hola ", nombre)

#Se llama a la función para que se ejecute
saludo()