import attr

from python_sokoban.color import Color
from python_sokoban.entities.pit import Pit
from python_sokoban.entity import Entity
from python_sokoban.point import Point


@attr.s(auto_attribs=True)
class Boulder(Entity):
    location: Point = Point(0, 0)
    color: Color = Color.cyan
    character: str = "0"
    movable: bool = True

    def collide(self, x: int, y: int, entity: Entity, level: list[Entity]) -> bool:
        if isinstance(entity, Pit):
            level.remove(self)
            level.remove(entity)
            return True
        return False
