import curses
from typing import cast

from attr import define

from python_sokoban.application import Application
from python_sokoban.entity import Entity
from python_sokoban.level import Level
from python_sokoban.state import State
from python_sokoban.tile import Tile


@define(auto_attribs=True)
class Game(State):
    level: Level
    show_cursor: bool = False

    def draw_tiles(self, _: curses.window) -> list[Tile]:
        return [cast(Tile, tile) for tile in self.tiles]

    def handle_input(self, key: str) -> None:
        match key:
            case "KEY_UP":
                self.level.player.move_by(0, -1, self.entities)
            case "KEY_DOWN":
                self.level.player.move_by(0, 1, self.entities)
            case "KEY_LEFT":
                self.level.player.move_by(-1, 0, self.entities)
            case "KEY_RIGHT":
                self.level.player.move_by(1, 0, self.entities)
            case "q":
                Application.quit()

    @property
    def tiles(self) -> list[Entity]:
        tiles = self.level.entities.copy()
        tiles.append(self.level.player)
        return tiles

    @property
    def entities(self) -> list[Entity]:
        return self.level.entities
