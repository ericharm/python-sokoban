import attr

from python_sokoban.color import Color
from python_sokoban.entity import Entity
from python_sokoban.point import Point


@attr.s(auto_attribs=True)
class Wall(Entity):
    location: Point = Point(0, 0)
    color: Color = Color.white
    character: str = "#"
