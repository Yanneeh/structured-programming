
import random

guessed = False

while guessed != True:
    num = int(input("Voer een nummer in tussen 1 en 10: "))

    if random.randint(1, 10) == num:
        print('Je hebt het getal geraden!')
        guessed = True
    else:
        print('Jammer, raad opnieuw...')
