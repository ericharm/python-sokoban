from __future__ import annotations

from typing import Optional

import attr

from python_sokoban.color import Color
from python_sokoban.point import Point
from python_sokoban.tile import Tile


@attr.s(auto_attribs=True)
class Entity(Tile):
    """
    An entity is a tile that can be moved around.
    """

    color: Color
    character: str
    location: Point = Point(0, 0)
    movable: bool = False

    def move_by(self, x: int, y: int, level: list[Entity]) -> bool:
        if not self.movable:
            return False
        next_location = Point(self.location.x + x, self.location.y + y)
        entity = _entity_at_point(level, next_location.x, next_location.y)
        if entity is None:
            self.move_to(next_location.x, next_location.y)
            return True
        else:
            return self.collide(x, y, entity, level)

    def move_to(self, x: int, y: int) -> None:
        self.location = Point(x, y)

    def collide(self, x: int, y: int, entity: Entity, level: list[Entity]) -> bool:
        del x, y, entity, level
        return False


def _entity_at_point(entities: list[Entity], x: int, y: int) -> Optional[Entity]:
    """
    Return an entity if there is one at point (x, y).
    """
    for entity in entities:
        if entity.location == Point(x, y):
            return entity
    return None
