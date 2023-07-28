def obtain_players_from_lineup(lineup: dict) -> list:
    team = lineup["response"][0]
    startXI = [players["player"]["name"] for players in team["startXI"]]
    substit = [players["player"]["name"] for players in team["substitutes"]]
    return [*startXI, *substit]
