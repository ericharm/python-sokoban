import attr

from python_sokoban.color import Color
from python_sokoban.point import Point
from python_sokoban.tile import Tile


@attr.s(auto_attribs=True)
class Entity(Tile):
    color: Color
    character: str
    location: Point = Point(0, 0)

    def move_by(self, x: int, y: int) -> None:
        self.location = Point(self.location.x + x, self.location.y + y)
