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
        stats_dictionary = {"strength": self.strength, "dexterity": self.dexterity, "constitution": self.constitution,
                            "intelligence": self.intelligence, "wisdom": self.wisdom, "charisma": self.charisma}
        if stat in stats_dictionary.keys():
            stats_dictionary[stat] += amount

    def stat_cost(self, stat):
        stats_dictionary = {"strength": self.strength, "dexterity": self.dexterity, "constitution": self.constitution,
                            "intelligence": self.intelligence, "wisdom": self.wisdom, "charisma": self.charisma}
        print(f"Attribute Points: {self.attribute_points}")
        print(f"\nHow many points would you like to increase {stats_dictionary[stat]} by? ")
        increase = input("Selection: ")
        cost = 0
        for number in range(stats_dictionary[stat], stats_dictionary[stat] + increase):
            if number <= 13:
                cost += 1
            elif number <= 15:
                cost += 2
            else:
                print(f"\nThat would increase {stat} beyond 15. Please select another stat.")
        if cost > self.attribute_points:
            print(f"\nThis increase requires {cost} attribute points and you only have {self.attribute_points}. Please"
                  f"select another stat.")
            self.stat_choice()
        else:
            print(f"\nIt will cost {cost} attribute points to increase {stat} from {stats_dictionary[stat]} to "
                  f"{stats_dictionary[stat]+ increase}. Do you want to apply this change Y/N?")
            choice = input("Selection: ")
            if choice == "y":
                self.attribute_points -= cost
                print(self.attribute_points)
                self.stat_increase(stat, int(increase))
            else:
                print("Code isn't working.")
            return cost

def stat_choice():
    stats = {"1": "strength", "2": "dexterity", "3": "constitution", "4": "intelligence", "5": "wisdom",
             "6": "charisma"}
    print("\nWhich stat would you like to choose. Please select a number")
    print()
    for key, value in stats.items():
        print(key, value)
    print()
    choice = input("Selection: ")
    while choice not in stats.keys():
        choice = input("\nPlease select a valid number.")
    return choice