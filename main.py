from character_dnd import Character_DnD

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

my_character.change_attribute_points()
# my_character.weapon_and_armor()
print(my_character.attribute_points)
print(my_character)
