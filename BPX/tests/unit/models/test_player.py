import pytest

from server import source


def test_model_player():
    player = source.models.Player(
        username = "Asgrim",
        alliance = "ONI",
        rank = "R4",
        language = "English",
        time_zone = "CST", 
    )
    assert player.username == "Asgrim"
    assert player.alliance == "ONI"
    assert player.rank == "R4"

def test_model_player_not_found():
    with pytest.raises(
        ValueError,
        match="Player not found."
    ):
        source.models.Player(
            username = "unknown",
            alliance = "ONI",
            rank = "R4",
            language = "English",
            time_zone = "CST", 
        )

def test_model_player_invalid_rank():
    rank = 0
    with pytest.raises(
        ValueError,
        match=f"{rank} is not a rank."
    ):
        source.models.Player(
            username = "unknown",
            alliance = "ONI",
            rank = rank,
            language = "English",
            time_zone = "CST", 
        )


def test_model_player_troops():
    ...
