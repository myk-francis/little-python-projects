"""Bagels, by Michael Francis
A deductive logic game where you must guess a number based on clues.
Tags: short, game, puzzle"""

import random
NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''Bagels, a deductive logic game.
By Michael Francis
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say: That means:
Pico One digit is correct but in the wrong position.
Fermi One digit is correct and in the right position.
Bagels No digit is correct.
For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True:  # Main loop
        # This stores the secret number players need to guess
        secret_number = get_secret_number()
        print('I have thought up a number. \nYou have {} guesses to get it.'.format(
            MAX_GUESSES))
        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(num_guesses))
                guess = input('> ')
            clues = get_clues(guess, secret_number)
            print(clues)
            num_guesses += 1
            if guess == secret_number:
                break
            if num_guesses > MAX_GUESSES:
                print('You ran out of guesses. The answer was {}.'.format(
                    secret_number))

        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
        print("Thanks for playing!")


def get_secret_number():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789')
    random.shuffle(numbers)
    secret_number = ''
    for i in range(NUM_DIGITS):
        secret_number += str(numbers[i])
    return secret_number


def get_clues(guess, secret_number):
    """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
    if guess == secret_number:
        return 'You got it!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append('Fermi')
        elif guess[i] in secret_number:
            clues.append('Pico')
    if not clues:
        return 'Bagels'
    return ' '.join(clues)


# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
