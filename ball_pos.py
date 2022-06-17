# Guess Ball Position Game

from random import shuffle
mylist = [' ','O',' ']

def shuffle_list():
    shuffle(mylist)
    return mylist

def user_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input(" Please Guess the Ball Position at 0,1 or 2:  ")

    return int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Great, Correct Guess!!!')
    else:
        print('Sorry, Wrong Guess...')
        print(mylist)

# Function Calls or Logic

mixed_up = shuffle_list()

guess = user_guess()

check_guess(mixed_up,guess)
