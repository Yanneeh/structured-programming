import random
from itertools import permutations
from func import *

colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'white']


def conv_list(lst):
    return list(lst)


def generate_posibilities(colors):

    posibilities = list(map(conv_list, permutations(colors, 4)))

    return posibilities

def filter_posibilities(guess, pins, posibilities):
    new_posibilities = []

    red_pins = pins.count('red')
    white_pins = pins.count('white')

    for i in range(len(posibilities)):
        pins_check = check_guess(posibilities[i], guess)

        if pins_check.count('red') == red_pins:
            if pins_check.count('white') == white_pins:
                new_posibilities.append(posibilities[i])

    return new_posibilities

# Pick random guesses
def random_solve():

    posibilities = generate_posibilities(colors)

    return random.choice(posibilities)

# The simple approach
def simple_solve(guess, pins, posibilities):

    posibilities = filter_posibilities(guess, pins, posibilities)

    new_guess = random.choice(posibilities)

    return new_guess
