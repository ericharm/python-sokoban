from __future__ import annotations

import curses

import attr

from python_sokoban.color import Color
from python_sokoban.point import Point


@attr.s(auto_attribs=True)
class Tile:
    """
    A tile is a single character that can be rendered to the screen.
    """

    color: Color
    character: str
    location: Point = Point(0, 0)

    @staticmethod
    def from_string(string: str, color: Color = Color.white) -> list[Tile]:
        x = 0
        y = 0
        tiles = []
        for char in string:
            if char == "\n":
                y += 1
                x = 0
                continue
            tile = Tile(location=Point(x, y), color=color, character=char)
            tiles.append(tile)
            x += 1
        return tiles

    @staticmethod
    def offset_tiles(tiles: list[Tile], x: int, y: int) -> list[Tile]:
        return [
            Tile(
                location=tile.location + Point(x, y),
                color=tile.color,
                character=tile.character,
            )
            for tile in tiles
        ]

    @staticmethod
    def centerize_tiles(tiles: list[Tile]) -> Point:
        max_x = max(tile.location.x for tile in tiles)
        max_y = max(tile.location.y for tile in tiles)
        screen_width = curses.COLS
        screen_height = curses.LINES
        offset_x = int((screen_width - max_x) / 2)
        offset_y = int((screen_height - max_y) / 2)
        return Point(offset_x, offset_y)

    def draw(self, screen: curses.window, offset: Point) -> None:
        screen.addch(
            self.location.y + offset.y,
            self.location.x + offset.x,
            self.character,
            curses.color_pair(self.color.value),
        )

    @property
    def x(self) -> int:
        return self.location.x

    @property
    def y(self) -> int:
        return self.location.y
