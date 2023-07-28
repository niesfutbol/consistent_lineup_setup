import json
import pandas as pd
import pytest
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


def test_obtain_players_from_lineup():
    expected_players = played_time["player"].to_list()
    obtained_players = cls.obtain_players_from_lineup(lineup)
    assert expected_players == obtained_players


@pytest.mark.skip()
def test_obtain_played_minutes():
    expected_minutes = played_time["minutes"].to_list()
    obtained_minutes = cls.obtain_played_minutes_from_lineup(lineup, events)
    assert expected_minutes == obtained_minutes
