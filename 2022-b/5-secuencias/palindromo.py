'''
una cadena de caracteres se considera palindromo cuando se puede
leer la misma palabra de izquierda a derecha o viceversa.

Ejemplo:

- aba
- abba
- mom
- noon

Escribir una función is_palindrome que reciba un string y retorne 
true si el mismo es palindromo y false caso contrario.

Obs: No se puede crear una nueva secuencia en la solucion propuesta.
'''

def is_palindrome(string: str) -> bool:
    max_length = len(string)
    for i in range(len(string)):
        if string[i] != string[max_length - 1 - i]:
            return False
    
    return True
    


