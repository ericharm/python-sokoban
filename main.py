import curses
from python_sokoban.application import Application
from python_sokoban.states.game import Game


def main(screen: curses.window) -> None:
    game = Game()
    application = Application()
    application.push_state(game)
    while application.is_running:
        screen.clear()
        tiles = application.current_state.draw()
        [tile.draw(screen=screen) for tile in tiles]
        application.current_state.handle_input(key=screen.getkey())


application = Application()
curses.wrapper(main)
