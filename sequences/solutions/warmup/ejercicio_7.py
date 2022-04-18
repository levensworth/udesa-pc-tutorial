

from typing import List


def remove_duplicates(a_list: List) -> List:
    if len(a_list) < 2:
        return a_list # there can't be any duplicates

    result = [a_list[0]]
    
    for i in range(1, len(a_list)):
        if result[-1] != a_list[i]:
            result.append(a_list[i])
    
    
    return result

