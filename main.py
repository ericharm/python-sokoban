import curses
from python_sokoban.application import Application
from python_sokoban.states.game import Game


def main(screen: curses.window) -> None:
    _init_curses()
    game = Game()
    application = Application()
    application.push_state(game)
    while application.is_running:
        screen.clear()
        tiles = application.current_state.draw()
        [tile.draw(screen=screen) for tile in tiles]
        application.current_state.handle_input(key=screen.getkey())


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


application = Application()
curses.wrapper(main)
