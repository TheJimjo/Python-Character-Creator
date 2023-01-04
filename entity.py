class Entity:
    def __init__(self, name):
        self.name = name
        self.max_hp = 0
        self.current_hp = 0


    def get_hp_str(self):
        return f"{self.name} has {self.current_hp} out of {self.max_hp}"


    def take_damage(self, amount):
        if self.current_hp <= amount:
            self.current_hp= 0
            print(f"{self.name}'s lifeless form crumples to the floor.")
        else:
            self.current_hp -= amount
            print(f"{self.name} takes {amount} damage and has {self.current_hp} hp remaining of {self.max_hp}.")
