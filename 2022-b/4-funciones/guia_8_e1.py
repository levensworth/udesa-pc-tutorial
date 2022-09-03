'''
Implemente una funcion que reciba un numero flotante y devuelva
la cantidad de digitos.
'''


def count_int_part(number: float) -> int:
    '''
    Counts the number of integer decimals of a given number.
    Args:
    number (int | float): a given number

    Returns: 
    (int) number of digits
    '''

    integer_rep =  int(abs(number))
    return len(str(integer_rep))


print(count_int_part(231.56))