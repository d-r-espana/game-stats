from django.db import models


from .Player import Player

class Alliance(models.Model):
    alliance_name = models.CharField()
    alliance_abbrev = models.CharField()
    # members = ForeignKey()

    class Meta:
           app_label = 'server'      

    def add_player():
            # if R4+, permission to add player
            ...
        
    def remove_player():
            # if R4+, permission to remove player
            ...
        