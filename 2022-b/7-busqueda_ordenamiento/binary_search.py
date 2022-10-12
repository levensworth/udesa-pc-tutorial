''''
Implementación de Binary search
'''


from typing import List


def binary_search(ord_list: List, query) -> int:
    '''
    Esta función busca de forma eficiente el elemento query dentro de una lista ordenada.
    
    Args:
    - ord_list: (List) es una lista de elementos ordenados de menor a mayor.
    - query: (Any) elemento a buscar dentro de la lista ord_list.
    
    Returns:
    (int) el indice en el que se encontró una aparición del elemento "query".
    En caso de no encontrar el elemento devuelve -1.
    '''

    min_pointer = 0
    max_pointer = len(ord_list)-1

    while min_pointer <= max_pointer:
        current_idx = (min_pointer + max_pointer)//2

        if ord_list[current_idx] == query:
            return current_idx

        if query < ord_list[current_idx]:
            max_pointer = current_idx
        
        if query > ord_list[current_idx]:
            # en este caso agregamos uno porque la operación de 
            # división entera redondea hacia el entero menor.
            min_pointer = current_idx + 1

    return -1 
            
            
            


