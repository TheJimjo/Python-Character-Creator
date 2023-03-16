class NPC:
    def __init__(self, name="none", shop="none", introduction="none", wares=None):
        if wares is None:
            wares = {}
        self.name = name
        self.introduction = introduction
        self.wares = wares
        self.shop = shop

    def introduction(self):
        print(f"\nWelcome to {self.name}'s {self.shop}!")
        pass  # Need to add code to indicate what is available for purchase.

    def wares_selection(self, name, player):
        print(f"The {name} has the following items available.")
        count = 1
        for item in self.wares:
            if self.wares[item][0] == player.job:
                print(f"({count}) {self.wares[item][1]} for {str(self.wares[item][2])} gold.")
                count += 1
        print("Which item would you like to purchase?")
        input("Selection")


def merchant_selection():
    print("Which merchant would you like to visit? (1) Armorer or (2) Weaponsmith?")
    print("")
    input("Selection: ")


Armorer = NPC("Armorer", "Armorsmithy", "Greetings, contestant.",
              {0: ["Fighter", "Iron Helmet", 25],  # Class, Item Name, Cost, Armor Increase
               1: ["Fighter", "Iron Breastplate", 50],
               2: ["Fighter", "Iron Greaves", 25],
               3: ["Rogue", "Leather Helmet", 20],
               4: ["Rogue", "Leather Armor", 40],
               5: ["Rogue", "Leather Leg Pads", 20]})

Weaponsmith = NPC("Weaponsmith", "Weaponsmithy", "Hello, challenger. ",
                  {0: ["Fighter", "Magical Greatsword", 50],
                   1: ["Fighter", "Legendary Greatsword", 500],
                   2: ["Fighter", "Magical Sword and Shield", 50],
                   3: ["Fighter", "Legendary Sword and Shield", 500],
                   4: ["Rogue", "Magic Short Sword", 50],
                   5: ["Rogue", "Legendary Short Sword", 500],
                   6: ["Rogue", "Magic Dagger", 50],
                   7: ["Rogue", "Legendary Dagger", 500]})
