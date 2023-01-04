from random import randint

roll = lambda a, b: sum([randint(1, b) for i in range(a)])
