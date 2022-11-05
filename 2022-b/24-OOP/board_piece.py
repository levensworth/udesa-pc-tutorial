from typing import Tuple, Union

from creatures_interface import Creature


class Block:
    EMPTY_BLOCK = chr(9618)
    BLOCKED_BLOCK = chr(9608)

    def __init__(self, loc: Tuple[int, int], is_wall: bool):
        self.__is_wall = is_wall
        self._img = self.BLOCKED_BLOCK if is_wall else self.EMPTY_BLOCK
        self.__loc = loc

    def get_loc(self) -> Tuple[int, int]:
        return self.__loc

    def is_free(self) -> bool:
        return not self.__is_wall

    def __str__(self):
        return self._img


class Goal(Block):
    def __init__(self, loc: Tuple[int, int]):
        super().__init__(loc=loc, is_wall=False)
        self._img = chr(128682)


class Item(Block):
    def use_against(self, object: Union[Block, Creature]):
        raise NotImplementedError("You need to implement this method")


class Pickaxe(Item):
    def __init__(self, loc: Tuple[int, int]):
        super().__init__(loc=loc, is_wall=False)
        self._img = chr(9935)
