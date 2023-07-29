from consistent_lineup_setup import obtain_played_minutes_from_lineup


class Obtainer_Played_Minutes:
    def __init__(self) -> None:
        self._events = None
        self._lineup = None
        self.played_minutes = None
        self.team = "Tepatitlán"

    def set_events(self, events) -> None:
        self._events = events

    def set_lineup(self, lineup) -> None:
        self._lineup = lineup

    def obtain_played_minutes(self) -> None:
        self.played_minutes = obtain_played_minutes_from_lineup(self._lineup, self._events)
        self.played_minutes["team"] = self.team
