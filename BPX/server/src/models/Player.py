# class for player data
import json


class Player:
    def __init__(self, username, alliance, rank, language, time_zone, Troops = None):
        self.alliance = alliance
        self.rank = rank
        self.username = username
        self.language = language
        self.time_zone = time_zone
        self.troops = Troops

    Rank_PARAMS_MAPPING = {
        "R5": 0,
        "R4": 1,
        "R3": 2,
        "R2": 3,
        "R1": 4
    }

    # TODO: Add Alliance verification.

    @property
    def rank(self):
        return self._rank
    
    @rank.setter
    def rank(self, rank):
        if rank not in self.Rank_PARAMS_MAPPING:
            raise ValueError(f"{rank} is not a rank.")
        
        self._rank = rank

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        """
        Verify that the Player's username exists as the expected alliance and rank.
        
        """

        try:
            
            with open('temp.json', 'r') as file:
                data = json.load(file)
                alliance = data[self.alliance]
                rank = self.Rank_PARAMS_MAPPING[self.rank]
                players = alliance[rank][self.rank]

            # TODO: remove above in exchange for mongoDB alliance member lookup

                if username not in players:
                    raise ValueError("Player not found.")
                
                self._username = username
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise RuntimeError(f"Database error: {e}")
