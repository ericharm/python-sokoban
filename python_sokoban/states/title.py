from typing import List

from python_sokoban.application import Application
from python_sokoban.color import Color
from python_sokoban.state import State
from python_sokoban.tile import Tile


class Title(State):
    def draw(self) -> List[Tile]:
        return Tile.from_string("Title \nScreen", Color.cyan)

    def handle_input(self, key: str) -> None:
        if key == "q":
            Application().states.pop()
