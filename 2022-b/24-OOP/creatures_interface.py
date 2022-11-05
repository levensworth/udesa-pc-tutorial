from typing import Tuple


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

    def __str__(self) -> str:
        return self.get_image()
