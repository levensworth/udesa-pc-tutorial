
from argparse import ArgumentError
from typing import Dict

def fibonacci(n: int) -> int:
    if n < 1:
        raise ArgumentError(None, message='n should be greater than 0')
    
    if n in (1, 2):
        return 1
    
    current = 1
    fibo_1_prev = 1
    
    for _ in range(n, 2, -1):
        new_current =  current + fibo_1_prev
        fibo_1_prev = current
        current = new_current
    return current



def fibonacci_cached(n: int, cache: Dict) -> int:
    if n not in cache:
        cache[n] = fibonacci(n)
    
    return cache[n]



    
    
    
        


