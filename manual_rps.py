import random

def play():

    def get_computer_choice():
        computer_choice = random.choices(['rock', 'paper', 'scissors'])[0]
        return computer_choice

    def get_user_choice():
        user_choice = input('Input an option from: rock, paper, scissors. ')
        return user_choice

    def get_winner(computer_choice, user_choice):
        if computer_choice == 'rock' and user_choice == 'scissors' or computer_choice == 'scissors' and user_choice == 'paper' or computer_choice == 'paper' and user_choice == 'rock':
            print('You lost!')

        elif user_choice == 'rock' and computer_choice == 'scissors' or user_choice == 'scissors' and computer_choice == 'paper' or user_choice == 'paper' and computer_choice == 'rock':
            print('You won!')

        else:
            print('It is a tie')

    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)

play()