
from typing import List


def abs_dif(a_list: List[float]) -> float:
    if len(a_list) <= 1:
        return 0.0
    
    max_dif = -1.0 # simple init
    for i in range(len(a_list) -1):
        current_dif = abs(a_list[i] - a_list[i+1])
        max_dif = max(max_dif, current_dif)
        
    return max_dif


    

