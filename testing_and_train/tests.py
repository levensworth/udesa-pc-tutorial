from .solutions.zip_lists import zip_lists
from .solutions.counter import counter


def test_zip_equal_lists():
    list_1 = [1,2,3,4,5]
    list_2 = [6,7,8,9,10]
    
    result = zip_lists(list_1, list_2)
    assert len(result) == len(list_1), 'missing elements'
    assert result[0] == (1, 6)
    assert result[-1] == (5, 10)

    

