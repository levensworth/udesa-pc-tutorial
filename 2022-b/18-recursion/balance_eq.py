'''
Consigna:

Implementar una función recursiva `get_balance` que dado una expresión matemática (en string)
retorne el balance de parentesis.
Ejemplo: `56 + (a - 7 - ( 12 + c) - t * 678)` retornaría 0, significando que está balanceada.
`56 + (a - 7 -  12 + c) - t * 678)` retornaría distinto de cero, didicando que no está balanceada.

''' 


def get_balance(exp: str) -> int:
    
    if len(exp) == 0:
        return 0
    
    resp = 0
    
    if exp[0] == '(':
        resp = 1
    if exp[0] == ')':
        resp = -1

    return resp  + get_balance(exp[1:])

    
    
    
    
    