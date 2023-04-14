from dataclasses import dataclass
from typing import Callable

from python_sokoban.color import Color
from python_sokoban.tile import Tile


@dataclass
class Option:
    text: str
    action: Callable


@dataclass
class OptionsList:
    options: list[Option]
    left_column_x_offset: int
    right_column_x_offset: int
    y_offset: int
    selected_option_index: int = 0

    def handle_input(self, key: str) -> None:
        if key == "KEY_UP":
            self.selected_option_index -= 1
        if key == "KEY_DOWN":
            self.selected_option_index += 1
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
        left_x_offset = self.left_column_x_offset
        right_x_offset = self.right_column_x_offset
        base_y_offset = self.y_offset

        x_offset = left_x_offset
        y_offset = base_y_offset
        tiles: list[Tile] = []
        is_left = True
        for option in self.options:
            tiles.extend(
                Tile.offset_tiles(
                    Tile.from_string(option.text, Color.white), x_offset, y_offset
                )
            )
            is_left = not is_left
            x_offset = left_x_offset if is_left else right_x_offset
            if is_left:
                y_offset += 2

        return tiles

    @property
    def max_option_index(self):
        return len(self.options) - 1

    @property
    def selected_option(self):
        return self.options[self.selected_option_index]

    @property
    def cursor_position(self):
        return (3, 3)
