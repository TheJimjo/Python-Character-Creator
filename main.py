#!/usr/bin/env python3

from character import Character
from monster import monsters


def fight(p1, p2):
    while p1.current_hp > 0 and p2.current_hp > 0:
        p1.attack(p2)
        if p2.current_hp > 0:
            p2.attack(p1)


if __name__ == "__main__":
    foo = Character()
    bar = monsters["Kobold"]
    fight(foo, bar)
