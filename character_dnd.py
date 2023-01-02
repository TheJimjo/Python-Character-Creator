import math
from random import randint


# Class to represent a base D&D character.
class Character_DnD:
    def __init__(self, name, species="unknown", job="nobody", level=1, strength=8, dexterity=8, constitution=8,
                 intelligence=8, wisdom=8, charisma=8, weapon="none", weapon_value=0, armor="none"):
        self.name = name
        self.species = species
        self.job = job
        self.level = level
        self.strength = strength
        self.strength_mod = int(math.floor((strength - 10) / 2))
        self.dexterity = dexterity
        self.dexterity_mod = int(math.floor((dexterity - 10) / 2))
        self.constitution = constitution
        self.constitution_mod = int(math.floor((constitution - 10) / 2))
        self.intelligence = intelligence
        self.intelligence_mod = int(math.floor((intelligence - 10) / 2))
        self.wisdom = wisdom
        self.wisdom_mod = int(math.floor((wisdom - 10) / 2))
        self.charisma = charisma
        self.charisma_mod = int(math.floor((charisma - 10) / 2))
        self.is_dead = False
        self.hit_die = 6
        self.hit_points = ((self.hit_die / 2) + self.constitution_mod) * self.level
        self.armor = armor
        self.armor_bonus = 0
        self.armor_class = 10 + self.dexterity_mod + self.armor_bonus
        self.weapon = weapon
        self.weapon_value = weapon_value
        self.attribute_points = 26

    # Report back character name, species, job, stats, and equipment.
    def __repr__(self):
        return f"\n{self.name} is a level {self.level} {self.species} {self.job} with these stats:" \
               f"\n{self.strength} Strength \n{self.dexterity} Dexterity \n{self.constitution} Constitution " \
               f"\n{self.intelligence} Intelligence \n{self.wisdom} Wisdom \n{self.charisma} Charisma. \nThey attack" \
               f" using a {self.weapon}  and has an armor class of {self.armor_class}"

    # Report back character is dead.
    def is_dead(self):
        self.is_dead = True
        if self.hit_points <= 0:
            print(f"{self.name} is at zero hit points and is dead.")

    # Display character's stats.
    def stat_display(self):
        return f"Your stats are as follows:\nStrength: {self.strength}\nDexterity: {self.dexterity}\n" \
               f"Constitution: {self.constitution}\nIntelligence: {self.intelligence}\nWisdom: {self.wisdom}\n" \
               f"Charisma{self.charisma}"

    # Change attribute points based on what stat was increased in stat_increase method.
    def change_attribute_points(self):
        while self.attribute_points > 0:
            print(f"\nYou have {self.attribute_points} points remaining. and the following stats:\n\nStrength: "
                  f"{self.strength}\nDexterity: {self.dexterity}\nConstitution: {self.constitution}\nIntelligence: "
                  f"{self.intelligence}\nWisdom: {self.wisdom}\nCharisma: {self.charisma}\n")
            which_stat = input("Which stat would you like to increase? Please select from strength, dexterity, "
                               "constitution, intelligence, wisdom, and Charisma. ")
            if which_stat.lower not in ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]:
                print(f"\nWhoops, '{which_stat}' wasn't an option. Please select from Strength, Dexterity, "
                      f"Constitution, Intelligence,Wisdom, or Charisma.")
            self.stat_increase(which_stat)

    # Increase a specific stat and ensure stat_mod is correct.
    def stat_increase(self, stat):
        while self.attribute_points > 0:
            if stat.lower() == "strength" and self.strength < 15:
                self.strength += 1
                self.strength_mod = int(math.floor((self.strength - 10) / 2))
                if self.strength in range(9, 14):
                    self.attribute_points -= 1
                else:
                    self.attribute_points -= 2
                self.change_attribute_points()
            elif stat.lower() == "dexterity" and self.dexterity < 15:
                self.dexterity += 1
                self.dexterity_mod = int(math.floor((self.dexterity - 10) / 2))
                self.armor_class = 10 + self.dexterity_mod + self.armor_bonus
                if self.dexterity in range(9, 14):
                    self.attribute_points -= 1
                else:
                    self.attribute_points -= 2
            elif stat.lower() == "constitution" and self.constitution < 15:
                self.constitution += 1
                self.constitution_mod = int(math.floor((self.constitution - 10) / 2))
                self.hit_points = ((self.hit_die / 2) + self.constitution_mod) * self.level
                if self.constitution in range(9, 14):
                    self.attribute_points -= 1
                else:
                    self.attribute_points -= 2
            elif stat.lower() == "intelligence" and self.intelligence < 15:
                self.intelligence += 1
                self.intelligence_mod = int(math.floor((self.intelligence - 10) / 2))
                if self.intelligence in range(9, 14):
                    self.attribute_points -= 1
                else:
                    self.attribute_points -= 2
            elif stat.lower() == "wisdom" and self.wisdom < 15:
                self.wisdom += 1
                self.wisdom_mod = int(math.floor((self.wisdom - 10) / 2))
                if self.wisdom in range(9, 14):
                    self.attribute_points -= 1
                else:
                    self.attribute_points -= 2
            elif stat.lower() == "charisma" and self.charisma < 15:
                self.charisma += 1
                self.charisma_mod = int(math.floor((self.charisma - 10) / 2))
                if self.charisma in range(9, 14):
                    self.attribute_points -= 1
                else:
                    self.attribute_points -= 2
            print(f"\n{stat} is already at 15 and cannot be increased further")
            break

    # User selects from two weapon / magic options based on job.
    def weapon_and_armor(self):
        if self.job.lower() == "fighter":
            weapon_choice = input(
                "Would you like to use a Greatsword (1) for 1d12 damage or a Flail and Shield (2) for "
                " 1d10 damage and +2 AC? Please input 1 or 2. ")
            if weapon_choice == 1:
                self.weapon = "Greatsword"
                self.weapon_value = randint(1, 12)
            else:
                self.weapon = "Flail and Shield"
                self.weapon_value = randint(1, 8)
                self.armor_bonus += 2
