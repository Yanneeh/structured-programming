import random
from main import colors

def generate_possibilities(colors):
    pass

def solve(guesses):

    guess = []
    for i in range(4):
        guess.append(random.choice(colors))

    return guess
