from __future__ import annotations

from random import choice
from typing import Dict, List, Tuple, Union

from board_piece import Block, Item
from creatures_interface import Creature


class Walker(Creature):
    def __init__(self, img: str, n_steps: int) -> None:
        super().__init__(img)
        self.__step_counter = n_steps
        self.__toosl: List[Item] = []

    def set_loc(self, new_loc: Tuple[int, int]) -> None:
        if self.__step_counter <= 0:
            raise ValueError("Walker out of steps!")

        self.__step_counter -= 1
        return super().set_loc(new_loc)

    def get_alive(self) -> bool:
        return self.__step_counter > 0

    def get_steps(self) -> int:
        return self.__step_counter

    def get_move(
        self, user_intention: str, directions: Dict[str, Tuple[int, int]]
    ) -> Tuple[int, int]:
        direction = directions[user_intention]
        current_loc = self.get_loc()
        new_loc = (current_loc[0] + direction[0], current_loc[1] + direction[1])
        return new_loc


class Goblin(Creature):
    def __init__(self, init_pos: Tuple[int, int]) -> None:
        super().__init__(img='G')
        self.set_loc(init_pos)
        self.is_alive = True

    def get_pos(self, possible_moves: List[str]) -> str:
        delta = choice(possible_moves)
        return delta

    def get_move(self, directions: Dict[str, Tuple[int, int]]) -> Tuple[int, int]:
        if not self.is_alive:
            raise ValueError()

        position = self.get_loc()

        delta = directions[self.get_pos(list(directions.keys()))]

        new_position = (position[0] + delta[0], position[1] + delta[1])

        return new_position

    def react_to_move(
        self, is_position_free: bool, new_position: Tuple[int, int]
    ) -> Union[Block, Goblin]:
        if is_position_free:
            return self

        self.is_alive = False
        return Block(self.get_loc(), is_wall=True)
