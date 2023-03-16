from character_dnd import Character_DnD
from Monster import Monster_DnD
from random import randint
from NPC import *


my_character = Character_DnD()
Kobold = Monster_DnD("Kobold", 5, 12, "a dagger", randint(1, 4), "1/8", -1, 4)
red_dragon = Monster_DnD("the Ancient Red Dragon", 546, 22, "a Bite", randint(2, 10) + 24, 24, 9, 17)

my_character.starting_character_information()
# my_character.weapon_choice()
# my_character.armor_choice()
# # my_character.hit_points = 50
# my_character.player_attack(Kobold)
# my_character.player_loadout()
# my_character.stat_display()
# # my_character.player_attack(red_dragon)
# # red_dragon.monster_attack(my_character)
# # Kobold.monster_attack(my_character)
#
Armorer.wares_selection("Armorer", my_character)