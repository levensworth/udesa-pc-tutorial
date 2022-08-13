
from typing import List


# 1
def reverse_list(a_list: List) -> List:
    idx = 0
    reverse_idx = len(a_list) - 1
    while idx < (len(a_list) // 2):
        aux = a_list[idx]
        a_list[idx] = a_list[reverse_idx]
        a_list[reverse_idx] = aux

        # update pointer
        idx +=1
        reverse_idx -= 1

    return a_list

