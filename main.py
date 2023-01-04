from character_dnd import Character_DnD
from character_dnd import Monster_DnD
from random import randint

# Getting input on character name.
character_name = input(
    "Please type what you would like your character name to be? ")
# Getting input on character species.
character_species = input("Please type what you would like your character species to be? Please choose from Human, "
                          "Elf, or Dwarf. Then hit enter. ")

while character_species.lower() not in ["human", "elf", "dwarf"]:
    character_species = input("Whoops, looks like you didn't choose one of the previous species. Please choose from "
                              "Human, Elf, or Dwarf. Then hit enter. ")
# Getting input on character job.
character_job = input("Please type what you would like your character's job to be? Please choose from Fighter, Rogue, "
                      "or Wizard. Then hit enter. ")

while character_job.lower() not in ["fighter", "rogue", "wizard"]:
    character_job = input("Whoops, looks like you didn't choose one of the previous jobs. PLease choose from Fighter, "
                          "Rogue, or Wizard. Then hit enter. ")

my_character = Character_DnD(character_name, character_species, character_job)
Kobold = Monster_DnD("Kobold", 5, 12, "a dagger", randint(1, 4), "1/8", -1, 4)
red_dragon = Monster_DnD("the Ancient Red Dragon", 546, 22, "a Bite", randint(2, 10) + 24, 24, 9, 17)

my_character.change_attribute_points()
my_character.weapon_choice()
my_character.armor_choice()
my_character.player_attack(Kobold)
my_character.player_attack(red_dragon)
red_dragon.monster_attack(my_character)
Kobold.monster_attack(my_character)
# print(my_character.attribute_points)
# print(my_character)
