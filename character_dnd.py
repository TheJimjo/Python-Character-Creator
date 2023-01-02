import math
from random import randint


class Character_DnD:
    def __init__(self, name, species="unknown", job="nobody", level=1, strength=8, dexterity=8, constitution=8,
                 intelligence=8, wisdom=8, charisma=8, weapon="none", weapon_value=0, armor="none"):
        # To create a D&D character, give it a name, a species, and a level. This will form a baseline that can be built off by adding a class and stats.
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
        self.hit_points = ((self.hit_die / 2) + self.constitution_mod) * level
        self.armor = armor
        self.armor_bonus = 0
        self.armor_class = 10 + self.dexterity_mod + self.armor_bonus
        self.weapon = weapon
        self.weapon_value = weapon_value

    def __repr__(self):
        # This will report back the D&D character name, species, job, full stat block.
        return f"{self.name} is a level {self.level} {self.species} {self.job} with these stats:" \
               f"\n{self.strength} Strength \n{self.dexterity} Dexterity \n{self.constitution} Constitution " \
               f"\n{self.intelligence} Intelligence \n{self.wisdom} Wisdom \n{self.charisma} Charisma. \nThey attack" \
               f" using a {self.weapon}  and has an armor class of {self.armor_class}"

    def is_dead(self):
        # This will report back that the character is dead.
        self.is_dead = True
        if self.hit_points <= 0:
            print("{name} is at zero hit points and is dead.".format(
                name=self.name.title))

    def stat_increase(self):
        character_attribute_points = 26
        while character_attribute_points > 0:
            print(
                f"You currently have {character_attribute_points} points available to spend.")
            print(f"Strength: {self.strength} \nDexterity: {self.dexterity} \nConstitution: {self.constitution} \n"
                  f"Intelligence: {self.intelligence} \nWisdom: {self.wisdom} \nCharisma: {self.charisma}")
            character_attribute_build = input("\nPlease select from Strength, Dexterity, Constitution, Wisdom, "
                                              "Intelligence, or Charisma. \nIf you would like to see how many points"
                                              " it will take to increase a stat, please type 'stats'. ")
            if character_attribute_build == "stats":
                character_attribute_build = input(
                    "Each single point increase from 8 to 13 will cost one attribute point. \nIncreasing to 14 or 15"
                    " will cost two attribute points each. \nNo stat may be higher than 15 before species bonuses. "
                    "\nPlease select from strength, dexterity, constitution, intelligence, wisdom, or charisma. ")
                continue
            if character_attribute_build.lower() == "strength":
                if self.strength > 14:
                    character_attribute_build = input(
                        "You cannot increase strength higher than 15. Please select another stat."
                        " If you would like to see how many points to increase a stat, please "
                        "type 'stats.' ")
                else:
                    self.strength += 1
                    if 8 <= self.strength <= 13:
                        character_attribute_points -= 1
                    else:
                        character_attribute_points -= 2
                    print(
                        f"Your strength is now {self.strength}. You have {character_attribute_points} remaining.")
                continue
            if character_attribute_build.lower() == "dexterity":
                if self.dexterity > 14:
                    character_attribute_build = input(
                        "You cannot increase dexterity higher than 15. Please select another stat."
                        " If you would like to see how many points to increase a stat, please "
                        "type 'stats.' ")
                else:
                    self.dexterity += 1
                    if 8 <= self.dexterity <= 13:
                        character_attribute_points -= 1
                    else:
                        character_attribute_points -= 2
                    print(
                        f"Your dexterity is now {self.dexterity}. You have {character_attribute_points} remaining.")
                continue
            if character_attribute_build.lower() == "constitution":
                if self.constitution > 14:
                    character_attribute_build = input(
                        "You cannot increase constitution higher than 15. Please select another stat."
                        " If you would like to see how many points to increase a stat, please "
                        "type 'stats.' ")
                else:
                    self.constitution += 1
                    if 8 <= self.constitution <= 13:
                        character_attribute_points -= 1
                    else:
                        character_attribute_points -= 2
                    print(
                        f"Your constitution is now {self.constitution}. You have {character_attribute_points} remaining.")
                continue
            if character_attribute_build.lower() == "intelligence":
                if self.intelligence > 14:
                    character_attribute_build = input(
                        "You cannot increase intelligence higher than 15. Please select another stat."
                        " If you would like to see how many points to increase a stat, please "
                        "type 'stats.' ")
                else:
                    self.intelligence += 1
                    if 8 <= self.intelligence <= 13:
                        character_attribute_points -= 1
                    else:
                        character_attribute_points -= 2
                    print(
                        f"Your intelligence is now {self.intelligence}. You have {character_attribute_points} remaining.")
                continue
            if character_attribute_build.lower() == "wisdom":
                if self.wisdom > 14:
                    character_attribute_build = input(
                        "You cannot increase wisdom higher than 15. Please select another stat."
                        " If you would like to see how many points to increase a stat, please "
                        "type 'stats.' ")
                else:
                    self.wisdom += 1
                    if 8 <= self.wisdom <= 13:
                        character_attribute_points -= 1
                    else:
                        character_attribute_points -= 2
                    print(
                        f"Your wisdom is now {self.wisdom}. You have {character_attribute_points} remaining.")
                continue
            if character_attribute_build.lower() == "charisma":
                if self.charisma > 14:
                    character_attribute_build = input(
                        "You cannot increase charisma higher than 15. Please select another stat."
                        " If you would like to see how many points to increase a stat, please "
                        "type 'stats.' ")
                else:
                    self.charisma += 1
                    if 8 <= self.charisma <= 13:
                        character_attribute_points -= 1
                    else:
                        character_attribute_points -= 2
                    print(
                        f"Your charisma is now {self.charisma}. You have {character_attribute_points} remaining.")
                continue
        print(f"Your final stats are:\n\n"
              f"Strength: {self.strength} \nDexterity: {self.dexterity} \nConstitution: {self.constitution} \n"
              f"Intelligence: {self.intelligence} \nWisdom: {self.wisdom} \nCharisma: {self.charisma}")

    def weapon_and_armor(self):
        if self.job.lower() == "fighter":
            weapon_choice = input("Would you like to use a Greatsword (1) for 1d12 damage or a Flail and Shield (2) for "
                                  " 1d10 damage and +2 AC? Please input 1 or 2. ")
            if weapon_choice == 1:
                self.weapon = "Greatsword"
                self.weapon_value = randint(1, 12)
            else:
                self.weapon = "Flail and Shield"
                self.weapon_value = randint(1, 8)
                self.armor_bonus += 2
        # if self.job.lower() == "rogue":
        #     weapon_choice = input(
        #         "Would you like to use a dagger (1) for 1d4 damage or a ? Please input 1 or 2. ")
