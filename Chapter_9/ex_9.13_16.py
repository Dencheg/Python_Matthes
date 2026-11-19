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

# 9.13
class Lottery():
    """lottery from ten numbers and five letters"""
        
    def __init__(self, lottery_list):
        """initialized lottery attributes"""
        self.lottery_list = lottery_list
        self.result_list = []

    def lottery_start(self):
        """lottery game"""
        self.result_list = []
        i = 4
        while i != 0:
            result = choice(self.lottery_list)
            self.result_list.append(result)
            i -= 1
        return self.result_list
    
    def lottery_winer(self):
        """winning combination"""
        print(f'Winning combination: {self.result_list}')

lottery_list = ['5', '7', '11', '8', '16', '3', '21', '35', '4', '9',
                'v', 'e', 'R', 'x', 'L', ]
lottery_1 = Lottery(lottery_list)
probability_1 = lottery_1.lottery_start()
lottery_1.lottery_winer()
 
# 9.14
def probability_start(probability, lottery_list):
    """probabilty winning"""
    result_list = []
    k = 0 
    while True:
        k += 1
        i = 4
        while i != 0:
            result = choice(lottery_list)
            result_list.append(result)
            i -= 1
        if probability == result_list:
            print(f'Probabilty winning: {k}')
            break
        else:
            result_list = []

probability_start(probability_1, lottery_list)

# 9.15
# learning home