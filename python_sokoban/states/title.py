import curses

from attr import define

from python_sokoban.application import Application
from python_sokoban.color import Color
from python_sokoban.state import State
from python_sokoban.states.stage_select import StageSelect
from python_sokoban.tile import Tile


@define(auto_attribs=True)
class Title(State):
    def draw_tiles(self, _: curses.window) -> list[Tile]:
        tiles = _title_tiles()
        tiles.extend(_option_tiles())
        return tiles

    def handle_input(self, key: str) -> None:
        del key
        Application.swap_state(StageSelect())

    def draw_cursor(self) -> None:
        pass


def _title_tiles() -> list[Tile]:
    title = Tile.from_string("Title Screen", Color.magenta)
    return Tile.offset_tiles(title, 0, -5)


def _option_tiles() -> list[Tile]:
    option = Tile.from_string("Press any key to continue", Color.white)
    return Tile.offset_tiles(option, 0, 5)
