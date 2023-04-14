from attr import define

from python_sokoban.application import Application
from python_sokoban.color import Color
from python_sokoban.level import Level
from python_sokoban.options_list import Option, OptionsList
from python_sokoban.point import Point
from python_sokoban.state import State
from python_sokoban.states.game import Game
from python_sokoban.tile import Tile


def select_level(file_name: str) -> None:
    Application.swap_state(Game(Level.from_file(file_name)))


options = [
    Option(text="Level 1", action=lambda: select_level("data/1.lvl")),
    Option(text="Level 2", action=lambda: select_level("data/2.lvl")),
    Option(text="Level 3", action=lambda: select_level("data/3.lvl")),
    Option(text="Level 4", action=lambda: select_level("data/4.lvl")),
    Option(text="Level 5", action=lambda: select_level("data/5.lvl")),
    Option(text="Level 6", action=lambda: select_level("data/6.lvl")),
    Option(text="Level 7", action=lambda: select_level("data/7.lvl")),
    Option(text="Level 8", action=lambda: select_level("data/8.lvl")),
]

stage_select_options = OptionsList(
    options=options,
    left_column_x_offset=-3,
    right_column_x_offset=8,
    y_offset=3,
)


@define(auto_attribs=True)
class StageSelect(State):
    show_cursor: bool = True

    def draw_tiles(self) -> list[Tile]:
        return self._get_heading() + stage_select_options.draw()

    def draw_cursor(self) -> Point:
        x, y = stage_select_options.cursor_position
        heading_height = 1
        y += heading_height
        return Point(x, y)

    def handle_input(self, key: str) -> None:
        stage_select_options.handle_input(key)

    def _get_heading(self) -> list[Tile]:
        return Tile.from_string("Stage Select", Color.cyan)
