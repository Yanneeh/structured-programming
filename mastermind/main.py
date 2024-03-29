import time
import sys
import random
from termcolor import cprint, colored

from func import *
from algo import random_solve, simple_solve, generate_posibilities

# Zes hoofdkleuren.
colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'white']

# Default gamemode is code-breker.
gamemode = 1

def start():
	clear_screen()

	# Title screen
	typewriter("""               _
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
	cprint('(C) Yannick van Diermen, 2020', 'blue') #vette copyright hoor!
	print('\n')
	cprint('press enter to start ...', attrs=['blink'], end="")

	start = input()

	clear_screen()

	typewriter('There are two gamemodes.')
	print('\r')
	typewriter('You either play as code-maker or as code-breaker.')
	print('\n')

def init():
	clear_screen()

	typewriter('Lets start by picking a gamemode:', 'cyan')
	print('\r')
	cprint('(1) code-maker')
	cprint('(2) code-breaker')

	gamemode_choice = input()
	#mooi afgevangen van dingen.
	try:
		if int(gamemode_choice) == 1:
			typewriter('You chose to be the code-maker.' , 'cyan')
			time.sleep(1)
			print('\r')

			return 1

		elif int(gamemode_choice) == 2:
			typewriter('You chose to be the code-breaker.' , 'cyan')
			time.sleep(1)
			print('\r')

			return 2
	except:
		cprint('Please enter the right number.' , 'red')
		sys.exit()


def game():

	clear_screen()

	guesses = []

	if gamemode == 1:
		clear_screen()

		show_colors(colors)

		code = custom_code(colors)

		clear_screen()

		typewriter('The computer is going to guess your code.', 'green')
		time.sleep(1)
		print('\n')

		posibilities = generate_posibilities(colors)

		guess = random.choice(posibilities)

		while len(guesses) < 10:

			clear_screen()

			guesses.append(guess)

			show_guesses(guesses, code)

			time.sleep(1)

			answer = check_guess(guess, code)

			if check_answer(answer):
				cprint(f'De computer has won the game within {len(guesses)} guesses!', 'green', attrs=['blink'])
				print('\n')
				break

			guess = simple_solve(guess, answer, posibilities)

	elif gamemode == 2:

		code = random_code(colors)

		typewriter('Lets start round one.', 'green')
		time.sleep(1)
		print('\n')

		while len(guesses) < 10:

			clear_screen()

			show_guesses(guesses, code)

			show_colors(colors)

			cprint('Guess four colors ...', 'cyan', attrs=["blink"])

			guess = input()

			guess = format_input(guess)

			guesses.append(guess)

			answer = check_guess(guess, code)

			if check_answer(answer):
				print('\n')
				cprint('Je hebt gewonnen!', 'green', attrs=['blink'])
				print('\n')
				break


def stop_game():
	cprint('Do you want to play again?', 'cyan', attrs=['blink'])
	cprint('(1) Yes')
	cprint('(2) No')

	choice = input()

	try:
		if int(choice) == 1:
			return False

		elif int(choice) == 2:
			return True
		else:
			return True

	except Exception as e:
		return True

# Start scene
start()

# Main game loop
while True:

	# Init scene
	gamemode = init()

	# Game scene
	game()

	# Vraag de speler of diegene verder wilt spelen.
	if stop_game():
		break
