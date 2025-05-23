from math import gcd

a = int(input('Enter number a: '))
b = int(input('Enter number b: '))
print(gcd(a, b))

import random

def rock_paper_scissors():
    choices = ['Rock', 'Scissors', 'Paper']
    computer_choice = random.choice(choices)
    user_choice = input('Enter your choice (Rock, Scissors, Paper): ')
    if user_choice == computer_choice:
        print('Draw!')
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        print('You win!')
    else:
        print('You lose!')
