import random

rock = print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper = print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

scissors = print('''
    _______
---'   ____)____1
          ______)
       __________)
      (____)
---.__(___)
''')

print("Welcome and Let's play Rock Paper Scissors!")

# Get the user's name and validate it.
while True:
    user_name = input('Please input your name: ').capitalize()
    if user_name.isalpha():
        print()
        break
    else:
        print("Invalid entry: players name must be an alphabet")

# game rules and validation.
while True:
    game_rules = input("\nThere are 3 rules:\n \
    \nRock wins against scissors.\n\
    \nScissors win against paper.\n\
    \nPaper wins against rock.\n\
    \nDo you want to play? Press 'Y' to continue or 'N' to quit the game. ")
    if game_rules == "Y":
        print()
        break
    elif game_rules == "N":
        print(f"The game ended! Bye {user_name}")
        exit()

    else:
        print("Invalid entry: enter 'Y'")
# Logic of the game.


def game_logic():
    """
    This function is the logic of our game.
    """

    possible_actions = ["rock", "paper", "scissors"]
    user_action = input(f"Hello {user_name}! Enter rock, paper or scissors ")
    computer = random.choice(possible_actions)    
    if (user_action not in possible_actions):
        user_action = input("Invalid emtry: Enter rock, paper or scissors ") 
        if (user_action not in possible_actions):
            print(f"Invalid entry again:Please read again the rules before starting a new game.\
            \nBye {user_name}\n")
            quit()
  
    if user_action == computer:
        print(f"You choose {user_action}, computer chose {computer}. It's a draw!")
        
    elif user_action == "rock":
        if computer == "paper":
            print(f"You lose! {computer} covers {user_action}!")
           
        if computer == "scissors":
            print(f'You win! {user_action} smashes {computer}!')
           
    elif user_action == "scissors":
        if computer == "paper":
            print(f"You win! {user_action} cuts {computer}!")
            
        if computer == "rock":
            print(f"You lose! {computer} smashes {user_action}!")
            
    elif user_action == "paper":
        if computer == "scissors":
            print(f"You lose! {computer} cuts {user_action}!")
            
        if computer == "rock":
            print(f"You win! {user_action} covers {computer}!")  

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
            print("Invalid choice. Enter 'n' for a new game or 'q' to quit the game. ")

# Allow user to restart or quit the game.


while True:

    game_logic()
    restart()