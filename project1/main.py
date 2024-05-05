import random


NUM_DIGITS = 3
MAX_GUESSES = 10


def main(num_digits: int, max_guesses: int):
    greetings()
    while True:
        secret_num = get_secret_num(num_digits)
        print('I have thought up a number.')
        print(f'You have {max_guesses} guesses to get it.')

        for i in range(1, max_guesses + 1):
            guess = ''
            while len(guess) != num_digits or not guess.isdecimal():
                print(f'Guess #{i}:')
                guess = input('> ')
            clues = get_clues(guess, secret_num)
            print(clues)
            if guess == secret_num:
                break
        else:
            print('You ran out of guesses.')
            print(f'The answer was {secret_num}')

        print('Do you want to play again? (y or n)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def greetings():
    print(f'''Bagels, a deductive logic game.
    By Dmitry.
    
    I am thinking of a 3-digit number. Try to guess what it is.
    Here are some clues:
    When I say:    That means:
        Pico           One digit is correct but in the wrong position.   
        Fermi          One digit is correct and in the right position.
        Bagels         No digit is correct.''')


def get_secret_num(count: int):
    numbers = list('0123456789')
    random.shuffle(numbers)
    return ''.join(numbers[:count])


def get_clues(guess, secret_num):
    if guess == secret_num:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')

    if not guess:
        return 'Bagels'
    clues.sort()
    return ' '.join(clues)


if __name__ == '__main__':
    main(NUM_DIGITS, MAX_GUESSES)
