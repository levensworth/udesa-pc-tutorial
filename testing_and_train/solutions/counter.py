
from typing import List


def counter(text: str) -> List:
    counter_dict = {}
    for word in text.split():
        counter_dict[word.lower()] = counter_dict.get(word.lower(), 0)+ 1
    
    return list(counter_dict.items())
