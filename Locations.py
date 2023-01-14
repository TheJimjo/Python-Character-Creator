class Location:
    def __init__(self, name, interaction, encounter, reward):
        self.name = name
        self.interaction = interaction
        self.encounter = encounter
        self.reward = reward


Caves = Location(
    "The caves",  # Location Name
    "Enter",  # How to enter
    "Troll",  # Encounter
    "a stockpile of 50 gold")  # Reward

Forest = Location(
    "The forest",  # Name
    "Enter",  # Interaction
    "Elven Warrior",  # Encounter
    "a stockpile of 50 gold")  # Reward

Crypt = Location(
    "The crypt",  # Name
    "Enter",  # Interaction
    "Undead Necromancer",  # Encounter
    "a stockpile of 50 gold")  # Reward
