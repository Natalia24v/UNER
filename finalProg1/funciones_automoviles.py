'''1. La empresa Burnout se dedica a la comercialización de automóviles y necesita un software
para procesar un archivo de datos que le envían sus proveedores. A tal fin el equipo de
programadores del que forma parte le encarga la programación de las siguientes funciones:
1.a) Crear un módulo llamado funciones_automoviles.py y en él programar las siguientes
funciones:
def leer_archivo():
""" Devuelve una lista de automóviles. """
cadena = ''
with open('autos.json','rt',encoding="utf-8") as archivo:
cadena = archivo.read()
return json.loads(cadena)
def filtrar_por_tipo(lista, tipo):
""" Devuelve los automóviles del tipo pasado por parámetro
por parámetro. """
def filtrar_precio_mayor(lista, importe):
""" Devuelve los automóviles cuyo importe supera el pasado
por parámetro. """
def calcular_valor_total(lista):
"""Devuelve la sumatoria de todos los precios de los
automóviles. """
def ordenar_por_precio(lista):
""" Ordena los automóviles por el atributo precio. """
Las funciones anteriormente mencionadas deberán tratar con una lista de elementos de tipo
diccionario que contenga las siguientes propiedades de automóviles:
Propiedad Tipo de datos Observaciones
Número int
Modelo str
Marca str
Tipo str Sedán, Berlina, SUV, Camioneta
Color str
Precio float'''
import json

""" Devuelve una lista de automóviles. """
def cargar_datos():
  cadena = ''
  with open('autos.json','rt',encoding="utf-8") as archivo:
    cadena = archivo.read()
    return json.loads(cadena)

def filtrar_por_tipo(lista, tipo):
# Devuelve los automóviles del tipo pasado por parámetro.
  automoviles_filtrados = []
  for auto in lista:
    if auto['tipo'] == tipo:
      automoviles_filtrados.append(auto)
  return automoviles_filtrados

def filtrar_precio_mayor(lista, importe):
#""" Devuelve los automóviles cuyo importe supera el pasado por parámetro. """
  for auto in lista:
    if auto['precio'] > importe:
      return auto

def calcular_valor_total(lista):
#"""Devuelve la sumatoria de todos los precios de los automóviles. """
  return sum(auto['precio'] for auto in lista)

def obtener_precio(auto):
    return auto['precio']
def ordenar_por_precio(lista):
#""" Ordena los automóviles por el atributo precio. """
  return sorted(lista, key=obtener_precio, reverse=True)
    

