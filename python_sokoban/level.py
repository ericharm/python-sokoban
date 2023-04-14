from __future__ import annotations

from typing import Optional

from attr import define

from python_sokoban.entities.boulder import Boulder
from python_sokoban.entities.exit import Exit
from python_sokoban.entities.pit import Pit
from python_sokoban.entities.player import Player
from python_sokoban.entities.wall import Wall
from python_sokoban.entity import Entity
from python_sokoban.point import Point


@define
class Level:
    """
    A level is a collection of entities.
    """

    entities: list[Entity]
    player: Player

    @staticmethod
    def from_file(file_path: str) -> Level:
        entities: list[Entity] = []
        player: Optional[Player] = None
        x = 0
        y = 0

        with open(file_path, "r") as file:
            for line in file:
                for char in line:
                    if char == "\n":
                        y += 1
                        x = 0
                        continue
                    entity = _entity_from_character(char, x, y)
                    if entity:
                        if isinstance(entity, Player):
                            player = entity
                        else:
                            entities.append(entity)
                    x += 1
            assert player is not None
            return Level(entities=entities, player=player)


def _entity_from_character(char: str, x: int, y: int) -> Optional[Entity]:
    match char:
        case "@":
            return Player(location=Point(x, y))
        case "#":
            return Wall(location=Point(x, y))
        case "0":
            return Boulder(location=Point(x, y))
        case "^":
            return Pit(location=Point(x, y))
        case "X":
            return Exit(location=Point(x, y))
        case _:
            return None
