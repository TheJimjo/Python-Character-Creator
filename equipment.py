from dataclasses import dataclass


# THIS NEEDS TO BE FIXED
MAX_INT = 99999


@dataclass
class Armor:
    name: str
    proficiency: str
    cost_gp: int
    ac: int
    max_dex_bonus: int
    min_str: int
    stealth_disadvantage: bool
    weight: int


armors = list()
armors.append(Armor("Scale Mail", "medium", 50, 14, 2, 0, True, 45))
armors.append(Armor("Studded Leather", "light", 10, 11, MAX_INT, 0, False, 13))


@dataclass
class Weapon:
    name: str
    martial: bool
    ranged: bool
    cost: int
    damage: (int, int)
    damage_type: str
    weight: int
    finesse: bool
    heavy: bool
    light: bool
    loading: bool
    range_distance: (int, int)
    reach: bool
    thrown: bool
    two_handed: bool
    versatile: bool
    versatile_damage: (int, int)


weapons = list()
weapons.append(Weapon("Club", # name
                      False, # martial
                      False, # ranged
                      1, # cost
                      (1, 4), # damage
                      "bludgeoning", # damage type
                      2, # weight
                      False, # finesse
                      False, # heavy
                      False, # light
                      False, # loading
                      (0, 0), # range distance
                      False, # reach
                      False, # thrown
                      False, # two handed
                      False, # versatile
                      (0, 0))) # versatile damage
weapons.append(Weapon("Greatsword", # name
                      True, # martial
                      False, # ranged
                      50, # cost
                      (2, 6), # damage
                      "slashing", # damage type
                      6, # weight
                      False, # finesse
                      True, # heavy
                      False, # light
                      False, # loading
                      (0, 0), # range distance
                      False, # reach
                      False, # thrown
                      True, # two handed
                      False, # versatile
                      (0, 0))) # versatile damage
