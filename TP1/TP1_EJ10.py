#10. Escriba un programa que indique si un texto es palindromo, es decir, 
#se escribe igual al derecho que al revés. Por ejemplo: rayar, kayak, somos.

txt = input("Ingrese una palabra o frase: ")

# Se usa el operador de slicing para invertir el string o cadena de texto, se evalua si la sentencia 
# es verdadera usando estructura de control if else
if txt == txt[::-1]: 
    print("Es palíndromo")
else:
    print("No es palíndromo")   