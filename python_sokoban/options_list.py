from dataclasses import dataclass
from typing import Callable

from python_sokoban.color import Color
from python_sokoban.point import Point
from python_sokoban.tile import Tile

SELECTED_OPTION_CURSOR_GUTTER = 2
Y_SPACING = 2


@dataclass
class Option:
    text: str
    action: Callable


@dataclass
class OptionsList:
    options: list[Option]
    column_offsets: list[int]
    y_offset: int
    selected_option_index: int = 0

    def handle_input(self, key: str) -> None:
        if key == "KEY_UP":
            self.selected_option_index -= 2
        if key == "KEY_DOWN":
            self.selected_option_index += 2
        if key == "KEY_LEFT":
            self.selected_option_index -= 1
        if key == "KEY_RIGHT":
            self.selected_option_index += 1

        if self.selected_option_index < 0:
            self.selected_option_index = self.max_option_index
        if self.selected_option_index > self.max_option_index:
            self.selected_option_index = 0

        if key == "\n":
            self.selected_option.action()

    def draw(self) -> list[Tile]:
        base_y_offset = self.y_offset
        column_index = 0
        x_offset = self.column_offsets[column_index]
        y_offset = base_y_offset

        tiles: list[Tile] = []
        for option in self.options:
            tiles.extend(
                Tile.offset_tiles(
                    Tile.from_string(option.text, Color.white), x_offset, y_offset
                )
            )
            column_index = (column_index + 1) % self.column_count
            x_offset = self.column_offsets[column_index]
            if column_index == 0:
                y_offset += Y_SPACING

        return tiles

    @property
    def max_option_index(self) -> int:
        return len(self.options) - 1

    @property
    def selected_option(self) -> Option:
        return self.options[self.selected_option_index]

    @property
    def column_count(self) -> int:
        return len(self.column_offsets)

    @property
    def max_column_index(self) -> int:
        return self.column_count - 1

    @property
    def cursor_position(self) -> Point:
        column_index = self.selected_option_index % self.column_count
        x = self.column_offsets[column_index]
        x -= SELECTED_OPTION_CURSOR_GUTTER
        y = Y_SPACING + int(self.selected_option_index / self.column_count) * Y_SPACING
        return Point(x, y)
