import os
import time
import sys
import random
from termcolor import colored, cprint

#---------- Console print enhancers ------------#

def typewriter(word, color='white', delay=0.1):
	for char in word:
		time.sleep(delay)
		sys.stdout.write(colored(char, color))
		sys.stdout.flush()

def clear_screen():
	os.system('clear')


#---------- Game screen prints ----------#

def show_guesses(guesses, code):
	print('\n')

	if len(guesses) > 0:
		cprint('*-------------------------*', 'magenta')
		for row in guesses:
			cprint('|', 'magenta', end=" ")
			for i in range(len(row)):
				cprint('o', row[i], end=" ")
				cprint('|', 'magenta', end=" ")

			answer = check_guess(row, code)

			for j in range(len(answer)):
				cprint('*', answer[j], end=" ")

			cprint('|', 'magenta', end=" ")

			print('\r')

		cprint('*-------------------------*', 'magenta')

		print('\n')

def show_colors(colors):
	cprint('*-----------------------------------------------*', 'magenta')
	cprint('|', 'magenta', end=" ")
	for color in colors:
		cprint(color, color, end=" ")
		cprint('|', 'magenta', end=" ")
	print('\r')
	cprint('*-----------------------------------------------*', 'magenta')

	print('\n')

#------------- Core game functions ----------#

def format_input(str):

	formatted = str.split(',')

	for i in range(len(formatted)):
		formatted[i] = formatted[i].strip()

	return formatted

def check_guess(guess, code):
	pins = []
	checked = []

	for i in range(4):
		if guess[i] == code[i]:
			checked.append(guess[i])
			pins.append('red')

	for i in range(4):
		if guess[i] in code and guess[i] not in checked:
			checked.append(guess[i])
			pins.append('white')

	for i in range(4-len(pins)):
		pins.append('grey')

	random.shuffle(pins)

	return pins

def check_answer(answer):
	if answer.count('red') > 3:
		return True

def random_code(colors):
	colors_copy = colors.copy()
	code = []

	for i in range(4):
		color = random.choice(colors_copy)
		code.append(color)
		colors_copy.remove(color)

	return code

def custom_code(colors):
	cprint('Choose four colors ...', 'cyan', attrs=["blink"])

	code = input()

	print('\n')

	code = format_input(code)

	for choice in code:
		if choice in colors:
			continue
		else:
			cprint('Code not constructed properly')
			sys.exit()

	return code
