# 9.12
from random import randint, choice

class Dice():
    """roll of the dice main class"""
    
    def __init__(self, size):
        """initializing dice atributtes"""
        self.size = int(size)
        self.result = []

    def dice_roll(self):
        """Modulate ten roll"""
        i = 10
        while i != 0:
            roll = randint(1, self.size)
            self.result.append(roll)
            i -= 1 
        print(f'Result (dice {self.size} size, 10 rolls):\n{self.result}')

dice_6 = Dice(6)
dice_6.dice_roll()

dice_10 = Dice(10)
dice_10.dice_roll()

dice_12 = Dice(12)
dice_12.dice_roll()

print()
