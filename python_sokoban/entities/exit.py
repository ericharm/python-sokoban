import attr

from python_sokoban.application import Application
from python_sokoban.color import Color
from python_sokoban.entity import Entity
from python_sokoban.states.victory import Victory


@attr.s(auto_attribs=True)
class Exit(Entity):
    color: Color = Color.green
    character: str = "X"

    def move_by(self, x: int, y: int, level: list[Entity]) -> bool:
        Application.swap_state(Victory())
        return False
