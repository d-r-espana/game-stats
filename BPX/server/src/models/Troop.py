from .Hero import Hero

# class for troop data

# 5 heroes
# get troop type (shooter, fighter, rider)

# Class for a single Troop
class Troop:
    def __init__(
            self,
            heroes: list[Hero] = None,
            troop_type: str = None,
            hero_cp: int = 0,
            tech_cp: int = 0,
            equipment_cp: int = 0,
            troop_cp: int = 0,
            troop_atk: int = 0,
            troop_atk_bonus: int = 0,
            troop_def: int = 0,
            troop_def_bonus: int = 0,
            troop_hp: int = 0,
            troop_total_dmg: int = 0,
            troop_total_dmg_bonus: int = 0):
         self.heroes = heroes
         self.troop_type = troop_type
         self.hero_cp = hero_cp
         self.tech_cp = tech_cp
         self.equipment_cp = equipment_cp
         self.troop_cp = troop_cp
         self.troop_atk = troop_atk
         self.troop_atk_bonus = troop_atk_bonus
         self.troop_def = troop_def
         self.troop_def_bonus = troop_def_bonus
         self.troop_hp = troop_hp
         self.troop_total_dmg = troop_total_dmg
         self.troop_total_dmg_bonus = troop_total_dmg_bonus
         ...

    @property
    def set_heroes(heroes):
        ...
        
    def set_troop_type():
        ...

# Class for all Player's Troops
class Troops:
    def __init__(self, troops: list[Troop] = None):
        self.troops = troops
        ...
