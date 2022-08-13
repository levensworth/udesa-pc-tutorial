
# Recuerden que solo pedimos implementar bubble sort o insertion sort.
# si el ejercicio no acalara que pueden utilizar las funciones de sort propias de Python
# por default deben asumir que no pueden utilizarlas y deben implementar sus propias formas de sort.

from typing import List


def sort_list(a_list: List) -> List:

    for i in range(len(a_list)-1):
        for j in range(1, len(a_list)):
            if a_list[i] > a_list[j]:
                # make swap
                aux = a_list[i]
                a_list[i] = a_list[j]
                a_list[j] = aux
    return a_list






