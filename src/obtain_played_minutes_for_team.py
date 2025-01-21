import os
import json
import pandas as pd
import numpy as np
import consistent_lineup_setup as cls


def read_json(file_name):
    f = open(
        file_name,
    )
    league = json.load(f)
    f.close()
    return league

league_id = "263"
folder = {"135": "serie_a", "94": "primeira", "263": "liga_expansion", "262": "liga_mx"}
all_matches = read_json(f"/workdir/tests/data/data_file_{league_id}_2022.json")
path = f"/workdir/tests/data/{folder[league_id]}"
matches_files = dir_list = os.listdir(path)
id_matches = list(set([file.split(".")[0].split("_")[2] for file in dir_list]))

Obtainer = cls.Obtainer_Played_Minutes()
results = []
for id_match in id_matches:
    name_match = [
        match["league"]["round"]
        for match in all_matches["response"]
        if match["fixture"]["id"] == int(id_match)
    ]
    date = [
        match["fixture"]["date"]
        for match in all_matches["response"]
        if match["fixture"]["id"] == int(id_match)
    ]
    print(id_match)
    lineup = read_json(f"/workdir/tests/data/{folder[league_id]}/data_lineup_{id_match}.json")
    events = read_json(f"/workdir/tests/data/{folder[league_id]}/data_events_{id_match}.json")
    Obtainer.set_events(events)
    Obtainer.set_lineup(lineup)
    Obtainer.obtain_played_minutes(dx_team=0)
    Obtainer.played_minutes["match"] = name_match[0]
    Obtainer.played_minutes["date"] = date[0]
    results.append(Obtainer.played_minutes)
    Obtainer.obtain_played_minutes(dx_team=1)
    Obtainer.played_minutes["match"] = name_match[0]
    Obtainer.played_minutes["date"] = date[0]
    results.append(Obtainer.played_minutes)
pd.concat(results).to_csv(f"played_minutes_{league_id}.csv", index=False)
