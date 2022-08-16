'''
Escriba un programa que le solicite al usuario el ingreso de tres palabras y otros dos parámetros,
separador (caracter o texto para separar cada argumento a imprimir) y fin (caracter o texto para
imprimir al final de todo) de manera tal que el resultado se imprima como el siguiente ejemplo:
Enter word 1: <Pensamiento>
Enter word 2: <Computacional>
Enter word 3: <UDESA>
Enter separator: <->
Enter last string: <!!!>
Pensamiento-Computacional-UDESA!!!
El texto de salida debe ser guardado en una variable llamada full_str, que guarde un string con la
concatenación de todas las entradas y lo imprima en pantalla.
'''

word_1 = input('Enter word 1: ')
word_2 = input('Enter word 2: ')
word_3 = input('Enter word 3: ')

separator = input('Enter separator: ')
last_string = input('Enter last string: ')

print(word_1, word_2, word_3, sep=separator, end=last_string)

