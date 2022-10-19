'''
Consigna:

Implementar una función que dados 2 listas de enteros ordenados,
devuevla una nueva lista ordenada con el contenido de ambas listas.

ejemplo:

si las listas iniciales son"

[1,1,4,7]
[3,4,8,9]

obtendremos el resultado:
[1,1,3,4,4,7,8,9]

'''


from typing import List


def merge_lists(a_list: List[int], b_list: List[int]) -> List[int]:

    result = []
    
    idx_a = 0
    idx_b = 0

    while idx_a < len(a_list) and idx_b < len(b_list):

        if a_list[idx_a] > b_list[idx_b]:
            result.append(b_list[idx_b])
            idx_b += 1

        elif a_list[idx_a] < b_list[idx_b]:
            result.append(a_list[idx_a])
            idx_a += 1

        else:
            result.append(a_list[idx_a])
            result.append(b_list[idx_b])
            idx_a += 1
            idx_b += 1

    
    result += a_list[idx_a:]

    result += b_list[idx_b:]

    return result
    
        
print(merge_lists([1,1,4,7], [3,4,8,9]))

