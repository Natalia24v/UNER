# 1. Crear un programa que almacene en una lista las materias de esta u otra carrera y que las
# muestre por pantalla. (La lista debe ser predefinida, no debe ser ingresada por el usuario).

materias = ["Programacion 1", "Introduccion a la Informatica", "Diseño Gráfico", 
            "Arquitectura de Computadoras", "Prosramación II", "Sistemas Operativos", 
            "Introducción al Desarrollo Web", "Bases de Datos", "Redes de Datos", 
            "Prosramación III", "Inseniería de Software", "Desarrollo de Aplicaciones Web", 
            "Desarrollo para Móvil es", "Multimedia v Juegos en Web"]

print(f"Las materias de la carrera son:\n" + "\n".join(materias))