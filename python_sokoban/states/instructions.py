from python_sokoban.application import Application
from python_sokoban.color import Color
from python_sokoban.state import State
from python_sokoban.tile import Tile


class Instructions(State):
    def draw_tiles(self) -> list[Tile]:
        return _instructions_tiles()

    def draw_cursor(self) -> None:
        pass

    def handle_input(self, key: str) -> None:
        if key == "\n":
            Application.reset()


def _read_instructions() -> list[str]:
    with open("data/instructions.txt", "r") as file:
        return file.readlines()


def _instructions_tiles() -> list[Tile]:
    instructions = "".join(_read_instructions())
    return Tile.from_string(instructions, Color.yellow)
