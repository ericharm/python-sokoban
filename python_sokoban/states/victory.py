from python_sokoban.application import Application
from python_sokoban.color import Color
from python_sokoban.state import State
from python_sokoban.tile import Tile


class Victory(State):
    def draw_tiles(self) -> list[Tile]:
        return Tile.from_string("You win", Color.cyan)

    def handle_input(self, key: str) -> None:
        del key
        Application().reset()

    def draw_cursor(self) -> None:
        return None
