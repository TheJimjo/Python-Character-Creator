import math
from random import randint
from dataclasses import dataclass

from entity import Entity
from equipment import armors, weapons
from dice import roll


CHARACTER_ATTRIBUTES = ("Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma")


@dataclass
class PlayerClass:
    name: str
    starting_hp: int
    hit_die: int


classes = list()
classes.append(PlayerClass("Fighter", 6, 10))


class Character(Entity):
    def __init__(self):
        Entity.__init__(self, input("Name your character: "))
        self.level = 1
        self.picker("class", classes)
        self.reset_attributes()
        self.pick_attributes(26)
        self.max_hp = self.player_class.starting_hp + \
                      self.get_attribute_mod(CHARACTER_ATTRIBUTES[2]) * self.level
        self.current_hp = self.max_hp
        print(self.get_attrs_str())
        self.picker("armor", armors)
        self.picker("weapon", weapons)


    def get_attribute_mod(self, attribute):
        return math.floor((self.attributes[attribute] - 10) / 2)


    def get_attribute_mod_cost(self, attribute):
        a = self.attributes[attribute]
        if a < 14:
            return 1
        elif a == 14:
            return 2
        elif a > 14:
            return "MAX"


    def reset_attributes(self):
        self.attributes = dict()
        for a in CHARACTER_ATTRIBUTES:
            self.attributes[a] = 8


    def pick_attributes(self, points):
        numbers = range(1, len(CHARACTER_ATTRIBUTES) + 1)
        error = ""

        while points > 0:
            print("   Attribute\tValue\tModifier\tCost")
            for n, a in zip(numbers, CHARACTER_ATTRIBUTES):
                print(f"{n}: {a}\t{self.attributes[a]}\t{self.get_attribute_mod(a)}\t{self.get_attribute_mod_cost(a)}")
            print()
            print(f"Attribute Points: {points}")
            print(error)
            try:
                choice = int(input("Choose an attribute to increase: "))
            except ValueError:
                error = f"Please pick a number between {min(numbers)} and {max(numbers)}"
                continue

            print()
            if choice in numbers:
                choice -= 1
                a = CHARACTER_ATTRIBUTES[choice]
                cost = self.get_attribute_mod_cost(a)
                if cost == "MAX":
                    error = f"{CHARACTER_ATTRIBUTES[choice]} is at maximum"
                elif cost <= points:
                    self.attributes[a] += 1
                    points -= cost
                    error = ""
                else:
                    error = f"Not enough points to increase {a}"
            else:
                error = f"Please pick a number between {min(numbers)} and {max(numbers)}"


    def get_attack_bonus(self):
        return self.get_attack_attr_bonus() + self.get_proficiency_bonus()


    def get_attack_attr_bonus(self):
        return max(self.get_attribute_mod["Strength"],
                   self.get_attribute_mod["Dexterity"]) \
                   if self.weapon.finesse else self.get_attribute_mod("Strength")


    def get_proficiency_bonus(self):
        return math.floor(2 + ((self.level - 1) * 0.25))


    def roll_weapon_damage(self):
        return roll(self.weapon.damage[0], self.weapon.damage[1], self.get_attack_attr_bonus())
        

    def __str__(self):
        return f"{self.name} is a level {self.level} {self.player_class.name}\n" \
               f"{self.get_health_str()}\n" \
               f"Armor: {self.armor.name}  AC: {self.armor.armor_class}  Weapon: {self.weapon.name}" \
               f"{self.get_attrs_str()}"


    def get_attrs_str(self):
        return ''.join([f"{a}: {self.attributes[a]}\n" for a in CHARACTER_ATTRIBUTES])


    def picker(self, pick_type, pick_list):
        choices = [g.name for g in pick_list]
        numbers = range(1, len(pick_list) + 1)

        for i, name in zip(numbers, choices):
            print(f"{i}: {name}")

        prompt = f"Which {pick_type} would you like? "

        while True:
            choice = int(input(prompt))
            if choice in numbers:
                break
            else:
                prompt = f"Please pick a number between {min(numbers)} and {max(numbers)}: "

        if pick_type == "armor":
            self.armor = armors[choice - 1]
            print(f"You chose {self.armor.name}.\n")
        elif pick_type == "weapon":
            self.weapon = weapons[choice - 1]
            print(f"You chose {self.weapon.name}.\n")
        elif pick_type == "class":
            self.player_class= classes[choice - 1]
            print(f"You chose {self.player_class.name}.\n")


    def attack(self, enemy):
        attack_roll = roll(1, 20, self.get_attack_bonus())
        print(f"{self.name} swings their {self.weapon.name} at the {enemy.name}!")
        print(attack_roll)
        if enemy.armor_class < attack_roll.result:
            print(f"{self.name} smacks the {enemy.name} a good one! {attack_roll.result} vs {enemy.get_ac()} AC")
            damage_roll = self.roll_weapon_damage()
            print(damage_roll)
            enemy.take_damage(damage_roll.result)
        else:
            print(f"{self.name} wiffs!")


    def get_ac(self):
        return self.armor.ac + min(self.armor.max_dex_bonus, self.attributes["Dexterity"])
