import random
import math


def roll(sides=6):
    return int(math.ceil(random.random() * sides))