from typing import Tuple
from random import choice

class Creature:
    
    def __init__(self, img: str) -> None:
        self._loc = (0, 0)
        self._image = img

    def get_loc(self) -> Tuple[int, int]:
        return self._loc
        
    def set_loc(self, new_loc: Tuple[int, int]) -> None:
        self._loc = new_loc

    def get_image(self) -> str:
        return self._image


class Walker(Creature):
    def __init__(self, img: str, n_steps: int) -> None:
        super().__init__(img)
        self.__step_counter = n_steps

    def set_loc(self, new_loc: Tuple[int, int]) -> None:
        if self.__step_counter <= 0:
            raise ValueError('Walker out of steps!')    
        
        self.__step_counter -= 1
        return super().set_loc(new_loc)

    def get_alive(self) -> bool:
        return self.__step_counter > 0
        


class Goblin(Creature):
    def __init__(self, ) -> None:
        super().__init__(img='G')


    def get_pos(self) -> Tuple[int, int]:
        moves = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0),
        ]
        
        delta =  choice(moves)
        current = self.get_loc()
        return (current[0] + delta[0], current[1] + delta[1])
    
    
        

    
    




