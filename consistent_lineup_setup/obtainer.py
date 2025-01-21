from typing import Optional
from consistent_lineup_setup import obtain_played_minutes_from_lineup


class Obtainer_Played_Minutes:
    def __init__(self) -> None:
        self._events: Optional[dict] = None
        self._lineup: Optional[dict] = None
        self.played_minutes: Optional[int] = None
        self.dx_team: Optional[int] = None
        self.team: Optional[str] = None

    def set_events(self, events) -> None:
        self._events = events

    def set_lineup(self, lineup) -> None:
        self._lineup = lineup

    def obtain_played_minutes(self, dx_team: int) -> None:
        self.dx_team = dx_team
        self.team = self._lineup["response"][self.dx_team]["team"]["name"]
        self.played_minutes = obtain_played_minutes_from_lineup(
            self._lineup, self._events, self.dx_team, self.team
        )
        self.played_minutes["team"] = self.team
