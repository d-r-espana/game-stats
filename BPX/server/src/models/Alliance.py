from django.db import models


from .Player import Player

class Alliance(models.Model):
    alliance_name = models.CharField()
    alliance_abbrev = models.CharField()
    # members = ForeignKey()

    def __init__(self, name, abbrev, players):        

        def add_player():
            # if R4+, permission to add player
            ...
        
        def remove_player():
            # if R4+, permission to remove player
            ...
        