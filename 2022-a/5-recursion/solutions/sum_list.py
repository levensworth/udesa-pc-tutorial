
def reduce_list_sum(a_list: list) -> int:
    '''
    Dado una lista de enteros retorna la suma de todos sus elementos
    '''

    if len(a_list) == 0:
        return None

    if len(a_list) == 1:
        return a_list[0]

    return a_list[0] + reduce_list_sum(a_list[1:])
