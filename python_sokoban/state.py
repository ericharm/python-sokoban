import curses
from abc import ABC, abstractmethod
from typing import Optional, Tuple

from attr import define

from python_sokoban.tile import Tile


@define(auto_attribs=True)
class State(ABC):
    """
    A state is a layer of the application with its own rendering and input handling.
    """

    show_cursor: bool = False

    def __attrs_post_init__(self) -> None:
        if self.show_cursor:
            curses.curs_set(1)
        else:
            curses.curs_set(0)

    @abstractmethod
    def draw_tiles(self) -> list[Tile]:
        pass

    @abstractmethod
    def draw_cursor(self) -> Optional[Tuple[int, int]]:
        pass

    @abstractmethod
    def handle_input(self, key: str) -> None:
        pass
