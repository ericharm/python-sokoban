from typing import List, cast

from python_sokoban.application import Application
from python_sokoban.entity import Entity
from python_sokoban.level import Level
from python_sokoban.state import State
from python_sokoban.tile import Tile


class Game(State):
    level = Level.from_file("data/1.lvl")

    def draw(self) -> List[Tile]:
        return [cast(Tile, tile) for tile in self.tiles]

    def handle_input(self, key: str) -> None:
        if key == "q":
            Application().states.pop()

    @property
    def tiles(self) -> List[Entity]:
        tiles = self.level.entities.copy()
        tiles.append(self.level.player)
        return tiles
