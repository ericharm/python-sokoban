from __future__ import annotations

import curses
from typing import List

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
    def from_string(string: str, color: Color = Color.white) -> List[Tile]:
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

    def draw(self, screen: curses.window) -> None:
        screen.addch(
            self.location.y,
            self.location.x,
            self.character,
            curses.color_pair(self.color.value),
        )
