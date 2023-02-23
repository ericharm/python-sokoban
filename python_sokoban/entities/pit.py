import attr

from python_sokoban.color import Color
from python_sokoban.entity import Entity


@attr.s(auto_attribs=True)
class Pit(Entity):
    color: Color = Color.yellow
    character: str = "^"
