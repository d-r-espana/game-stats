from .Player import Player

class Alliance:
    def __init__(self, name, abbrev, players):
        self.name = name
        self.abbrev = abbrev
        self.players: list[Player] = players
        ...
        

        def add_player():
            # if R4+, permission to add player
            ...
        
        def remove_player():
            # if R4+, permission to remove player
            ...

        def 