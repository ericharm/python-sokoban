import attr

from python_sokoban.color import Color
from python_sokoban.entity import Entity


@attr.s(auto_attribs=True)
class Player(Entity):
    color: Color = Color.magenta
    character: str = "@"
    movable: bool = True

    def collide(self, x: int, y: int, entity: Entity, level: list[Entity]) -> bool:
        if entity.move_by(x, y, level):
            self.move_to(self.location.x + x, self.location.y + y)
            return True
        return False
