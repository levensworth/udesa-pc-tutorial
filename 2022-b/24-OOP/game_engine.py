from random import choice, sample
from typing import Dict, List, Tuple

from board_piece import Block, Goal, Item, Pickaxe
from creatures import Goblin, Walker
from map import Map


class GameEngine:
    AMOUNT_OF_MONSTERS = 5

    def __init__(self, board: Map, player: Walker) -> None:
        self.__board = board
        self.__player = player
        self.__board.move_entity(player, player.get_loc())

        self.__goal = self._create_goal()
        self.__items = self._create_items()

        self.__monsters: List[Goblin] = self.__create_monsters(
            amount=self.AMOUNT_OF_MONSTERS
        )

    def _create_goal(self) -> Goal:
        goal_pos = list(self.__board.get_dim())
        goal_pos[0] -= 1
        goal_pos[1] -= 1
        return Goal(tuple(goal_pos))

    def _create_items(self) -> List[Item]:
        free_locs = self.__board.get_locations(filter_by=Block.EMPTY_BLOCK)
        loc = choice(free_locs)
        return [Pickaxe(loc)]

    def __create_monsters(self, amount: int) -> List[Goblin]:
        # get empty locations
        empty_places = self.__board.get_locations(filter_by=Block.EMPTY_BLOCK)

        monsters = [Goblin(init_pos=loc) for loc in sample(empty_places, k=amount)]
        for monster in monsters:
            self.__board.move_creature(monster, monster.get_loc())

        return monsters

    def show_state(self):
        print(self.__board.render_state(self._get_entities()))

    def player_won(self) -> bool:
        return self.__player.get_loc() == self.__goal.get_loc()

    def player_dead(self) -> bool:
        return not self.__player.get_alive()

    def compute_state(self, user_selection: str):

        self._move_monsters()

        self._move_player(user_selection)

        print(self.__board.render_state(self._get_entities()))
        print(
            f"Moves left: {self.__player.get_steps()} | Char: {self.__player.get_image()}"
        )

    def _move_monsters(self) -> None:
        alived_monsters = [mons for mons in self.__monsters if mons.is_alive]
        for monster in alived_monsters:
            self._move_monster(monster)

    def _move_player(self, user_selection: str) -> None:
        possible_position = self.__player.get_move(
            user_intention=user_selection, directions=self.__board.MOVES
        )

        if not self.__board.check_limits(possible_position):
            new_position = self.__player.get_loc()
        elif self.__board.is_free(possible_position) or self.__board.is_goal(
            possible_position
        ):
            new_position = possible_position
        else:
            new_position = self.__player.get_loc()

        self.__board.move_object(Block(self.__player.get_loc(), is_wall=False))
        self.__board.move_entity(self.__player, new_position)

    def _move_monster(self, monster: Goblin) -> None:

        new_position = monster.get_move(self.__board.MOVES)
        is_valid_position = self.__board.check_limits(
            new_position
        ) and self.__board.is_free(new_position)
        if not is_valid_position:
            pass
        reaction = monster.react_to_move(is_valid_position, new_position)
        self.__board.move_object(Block(monster.get_loc(), is_wall=False))
        self.__board.move_entity(reaction, new_position=new_position)

    def _get_entities(self) -> Dict[Tuple[int, int], Block]:
        entities: Dict[Tuple[int, int], Block] = {e.get_loc(): e for e in self.__items}
        entities[self.__goal.get_loc()] = self.__goal
        return entities