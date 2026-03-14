from django.db import models
import settings
import prefill


from .Troop import Troop


alliances = prefill.public_data.get("Alliances", {})

def get_languages():
    return {i: i for i in settings.LANGUAGE_CODE}

def get_time_zones():
    return {i: i for i in settings.TIME_ZONE}


class PlayerManager(models.Manager):
    def create_player(self, username, **kwargs):
        player = self.create(username=username, **kwargs)
        return player

class Player(models.Model):
    alliance = models.CharField(max_length=30)
    rank = models.CharField(max_length=2)
    username = models.CharField(max_length=30, unique=True)
    # troops = models.ForeignKey(Troop)
    language = models.CharField(choices=get_languages)
    time_zone = models.CharField(choices=get_time_zones)

    objects = PlayerManager()

    class Meta:
        app_label = 'server'

    def __str__(self):
        return self.username
    
    def verify_membership(self):
        ranks = alliances.get(self.alliance)
        if not ranks:
            return False, "Alliance not found."
        
        verified_members = ranks.get(self.rank)
        if isinstance(verified_members, list) and self.username in verified_members:
            return True, "Verified."
        
        return False, "Player not found."
