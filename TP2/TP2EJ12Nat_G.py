#12. Pedir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro
#mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día
#ingresado no es ninguno de esos, imprimir otro mensaje.

#Se inicia la función que dará un mensaje segun el dia ingresado
def mensajePorDia():
    #Se crea una variable para almacenar el dia ingresado por el usuario
    dia = input("Ingresa un dia de la semana: ").lower()
    #Se crea un condicional para que el programa sepa que dia es
    if dia == "lunes":
        print("Hola hoy es lunes, tienes clase de Inglés!")
    elif dia == "viernes":
        print("Hola es viernes hoy tienes clase de programación!")
    elif dia == "sabado" or dia == "domingo":
        print("Es sabado o domingo tienes clases de cocina")
    else:
        print("Hoy no hay actividades programadas!")

#Se llama a la función para ser ejecutada
mensajePorDia()