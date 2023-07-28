import pandas as pd


def obtain_players_from_lineup(lineup: dict) -> list:
    team = lineup["response"][0]
    startXI = [players["player"]["name"] for players in team["startXI"]]
    substit = [players["player"]["name"] for players in team["substitutes"]]
    return [*startXI, *substit]


def obtain_played_minutes_from_lineup(lineup: dict, events: dict) -> list:
    team = lineup["response"][0]
    minutes_sta = [90 for players in team["startXI"]]
    minutes_tit = [0 for players in team["substitutes"]]
    players = obtain_players_from_lineup(lineup)
    minutes = [*minutes_sta, *minutes_tit]
    return pd.DataFrame(list(zip(players, minutes)), columns=["player", "minutes"])


def obtain_info_in(events: dict) -> dict:
    in_p = obtain_getin(events)
    minutes = [90 - minute for minute in obtain_time_of_substitution(events)]
    return dict(zip(in_p, minutes))


def obtain_info_out(events: dict) -> dict:
    in_p = obtain_who_getout(events)
    minutes = obtain_time_of_substitution(events)
    return dict(zip(in_p, minutes))


def obtain_getin(events: dict) -> list:
    return _obtain_substitutes(events, in_or_out="assist")


def obtain_who_getout(events: dict) -> list:
    return _obtain_substitutes(events, in_or_out="player")


def obtain_time_of_substitution(events: dict) -> list:
    ins = [
        event["time"]["elapsed"]
        for event in events["response"]
        if ((event["type"] == "subst") & (event["team"]["name"] == "Tepatitlán"))
    ]
    return ins


def _obtain_substitutes(events: dict, in_or_out: str) -> list:
    ins = [
        event[in_or_out]["name"]
        for event in events["response"]
        if ((event["type"] == "subst") & (event["team"]["name"] == "Tepatitlán"))
    ]
    return ins
