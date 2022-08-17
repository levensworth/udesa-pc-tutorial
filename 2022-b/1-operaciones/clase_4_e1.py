'''
Implemente un programa que solicite por consola un numero entero (puede ser positivo o negativo) 
y luego imprima un mensaje indicando a cual/cuales de las siguientes categorias petence.
- numero positivo
- numero negativo
- numeros positivos multiplos de 2
- numoer positivos multiplos de 5
- numeros negativos multiplos de 4
- numeros negativos multiplos de 7
- ceo
'''
numero  = int(input('Ingrese un numero: '))

if numero  > 0:
    print('es positivo')
    if numero % 2 == 0:
        print('es par')
    
    if numero % 5 == 0:
        print('es divisible por 5')

elif numero < 0:
    print('es negativo')

    if numero % 4 == 0:
        print('es multiplo de 4')

    if numero % 7 == 0:
        print('es divisible por 7')
else:
    print('es cero')






