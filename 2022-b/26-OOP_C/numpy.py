from __future__ import annotations
from typing import Union, Tuple, List, Iterable

class MyArray:
    def __init__(self, array: Union[List, Tuple]) -> None:
        self.__array = self._generate_array(array, self._get_array_type(array))
        self.__size = len(array)

    def _get_array_type(self, array: Union[List, Tuple]):
        
        array_type = bool
        for elem in array:
            if type(elem) == float:
                array_type = float
            if type(elem) == int and array_type == bool:
                array_type = int
            
        return array_type


    def _generate_array(self, data: Union[List, Tuple], data_type) -> List:
        array = []
         
        for elem in data:
            array.append(data_type(elem))

        return array


    def __getitem__(self, idx):
        
        return self.__array[idx]

    def __setitem__(self, idx, value):
        
        self.__array[idx] = value

    def __len__(self)-> int:
        return self.__size

    def __radd__(self, other) -> MyArray:
        return self + other

    def __rmul__(self, other) -> MyArray:
        return self * other

    def __add__(self, other) -> MyArray:
        if isinstance(other, int):
            return self._scalar_add(other)
        
        if self.__size != other.__size:
            raise ValueError('The size of each array does not match!')

        result = []

        for i in range(len(other)):
            result.append(self[i] + other[i])
        return MyArray(result)

    def __sub__(self, other) -> MyArray:
        if isinstance(other, int):
            return self._scalar_add(-other)

        if self.__size != other.__size:
            raise ValueError('The size of each array does not match!')

        result = []

        for i in range(len(other)):
            result.append(self[i] - other[i])
        return MyArray(result)

    
    def __mul__(self, other)-> MyArray:
        if isinstance(other, int):
            return self._scalar_mult(other)

        if self.__size != other.__size:
            raise ValueError('The size of each array does not match!')

        result = []        
        for i in range(len(other)):
            result.append(self[i] * other[i])
        return MyArray(result)

    
    def __pow__(self, other)-> MyArray:
        if isinstance(other, int):
            return self._scalar_pow(other)

        if self.__size != other.__size:
            raise ValueError('The size of each array does not match!')

        result = []        
        for i in range(len(other)):
            result.append(self[i] ** other[i])
        return MyArray(result)

    def _scalar_mult(self, scalar: Union[int, float]) -> MyArray:
        
        array = []
        for elem in self.__array:
            array.append(elem * scalar)
        
        return MyArray(array)

    def _scalar_pow(self, scalar: int) -> MyArray:
        result = self
        for i in range(scalar):
            result = result ** self
        return result    

    def _scalar_add(self, scalar: Union[int, float, bool]) -> MyArray:
        result = []
        for elem in self.__array:
            result.append(elem + scalar)

        return MyArray(result)

    def __str__(self) -> str:
        return str(self.__array)

    def dot(self, other) -> MyArray:
        if self.__size != other.__size:
            raise ValueError('The size of each array does not match!')

        result = 0
        for i in range(len(other)):
            result += self[i] * other[i]
        return MyArray([result])

    @staticmethod
    def linspace(start: float, end: float, length: float) -> MyArray:
        
        array = []
        
        value = start
        delta = (end - start)/length
        while value <= end:
            array.append(value)
            value = value + delta
        
        return MyArray(array)
        

        
    
v1 = MyArray([1,3.0,5])
v2 = MyArray([2.2,4,6])
v3 = v1+v2
v4 = v1*v2
e = v1.dot(v2)
n = MyArray.linspace(0,9,10)
f1 = n*2 + 5
f2 = 2*n**2 + 3*n + 1

print(f1)
print(f2)



    
    
                

            
        
