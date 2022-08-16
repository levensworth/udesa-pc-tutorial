'''
Escribir un programa en Python que convierta millas a kilómetros. Se deben
imprimir los siguientes mensajes:
Bienvenido (ingrese su nombre): <nombre>
Ingrese las millas a convertir: <millas>
Hola <nombre>, la conversión resulta:
 <resultado> km
Guarde el programa en un archivo que se llame m2k.py
'''

name = input('Bienvenido (ingrese su nombre): ')
miles = float(input('Ingrese las millas a convertir:'))

mile_kilometer_ratio = 1.609344

kilometers = miles * mile_kilometer_ratio

# Notar que en este caso usamos f-strings para generar la cadena de texto completa.
# la notación {kilometers:.2f} indica a Python que queremos visualizar solamente 2 decimales de
# la variable kilometers
print(f'Hola {name}, la conversión resulta:\n {kilometers:.2f} Km')

