dias = float(input("Ingrese la cantidad de dias a procesar: "))

horas = dias * 24
minutos = horas * 60

segundos = minutos * 60

print("En " + str(dias) + " días hay:\n" +
      str(horas) + " horas\n" +
      str(minutos) + " minutos\n" +
      str(segundos) + " segundos")