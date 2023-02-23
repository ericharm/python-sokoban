import curses
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
            _init_curses()
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

    @property
    def current_state(self) -> State:
        return self.states[-1]

    @property
    def is_running(self) -> bool:
        return len(self.states) > 0


def _init_curses() -> None:
    curses.initscr()
    curses.start_color()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(8, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.noecho()
    curses.cbreak()
