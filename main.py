import curses
from python_sokoban.application import Application
from python_sokoban.states.game import Game

# from python_sokoban.states.title import Title


def main(screen: curses.window) -> None:
    # title_screen = Title()
    game = Game()
    application = Application()
    application.push_state(game)
    while application.is_running:
        tiles = application.current_state.draw()
        [tile.draw(screen=screen) for tile in tiles]
        application.current_state.handle_input(key=screen.getkey())


application = Application()
curses.wrapper(main)
