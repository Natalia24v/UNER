#13. Que resuelva el siguiente problema: los alumnos de un curso se han dividido en dos grupos
#A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un
#nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el
#resto. Escribir un programa que pregunte al usuario su nombre y sexo y muestre por pantalla
#el grupo que le corresponde.

# se define función que indica a quegrupo pertenece un usuario
def queGrupo():
    #Se inicializanlas variables que toman el nombre y sexo ingresados por el usuario
    nombre = input("Ingrese su nombre: ")
    sexo = input("Ingrese su sexo (f para femenino o m para masculino): ").lower()
    # Se evalua el grupo al que pertenece el usuario con condicional if
    if (sexo == "f" and nombre[0] < "m") or (sexo == "m" and nombre[0] > "n"):
        print("Pertenece al Grupo A")
    else:
        print("Pertenece al Grupo B")

#Se llama a la función queGrupo para ser ejecutada
queGrupo()