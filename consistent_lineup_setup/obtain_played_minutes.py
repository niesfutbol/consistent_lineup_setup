def obtain_players_from_lineup(lineup: dict) -> list:
    team = lineup["response"][0]
    startXI = [players["player"]["name"] for players in team["startXI"]]
    substit = [players["player"]["name"] for players in team["substitutes"]]
    return [*startXI, *substit]


def obtain_played_minutes_from_lineup(lineup: dict, events: dict) -> list:
    team = lineup["response"][0]
    minutes_sta = [90 for players in team["startXI"]]
    minutes_tit = [90 for players in team["substitutes"]]
    return [*minutes_sta, *minutes_tit]


def obtain_getin(events: dict) -> list:
    ins = [
        event["assist"]["name"]
        for event in events["response"]
        if ((event["type"] == "subst") & (event["team"]["name"] == "Tepatitlán"))
    ]
    return ins


def obtain_who_getout(events: dict) -> list:
    ins = [
        event["player"]["name"]
        for event in events["response"]
        if ((event["type"] == "subst") & (event["team"]["name"] == "Tepatitlán"))
    ]
    return ins
