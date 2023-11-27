import random

GUESS_DIGITS = 3 # We can make the game even harder by change the number of digits to more than 3
NUM_OF_GUESS = 10

def mainloop():
    print('''Welcome To 3-Digit Number Guessing Game.\nThe Game Is Simple.\nWhen I say:      That means:                 
Pico        \t One digit is correct but in the wrong position.
Fermi       \t One digit is correct and in the right position.
Bagels      \t No digit is correct.''')
    while True:
        secret_number = get_secret_num()
        print('''I have thought up a number.\nYou have {} guesses to get it.'''.format(NUM_OF_GUESS))
        guesses_left = NUM_OF_GUESS -1
        while guesses_left >= 0:
            guess =''
            while len(guess) != GUESS_DIGITS or not guess.isdecimal():
                guess = str(input("Guess a {} Digit number:".format(GUESS_DIGITS)))
            clues = get_clue(guess,secret_number)
            print(clues)
            guesses_left-=1
            if guess == secret_number:
                break
            elif guesses_left < 0 :
                print('''No More Guesses left.\n The secret number was {}'''.format(secret_number))
                break
        check = input('''Do you want to play again? Choose (yes or no):''').lower()
        while (check!= 'yes' and check!='no'):
            check = input('''Do you want to play again? Choose (yes or no):''')
        if check.lower() == 'no':
            break



    print('Goodbye')

def get_secret_num():
    """
    This function returns random 3-digit number
    :return:
    """
    number_to_guess=''
    numbers = list('0123456789')
    random.shuffle(numbers)
    for i in range(GUESS_DIGITS):
        number_to_guess+=numbers[i]
    return number_to_guess


def get_clue(guess,secret_number):
    if guess == secret_number:
        return "You Got it"
    clues_list = []
    for i in range(len(guess)):
        if guess[i] == secret_number[i]: # Correct Digit in place
            clues_list.append('Fermi')
        elif guess[i] in secret_number :
            clues_list.append('Pico')
    if not len(clues_list):
        return 'Bagels'
    else :
        return ''.join(clues_list)



if __name__ == '__main__':
    mainloop()