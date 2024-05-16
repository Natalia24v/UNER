#11. Programe una aplicación de consola que muestre los primeros 
#5 caracteres de una cadena de texto ingresada por el usuario.

print("Ingrese una cadena de texto: ")
txt = input()

# Usamos el operador de slicing para obtener los primeros 5 caracteres
primeros_cinco = txt[:5]
print("Los primeros 5 caracteres del texto ingresado son:", primeros_cinco)