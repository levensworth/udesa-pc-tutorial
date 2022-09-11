'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

Escribir una función que reciba por parametro el numero de digitos máximo a utilizar (N)
y retorne el valor del palindromo más alto que se puede generar por números de hasta N digitos.
En caso de error en los parámetros retornar None

Obs: Considere que resguardos hay que tener sobre el parámetro N. (puede ser negativo?)

Ejemplo:

find_palindrome(2)
debe retornar 9009 


soruce: https://projecteuler.net/problem=4
'''






def is_palindrome(string: str) -> bool:
    max_length = len(string)
    for i in range(len(string)):
        if string[i] != string[max_length - 1 - i]:
            return False
    
    return True


def find_palindrome(number_of_digits: int) -> int:
    
    if number_of_digits < 0:
        return None

    max_number = int('9' * number_of_digits)
    
    for i in range(max_number, 1, -1):
        for j in range(max_number, 1, -1):
            product  = i * j
            if is_palindrome(str(product)):
                return product
    
    return None # nunca llegaria a este punto.


print(find_palindrome(3))