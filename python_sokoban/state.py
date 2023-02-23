from abc import ABC, abstractmethod
from typing import List

from python_sokoban.tile import Tile


class State(ABC):
    """
    A state is a layer of the application with its own rendering and input handling.
    """

    @abstractmethod
    def draw(self) -> List[Tile]:
        pass

    @abstractmethod
    def handle_input(self, key: str) -> None:
        pass
