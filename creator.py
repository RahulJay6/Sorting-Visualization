import random

number_of_bars = 125

class Collection:
    def __init__(self):
        self.numbers = list()
        for i in range(0,number_of_bars):
            num = random.randint(1,100)
            self.numbers = self.numbers + [num]

    def createlist(self):
        for i in range(0,number_of_bars):
            num = random.randint(1,100)
            self.numbers[i] = num

    
