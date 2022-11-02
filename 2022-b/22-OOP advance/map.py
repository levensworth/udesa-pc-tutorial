from copy import copy
from typing import List, Set, Tuple
from random import random




class Map:

    EMPTY_BLOCK = chr(9618)
    BLOCKED_BLOCK = chr(9608)

    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height
        self.__obstacle_prob = 0.2
        self.__matrix = self._create_render(width=width, height=height)


    def _create_render(self, width: int, height: int) -> List[List[str]]:
        render = []
        
        for row in range(height):
            new_row = []
            for col in range(width):
                block = Map.EMPTY_BLOCK if random() > 0.2 else Map.BLOCKED_BLOCK
                new_row.append(block)
            render.append(new_row)
        
        return render


    def create_string_display(self,) -> str:
        
        str_map = ''
        
        for row in self.__matrix:
            str_row = ''.join(row)
            str_row += '\n'
            str_map += str_row

        return str_map


    def get_dim(self) -> Tuple[int, int]:
        return (self.__height, self.__width)

    def get_prob(self) -> float:
        return self.__obstacle_prob

    def get_map(self) -> List[List[int]]:
        return self.__matrix

    def render(self) -> None:
        print(self.create_string_display())

    def __str__(self) -> str:
        return '[Map] This class contains the representation for a given map.'

    def __repr__(self) -> str:
        return f'[Map Instance] of {self.get_dim()} with prob: {self.get_prob()} for obstacles'
    

    

    
      
            
        


map = Map(4, 4)

print(map.create_string_display())




