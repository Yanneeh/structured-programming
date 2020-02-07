import os
import time
import sys
import random
from termcolor import cprint, colored


# Globals of alle variabelen binnen functie met returns?
colors = ['red', 'green', 'cyan', 'grey', 'yellow', 'blue', 'magenta', 'white']
gamemode = None

def typewriter(word, color='white', delay=0.1):
	for char in word:
		time.sleep(delay)
		sys.stdout.write(colored(char, color))
		sys.stdout.flush()

def clear_screen():
	os.system('clear')

def clean_guess(guess):

	formatted_guess = guess.split(',')

	for i in range(len(formatted_guess)):
		formatted_guess[i] = formatted_guess[i].strip()

	return formatted_guess

clean_guess('red, de, blue, cyan')

def check_guess(guess, code):
	pass

def start():
	clear_screen()

	# Title screen
	typewriter("""              _
              | |
 __      _____| | ___ ___  _ __ ___   ___
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ \r
  \ V  V /  __/ | (_| (_) | | | | | |  __/
 | \_/\_/ \___|_|\___\___/|_| |_| |_|\___|
 | |_ ___
 | __/ _ \            _                      _           _
 | || (_) |          | |                    (_)         | |
  \__\___/   __ _ ___| |_ ___ _ __ _ __ ___  _ _ __   __| |
 | '_ ` _ \ / _` / __| __/ _ \ '__| '_ ` _ \| | '_ \ / _` |
 | | | | | | (_| \__ \ ||  __/ |  | | | | | | | | | | (_| |
 |_| |_| |_|\__,_|___/\__\___|_|  |_| |_| |_|_|_| |_|\__,_|""", 'green', 0.005)

	print('\n')
	cprint('(C) Yannick van Diermen, 2020', 'blue')
	print('\n')
	cprint('press enter to start ...', attrs=['blink'], end="")

	start = input()

def init():
	clear_screen()

	# Rules

	# typewriter("First let's explain the rules.", 'green')
	# print('\r')
	# cprint('There are eight colors', attrs=["blink"])
	# time.sleep(0.5)
	# cprint('There are m', attrs=["blink"])
	# time.sleep(0.5)

	# print('\n')
	# time.sleep(0.5)

	typewriter('There are two gamemodes.')
	print('\r')
	typewriter('You either play as code-maker or as code-cracker.')
	print('\n')
	typewriter('Lets start by picking a gamemode:', 'cyan')
	print('\r')
	cprint('(1) code-maker')
	cprint('(2) code-cracker')

	gamemode_choice = input()

	try:
		if int(gamemode_choice) == 1:
			typewriter('You chose to be the code-maker' , 'cyan')
			print('\r')

			cprint('Function not implemented yet', 'red')
			sys.exit()

			gamemode = 1

		elif int(gamemode_choice) == 2:
			typewriter('You chose to be the code-cracker' , 'cyan')
			time.sleep(1)
			print('\r')

			gamemode = 2
	except:
		cprint('Please enter the right number.' , 'red')
		sys.exit()


def game():
	clear_screen()

	guessed = False
	guesses = []
	code = []

	colors = ['red', 'green', 'cyan', 'grey', 'yellow', 'blue', 'magenta', 'white']

	gamemode = 2

	typewriter('Lets start round one.', 'green')
	time.sleep(1)
	print('\n')

	if gamemode == 1:
		pass

	elif gamemode == 2:

		# Pick random code
		for i in range(4):
			color = random.choice(colors)
			code.append(color)
			colors.remove(color)

		while len(guesses) < 10:

			# TODO: Print the previous result here.

			cprint('Guess four colors ...', 'cyan', attrs=["blink"])

			guess = input()

			guess = clean_guess(guess)

			answer = check_guess(guess, code)

			if answer:
				guessed = True
			else:
				guesses.append(guess)

		if guessed:
			print('you guessed it')

start()

init()

game()

# while True:
# 	init()
#
# 	game()
#
# 	cprint('Do you want to play again?', 'cyan')
# 	cprint('(1) Yes')
# 	cprint('(2) No')
#
# 	choice = input()
#
# 	try:
# 		if int(choice) == 1:
# 			continue
#
# 		elif int(choice) == 2:
# 			break
#
# 	except:
# 		cprint('Please enter the right number.' , 'red')
