""" import random module """
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Adding game images in a list
game_images = [rock, paper, scissors]
# Print the welcome message
print("Welcome and Let's play Rock Paper Scissors!")

# game rules and validation.
while True:
    game_rules = input("\nThere are 3 rules:\n \
    \nRock wins against scissors.\n\
    \nScissors win against paper.\n\
    \nPaper wins against rock.\n\
    \nDo you want to play? Press 'Y' to continue or 'N' to quit the game. ")
    if game_rules.upper() == "Y":
        print()
        break
    elif game_rules.upper() == "N":
        print("The game ended!")
        quit()

    else:
        print("Invalid entry: enter 'Y'")

# Get the user's name and validate it.
while True:
    user_name = input('Please input your name: ').capitalize()
    if user_name.isalpha():
        print()
        break
    else:
        print("Invalid entry: players name must be an alphabet")

# Logic of the game. Credit: devdojo.com


def game_logic():
    """
    This function is the logic of our game.
    """
    user_action = check_input()
    print("User choice: ")
    print(game_images[user_action])
    computer = random.randint(0, 2)
    print("Computer Choice: ")
    print(game_images[computer])
    if user_action == 0 and computer == 2:
        print("You win! 🎉")
    elif computer == 0 and user_action == 2:
        print("You lose.  ☠")
    elif computer > user_action:
        print("You lose. ☠")
    elif user_action > computer:
        print("You win!🎉")
    elif computer == user_action:
        print("It's a draw.")

# This function check the validity of the input


def check_input():

    """
    This function check the validity of the inputsY
    """
    valid_inputs = [0, 1, 2]
    user_input = -1
    while user_input not in valid_inputs:
        user_input = int(input('Enter: 0 Rock, 1 Paper or 2 Scissors '))
    return user_input


# ask player to restart the game.


def restart():
    '''
    This functions allowed the user to restart or continue the game
    '''

    while True:
        user_restart = input("Enter 'q' to quit, 'n' for a new game ")
        if user_restart.lower() == "n":
            game_logic()
        elif user_restart.lower() == "q":
            print(f"The game ended! Bye {user_name}")
            quit()
        elif user_restart != "n" or "q":
            print("Invalid choice. Enter 'n' for a new game or 'q' to quit. ")

# Allow user to restart or quit the game.


while True:

    game_logic()
    restart()
