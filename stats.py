# OOP: Stats can be chosen. They can be increased. They can be decreased.

class Stats:
    def __init__(self, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.attribute_points = 26

    def stat_increase(self, stat, amount):
        print("Code is running")
        if stat == "strength":
            self.strength += amount
        elif stat == "dexterity":
            self.dexterity += amount
        elif stat == "constitution":
            self.dexterity += amount
        elif stat == "intelligence":
            self.intelligence += amount
        elif stat == "wisdom":
            self.wisdom += amount
        elif stat == "charisma":
            self.charisma += amount
        print(f"\n{stat} is now {self.strength}")

    def stat_cost(self, stat, increase):
        stats_dictionary = {"strength": self.strength, "dexterity": self.dexterity, "constitution": self.constitution,
                            "intelligence": self.intelligence, "wisdom": self.wisdom, "charisma": self.charisma}
        cost = 0
        for number in range(stats_dictionary[stat], stats_dictionary[stat] + increase):
            print(range(stats_dictionary[stat], stats_dictionary[stat] + increase))
            if number in range(8, 14):
                cost += 1
            elif number in range(14, 16):
                cost += 2
            else:
                print(f"\nThat would increase {stat} beyond 15. Please select another stat.")
                self.stat_choice()
        if cost > self.attribute_points:
            print(f"\nThis increase requires {cost} attribute points and you only have {self.attribute_points}. Please"
                  f"select another stat.")
            self.stat_choice()
        else:
            print(f"\nIt will cost {cost} attribute points to increase {stat} from {stats_dictionary[stat]} to "
                  f"{stats_dictionary[stat]+ increase}. Do you want to apply this change Y/N?")
            choice = input("Selection: ")
            if choice == "y":
                self.stat_increase(stat, int(increase))
                print(f"\n {stat} is now {stats_dictionary[stat]}")
            else:
                print("Code isn't working.")



            return cost

    def stat_choice(self):
        stats = {"1": "strength", "2": "dexterity", "3": "constitution", "4": "intelligence", "5": "wisdom",
                 "6": "charisma"}
        print("\nWhich stat would you like to increase. Please choose a number.")
        print()
        for key, value in stats.items():
            print(key, value)
        print()
        choice = input("Selection: ")
        while choice not in stats.keys():
            choice = input("\nPlease select a valid number.")
        print(f"Attribute Points: {self.attribute_points}")
        print()
        print(f"\nHow many points would you like to increase {stats[choice]} by? ")
        amount = input("Selection: ")
        self.stat_cost(stats[choice], int(amount))



test = Stats()
test.stat_choice()







# stat_choice()

# def stat_increase(self, stat):
#     while self.attribute_points > 0:
#         if stat.lower() == "strength" and self.strength < 15:
#             self.strength += 1
#             self.strength_mod = int(math.floor((self.strength - 10) / 2))
#             if self.strength in range(9, 14):
#                 self.attribute_points -= 1
#             elif self.attribute_points <= 1:
#                 self.strength -= 1
#                 self.strength_mod = int(math.floor((self.strength - 10) / 2))
#                 print(
#                     f"\nYou only have 1 point remaining and changing {stat} from {self.strength} to "
#                     f"{self.strength + 1} requires 2 points. ")
#             else:
#                 self.attribute_points -= 2
#             self.change_attribute_points()
#         elif stat.lower() == "dexterity" and self.dexterity < 15:
#             self.dexterity += 1
#             self.dexterity_mod = int(math.floor((self.dexterity - 10) / 2))
#             self.armor_class = 10 + self.dexterity_mod + self.armor_bonus
#             if self.dexterity in range(9, 14):
#                 self.attribute_points -= 1
#             elif self.attribute_points <= 1:
#                 self.dexterity -= 1
#                 self.dexterity_mod = int(math.floor((self.dexterity - 10) / 2))
#                 self.armor_class = 10 + self.dexterity_mod + self.armor_bonus
#                 print(
#                     f"\nYou only have 1 point remaining and changing {stat} from {self.dexterity} to "
#                     f"{self.dexterity + 1} requires 2 points. ")
#             else:
#                 self.attribute_points -= 2
#         elif stat.lower() == "constitution" and self.constitution < 15:
#             self.constitution += 1
#             self.constitution_mod = int(math.floor((self.constitution - 10) / 2))
#             self.hit_points = ((self.hit_die / 2) + self.constitution_mod) * self.level
#             if self.constitution in range(9, 14):
#                 self.attribute_points -= 1
#             elif self.attribute_points <= 1:
#                 self.constitution -= 1
#                 self.constitution_mod = int(math.floor((self.constitution - 10) / 2))
#                 self.hit_points = ((self.hit_die / 2) + self.constitution_mod) * self.level
#                 print(
#                     f"\nYou only have 1 point remaining and changing {stat} from {self.constitution} to "
#                     f"{self.constitution + 1} requires 2 points. ")
#             else:
#                 self.attribute_points -= 2
#         elif stat.lower() == "intelligence" and self.intelligence < 15:
#             self.intelligence += 1
#             self.intelligence_mod = int(math.floor((self.intelligence - 10) / 2))
#             self.spell_save_dc = 8 + self.intelligence_mod + self.proficiency_modifier
#             if self.intelligence in range(9, 14):
#                 self.attribute_points -= 1
#             elif self.attribute_points <= 1:
#                 self.intelligence -= 1
#                 self.intelligence_mod = int(math.floor((self.intelligence - 10) / 2))
#                 self.spell_save_dc = 8 + self.intelligence_mod + self.proficiency_modifier
#                 print(
#                     f"\nYou only have 1 point remaining and changing {stat} from {self.intelligence} to "
#                     f"{self.intelligence + 1} requires 2 points. ")
#             else:
#                 self.attribute_points -= 2
#         elif stat.lower() == "wisdom" and self.wisdom < 15:
#             self.wisdom += 1
#             self.wisdom_mod = int(math.floor((self.wisdom - 10) / 2))
#             if self.wisdom in range(9, 14):
#                 self.attribute_points -= 1
#             elif self.attribute_points <= 1:
#                 self.wisdom -= 1
#                 self.wisdom_mod = int(math.floor((self.wisdom - 10) / 2))
#                 print(
#                     f"\nYou only have 1 point remaining and changing {stat} from {self.wisdom} to "
#                     f"{self.wisdom + 1} requires 2 points. ")
#             else:
#                 self.attribute_points -= 2
#         elif stat.lower() == "charisma" and self.charisma < 15:
#             self.charisma += 1
#             self.charisma_mod = int(math.floor((self.charisma - 10) / 2))
#             if self.charisma in range(9, 14):
#                 self.attribute_points -= 1
#             elif self.attribute_points <= 1:
#                 self.charisma -= 1
#                 self.charisma_mod = int(math.floor((self.charisma - 10) / 2))
#                 print(
#                     f"\nYou only have 1 point remaining and changing {stat} from {self.charisma} to "
#                     f"{self.charisma + 1} requires 2 points. ")
#             else:
#                 self.attribute_points -= 2
#         else:
#             print(f"\n{stat} is already at 15 and cannot be increased further")
#         break