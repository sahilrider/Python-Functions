"""
A simple dice roller which uses `random` module to generate dice rolls taking rolls
and number of sides the dice has as the parameter.

> dice(1, 6)
//  3 ((Any random number between 1 and 6))

> dice(6, 10)
// 4, 10, 4, 6, 8, 3 ((Any random number between 1 and 10 printed 6 times))
"""

import random

def dice(rolls, sides):
    for x in range(0, rolls):
        return random.randrange(1, sides + 1) 
