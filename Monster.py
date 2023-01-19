
from sys import exit
from random import randint

# Class represents a monster in DnD.
class Monster_DnD:
    def __init__(self, name, hit_points, armor_class, weapon, weapon_value, challenge_rating, constitution_save,
                 attack_bonus):
        self.name = name
        self.hit_points = hit_points
        self.armor_class = armor_class
        self.weapon = weapon
        self.weapon_value = weapon_value
        self.challenge_rating = challenge_rating
        self.is_dead = False
        self.constitution_save = constitution_save
        self.attack_bonus = attack_bonus

    def __repr__(self):
        return (f"\n {self.name} is a challenge rating {self.challenge_rating} monster with {self.hit_points} hit "
                f"points, {self.armor_class} armor class and that wields {self.weapon}. ")

    def monster_attack(self, player):
        attack_roll = (randint(1, 20))
        print(f"\n{self.name.title()} attempts to attack {player.name.title()} with {self.weapon}.")
        print(f"\n{self.name.title()} rolls an attack roll of {self.attack_bonus + attack_roll} compared to an AC of "
              f"{player.armor_class}. ")
        if player.armor_class <= self.attack_bonus + attack_roll:
            attack_damage = self.weapon_value
            print(f"\n{self.name.title()} has landed a hit for {attack_damage} points of damage.")
            player.lose_hit_points(attack_damage)
            if player.is_dead:
                print("\nThanks for playing")
                exit(0)
            else:
                player.attack_or_run(self)
        else:
            print(f"\n{player.name} has successfully evaded the attack.")
            player.attack_or_run(self)

    def lose_hit_points(self, amount):
        self.hit_points -= amount
        print(f"\n{self.name} has {self.hit_points} hit points remaining.")
        if self.hit_points <= 0:
            self.hit_points = 0
            self.is_dead = True
            print(f"\n{self.name} has died.")
        else:
            print(f"\n{self.name} takes {amount} damage and has {self.hit_points} hit points remaining.")
