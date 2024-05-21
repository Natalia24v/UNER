#10. Que el usuario ingrese un número entero positivo y muestre por pantalla lo siguiente:
    #a. Todos los números impares desde 1 hasta ese número separados por comas.
    #b. La cuenta atrás desde ese número hasta cero separados por comas.
    #c. Que indique si es primo o no.
    #d. Por último, su factorial.

# Iniciamos función procesarNumero
def procesarNumero():
  # Se pide al usuario que ingrese un número entero, positivo
  numInput = int(input("Ingresar un numero entero, positivo: "))

  # a. Todos los números impares desde 1 hasta ese número separados por comas.
  print("Todos los numeros impares hasta tu número son: ")
  # Se verifica que el número sea impar
  for i in range(1, numInput + 1, 2):
    print(i, end=", ")  # Imprime el número impar y luego una coma y un espacio
  print()  # Imprime una nueva línea

  # b. La cuenta atrás desde ese número hasta cero separados por comas.
  print("Cuenta atrás: ", end="")
  for i in range(numInput, -1, -1):
    print(i, end=", ") 
  # Imprime una nueva línea
  print()  

  # c. Que indique si es primo o no.
  def esPrimo(n):
    # Si es menos que 2 no es primo, por lo que devolvemos directamente falso
    if n < 2:  
      return False
    # Un rango que va desde el dos hasta el número que estamos comprobando
    for i in range(2, n):  
      # Si el resto da 0 no es primo, por lo que devolvemos Falso
      if n % i == 0:  
        return False
    # De lo contrario devuelve Verdadero
    return True

  if esPrimo(numInput):
    print("El numero: ", numInput, " es primo")
  else:
    print("El numero: ", numInput, " no es primo")

  # d. Por último, su factorial.
  def factorial(n):
    # Si el número es 0, el factorial es 1
    if n == 0:  
      return 1
    else:
      # Calcula el factorial de forma recursiva
      return n * factorial(n-1)  

  print("El factorial de ", numInput, " es ", factorial(numInput))

procesarNumero()
