import json
import pandas as pd
import consistent_lineup_setup as cls


def read_json(file_name):
    f = open(
        file_name,
    )
    league = json.load(f)
    f.close()
    return league


lineup = read_json("/workdir/tests/data/data_lineup_868614.json")
events = read_json("/workdir/tests/data/data_events_868614.json")
played_time = pd.read_csv("/workdir/tests/data/consistent_team.csv")


def test_obtainer():
    Obtainer = cls.Obtainer_Played_Minutes()
    Obtainer.set_events(events)
    Obtainer.set_lineup(lineup)
    Obtainer.obtain_played_minutes()
    expected_minutes = played_time["minutes"].to_list()
    obtained = Obtainer.played_minutes
    obtained_minutes = obtained["minutes"].to_list()
    assert expected_minutes == obtained_minutes
    expected_players = played_time["player"].to_list()
    obtained_players = obtained["player"].to_list()
    assert expected_players == obtained_players
    expected_team = played_time["team"].to_list()
    obtained_team = obtained["team"].to_list()
    assert expected_team == obtained_team
    Obtainer.obtain_played_minutes(dx_team=1)
    obtained = Obtainer.played_minutes
    obtained_team = obtained["team"].to_list()
    assert "Alebrijes de Oaxaca" == obtained_team[3]
