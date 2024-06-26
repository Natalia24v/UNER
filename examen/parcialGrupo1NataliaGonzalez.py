'''EJERCICIO 1)
Escribe un programa que lea las calificaciones de un grupo de estudiantes (el usuario ingresará las
calificaciones una a una y usará el valor “FIN” para finalizar la entrada de datos). El programa debe
cumplir con los siguientes requisitos:
Requisitos:
● Utilizar una lista para almacenar las calificaciones.
● Imprimir las calificaciones ordenadas de menor a mayor.
● Calcular y mostrar el promedio por pantalla.
● Contar el número de calificaciones ingresadas.
● Convertir todas las calificaciones a strings y unirlas en una sola cadena(string) separada por comas.
● Contar cuántos alumnos han aprobado la materia (sacaron una nota mayor o igual a 6).
● Calcular la calificación más baja y la más alta e Imprimir por pantalla un mensaje con el
siguiente formato: “La calificación más baja fue XX y la más alta XX.”
● Vaciar la lista.'''

#Se inicializa la lista vacia que almacenará las calificaciones
calificaciones = []
#Se leen las calificaciones hasta que el usuario ingrese "FIN"
entrada = input("Ingresa una calificación o ingresa la palabra 'FIN' para terminar: ")
while entrada != "FIN":
    #Se vverifica que la entrada sea un número y lo agregamos a la lista
    try:
        calificacion = float(entrada)
        calificaciones.append(calificacion)
    except ValueError:
        print("Por favor, ingresa un número válido o 'FIN' para terminar.")
    entrada = input("Ingresa una calificación o la palabra 'FIN' para terminar: ")

#Se mprimime las calificaciones ordenadas de menor a mayor
calificaciones.sort()
print("Calificaciones ordenadas:", calificaciones)

#Se calcula y muestra el promedio
promedio = sum(calificaciones) / len(calificaciones)
print("Promedio de calificaciones:", promedio)

#Se cuenta el número de calificaciones ingresadas
print("Número total de calificaciones ingresadas:", len(calificaciones))

#Se convierten todas las calificaciones a strings y se unen en una cadena separada por comas
calificaciones_str = ", ".join([str(calif) for calif in calificaciones])
print("Calificaciones unidas en una cadena:", calificaciones_str)

#Se cuenta cuántos alumnos han aprobado la materia
aprobados = len([calif for calif in calificaciones if calif >= 6])
print("Número de alumnos que aprobaron la materia:", aprobados)

#Se calcula la calificación más baja y la más alta
minCalificacion = min(calificaciones)
maxCalificacion = max(calificaciones)
print(f"La calificación más baja fue {minCalificacion} y la más alta {maxCalificacion}.")

#Se vacía la lista
calificaciones.clear()