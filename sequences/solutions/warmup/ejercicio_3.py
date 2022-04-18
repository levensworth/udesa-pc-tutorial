

from typing import List


def has_negative(a_list: List) -> List:
    '''
    Given a list of integers, filter the negative values.
    Params:
        - a_list: List of integers
    Returns:
    List of non negative integers from the original list.
    '''

    result = []
    for elem in a_list:
        if elem >= 0:
            result.append(elem)
    return result



"""
A este punto vimos que hay una temática muy parecida con los casos donde nos piden que filtremos
una lista dado una condición. Si notó el patrón, piense el siguiente problema:
Escriba una función filter_list que reciba un lista y un predicado como argumentos. Dicha función debe
retornar una nueva lista que contenga los elementos que cumplan el predicado.
Obs: un predicado es una función que recibe un argumento y retorna Ture o False.

Ejemplo de uso:

Si quiero filtrar los elementos negativos de una lista seria

def is_negative(x): # esto es un predicado
    return x < 0

resultado = filter_list([1,2,3,4, -3, 0, -2], is_negative)

resultado deberia tener el valor de [1,2,3,4,0]

===========================================
Ahora el enunciado de filtrar multiplos es simplemente:

def is_multiple_of_3(x):
    return x %3 == 0

filter_list([3,4,5....], is_multiple_of_3)

"""


def filter_list(a_list: List, predicate) -> List:
    '''
    Simple implementation of filter without generators. 
    Params:
        - a_list: list to filter.
        - predicate: function to evaluate each element.
    
    Returns:
        - List of element whose predicate evaluation were Positive.
    '''
    
    result = []
    for elem in a_list:
        if predicate(elem):
            result.append(elem)
    return result


