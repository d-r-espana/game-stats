from django.db import models
# import settings


class Hero(models.Model):
    hero_type = models.CharField(choices=('Shooter', 'Fighter', 'Rider'))
    hero_attack = models.IntegerField()
    hero_defence = models.IntegerField()
    units = models.IntegerField()
    hero_name = models.CharField()
