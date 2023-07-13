## Created 07.13.2023

import string
import random

letter_list = string.ascii_lowercase

def get_random_letter():
    return random.choice(letter_list)

def is_valid_input(x):
    if (not x.isalpha()) or (x not in letter_list) or (len(x) != 1):
        print("Input must be a single lowercase letter.")
        return False

print("Guess a single letter!")
random_letter = get_random_letter()
letter_guess = input()

while letter_guess != random_letter:
    if is_valid_input(letter_guess) == False:
        letter_guess = input()
    else:
        print("Incorrect!")
        letter_guess = input()

print("Correct!")
print("Done.")
