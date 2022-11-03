from typing import TYPE_CHECKING, List, Tuple
from random import random, choice
import os
import getch
from creatures import Walker



class Map:

    EMPTY_BLOCK = chr(9618)
    BLOCKED_BLOCK = chr(9608)
    GOAL = 'X'

    MOVES = {
        'a': (0, -1),
        'd': (0, 1),
        's': (1, 0),
        'w': (-1, 0),
    }

    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height
        self.__obstacle_prob = 0.2
        self.__matrix = self._create_render(width=width, height=height)

        self.__matrix[-1][-1] = self.GOAL


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
    

    # ============== new ================

    def check_limits(self, loc: Tuple[int, int]) -> bool:
        is_width_contained = -1 < loc[0] < self.__width 
        is_height_contained = -1 < loc[1] < self.__height 

        return is_width_contained and is_height_contained

    def is_free(self, loc: Tuple[int, int]) -> bool:
        
        return self.__matrix[loc[0]][loc[1]] in (self.EMPTY_BLOCK, self.GOAL)

    def move_walker(self, walker: Walker, keyboard: str) -> Tuple[int, int]:
        
        current_loc = walker.get_loc()
        delta = self.MOVES.get(keyboard, (0, 0))
        new_loc = (current_loc[0] + delta[0], current_loc[1] + delta[1])
        if self.check_limits(new_loc) and self.is_free(new_loc):
            walker.set_loc(new_loc)
        else:
            new_loc = current_loc

        return new_loc

    def render_walker(self, walker: Walker, keyboard: str) -> None:
        position = walker.get_loc()
        # set current position as empty
        self.__matrix[position[0]][position[1]] = self.EMPTY_BLOCK
        
        position = self.move_walker(walker, keyboard)
        # set new location with walker image
        self.__matrix[position[0]][position[1]] = walker.get_image()

        disp = self.create_string_display()

        print(disp)

    
    def has_reach_goal(self, walker: Walker) -> bool:
        return walker.get_loc() == (self.__height-1, self.__width-1)


def main():
    
    map = Map(10, 10)
    walker =  Walker('W', 30)
    
    map.render_walker(walker, 'q')
    keyboard = getch.getch()
    while keyboard != 'q':
        os.system('clear') # clears screen
        try:
            map.render_walker(walker, keyboard)
        except ValueError:
            print('You are out of steps! better luck!')
            exit()
        if map.has_reach_goal(walker):
            print('YOU WON!')
            exit()
        keyboard = getch.getch()
        


if __name__ == '__main__':
    main()
