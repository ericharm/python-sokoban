from typing import Optional, cast

from attr import define

from python_sokoban.application import Application
from python_sokoban.entities.player import Player
from python_sokoban.entity import Entity
from python_sokoban.level import Level
from python_sokoban.state import State
from python_sokoban.tile import Tile


@define(auto_attribs=True)
class Game(State):
    level: Optional[Level] = None

    def draw_tiles(self) -> list[Tile]:
        return [cast(Tile, tile) for tile in self.tiles]

    def draw_cursor(self) -> None:
        pass

    def handle_input(self, key: str) -> None:
        match key:
            case "KEY_UP":
                self.player.move_by(0, -1, self.entities)
            case "KEY_DOWN":
                self.player.move_by(0, 1, self.entities)
            case "KEY_LEFT":
                self.player.move_by(-1, 0, self.entities)
            case "KEY_RIGHT":
                self.player.move_by(1, 0, self.entities)
            case "q":
                Application.quit()

    @property
    def assert_level(self) -> Level:
        assert self.level
        return self.level

    @property
    def tiles(self) -> list[Entity]:
        tiles = self.assert_level.entities.copy()
        tiles.append(self.assert_level.player)
        return tiles

    @property
    def entities(self) -> list[Entity]:
        return self.assert_level.entities

    @property
    def player(self) -> Player:
        return self.assert_level.player
