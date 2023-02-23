from typing import List

from python_sokoban.state import State


class Application:
    """
    The application class is a singleton that manages the game's states.
    """

    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(Application, cls).__new__(cls)
            cls.states: List[State] = []
        return cls.instance

    @staticmethod
    def get_instance():
        if Application.instance is None:
            Application.instance = Application()
        return Application.instance

    @staticmethod
    def push_state(state: State) -> None:
        Application.states.append(state)

    @staticmethod
    def swap_state(state: State) -> None:
        Application.states.pop()
        Application.push_state(state)

    @staticmethod
    def quit() -> None:
        Application.states = []

    @property
    def current_state(self) -> State:
        return self.states[-1]

    @property
    def is_running(self) -> bool:
        return len(self.states) > 0
