from random import random
from typing import Dict, List, Tuple, Union

from board_piece import Block, Goal
from creatures_interface import Creature


class Map:

    MOVES: Dict[str, Tuple[int, int]] = {
        "a": (0, -1),
        "d": (0, 1),
        "s": (1, 0),
        "w": (-1, 0),
    }

    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height
        self.__obstacle_prob = 0.2
        self.__matrix: List[List[Union[Block, Creature]]] = self._create_render(width=width, height=height)  # type: ignore

    def _create_render(self, width: int, height: int) -> List[List[Block]]:
        render = []

        for row in range(height):
            new_row = []
            for col in range(width):
                is_wall = random() < self.__obstacle_prob
                block = Block((row, col), is_wall=is_wall)
                new_row.append(block)
            render.append(new_row)

        return render

    def create_string_display(self, matrix: List[List[str]]) -> str:

        str_map = ""

        for row in matrix:
            str_row = [str(i) for i in row]
            str_row = "".join(str_row)
            str_row += "\n"
            str_map += str_row

        return str_map

    def render_state(self, items: Dict[Tuple[int, int], Block]) -> str:
        actual_board = []

        for row in range(self.__width):
            current_row = []
            for col in range(self.__height):
                default_obj = self.__matrix[row][col]
                obj = items.get((row, col), default_obj)
                current_row.append(str(obj))
            actual_board.append(current_row)

        return self.create_string_display(actual_board)

    def get_dim(self) -> Tuple[int, int]:
        return (self.__height, self.__width)

    def get_prob(self) -> float:
        return self.__obstacle_prob

    def check_limits(self, loc: Tuple[int, int]) -> bool:
        is_width_contained = -1 < loc[0] < self.__width
        is_height_contained = -1 < loc[1] < self.__height

        return is_width_contained and is_height_contained

    def is_free(self, loc: Tuple[int, int]) -> bool:

        aux = self.__matrix[loc[0]][loc[1]]
        if isinstance(aux, Block):
            return aux.is_free()

        # then it's some kind of creature
        return False

    def get_locations(self, filter_by: str) -> List[Tuple[int, int]]:
        """
        Given a filter, return the list of locations within the map that
        contain the item.

        Args:
        filter_by: (str) the item to search for [EMPTY_BLOCK, BLOCKED_BLOCK, GOAL]

        returns:
        a list with the tuples (positions) in which the items was found.
        """

        result = []
        for row in range(self.__width):
            for col in range(self.__height):
                if str(self.__matrix[row][col]) == filter_by:
                    result.append((row, col))
        return result

    def move_entity(
        self, entity: Union[Block, Creature], new_position: Tuple[int, int]
    ) -> Tuple[int, int]:

        if isinstance(entity, Block):
            return self.move_object(object=entity)
        if isinstance(entity, Creature):
            return self.move_creature(creature=entity, new_position=new_position)

        raise ValueError(f"Unknown entity {entity}")

    def move_creature(
        self, creature: Creature, new_position: Tuple[int, int]
    ) -> Tuple[int, int]:
        self.__matrix[new_position[0]][new_position[1]] = creature
        creature.set_loc(new_position)

        return new_position

    def move_object(self, object: Block) -> Tuple[int, int]:
        new_position = object.get_loc()
        self.__matrix[new_position[0]][new_position[1]] = object
        return new_position

    def is_goal(self, loc: Tuple[int, int]) -> bool:
        return isinstance(self.__matrix[loc[0]][loc[1]], Goal)

    def __str__(self) -> str:
        return "[Map] This class contains the representation for a given map."

    def __repr__(self) -> str:
        return f"[Map Instance] of {self.get_dim()} with prob: {self.get_prob()} for obstacles"
