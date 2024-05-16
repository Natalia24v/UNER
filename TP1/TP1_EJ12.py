#12. Pedir al usuario que ingrese una fecha en formato dd/mm/aaaa e imprimir en pantalla el
#día, mes y año. Ej: Usuario ingresa: 17/05/1985
#Programa imprime: Día: 17, Mes: 05 y Año: 1985

fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
#se extrae el día de la fecha, tomando los primeros dos caracteres de la cadena con el operador slicing
dia = fecha[0:2]
#se extrae el mes de la fecha, tomando los caracteres del tercer al quinto con el operador slicing
mes = fecha[3:5]
#se extrae el año de la fecha, tomando los caracteres del sexto al décimo con el operador slicing
anio = fecha[6:10]

print("Día: ", dia, ", Mes: ", mes, " y Año: ", anio)