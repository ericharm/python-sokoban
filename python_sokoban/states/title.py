from attr import define

from python_sokoban.application import Application
from python_sokoban.color import Color
from python_sokoban.options_list import Option, OptionsList
from python_sokoban.point import Point
from python_sokoban.state import State
from python_sokoban.states.instructions import Instructions
from python_sokoban.states.stage_select import StageSelect
from python_sokoban.tile import Tile

_options = OptionsList(
    options=[
        Option(text="Play", action=lambda: Application.swap_state(StageSelect())),
        Option(
            text="Instructions", action=lambda: Application.swap_state(Instructions())
        ),
        Option(text="Quit", action=lambda: Application.quit()),
    ],
    column_offsets=[0],
    y_offset=3,
)


@define(auto_attribs=True)
class Title(State):
    show_cursor: bool = True

    def draw_tiles(self) -> list[Tile]:
        return _title_tiles() + _options.draw()

    def draw_cursor(self) -> Point:
        x, y = _options.cursor_position
        heading_height = 1
        y += heading_height
        return Point(x, y)

    def handle_input(self, key: str) -> None:
        _options.handle_input(key)


def _title_tiles() -> list[Tile]:
    title = Tile.from_string("Title Screen", Color.magenta)
    return Tile.offset_tiles(title, 0, -5)
