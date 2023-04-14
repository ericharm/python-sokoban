from python_sokoban.state import State


class Application:
    """
    The application class is a singleton that manages the game's states.
    """

    states: list[State] = []
    resetting = False

    @staticmethod
    def push_state(state: State) -> None:
        Application.resetting = False
        Application.states.append(state)

    @staticmethod
    def pop_state() -> None:
        Application.states.pop()

    @staticmethod
    def swap_state(state: State) -> None:
        Application.pop_state()
        Application.push_state(state)
        if len(Application.states) > 1:
            raise Exception("Application has more than one state.")

    @staticmethod
    def reset() -> None:
        Application.resetting = True

    @staticmethod
    def quit() -> None:
        Application.states = []

    @staticmethod
    def current_state() -> State:
        return Application.states[-1]

    @staticmethod
    def is_running() -> bool:
        return len(Application.states) > 0
