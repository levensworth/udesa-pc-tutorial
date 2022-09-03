'''
Escribir una funcion tal que calcule el n-esimo termino de 
la secuecnia Fibonacci, retorne el valor del mismo y si es par o impar.

Ejemplo:

>>> val, is_even = fibo(6)
>>> print(val)
8
>>> print(is_even)
True

Source: https://projecteuler.net/problem=2
'''

def fibo(index: int):
    '''
    Calcula el numero de la secuencia Fibonacci 
    y retorna su valor de paridad.
    
    Args:
    index (int): el cardinal de la secuencia

    Return:
    (int, bool) el numero y su paridad.

    '''
    if index < 3:
        return 1, False

    prev = 1
    cur = 1

    for _ in range(index -2):
        aux = cur
        cur = cur + prev
        prev = aux

    is_even = cur % 2 == 0
    return cur, is_even