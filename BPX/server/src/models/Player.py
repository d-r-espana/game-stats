from django.db import models
import settings
import prefill


from .Troop import Troop


PUBLIC_DATA = prefill

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

    def __str__(self):
        return self.username
    
    def verify_membership(self):
        alliances = PUBLIC_DATA.get("Alliances", {})

        if self.alliance not in alliances:
            return False, "Alliance unregistered or not found."
        
        ranks = alliances[self.alliance]
        if self.rank in ranks:
            verified_members = ranks[self.rank]
            if isinstance(verified_members, list):
                if self.username in verified_members or self.username == verified_members:
                    return True, "Verified"
        else:
            return False, "Player not found."  
