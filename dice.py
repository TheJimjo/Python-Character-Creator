from random import randint

class RollResult:
    def __init__(self, roll, modifier, result, string):
        self.roll = roll
        self.modifier = modifier
        self.result = result
        self.string = string

    def __str__(self):
        return self.string

def roll(count, sides, modifier):
    roll = [randint(1, sides) for i in range(count)]
    roll_string = "(" + ", ".join([str(n) for n in roll]) + ")"
    result = sum(roll) + modifier
    string = f"Rolled {count}d{sides} + {modifier}: {result} {roll_string}"
    return RollResult(roll, modifier, result, string)

def roll_advantage(modifier):
    roll = [randint(1, 20) for i in range(2)]
    roll_string = "(" + ", ".join([str(n) for n in roll]) + ")"
    result = max(roll) + modifier
    string = f"Rolled 1d20 + {modifier} with advantage: {result} {roll_string}"
    return RollResult(roll, modifier, result, string)

def roll_disadvantage(modifier):
    roll = [randint(1, 20) for i in range(2)]
    roll_string = "(" + ", ".join([str(n) for n in roll]) + ")"
    result = min(roll) + modifier
    string = f"Rolled 1d20 + {modifier} with disadvantage: {result} {roll_string}"
    return RollResult(roll, modifier, result, string)
