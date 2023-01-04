from entity import Entity
from dice import roll


class Monster(Entity):
    def __init__(self,
                 name,
                 hit_points,
                 armor_class,
                 attack_name,
                 attack_bonus,
                 damage_roll,
                 damage_bonus):
        Entity.__init__(self, name)
        self.name = name
        self.max_hp = hit_points
        self.current_hp = self.max_hp
        self.armor_class = armor_class
        self.attack_name = attack_name
        self.attack_bonus = attack_bonus
        self.damage_roll = damage_roll
        self.damage_bonus = damage_bonus


    def __repr__(self):
        return (f"\n {self.name} is a challenge rating {self.challenge_rating} monster with {self.hit_points} hit "
                f"points, {self.armor_class} armor class and that wields {self.weapon}. ")


    def attack(self, enemy):
        attack_roll = roll(1, 20, self.attack_bonus)
        print(f"{self.name} swings their {self.attack_name} at the {enemy.name}!")
        print(attack_roll)
        if enemy.get_ac() < attack_roll.result:
            print(f"{self.name} smacks {enemy.name} a good one! {attack_roll.result} vs {enemy.get_ac()} AC")
            damage_roll = roll(self.damage_roll[0], self.damage_roll[1], self.damage_bonus)
            print(damage_roll)
            enemy.take_damage(damage_roll.result)
        else:
            print(f"{self.name} wiffs!")


    def get_ac(self):
        return self.armor_class


monsters = dict()
monsters["Kobold"] = Monster("Kobold",
                             5,
                             12,
                             "dagger",
                             0,
                             (1, 4),
                             0)
