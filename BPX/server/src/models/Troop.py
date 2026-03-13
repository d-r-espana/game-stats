from django.db import models


from .Hero import Hero

# class for troop data

# 5 heroes
# get troop type (shooter, fighter, rider)

# Class for a single Troop
class Troop(models.Model):
    # heroes = models.ForeignKey()
    # troop_type = models.ForeignKey()
    tech_cp = models.IntegerField()
    equip_cp = models.IntegerField()
    troop_atk_bonus = models.IntegerField()
    troop_def = models.IntegerField()
    troop_def_bonus = models.IntegerField()
    troop_hp = models.IntegerField()
    troop_total_dmg = models.IntegerField()
    troop_total_dmg_bonus = models.IntegerField()

    # @property
    # def set_heroes(heroes):
    #     ...
        
    # def set_troop_type():
    #     ...
