'''EJERCICIOS
2. Cree un archivo con nombre principal.py que se constituya como programa principal y en él:
2.a) Ponga a prueba las funciones programadas en el punto anterior (sin hacer interacción
con el usuario usando input/print. Ver apartado siguiente).
'''
import funciones_automoviles
def main():
    autos = funciones_automoviles.cargar_datos()

    sedanes = funciones_automoviles.filtrar_por_tipo(autos, "Sedán")
    autos_caros = funciones_automoviles.filtrar_precio_mayor(autos, 2500000)
    valor_total = funciones_automoviles.calcular_valor_total(autos)
    autos_ordenados = funciones_automoviles.ordenar_por_precio(autos)

  
    print(sedanes)
    print(autos_caros)
    print(valor_total)
    print(autos_ordenados)

if __name__ == "__main__":
    main()
