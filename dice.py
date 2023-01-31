from random import randint

class RollResult:
    def __init__(self, roll, modifier, results, string):
        self.roll = roll
        self.modifier = modifier
        self.results = results
        self.string = string

    def __str__(self):
        return self.string


def roll(count, sides, modifier):
    roll = [randint(1,sides) for i in range(count)]
    roll_string = "(" + ", ".join([str(n) for n in roll]) + ")"
    result = sum(roll) + modifier
    string = f"Rolled {count}d{sides} + {modifier}: {roll_string} for a total of {result}."
    return RollResult(roll, modifier, result, string)