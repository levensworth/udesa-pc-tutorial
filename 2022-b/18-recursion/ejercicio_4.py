

from typing import List


def min_rec(a_list: List[int]) -> int:
    if len(a_list) == 0:
        return None

    if len(a_list) == 1:
        return a_list[0]

    if len(a_list) == 2:
        return a_list[0] if a_list[0] < a_list[1] else a_list[1]

    middle = len(a_list) // 2
    min_1 = min_rec(a_list=a_list[:middle])
    min_2 = min_rec(a_list=a_list[middle:])
    
    return min_1 if min_1 < min_2 else min_2


print(min_rec([1,2,3,4,55,78,8,453,332, -12]))

