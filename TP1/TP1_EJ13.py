#13. Programe una aplicación de consola que solicite al usuario su nombre, después su apellido y
#a continuación su año de nacimiento. Con esos datos deberá generar una sugerencia de
#usuario y contraseña. Por ejemplo: nombre: Martín, apellido: Francisconi, Año nacimiento:
#1985 -> Usuario: mfrancisconi, Contraseña: mf.1985.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

anio_nacimiento = input("Ingrese su año de nacimiento: ")

# Se genera una sugerencia de usuario tomando la primera letra del nombre concatenándola con el apellido completo.
usuario = nombre[0] + apellido
# Se genera una sugerencia de contraseña que se forma con la primera letra del nombre, 
#el apellido completo, un punto y el año de nacimiento.
contrasenia = nombre[0] + apellido + "." + anio_nacimiento

print("Usuario: " + usuario)
print("Contraseña: " + contrasenia)
