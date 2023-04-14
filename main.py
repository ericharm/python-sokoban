import curses
from python_sokoban.application import Application
from python_sokoban.states.title import Title
from python_sokoban.tile import Tile

# from python_sokoban.tile import Tile


def main(screen: curses.window) -> None:
    _init_curses()
    application = Application()
    _reset_application()
    while application.is_running():
        if Application.resetting:
            _reset_application()
        screen.clear()
        tiles = application.current_state().draw_tiles()
        offset = Tile.centerize_tiles(tiles)
        [tile.draw(screen=screen, offset=offset) for tile in tiles]
        if application.current_state().show_cursor:
            cursor_position = application.current_state().draw_cursor()
            assert cursor_position
            x, y = cursor_position
            screen.move(x, y)
        application.current_state().handle_input(key=screen.getkey())


def _reset_application() -> None:
    while len(Application.states) > 0:
        Application.pop_state()
    Application.push_state(Title())


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


curses.wrapper(main)
