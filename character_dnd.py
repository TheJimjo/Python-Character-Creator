import math
from random import randint
from dice import RollResult

# Test

# Class to represent a base D&D character.
class Character_DnD:
    def __init__(self, name = "nobody", species="unknown", job="nobody", level=1, strength=8, dexterity=8, constitution=8,
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
        self.attribute_points = 0
        self.attack_bonus = 0
        self.spell_save_dc = 8
        self.proficiency_modifier = 2
        self.log = {}
        self.gold = 0

    # Report back character name, species, job, stats, and equipment.
    def __repr__(self):
        return f"\n{self.name} is a level {self.level} {self.species} {self.job} with these stats:" \
               f"\n{self.strength} Strength \n{self.dexterity} Dexterity \n{self.constitution} Constitution " \
               f"\n{self.intelligence} Intelligence \n{self.wisdom} Wisdom \n{self.charisma} Charisma \nThey attack" \
               f" using {self.weapon}  and have an armor class of {self.armor_class}"

    # Report back character is dead.
    def is_dead(self):
        self.is_dead = True
        if self.hit_points <= 0:
            print(f"{self.name} is at zero hit points and is dead.")

    # Display character's stats.
    def stat_display(self):
        print(f"Your stats are as follows:\nStrength: {self.strength}\nDexterity: {self.dexterity}\n" \
              f"Constitution: {self.constitution}\nIntelligence: {self.intelligence}\nWisdom: {self.wisdom}\n" \
              f"Charisma: {self.charisma}")

    # Change attribute points based on what stat was increased in stat_increase method.
    def change_attribute_points(self):
        while self.attribute_points > 0:
            print(f"\nYou have {self.attribute_points} points remaining. and the following stats:\n\nStrength: "
                  f"{self.strength}\nDexterity: {self.dexterity}\nConstitution: {self.constitution}\nIntelligence: "
                  f"{self.intelligence}\nWisdom: {self.wisdom}\nCharisma: {self.charisma}\n")
            which_stat = input("Which stat would you like to increase? Please select from strength, dexterity, "
                               "constitution, intelligence, wisdom, and Charisma. ")
            if which_stat.lower() not in ["strength", "dexterity", "constitution", "intelligence", "wisdom",
                                          "charisma"]:
                print(f"\nWhoops, '{which_stat}' wasn't an option. Please select from Strength, Dexterity, "
                      f"Constitution, Intelligence,Wisdom, or Charisma.")
            else:
                self.stat_increase(which_stat)

    #Update stats based on species selection
    def species_change(self, species):
        if species.lower() == "human":
            self.strength += 1
            self.dexterity += 1
            self.constitution += 1
            self.intelligence += 1
            self.wisdom += 1
            self.charisma += 1
        elif species.lower() == "elf":
            self.dexterity += 2
        else:
            self.constitution += 2

    #Character creation input.
    def starting_character_information(self):
        character_name = input(
            "Please type what you would like your character name to be? ")
        self.name = character_name.title()
        character_species = input(
            "Please type what you would like your character species to be? Please choose from Human, "
            "Elf, or Dwarf. Then hit enter. ")
        while character_species.lower() not in ["human", "elf", "dwarf"]:
            character_species = input(
                "Whoops, looks like you didn't choose one of the previous species. Please choose from "
                "Human, Elf, or Dwarf. Then hit enter. ")
        character_job = input(
            "Please type what you would like your character's job to be? Please choose from Fighter, Rogue, "
            "or Wizard. Then hit enter. ")
        while character_job.lower() not in ["fighter", "rogue", "wizard"]:
            character_job = input(
                "Whoops, looks like you didn't choose one of the previous jobs. PLease choose from Fighter, "
                "Rogue, or Wizard. Then hit enter. ")
        self.change_attribute_points()
        self.job = character_job.title()
        self.species_change(character_species)

    # Increase a specific stat and ensure any attributes reliant on that stat recalculate.
    def stat_increase(self, stat):
        while self.attribute_points > 0:
            if stat.lower() == "strength" and self.strength < 15:
                self.strength += 1
                self.strength_mod = int(math.floor((self.strength - 10) / 2))
                if self.strength in range(9, 14):
                    self.attribute_points -= 1
                elif self.attribute_points <= 1:
                    self.strength -= 1
                    self.strength_mod = int(math.floor((self.strength - 10) / 2))
                    print(
                        f"\nYou only have 1 point remaining and changing {stat} from {self.strength} to "
                        f"{self.strength + 1} requires 2 points. ")
                else:
                    self.attribute_points -= 2
                self.change_attribute_points()
            elif stat.lower() == "dexterity" and self.dexterity < 15:
                self.dexterity += 1
                self.dexterity_mod = int(math.floor((self.dexterity - 10) / 2))
                self.armor_class = 10 + self.dexterity_mod + self.armor_bonus
                if self.dexterity in range(9, 14):
                    self.attribute_points -= 1
                elif self.attribute_points <= 1:
                    self.dexterity -= 1
                    self.dexterity_mod = int(math.floor((self.dexterity - 10) / 2))
                    self.armor_class = 10 + self.dexterity_mod + self.armor_bonus
                    print(
                        f"\nYou only have 1 point remaining and changing {stat} from {self.dexterity} to "
                        f"{self.dexterity + 1} requires 2 points. ")
                else:
                    self.attribute_points -= 2
            elif stat.lower() == "constitution" and self.constitution < 15:
                self.constitution += 1
                self.constitution_mod = int(math.floor((self.constitution - 10) / 2))
                self.hit_points = ((self.hit_die / 2) + self.constitution_mod) * self.level
                if self.constitution in range(9, 14):
                    self.attribute_points -= 1
                elif self.attribute_points <= 1:
                    self.constitution -= 1
                    self.constitution_mod = int(math.floor((self.constitution - 10) / 2))
                    self.hit_points = ((self.hit_die / 2) + self.constitution_mod) * self.level
                    print(
                        f"\nYou only have 1 point remaining and changing {stat} from {self.constitution} to "
                        f"{self.constitution + 1} requires 2 points. ")
                else:
                    self.attribute_points -= 2
            elif stat.lower() == "intelligence" and self.intelligence < 15:
                self.intelligence += 1
                self.intelligence_mod = int(math.floor((self.intelligence - 10) / 2))
                self.spell_save_dc = 8 + self.intelligence_mod + self.proficiency_modifier
                if self.intelligence in range(9, 14):
                    self.attribute_points -= 1
                elif self.attribute_points <= 1:
                    self.intelligence -= 1
                    self.intelligence_mod = int(math.floor((self.intelligence - 10) / 2))
                    self.spell_save_dc = 8 + self.intelligence_mod + self.proficiency_modifier
                    print(
                        f"\nYou only have 1 point remaining and changing {stat} from {self.intelligence} to "
                        f"{self.intelligence + 1} requires 2 points. ")
                else:
                    self.attribute_points -= 2
            elif stat.lower() == "wisdom" and self.wisdom < 15:
                self.wisdom += 1
                self.wisdom_mod = int(math.floor((self.wisdom - 10) / 2))
                if self.wisdom in range(9, 14):
                    self.attribute_points -= 1
                elif self.attribute_points <= 1:
                    self.wisdom -= 1
                    self.wisdom_mod = int(math.floor((self.wisdom - 10) / 2))
                    print(
                        f"\nYou only have 1 point remaining and changing {stat} from {self.wisdom} to "
                        f"{self.wisdom + 1} requires 2 points. ")
                else:
                    self.attribute_points -= 2
            elif stat.lower() == "charisma" and self.charisma < 15:
                self.charisma += 1
                self.charisma_mod = int(math.floor((self.charisma - 10) / 2))
                if self.charisma in range(9, 14):
                    self.attribute_points -= 1
                elif self.attribute_points <= 1:
                    self.charisma -= 1
                    self.charisma_mod = int(math.floor((self.charisma - 10) / 2))
                    print(
                        f"\nYou only have 1 point remaining and changing {stat} from {self.charisma} to "
                        f"{self.charisma + 1} requires 2 points. ")
                else:
                    self.attribute_points -= 2
            else:
                print(f"\n{stat} is already at 15 and cannot be increased further")
            break

    # User selects from two weapon / magic options based on job.
    def weapon_choice(self):
        if self.job.lower() == "fighter":
            weapon_choice = input(
                "\nWould you like to use a Greatsword (1) for 1d12 damage or a Flail and Shield (2) for "
                " 1d10 damage and +2 Armor Class? Please input 1 or 2. ")
            print(weapon_choice)
            if weapon_choice == "1":
                self.weapon = "a Greatsword"
                self.weapon_value = (randint(1, 12) + self.strength_mod)
                self.attack_bonus = self.strength_mod
            else:
                self.weapon = "a Flail and Shield"
                self.weapon_value = randint(1, 8)
                self.armor_bonus += 2
                self.armor_class = self.armor_class = 10 + self.dexterity_mod + self.armor_bonus
        elif self.job.lower() == "rogue":
            weapon_choice = input(
                "\nWould you like to use a Shortsword (1) for 1d6 damage or a Dagger (2) for "
                " 1d4 damage? Please input 1 or 2. ")
            if weapon_choice == "1":
                self.weapon = "a Shortsword"
                self.weapon_value = randint(1, 6)
            else:
                self.weapon = "a Dagger"
                self.weapon_value = randint(1, 4)
        elif self.job.lower() == "wizard":
            weapon_choice = input(
                "\nWould you like to use a Firebolt (1) for 1d10 damage or a Frostbite (2) for "
                " 1d6 cold damage and cause a Con save for disadvantage on the next attack roll? Please input 1 or 2. ")
            if weapon_choice == "1":
                self.weapon = "Firebolt"
                self.weapon_value = randint(1, 10)
            else:
                self.weapon = "Frostbite"
                self.weapon_value = randint(1, 6)

    # Lets the user select different armors, except the wizard. They just get Mage Armor.
    def armor_choice(self):
        if self.job.lower() == "fighter":
            armor_choice = input("\nWould you like Scale Mail (1) for 14 armor class plus your dexterity modifier "
                                 "(maximum +2) or Studded Leather (2) for 12 armor class plus your dexterity modifier?"
                                 "Please input 1 or 2. ")
            if armor_choice == "1":
                self.armor = "Scale Mail"
                self.armor_bonus += 4
                self.armor_class = 10 + self.dexterity_mod + self.armor_bonus
                if self.dexterity_mod > 2:
                    self.armor_class = 10 + 2 + self.armor_bonus
            else:
                self.armor = "Studded Leather"
                self.armor_bonus += 2
                self.armor_class = 10 + self.dexterity_mod + self.armor_bonus
        elif self.job.lower() == "rogue":
            armor_choice = input("\nWould you like Leather Armor (1) for 11 armor class plus your dexterity modifier or"
                                 " Studded Leather (2) for 12 armor class and no maximum dexterity modifier? Please "
                                 "input 1 or 2. ")
            if armor_choice == "1":
                self.armor = "Leather Armor"
                self.armor_bonus += 1
                self.armor_class = 10 + self.dexterity_mod + self.armor_bonus
            else:
                self.armor = "Studded Leather"
                self.armor_bonus += 2
                self.armor_class = 10 + self.dexterity_mod + self.armor_bonus
        if self.job.lower() == "wizard":
            self.armor = "Mage Armor"
            self.armor_class = 13 + self.dexterity_mod

    def player_loadout(self):
        print(f"{self.name} is wearing {self.armor} with {self.armor_class} armor class and wielding "
              f"{self.weapon}.")


    # Player attacks a monster.
    def player_attack(self, monster):
        attack_roll = (randint(1, 20))
        save_roll = (randint(1, 20))
        print(f"\n{self.name} attempts to attack the {monster.name} with {self.weapon}.")
        if self.weapon.lower() == "frostbite":
            con_save = monster.constitution_save + save_roll
            print(f"\n{monster.name} rolls a constitution saving throw of {con_save} "
                  f"compared to a spell save DC of {self.spell_save_dc}.")
            if con_save < self.spell_save_dc:
                print(f"\n{monster.name} has failed their save and takes {self.weapon_value} points of damage and "
                      f"has disadvantage on their next attack roll.")
                monster.lose_hit_points(self.weapon_value)
                if monster.is_dead:
                    print(f"\nCongratulations! You have slain the {monster.name}! Thanks for playing! ")
                else:
                    monster.monster_attack(self)
            else:
                print(f"\n{monster.name} has succeeded their save and suffers no ill effects.")
                monster.monster_attack(self)
        else:
            print(f"\n{self.name} rolls an attack roll of {self.attack_bonus + attack_roll} compared to an AC of "
                  f"{monster.armor_class}. ")
            if monster.armor_class < self.attack_bonus + attack_roll:
                attack_damage = self.weapon_value
                print(f"\n{self.name} has landed a hit for {attack_damage} points of damage.")
                monster.lose_hit_points(attack_damage)
            else:
                print(f"\n{monster.name} has successfully evaded the attack.")

    def lose_hit_points(self, amount):
        self.hit_points -= amount
        print(f"\n{self.name} has {self.hit_points} hit points remaining.")
        if self.hit_points <= 0:
            self.hit_points = 0
            self.is_dead = True
            print(f"\n{self.name} has died. Better luck next time.")
        else:
            print(f"\n{self.name} takes {amount} damage and has {self.hit_points} hit points remaining.")

    def attack_or_run(self, monster):
        choice = input("Do you wish to attack (1) or run (2)?")
        if choice == "1":
            self.player_attack(monster)
        elif choice == "2":
            pass # Need to add logic for running away and returning to town.
        else:
            print("You did not select attack (1) or run (2). ")
            self.attack_or_run(monster)



