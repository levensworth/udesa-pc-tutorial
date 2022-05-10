
from .solutions.zip_lists import zip_lists
# from .solutions.counter import counter
from .solutions.reverse_list import reverse_list
from .solutions.time_it import time_it
from .solutions.fibonacci import fibonacci, fibonacci_cached

def test_zip_equal_lists():
    list_1 = [1,2,3,4,5]
    list_2 = [6,7,8,9,10]
    
    result = zip_lists(list_1, list_2)
    assert len(result) == len(list_1), 'missing elements'
    assert result[0] == (1, 6)
    assert result[-1] == (5, 10)


def test_reverse_lists():
    example_list = [1,2,3,4]
    result = reverse_list(example_list)
    assert example_list == result, 'the list is different, you need to modify the original'
    assert len(example_list) == len(result)
    assert example_list[0] == 4


def test_fibnacci_time_comparison():
    epochs = 10000
    number  = 1000
    def test_fibo_exec(number):
        for _ in range(epochs):
            fibonacci(number)

    def test_fibo_cache_exec(number , cache):
        for _ in range(epochs):
            fibonacci_cached(number, cache)

    time_no_cache = time_it(test_fibo_exec, number)
    print(f'the process took: {time_no_cache} micro sec.')


    time_cache = time_it(test_fibo_cache_exec, number, {})
    print(f'the process took: {time_cache} micro sec.')
    raise ValueError