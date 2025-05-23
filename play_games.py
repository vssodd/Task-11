def mainMenu():
    while True:
        print('1. Rock, Paper, Scissors')
        print('2. Guess the Number')
        print('3. Exit')
        choice = input('Choose a game: ')
        if choice == '1':
            rock_paper_scissors()
        elif choice == '2':
            guess_the_number()
        elif choice == '3':
            break
        else:
            print('Invalid choice. Please try again.')

mainMenu()
