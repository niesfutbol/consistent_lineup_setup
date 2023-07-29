class Obtainer_Played_Minutes:
    def __init__(self) -> None:
        self._events = None
        self._lineup = None

    def set_events(self, events) -> None:
        self._events = events

    def set_lineup(self, lineup) -> None:
        self._lineup = lineup
