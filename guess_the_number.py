import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    while True:
        user_guess = int(input('Guess a number from 1 to 100: '))
        if user_guess > number_to_guess:
            print('Too high, try again.')
        elif user_guess < number_to_guess:
            print('Too low, try again.')
        else:
            print('Congratulations, you guessed the number!')
            break

guess_the_number()
